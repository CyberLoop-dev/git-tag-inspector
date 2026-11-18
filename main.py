#!/usr/bin/env python3
"""Inspect local Git tags for naming and target inconsistencies."""
import argparse
from collections import defaultdict
import json
import re
import subprocess
import sys
import time

SEMVER=re.compile(r"^v?(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)(?:[-+][0-9A-Za-z.-]+)?$")

def is_semver(name): return bool(SEMVER.fullmatch(name))

def parse_tag_rows(output,now=None,stale_days=365):
    now=int(now if now is not None else time.time())
    tags,targets=[],defaultdict(list)
    for line in output.splitlines():
        parts=line.split("\\x00")
        if len(parts)<6: continue
        name,object_type,created,subject,object_id,peeled=parts[:6]
        target=peeled or object_id
        try: timestamp=int(created or 0)
        except ValueError: timestamp=0
        item={"name":name,"annotated":object_type=="tag","target":target,"created":timestamp,
              "subject":subject,"semver":is_semver(name),"stale":bool(timestamp and now-timestamp>stale_days*86400)}
        tags.append(item)
        if target: targets[target].append(name)
    duplicates=[{"target":target,"tags":names} for target,names in targets.items() if len(names)>1]
    return {"tags":tags,"non_semver":[x["name"] for x in tags if not x["semver"]],
            "duplicate_targets":duplicates,"stale_tags":[x["name"] for x in tags if x["stale"]]}

def inspect_repo(repo,stale_days):
    fmt="%(refname:short)%00%(objecttype)%00%(creatordate:unix)%00%(subject)%00%(objectname)%00%(*objectname)"
    result=subprocess.run(["git","for-each-ref",f"--format={fmt}","refs/tags"],cwd=repo,text=True,capture_output=True,check=True)
    return parse_tag_rows(result.stdout,stale_days=stale_days)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",default=".")
    parser.add_argument("--stale-days",type=int,default=365)
    parser.add_argument("--json",action="store_true")
    args=parser.parse_args()
    try: report=inspect_repo(args.repo,max(0,args.stale_days))
    except (OSError,subprocess.CalledProcessError) as exc: print(f"git-tag-inspector: {exc}",file=sys.stderr); return 2
    if args.json: print(json.dumps(report,indent=2))
    else:
        print(f"Tags: {len(report['tags'])}")
        for tag in report["tags"]:
            flags=[]
            if not tag["semver"]: flags.append("non-semver")
            if tag["stale"]: flags.append("stale")
            if not tag["annotated"]: flags.append("lightweight")
            print(f"- {tag['name']} -> {tag['target'][:12]} {' '.join(flags)}")
        print(f"Duplicate targets: {len(report['duplicate_targets'])}")
    return 0

if __name__=="__main__": raise SystemExit(main())

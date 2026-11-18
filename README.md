<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=170&section=header&text=Git%20Tag%20Inspector&fontColor=ffffff&fontSize=38&animation=fadeIn" alt="Git Tag Inspector banner" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=19&duration=3000&pause=900&color=14B8A6&center=true&vCenter=true&width=820&lines=Audit%20release%20tags%2C%20versions%2C%20and%20duplicate%20targets" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/git-tag-inspector)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/git-tag-inspector)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/git-tag-inspector?style=flat)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/git-tag-inspector)

<img src="assets/illustration.svg" alt="Git Tag Inspector illustration" width="92%"/>
</div>

## :compass: Overview

A read-only Git CLI that inventories local tags, identifies non-semver names, distinguishes annotated from lightweight tags, and finds multiple tags pointing to the same commit.

## :sparkles: Features

- :white_check_mark: Lists tags with target commit and tag type
- :white_check_mark: Recognizes common semantic-version names
- :white_check_mark: Finds tags that point to the same commit
- :white_check_mark: Flags tags older than a configurable age

## :clapper: Demo

```bash
python main.py --repo . --stale-days 365
```

The example runs locally; no hosted service or upload is required.

## :rocket: Quick Start

```bash
python -m pip install -r requirements.txt
python main.py --repo .
```

Run `python main.py --help` to see all supported options.

## :toolbox: Tech Stack

- Python 3.10+ standard library and Git CLI
- Automated tests: unittest
- Local-first processing

## :file_folder: Folder Structure

```text
git-tag-inspector/\n├── main.py\n├── requirements.txt\n├── tests/test_core.py\n├── examples/README.md\n└── assets/illustration.svg
```

## :world_map: Roadmap

- [x] Core workflow and CLI
- [x] Example input and tests
- [ ] Additional report formats
- [ ] Continuous integration on supported platforms

## :handshake: Contributing

Issues and pull requests are welcome. Keep changes focused, document behavior changes, and add tests for new features.

## :page_facing_up: License

MIT - see [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,100:0f172a&height=100&section=footer" alt="Animated wave footer" width="100%"/></div>

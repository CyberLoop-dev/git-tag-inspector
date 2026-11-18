import unittest
from main import is_semver, parse_tag_rows

class TagInspectorTests(unittest.TestCase):
    def test_semver(self):
        self.assertTrue(is_semver("v1.2.3"))
        self.assertTrue(is_semver("1.2.3-rc.1"))
        self.assertFalse(is_semver("release-final"))
    def test_duplicate_targets(self):
        raw = "v1.0.0\x00commit\x001700000000\x00subject\x00abc\x00\nv1.0.1\x00commit\x001700000100\x00subject\x00abc\x00"
        result = parse_tag_rows(raw, now=1800000000)
        self.assertEqual(len(result["duplicate_targets"]), 1)
        self.assertEqual(result["duplicate_targets"][0]["tags"], ["v1.0.0", "v1.0.1"])

if __name__ == "__main__":
    unittest.main()

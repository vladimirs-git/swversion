"""unittests package"""

import os
import re
import unittest
from datetime import datetime, date
from pathlib import Path
from typing import Dict, Set

import tomli

from swversion.helpers import findall1

DDate = Dict[str, date]


def _make_pyproject_d(root: Path) -> dict:
    """Return data of pyproject.toml"""
    path = Path.joinpath(root, "pyproject.toml")
    fh = path.open(mode="rb")
    pyproject_d = tomli.load(fh)
    return pyproject_d


def _last_modified_date(root: Path) -> str:
    """Paths to .py files with last modified dates"""
    dates: Set[date] = set()
    for root_i, _, files_i in os.walk(str(root)):
        for file_ in files_i:
            if file_.endswith(".py"):
                path = os.path.join(root_i, file_)
                stat = os.stat(path)
                date_ = datetime.fromtimestamp(stat.st_mtime).date()
                dates.add(date_)
    date_ = sorted(dates)[-1]
    return str(date_)


ROOT = Path(__file__).parent.parent.resolve()
PYPROJECT = _make_pyproject_d(ROOT)


class Test(unittest.TestCase):
    """package"""

    def test_valid__version(self):
        """version in README, URL"""
        package = PYPROJECT["project"]["name"].replace("_", "-")
        dwl_url = PYPROJECT["project"]["urls"]["Download URL"]
        version_req = PYPROJECT["project"]["version"]

        for key, text in [
            ("pyproject.toml project.urls.DownloadURL", dwl_url)
        ]:
            is_regex_found = False
            for regex in [
                package + r".+/(.+?)\.tar\.gz",
                package + r"@(.+?)$",
            ]:
                versions = re.findall(regex, text, re.M)
                for version in versions:
                    is_regex_found = True
                    self.assertEqual(version, version_req, msg=f"version in {key}")
            self.assertEqual(is_regex_found, True, msg=f"absent {version_req} in {key}")

    def test_valid__version__changelog(self):
        """version in CHANGELOG"""
        version = PYPROJECT["project"]["version"]
        path = Path.joinpath(ROOT, "CHANGELOG.rst")
        text = path.read_text()
        regex = r"(.+)\s\(\d\d\d\d-\d\d-\d\d\)$"
        version_changelog = findall1(regex, text, re.M)
        self.assertEqual(version_changelog, version, msg=f"version in {path=}")

    def test_valid__date(self):
        """last modified date"""
        path = Path.joinpath(ROOT, "CHANGELOG.rst")
        text = path.read_text()
        regex = r".+\((\d\d\d\d-\d\d-\d\d)\)$"
        date_changelog = findall1(regex, text, re.M)
        last_modified = _last_modified_date(ROOT)
        self.assertEqual(date_changelog, last_modified, msg="last modified file")


if __name__ == "__main__":
    unittest.main()

"""This is the unique place in which the version number is defined.


"""

from collections import namedtuple


PRERELEASE_NORMALIZED_NAME = {"dev": "a",
                              "alpha": "a",
                              "beta": "b",
                              "candidate": "rc"}

MAJOR = 1
MINOR = 1
MICRO = 0

RELEV: str = "final"
"""RELEV must be 'dev' on the master branch, and can be "alpha", "beta",
"candidate" or "final" on a (pre)release branch."""

SERIAL: int = 0
"""SERIAL can be incremented to produce multiple alpha or release candidate
versions. It should be 0 on the development branch."""

_version_info = namedtuple(
    "version_info",
    ["major", "minor", "micro", "releaselevel", "serial"]
)

version_info = _version_info(MAJOR, MINOR, MICRO, RELEV, SERIAL)
"""Version tuple.
This can be used to reliably sort version numbers
(e.g. `if version_info[:3] <= (1, 1, 0): ...`)"""

version: str = "%d.%d.%d" % version_info[:3]
"""Version string (e.g. "1.0.0" or "1.1.0-rc0").
"""

if version_info.releaselevel != "final":
    _prerelease = PRERELEASE_NORMALIZED_NAME[version_info.releaselevel]
    version += "-%s%s" % (_prerelease, version_info.serial)

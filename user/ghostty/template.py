pkgname = "ghostty"
pkgver = "1.0.1"
pkgrel = 0
hostmakedepends = [
    "zig",
]
makedepends = [
    "pkgconf",
    "gtk4-devel",
    "libadwaita-devel",
]
pkgdesc = "Fast, feature-rich, and cross-platform terminal emulator"
maintainer = "Guilhem Baccialone <guilhem.baccialone@zaclys.net>"
license = "MIT"
url = "https://ghostty.org"
source = (
    f"https://github.com/ghostty-org/ghostty/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "bd12953c8bbe7149e2f94e7e578a88e981932a69aa483f5ce9a2cfba726e0015"


def build(self):
    self.do("zig", "build", "-Doptimize=ReleaseFast")


def install(self):
    self.do("zig", "-p", "user", "-Doptimize=ReleaseFast")

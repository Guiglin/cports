pkgname = "zig-prebuilt"
pkgver = "0.13.0"
pkgrel = 0
archs = ["x86_64"]
pkgdesc = "Pre-built Zig programming language toolchain"
maintainer = "Guilhem Baccialone <guilhem.baccialone@zaclys.net>"
license = "MIT"
url = "https://ziglang.org"
source = f"https://ziglang.org/download/{pkgver}/zig-linux-{self.profile().arch}-{pkgver}.tar.xz"
sha256 = "d45312e61ebcc48032b77bc4cf7fd6915c11fa16e4aad116b66c9468211230ea"


def install(self):
    self.install_license("LICENSE")
    self.install_bin("zig")
    self.install_files("lib", "usr/lib", name="zig")

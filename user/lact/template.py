pkgname = "lact"
pkgver = "0.7.2"
pkgrel = 0
build_style = "cargo"
make_build_args = ["-p", f"{pkgname}"]
hostmakedepends = [
    "blueprint-compiler",
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "linux-headers",
    "rust-std",
]
depends = ["hwdata", "libdrm"]
pkgdesc = "AMDGPU Controller application"
license = "MIT"
url = "https://github.com/ilya-zlobintsev/LACT"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "654e5d23a0c0ea6da1561180bb4bb1b62192fe3d4a069bb66347bb6753f222d9"
# We don't want to test hardware on CI machine
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/lact")
    self.install_file(
        "res/io.github.lact-linux.desktop", "usr/share/applications"
    )
    self.install_file("res/io.github.lact-linux.png", "usr/share/pixmaps")
    self.install_file(
        "res/io.github.lact-linux.svg", "usr/share/icons/hicolor/scalable/apps"
    )
    self.install_service(self.files_path / "lactd")
    self.install_license("LICENSE")

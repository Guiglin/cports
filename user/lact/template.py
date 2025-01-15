pkgname = "lact"
pkgver = "0.7.3"
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
sha256 = "212ac1eadcbc8d7112b7ee11176c6ab0aee04f53bda9cfb342679c2e1cf6a230"
# We don't want to test hardware on CI machine
options = ["!check"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/lact")
    self.install_file(
        "res/io.github.ilya_zlobintsev.LACT.desktop", "usr/share/applications"
    )
    self.install_file(
        "res/io.github.ilya_zlobintsev.LACT.png", "usr/share/pixmaps"
    )
    self.install_file(
        "res/io.github.ilya_zlobintsev.LACT.svg",
        "usr/share/icons/hicolor/scalable/apps",
    )
    self.install_service(self.files_path / "lactd")
    self.install_license("LICENSE")

pkgname = "lact"
pkgver = "0.7.1"
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
sha256 = "e9c8f133dce1c73b623db5e4742bd0a9a2f38b84cfd49d3f031e33b82895232e"
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

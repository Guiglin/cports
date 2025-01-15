pkgname = "lact"
pkgver = "0.7.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["-p", f"{pkgname}"]
hostmakedepends = [
    "blueprint-compiler",
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "clang",
    "gdk-pixbuf-devel",
    "git",
    "glib-devel",
    "gtk4-devel",
    "linux-headers",
    "pango-devel",
    "rust-std",
]
depends = [
    "cairo",
    "fontconfig",
    "freetype",
    "graphene",
    "glib",
    "gtk4",
    "hwdata",
    "libdrm",
    "pango",
]
pkgdesc = "AMDGPU Controller application"
maintainer = "Guilhem Baccialone <guilhem.baccialone@zaclys.net>"
license = "MIT"
url = "https://github.com/ilya-zlobintsev/LACT"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7780b4b528b02baaebf6bd87106267037b0a2011817c9932f29b6ccfb6357d8d"
# We don't want testing hardware on CI machine
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

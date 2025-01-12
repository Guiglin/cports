pkgname = "ghostty"
pkgver = "1.1.2"
pkgrel = 0
hostmakedepends = [
    "zvm",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "linux-headers",
    "oniguruma-devel",
    "pkgconf",
]
pkgdesc = "Fast, feature-rich, and cross-platform terminal emulator"
maintainer = "Guilhem Baccialone <guilhem.baccialone@zaclys.net>"
license = "MIT"
url = "https://ghostty.org"
source = (
    f"https://github.com/ghostty-org/ghostty/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "54d74a49df9f2e4b9a8b7c88372bdb78f4e3c4f072f6cee197c873e90ba27d19"
env = {
    "ZIG_GLOBAL_CACHE_DIR": "offline-cache",
    "DESTDIR": "zig-out",
    "ZVM_PATH": "zvm",
}


def prepare(self):
    self.do(
        "zvm",
        "i",
        "0.13.0",
        allow_network=True,
    )
    self.mkdir("offline-cache")
    self.do(
        "zvm",
        "run",
        "0.13.0",
        "build",
        "--fetch",
        allow_network=True,
    )
    self.do(
        "zvm",
        "run",
        "0.13.0",
        "fetch",
        "git+https://github.com/zigimg/zigimg#3a667bdb3d7f0955a5a51c8468eac83210c1439e",
        allow_network=True,
    )
    self.do(
        "zvm",
        "run",
        "0.13.0",
        "fetch",
        "git+https://github.com/mitchellh/libxev#f6a672a78436d8efee1aa847a43a900ad773618b",
        allow_network=True,
    )


def build(self):
    self.do(
        "zvm",
        "run",
        "0.13.0",
        "build",
        "-p",
        "/usr",
        "--system",
        f"{self.chroot_cwd}/offline-cache/p",
        "-Doptimize=ReleaseFast",
        "-Dcpu=baseline",
        "-Dpie=true",
        "-Demit-docs=false",
        f"-Dversion-string={pkgver}",
        "install",
    )


def install(self):
    self.install_bin("zig-out/usr/bin/ghostty")
    self.install_files(
        "zig-out/usr/share/applications",
        "usr/share",
    )
    self.install_files("zig-out/usr/share/ghostty", "usr/share")
    self.install_files("zig-out/usr/share/icons", "usr/share")
    self.install_files("zig-out/usr/share/nautilus-python", "usr/share")
    self.install_files("zig-out/usr/share/kio", "usr/share")
    self.install_files("zig-out/usr/share/nvim", "usr/share")
    self.install_files("zig-out/usr/share/vim", "usr/share")
    self.install_files("zig-out/usr/share/bat", "usr/share")
    self.install_files("zig-out/usr/share/fish", "usr/share")
    self.install_files("zig-out/usr/share/zsh", "usr/share")
    self.install_license("LICENSE")


@subpackage("ghostty-shell-integration")
def _(self):
    self.desc = "Ghostty shell integration"
    return [
        "usr/share/ghostty/shell-integration",
    ]

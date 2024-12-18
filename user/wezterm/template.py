pkgname = "wezterm"
pkgver = "20240203-110809-5046fc22"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["bash"]
makedepends = [
    "fontconfig-devel"
    "libssh2-devel"
    "libgit2-devel",
    "libx11-devel"
    "libxkbcommon-devel",
    "openssl-devel",
    "pkgconf",
    "rust-std",
    "wayland-devel"
    "xcb-util-devel",
    "xcb-util-image-devel",
    "xcb-util-keysyms-devel",
    "xcb-util-wm-devel",
    "zlib-ng-compat-devel",
    "zstd-devel"
]
pkgdesc = "A GPU-accelerated cross-platform terminal emulator and multiplexer"
maintainer = "Guilhem Baccialone <guilhem.baccialone@zaclys.net"
license = "MIT"
url = "https://wezfurlong.org/wezterm/"
sources = f"https://github.com/wez/wezterm/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3a02a68016ef48cdb2127308be20acafe94a568411e95b0e64dc590cf877b401"


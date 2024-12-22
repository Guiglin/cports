pkgname = "lutris"
pkgver = "0.5.18"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "gettext",
    "desktop-file-utils",
    "python-setuptools",
    "python-gobject",
    "gtk+3-devel",
]
depends = [
    "python-dbus",
    "python-gobject",
    "python-pyyaml",
    "python-evdev",
    "python-pillow",
    "pciutils",
    "cabextract",
    "gtk+3",
    "xrandr",
    "unzip",
    "7zip",
    "mesa-utils",
    "gnome-desktop",
    "python-requests",
    "webkitgtk4-devel",
    "webkitgtk-devel",
    "python-distro",
    "python-lxml",
    "python-magic",
    "python-certifi",
]
pkgdesc = "Open gaming platform for managing games in a unified way"
maintainer = "Guilhem Baccialone <guilhem.baccialone@zaclys.net>"
license = "GPL-3.0-or-later"
url = "https://lutris.net"
source = f"https://github.com/lutris/lutris/archive/v{pkgver}.tar.gz"
sha256 = "b9d4ad052d1c750910940d5cc7c583967c0c65c1584b7f4a1abaf46e40c3d8d1"

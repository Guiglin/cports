pkgname = "tilda"
pkgver = "2.0.0"
pkgrel = 0
build_style = "gnu_configure"
configure_env = {"NOCONFIGURE": "1"}
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libconfuse-devel",
    "vte-gtk3-devel",
]
depends = [
    "desktop-file-utils",
]
pkgdesc = "GTK drop down terminal similar to guake"
maintainer = "Guilhem Baccialone <guilhem.baccialone@zaclys.net>"
license = "GPL-2.0-or-later"
url = f"https://github.com/lanoxx/{pkgname}"
source = f"{url}/archive/{pkgname}-{pkgver}.tar.gz"
sha256 = "ff9364244c58507cd4073ac22e580a4cded048d416c682496c1b1788ee8a30df"

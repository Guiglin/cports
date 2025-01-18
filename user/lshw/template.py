pkgname = "lshw"
pkgver = "02.20"
_pkgver = f"B.{pkgver}"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "all",
    "gui",
    f"VERSION={_pkgver}",
    "NO_VERSION_CHECK=1",
    "ZLIB=1",
]
make_install_args = [
    "install",
    "install-gui",
    f"VERSION={_pkgver}",
    "NO_VERSION_CHECK=1",
    "ZLIB=1",
]
make_use_env = True
hostmakedepends = ["gettext", "pkgconf"]
makedepends = [
    "gettext-devel",
    "gtk+3-devel",
    "linux-headers",
    "zlib-ng-compat-devel",
]
depends = [
    "cmd:gzip!chimerautils",
]
pkgdesc = "Hardware Lister"
maintainer = "Guilhem Baccialone <guilhem.baccialone@zaclys.net>"
license = "GPL-2.0-only"
url = "https://ezix.org/project/wiki/HardwareLiSter"
source = f"https://www.ezix.org/software/files/lshw-{_pkgver}.tar.gz"
sha256 = "06d9cf122422220e5dc94e8ea5b01816a69bb6b59368f63d7f21fff31fc6922a"
hardening = ["vis", "cfi"]
# no tests available and may fail to link ./core/liblshw.a
options = ["!check", "!linkparallel"]


def post_install(self):
    self.install_file(
        "src/gui/integration/gtk-lshw.desktop", "usr/share/applications"
    )
    self.install_file(
        "src/gui/integration/gtk-lshw.appdata.xml", "usr/share/metainfo"
    )
    self.install_file(
        "src/gui/integration/gtk-lshw.pam", "usr/lib/pam.d", name="gtk-lshw"
    )


@subpackage("gtk-lshw")
def _(self):
    self.subdesc = "GTK ui"
    self.depends = [
        self.parent,
    ]
    return [
        "cmd:gtk-lshw",
        "usr/share/lshw/artwork",
        "usr/share/lshw/ui",
    ]

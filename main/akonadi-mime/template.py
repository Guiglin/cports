pkgname = "akonadi-mime"
pkgver = "25.04.1"
pkgrel = 0
build_style = "cmake"
# broken for some reason
make_check_args = ["-E", "mailserializerplugintest"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "libxslt-progs",
]
makedepends = [
    "akonadi-devel",
    "ki18n-devel",
    "kio-devel",
    "kitemmodels-devel",
    "kmime-devel",
    "kxmlgui-devel",
    "libxslt-devel",
    "qt6-qtdeclarative-devel",
    "shared-mime-info",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Akonadi mime libraries"
license = "LGPL-3.0-only"
url = "https://api.kde.org/kdepim/akonadi-mime/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-mime-{pkgver}.tar.xz"
)
sha256 = "934e1166f070d9262f7bf2ee55b102b3324c349be986435122973e4bca488fd2"


@subpackage("akonadi-mime-devel")
def _(self):
    self.depends += ["akonadi-devel"]
    return self.default_devel()

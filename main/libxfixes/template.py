pkgname = "libxfixes"
pkgver = "6.0.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libx11-devel"]
pkgdesc = "Xfixes library and extension of X RandR"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXfixes-{pkgver}.tar.gz"
sha256 = "e69eaa321173c748ba6e2f15c7cf8da87f911d3ea1b6af4b547974aef6366bec"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxfixes-devel")
def _(self):
    return self.default_devel()

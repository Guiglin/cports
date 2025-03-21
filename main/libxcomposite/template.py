pkgname = "libxcomposite"
pkgver = "0.4.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = ["xorgproto", "libxfixes-devel"]
pkgdesc = "X Composite library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXcomposite-{pkgver}.tar.gz"
sha256 = "3599dfcd96cd48d45e6aeb08578aa27636fa903f480f880c863622c2b352d076"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxcomposite-devel")
def _(self):
    return self.default_devel()

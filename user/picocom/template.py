pkgname = "picocom"
pkgver = "3.1"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "CPPFLAGS += -DNO_CUSTOM_BAUD",
    f"CPPFLAGS += -DVERSION_STR={pkgver}",
]
make_use_env = True
makedepends = ["linux-headers"]
pkgdesc = "Minimal dumb-terminal emulation program like minicom"
license = "GPL-2.0-or-later"
url = "https://github.com/npat-efault/picocom"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "e6761ca932ffc6d09bd6b11ff018bdaf70b287ce518b3282d29e0270e88420bb"
# no tests available
options = ["!check"]


def install(self):
    self.install_bin("picocom")
    self.install_man("picocom.1")

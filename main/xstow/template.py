pkgname = "xstow"
pkgver = "1.1.1"
pkgrel = 1
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["automake"]
makedepends = ["ncurses-devel"]
pkgdesc = "Tool for managing software built from source"
license = "GPL-2.0-or-later"
url = "http://xstow.sourceforge.net"
source = f"https://github.com/majorkingleo/xstow/releases/download/{pkgver}/xstow-{pkgver}.tar.bz2"
sha256 = "191535eb430f0456a5de3d82ff6a5f8c4a155ad3c6a65ecf80de7acf11065278"
hardening = ["vis", "cfi"]

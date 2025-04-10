pkgname = "tcllib"
pkgver = "1.21"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "tcl"]
makedepends = ["tcl-devel"]
pkgdesc = "Tcl standard library"
license = "TCL"
url = "https://core.tcl-lang.org/tcllib"
source = f"{url}/uv/tcllib-{pkgver}.tar.xz"
sha256 = "10c7749e30fdd6092251930e8a1aa289b193a3b7f1abf17fee1d4fa89814762f"

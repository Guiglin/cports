pkgname = "userspace-rcu"
pkgver = "0.13.1"
pkgrel = 0
build_style = "gnu_configure"
make_check_args = ["-j1"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Userspace RCU library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://liburcu.org"
source = f"https://www.lttng.org/files/urcu/{pkgname}-{pkgver}.tar.bz2"
sha256 = "3213f33d2b8f710eb920eb1abb279ec04bf8ae6361f44f2513c28c20d3363083"
tool_flags = {"CFLAGS": ["-DLITTLE_ENDIAN=4321", "-DBIG_ENDIAN=1234"]}
# XXX: tests pass when run outside the suite...
options = ["!check"]

if self.profile().endian == "big":
    tool_flags["CFLAGS"] += ["-DBYTE_ORDER=1234"]
else:
    tool_flags["CFLAGS"] += ["-DBYTE_ORDER=4321"]

@subpackage("userspace-rcu-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share/doc"])

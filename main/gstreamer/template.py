pkgname = "gstreamer"
pkgver = "1.24.6"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dptp-helper-permissions=none",  # manual
    "-Dpackage-origin=https://chimera-linux.org",
    "-Ddbghelp=disabled",
    "-Dintrospection=enabled",
    "-Ddefault_library=shared",
]
make_check_args = ["--timeout-multiplier", "4"]
hostmakedepends = [
    "bison",
    "docbook-xsl-nons",
    "flex",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "libcap-progs",
    "meson",
    "pkgconf",
    "python",
    "rust",
]
makedepends = [
    "bash-completion",
    "glib-devel",
    "libcap-devel",
    "libxml2-devel",
    "rust-std",
]
pkgdesc = "Core GStreamer libraries and elements"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/gstreamer/gstreamer-{pkgver}.tar.xz"
sha256 = "64342060d7c6f9e36a35e3be38a4f5ac3b41ed93b0853619be45141ef3cc1b9d"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
file_modes = {
    "usr/libexec/gstreamer-1.0/gst-ptp-helper": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/libexec/gstreamer-1.0/gst-ptp-helper": {
        "security.capability": "cap_net_bind_service,cap_net_admin+ep",
    },
}
options = ["!cross"]


@subpackage("gstreamer-devel")
def _devel(self):
    return self.default_devel(
        extra=["usr/share/gdb", "usr/share/gstreamer-1.0"]
    )

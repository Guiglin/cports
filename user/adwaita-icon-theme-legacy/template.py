pkgname = "adwaita-icon-theme-legacy"
pkgver = "46.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "gtk+3-update-icon-cache"]
pkgdesc = "Fullcolor icon theme providing fallback for legacy apps"
license = "LGPL-3.0-or-later OR CC-BY-SA-3.0"
url = "https://gitlab.gnome.org/GNOME/adwaita-icon-theme-legacy"
source = f"$(GNOME_SITE)/adwaita-icon-theme-legacy/{pkgver[:-2]}/adwaita-icon-theme-legacy-{pkgver}.tar.xz"
sha256 = "548480f58589a54b72d18833b755b15ffbd567e3187249d74e2e1f8f99f22fb4"

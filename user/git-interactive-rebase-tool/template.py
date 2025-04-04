pkgname = "git-interactive-rebase-tool"
pkgver = "2.4.1"
pkgrel = 3
build_style = "cargo"
prepare_after_patch = True
make_build_env = {"CARGO_PKG_VERSION": pkgver}
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["libgit2-devel", "rust-std"]
pkgdesc = "Sequence editor for git interactive rebase"
license = "GPL-3.0-or-later"
url = "https://github.com/MitMaro/git-interactive-rebase-tool"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0b1ba68a1ba1548f44209ce1228d17d6d5768d72ffa991909771df8e9d42d70d"


def post_extract(self):
    self.rm("build.rs")


def pre_prepare(self):
    # the version that is in there is busted on loongarch
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.170",
        allow_network=True,
    )


def post_install(self):
    self.install_man("src/interactive-rebase-tool.1")

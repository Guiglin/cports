pkgname = "wezterm"
pkgver = "20240203"
_srcver = f"{pkgver}-110809-5046fc22"
pkgrel = 0
build_style = "cargo"
configure_args = [
    "--no-default-features",
    "--features wezterm-gui/distro-defaults,wezterm-gui/wayland",
]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
    "zlib-ng-compat-devel",
]
makedepends = [
    "fontconfig-devel",
    "freetype-devel",
    "harfbuzz-devel",
    "openssl-devel",
    "rust-std",
    "libssh2-devel",
    "libx11-devel",
    "libxkbcommon-devel",
    "wayland-devel",
    "xcb-util-devel",
    "xcb-util-image-devel",
    "xcb-util-keysyms-devel",
    "xcb-util-wm-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
depends = [
    "fonts-noto-emoji-ttf",
    "fonts-roboto-ttf",
    # f"wezterm-terminfo-{pkgver}_{pkgrel}",
]
pkgdesc = "GPU-accelerated cross-platform terminal emulator and multiplexer"
maintainer = "Guilhem Baccialone <guilhem.baccialone@zaclys.net>"
license = "MIT"
url = "https://wezfurlong.org/wezterm"
source = f"https://github.com/wez/wezterm/releases/download/{_srcver}/wezterm-{_srcver}-src.tar.gz"
sha256 = "df60b1081d402b5a9239cc4cef16fc699eab68bbbeac9c669cb5d991a6010b2c"


def post_extract(self):
    self.mv(".cargo/config", ".cargo/config.toml")


def pre_configure(self):
    from cbuild.util import cargo

    cargo.Cargo(self).invoke("update", ["time"], None, False)


def check(self):
    from cbuild.util import cargo

    cargo.Cargo(self).check(
        args=[
            "--target ${RUST_TARGET}",
            "--workspace",
            "--locked --",
            "--skip e2e::sftp",
            "--skip escape::action_size",
            "--skip surface::line::storage::test::memory_usage",
            "--skip shapecache::test::ligatures_fira",
            "--skip shapecache::test::ligatures_jetbrains",
        ]
    )

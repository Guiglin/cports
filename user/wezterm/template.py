pkgname = "wezterm"
pkgver = "20240203.110809"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "wayland,distro-defaults",
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
    "libgit2-devel",
    "libssh2-devel",
    "libx11-devel",
    "libxkbcommon-devel",
    "lua5.4-devel",
    "openssl3-devel",
    "rust-std",
    "wayland-devel",
    "xcb-imdkit-devel",
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
]
pkgdesc = "GPU-accelerated cross-platform terminal emulator and multiplexer"
maintainer = "Guilhem Baccialone <guilhem.baccialone@zaclys.net>"
license = "MIT"
url = "https://wezfurlong.org/wezterm"
source = f"https://github.com/wez/wezterm/releases/download/{pkgver.replace('.', '-')}-5046fc22/wezterm-{pkgver.replace('.', '-')}-5046fc22-src.tar.gz"
sha256 = "df60b1081d402b5a9239cc4cef16fc699eab68bbbeac9c669cb5d991a6010b2c"


def post_extract(self):
    self.mv(".cargo/config", ".cargo/config.toml")


def pre_prepare(self):
    self.do(
        "cargo",
        "update",
        "--package",
        "time",
        "--precise",
        "0.3.36",
        allow_network=True,
    )


def check(self):
    from cbuild.util import cargo

    cargo.Cargo(self).check([
        "--workspace",
        "--locked",
        "--",
        "--skip",
        "e2e::sftp",
        "--skip",
        "shapecache::test::ligatures_fira",
        "--skip",
        "shapecache::test::ligatures_jetbrains",
        "--skip",
        "shaper::harfbuzz::test::ligatures",
        "--skip",
        "shapecache::test::bench_shaping",
    ])


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/wezterm")
    self.install_bin(f"target/{self.profile().triplet}/release/wezterm-gui")
    self.install_bin(
        f"target/{self.profile().triplet}/release/wezterm-mux-server"
    )
    self.install_bin(
        f"target/{self.profile().triplet}/release/strip-ansi-escapes"
    )
    self.install_completion("assets/shell-completion/bash", "bash")
    self.install_completion("assets/shell-completion/zsh", "zsh")
    self.install_completion("assets/shell-completion/fish", "fish")
    self.install_file(
        "assets/shell-integration/wezterm.sh",
        "etc/profile.d",
        name="org_wezfurlong_wezterm.sh",
    )
    self.install_file("assets/wezterm.desktop", "usr/share/applications")
    self.install_file("assets/wezterm.appdata.xml", "usr/share/metainfo")
    self.install_file(
        "assets/wezterm-nautilus.py", "usr/share/nautilus-python/extensions"
    )
    self.install_file(
        "assets/icon/wezterm-icon.svg",
        "usr/share/icons/hicolor/scalable/apps/",
        name="org.wezfurlong.wezterm.svg",
    )
    self.install_file(
        "assets/icon/terminal.png",
        "usr/share/icons/hicolor/128x128/apps",
        name="org.wezfurlong.wezterm.png",
    )
    self.install_license("licenses/ANGLE.md")

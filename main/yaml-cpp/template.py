pkgname = "yaml-cpp"
pkgver = "0.8.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DYAML_CPP_BUILD_TESTS=ON", "-DYAML_BUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["gtest-devel"]
pkgdesc = "C++ YAML parser and emitter"
license = "MIT"
url = "https://github.com/jbeder/yaml-cpp"
source = f"https://github.com/jbeder/yaml-cpp/archive/{pkgver}.tar.gz"
sha256 = "fbe74bbdcee21d656715688706da3c8becfd946d92cd44705cc6098bb23b3a16"
hardening = ["vis"]

if self.profile().wordsize == 32 or self.profile().arch == "riscv64":
    # narrowing
    configure_args += ["-DYAML_CPP_BUILD_TESTS=OFF"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("yaml-cpp-devel")
def _(self):
    return self.default_devel()

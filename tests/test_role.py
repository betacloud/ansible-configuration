# This file is subject to the terms and conditions defined in file 'LICENSE',
# which is part of this repository.


def test_packages_are_installed(Package):
    package = Package("git")
    assert package.is_installed

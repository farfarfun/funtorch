from funtorch import __version__


def test_version_is_public():
    assert __version__ == "0.0.4"


def test_version_is_semver_like():
    parts = __version__.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)

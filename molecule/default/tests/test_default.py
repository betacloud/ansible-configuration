def test_configuration_directory(host):
    f = host.file("/opt/configuration")
    assert f.exists
    assert f.is_directory

from app.models import Host


def test_new_host():
    host = Host(
        hostname="test-hostname",
        ll_ip="fe80::932b:9856:dead:beaf/64",
        ctrl_if="eno1",
        last_seen="1534186742")
    assert host.hostname == "test-hostname"
    assert host.ll_ip == "fe80::932b:9856:dead:beaf/64"
    assert host.ctrl_if == "eno1"
    assert host.last_seen == "1534186742"

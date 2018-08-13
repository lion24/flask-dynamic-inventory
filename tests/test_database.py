from datetime import datetime
from app.models import Host


def test_host_add(session):
    host = Host(hostname="test-hostname2",
                ll_ip="fe80::cafe:babe:dead:beaf/64",
                ctrl_if="eno2",
                last_seen=datetime.now())

    session.add(host)
    session.commit()

    assert host.id > 0
    assert session.query(Host).count() > 0


def test_add_multiple_hosts(session):
    host1 = Host(hostname="test-hostname2",
                 ll_ip="fe80::dead:beef:cafe:babe/64",
                 ctrl_if="eno2",
                 last_seen=datetime.now())

    host2 = Host(hostname="test-hostname2",
                 ll_ip="fe80::cafe:babe:dead:beaf/64",
                 ctrl_if="eno2",
                 last_seen=datetime.now())

    session.add(host1)
    session.add(host2)
    session.commit()

    assert session.query(Host).count() == 2

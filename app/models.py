from app.database import db


class Host(db.Model):
    """
    Class that represent a host in a dynamic inventory

    The following attributes of a host are stored in this table:
        hostname: name of the host
        ll_ip: link-local v6 IP used by ansible to connect on that host
        ctrl_if: ctrl iface where ll_ip is bound
        last_seen: timestamp of the last update from that host.
    """

    __tablename__ = "hosts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hostname = db.Column(db.String, nullable=False)
    ll_ip = db.Column(db.String, unique=True, nullable=False)
    ctrl_if = db.Column(db.String, nullable=False)
    last_seen = db.Column(db.TIMESTAMP, nullable=False)

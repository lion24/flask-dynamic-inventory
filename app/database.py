from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# from flask_sqlalchemy import SignallingSession, SQLAlchemy, SessionBase


# class TestSignallingSession(SignallingSession):
#     def __init__(self, db, autocommit=False, autoflush=True, **options):

#         SessionBase.__init__(self,
#                              autocommit=autocommit,
#                              autoflush=autoflush,
#                              **options)

#     def commit(self):
#         self.flush()
#         self.expire_all()


# class TestSQLAlchemy(SQLAlchemy):
#     def create_session(self, options):
#         return TestSignallingSession(self, **options)

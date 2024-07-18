import os
import tempfile

import pytest
from src.main.server.server import app
# from flaskr import create_app
# from .flaskr import get_db, init_db

"""dirname = os.path.dirname(os.path.realpath(__name__))
sql_file_path = dirname + '/init/schema.sql'

with open(sql_file_path, 'rb') as f:
    _data_sql = f.read().decode('utf8')"""

"""
@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)
"""


# @pytest.fixture
def client():
    return app.test_client()


"""@pytest.fixture
def runner(app):
    return app.test_cli_runner()"""

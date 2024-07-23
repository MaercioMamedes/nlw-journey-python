from src.server.server import create_app


def test_config():
    assert not create_app().testing
    app = create_app({'TESTING': True})
    assert app.testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'hello, world!'

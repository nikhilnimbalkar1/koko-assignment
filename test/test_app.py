from unittest.mock import patch


class TestApp:
    def test_index(self, client):
        response = client.get()
        assert response.status_code == 200
        assert response.text == 'Hello Koko!'

    def test_timeout(self, client):
        response = client.get('/timeout')
        assert response.status_code == 200

import pytest
import requests

def test_running():
    try:
        response = requests.get('http://localhost:8080/sample')
        assert response.status_code == 200
        assert 'Sample "Hello, World" Application' in response.text
    except Exception as e:
        pytest.fail('No webserver listening...')

"""Tests for the API."""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_convert():
    json = {
        "template": "Hi, {{ name }}!",
        "dummy_values": False,
        "input_type": 'yaml',
        "values": "name: 'John'",
        "show_whitespaces": False,
        "trim_blocks": False,
        "lstrip_blocks": False
    }
    response = client.post("/api/v1/render", json=json)
    assert response.status_code == 200
    assert response.content == b"Hi, John!"
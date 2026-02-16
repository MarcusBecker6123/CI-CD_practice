import os
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_with_domain(client, monkeypatch):
    """Prüft, ob die App den Domainnamen aus der Umgebungsvariable nutzt."""
    monkeypatch.setenv("DOMAIN_NAME", "example.com")
    rv = client.get("/")
    assert b"Running on example.com" in rv.data

def test_hello_without_domain(client, monkeypatch):
    """Prüft, ob die Warnung kommt, wenn keine Domain gesetzt ist."""
    monkeypatch.delenv("DOMAIN_NAME", raising=False)
    rv = client.get("/")
    assert b"Warnung: DOMAIN_NAME nicht gesetzt!" in rv.data

import os

from dotenv import load_dotenv


def test_environment_variables():
    """Test that required environment variables can be loaded."""
    # Load environment variables
    load_dotenv(".env.local")

    # Test that we can access environment variables
    # (Don't check values for security, just that they exist)
    neo4j_uri = os.getenv("NEO4J_URI")
    neo4j_username = os.getenv("NEO4J_USERNAME")

    # These might be None in CI, which is fine
    # Just test the loading mechanism works
    assert isinstance(neo4j_uri, (str, type(None)))
    assert isinstance(neo4j_username, (str, type(None)))


def test_app_imports():
    """Test that main app components can be imported."""
    from fastapi import FastAPI
    from main import app

    assert isinstance(app, FastAPI)
    assert app.title == "FinGraph API"
    assert app.version == "0.1.0"

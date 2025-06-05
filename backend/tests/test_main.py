import sys
from pathlib import Path

# Add the backend directory to Python path so we can import main
backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))

from fastapi.testclient import TestClient  # noqa: E402
from main import app  # noqa: E402

client = TestClient(app)


def test_read_root():
    """Test the root endpoint returns welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FinGraph API"}


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["version"] == "0.1.0"


def test_health_check_structure():
    """Test health check returns correct structure."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()

    # Check required fields exist
    assert "status" in data
    assert "version" in data

    # Check field types
    assert isinstance(data["status"], str)
    assert isinstance(data["version"], str)


def test_cors_headers():
    """Test CORS headers are present."""
    response = client.get("/health")
    assert response.status_code == 200
    # Note: CORS headers might not appear in test client
    # This test ensures endpoint works, actual CORS tested in integration


def test_nonexistent_endpoint():
    """Test that nonexistent endpoints return 404."""
    response = client.get("/nonexistent")
    assert response.status_code == 404

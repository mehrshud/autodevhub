# tests/__init__.py
import pytest
from unittest.mock import Mock
from typing import Dict

from autodevhub import User, Config

@pytest.fixture
def user_data() -> Dict:
    """Mock user data."""
    return {"id": 1, "name": "John Doe", "email": "john@example.com"}

@pytest.fixture
def config_data() -> Dict:
    """Mock config data."""
    return {"debug": True}

def test_user_init(user_data: Dict) -> None:
    """Test User initialization."""
    # Arrange
    user = User(user_data["id"], user_data["name"], user_data["email"])
    
    # Act and Assert
    assert user.id == user_data["id"]
    assert user.name == user_data["name"]
    assert user.email == user_data["email"]

def test_config_init(config_data: Dict) -> None:
    """Test Config initialization."""
    # Arrange
    config = Config(config_data["debug"])
    
    # Act and Assert
    assert config.debug == config_data["debug"]

def test_user_negative_id(user_data: Dict) -> None:
    """Test User with negative id."""
    # Act and Assert
    with pytest.raises(ValueError):
        User(-1, user_data["name"], user_data["email"])

def test_config_negative_debug(config_data: Dict) -> None:
    """Test Config with negative debug."""
    # Act and Assert
    with pytest.raises(ValueError):
        Config(-1)

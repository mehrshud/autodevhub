# tests/conftest.py
import pytest
from unittest.mock import Mock
from typing import Dict

@pytest.fixture
def mock_user() -> Dict:
    return {"id": 1, "name": "John Doe", "email": "johndoe@example.com"}

@pytest.fixture
def mock_config() -> Dict:
    return {"debug": True}

def test_user_creation(mock_user: Dict) -> None:
    # Arrange
    user = mock_user
    
    # Act
    # In this case, we're just testing the fixture, so no action needed
    
    # Assert
    assert user["id"] == 1
    assert user["name"] == "John Doe"
    assert user["email"] == "johndoe@example.com"

def test_config_debug(mock_config: Dict) -> None:
    # Arrange
    config = mock_config
    
    # Act
    # In this case, we're just testing the fixture, so no action needed
    
    # Assert
    assert config["debug"] is True

def test_invalid_user() -> None:
    # Arrange
    user = {"id": "a", "name": 123, "email": None}
    
    # Act
    # In this case, we're just testing the data, so no action needed
    
    # Assert
    with pytest.raises(TypeError):
        assert user["id"] == 1
        assert user["name"] == "John Doe"
        assert user["email"] == "johndoe@example.com"

def test_invalid_config() -> None:
    # Arrange
    config = {"debug": "a"}
    
    # Act
    # In this case, we're just testing the data, so no action needed
    
    # Assert
    with pytest.raises(TypeError):
        assert config["debug"] is True

@pytest.mark.parametrize("invalid_input", ["a", None, True, False])
def test_user_id_validation(mock_user: Dict, invalid_input) -> None:
    # Arrange
    mock_user["id"] = invalid_input
    
    # Act and Assert
    with pytest.raises(TypeError):
        assert isinstance(mock_user["id"], int)

@pytest.mark.parametrize("invalid_input", ["a", None, True, False])
def test_config_debug_validation(mock_config: Dict, invalid_input) -> None:
    # Arrange
    mock_config["debug"] = invalid_input
    
    # Act and Assert
    with pytest.raises(TypeError):
        assert isinstance(mock_config["debug"], bool)

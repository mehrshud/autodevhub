# tests/test_core.py

import pytest
from auto_dev_hub.core import User, Config
from unittest.mock import MagicMock

@pytest.fixture
def user():
    return User(id=1, name="Test User", email="test@example.com")

@pytest.fixture
def config():
    return Config(debug=True)

def test_user_creation(user: User):
    # Arrange
    expected_id = 1
    expected_name = "Test User"
    expected_email = "test@example.com"

    # Act
    actual_id = user.id
    actual_name = user.name
    actual_email = user.email

    # Assert
    assert actual_id == expected_id
    assert actual_name == expected_name
    assert actual_email == expected_email

def test_config_debug_mode(config: Config):
    # Arrange
    expected_debug = True

    # Act
    actual_debug = config.debug

    # Assert
    assert actual_debug == expected_debug

def test_user_invalid_email():
    # Arrange
    user = User(id=1, name="Test User", email="invalid")

    # Act and Assert
    with pytest.raises(ValueError):
        user.email = "invalid"

def test_config_invalid_debug_mode():
    # Arrange
    config = Config(debug="invalid")

    # Act and Assert
    with pytest.raises(TypeError):
        config.debug = "invalid"

def test_user_external_dependency(mocker: pytest.fixture):
    # Arrange
    mocker.patch("auto_dev_hub.core.send_email", return_value=None)

    # Act
    user = User(id=1, name="Test User", email="test@example.com")
    user.send_email()

    # Assert
    assert user.send_email.call_count == 1

# tests/test_api.py
from typing import Dict
import pytest
from api import Config, User
from unittest.mock import Mock

def test_create_config_success_arrange_act_assert():
    # Arrange
    debug = True
    config = Config(debug)

    # Act
    result = config.debug

    # Assert
    assert result == debug

def test_create_config_failure_arrange_act_assert():
    # Arrange
    debug = True
    with pytest.raises(TypeError):
        # Act
        Config(debug, invalid_param="test")

def test_create_user_success_arrange_act_assert():
    # Arrange
    user_id = 1
    name = "Test User"
    email = "test@example.com"
    user = User(user_id, name, email)

    # Act
    result_id = user.id
    result_name = user.name
    result_email = user.email

    # Assert
    assert result_id == user_id
    assert result_name == name
    assert result_email == email

def test_create_user_failure_arrange_act_assert():
    # Arrange
    user_id = 1
    name = "Test User"
    email = "test@example.com"
    with pytest.raises(TypeError):
        # Act
        User(user_id, name, email, invalid_param="test")

@pytest.mark.parametrize("test_input, expected", [
    ({"id": 1, "name": "Test User", "email": "test@example.com"}, True),
    ({"id": "invalid", "name": "Test User", "email": "test@example.com"}, False),
    ({"id": 1, "name": 123, "email": "test@example.com"}, False),
    ({"id": 1, "name": "Test User", "email": 123}, False),
])
def test_create_user_valid_input_arrange_act_assert(test_input: Dict, expected: bool):
    # Arrange
    try:
        # Act
        User(test_input["id"], test_input["name"], test_input["email"])
        result = True
    except TypeError:
        result = False

    # Assert
    assert result == expected

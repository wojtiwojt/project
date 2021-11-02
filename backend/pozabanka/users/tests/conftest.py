import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def test_user_data_for_signup():
    return {
        "email": "test.email@email.com",
        "password1": "user_password123",
        "password2": "user_password123",
    }


@pytest.fixture
def test_user_data():
    return {"email": "test.email@email.com", "password": "user_password123"}


@pytest.fixture
def create_test_user(test_user_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**test_user_data)
    test_user.set_password(test_user_data.get("password"))
    return test_user


@pytest.fixture
def authenticated_user(client, test_user_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**test_user_data)
    test_user.set_password(test_user_data.get("password"))
    test_user.save()
    client.login(**test_user_data)
    return test_user

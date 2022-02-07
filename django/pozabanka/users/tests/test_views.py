from django import urls
from django.contrib.auth import get_user_model
import pytest


@pytest.mark.parametrize("param", [("index-page"), ("registration"), ("login")])
def test_render_non_login_required_views(client, param):
    temp_url = urls.reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_registration_view(client, test_user_data_for_signup):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    signup_url = urls.reverse("registration")
    print(signup_url)
    response = client.post(signup_url, test_user_data_for_signup)
    assert user_model.objects.count() == 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_login_view(client, create_test_user, test_user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse("login")
    response = client.post(
        login_url,
        {
            "username": test_user_data.get("email"),
            "password": test_user_data.get("password"),
        },
    )
    assert response.status_code == 302
    assert response.url == urls.reverse("index-page")


@pytest.mark.django_db
def test_user_logout_view(client, authenticated_user):
    logout_url = urls.reverse("logout")
    response = client.get(logout_url)
    assert response.status_code == 300

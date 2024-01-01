from icecream import ic
import pytest
from app import schemas

# from .database import *
from app.config import settings

from jose import jwt


@pytest.fixture()
def test_user(client):
    user_data = {"email": "adityakeshari292002@gmail.com", "password": "password123"}

    res = client.post("/users/", json=user_data)  # create user
    assert res.status_code == 201
    ic(res.json())
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user


def test_create_user(client):
    res = client.post(
        "/users/",
        json={
            "email": "hello123@gmail.com",
            "password": "password123",
        },  # /users -->redirect status code 307 # /users/
    )

    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201


# def test_login_user(client, test_user):
#     res = client.post(
#         "/auth/login",
#         data={"username": test_user["email"], "password": test_user["password"]},
#     )
#     print(res.json())

#     assert res.status_code == 200


def test_login_user(test_user, client):
    res = client.post(
        "/auth/login/",
        data={"username": test_user["email"], "password": test_user["password"]},
    )
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(
        login_res.access_token, settings.secret_key, algorithms=[settings.algorithm]
    )
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("wrongemail@gmail.com", "password123", 403),
        ("sanjeev@gmail.com", "wrongpassword", 403),
        ("wrongemail@gmail.com", "wrongpassword", 403),
        (None, "password123", 422),
        ("sanjeev@gmail.com", None, 422),
    ],
)
def test_incorrect_login(client, email, password, status_code):
    res = client.post("/auth/login/", data={"username": email, "password": password})
    ic(email, res.status_code)
    assert res.status_code == status_code
    # assert res.json().get('detail') == 'Invalid Credentials'

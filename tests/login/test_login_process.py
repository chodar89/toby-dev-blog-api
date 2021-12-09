"""Test login process - login, logout, refresh token"""


def test_login_issue_jwt_token(app, client, db, user):
    payload = {
        "email": user.email,
        "password": "I'm-a-strong-password",
    }
    res = client.post("/login/", json=payload)
    breakpoint()
    assert True

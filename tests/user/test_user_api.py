"""Test User API resources"""


def test_user_list__get_200(app, client, db, user):
    res = client.get("/users/")
    res_json = res.get_json()
    assert res.status_code == 200
    assert len(res_json) == 1
    assert res_json[0]["id"] == str(user.id)


def test_user_list__post_200(app, client, db):
    payload = [{"email": "gandalf@gmail.com", "password": "MinesofMoria68"}]
    res = client.post("/users/", json=payload)
    res_json = res.get_json()
    assert res.status_code == 200
    assert len(res_json) == 1


def test_user_list__post_422(app, client, db):
    payload = [{"i_should_not_be_here": "me_too"}]
    res = client.post("/users/", json=payload)
    assert res.status_code == 422

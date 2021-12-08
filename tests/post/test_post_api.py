"""Test Post API resources"""
from datetime import datetime

from toby_dev_blog.models import Post


def test_post_list__get_200(app, client, db, post):
    res = client.get("/posts/")
    res_json = res.get_json()
    assert res.status_code == 200
    assert len(res_json) == 1
    assert res_json[0]["id"] == str(post.id)


def test_post_list__post_200(app, client, db):
    res = client.post("/posts/")
    payload = [
        {
            "slug": "bag-end",
            "title": "Short story about Bag End a Hobbit-hole",
            "meta_title": "Lord of The Rings. Short story about Bag End",
            "description": (
                "Bag End or Bag-End was a smial in Hobbiton, the residence of"
                " the Baggins Family and later the Gardner Family."
            ),
            "content": (
                "In a hole in the ground there lived a Hobbit. Not a nasty,"
                " dirty, wet hole, filled with the ends of worms and an oozy"
                " smell, nor yet a dry, bare, sandy hole with nothing in it to"
                " sit down on or to eat: it was a Hobbit-hole, and that means"
                " comfort."
            ),
            "is_featured": True,
            "is_published": True,
            "read_time": 2,
            "published_at": str(datetime.utcnow()),
        }
    ]
    res = client.post("/posts/", json=payload)
    res_json = res.get_json()
    assert res.status_code == 200
    assert res_json[0]["slug"] == "bag-end"


def test_post_list__post_422(app, client, db):
    payload = [{"i_should_not_be_here": "me_too"}]
    res = client.post("/posts/", json=payload)
    assert res.status_code == 422


def test_post__get_200(app, client, db, post):
    res = client.get(f"/posts/{post.slug}")
    res_json = res.get_json()
    assert res.status_code == 200
    assert res_json["id"] == str(post.id)


def test_post__get_404(app, client, db):
    res = client.get("/posts/unknown-slug")
    assert res.status_code == 404


def test_post__delete_204(app, client, db, post):
    res = client.delete(f"/posts/{post.slug}")

    assert res.status_code == 204
    assert len(Post.query.all()) == 0


def test_post__delete_404(app, client, db):
    res = client.delete("/posts/unknown-slug")
    assert res.status_code == 404


def test_post__patch_200(app, client, db, post):
    payload = {"title": "Look at me! I'm a new title!"}
    res = client.patch(f"/posts/{post.slug}", json=payload)
    res_json = res.get_json()
    assert res.status_code == 200
    assert res_json["id"] == str(post.id)
    assert res_json["title"] == payload["title"]


def test_post__patch_404(app, client, db):
    res = client.patch("/posts/unknown-slug")
    assert res.status_code == 404

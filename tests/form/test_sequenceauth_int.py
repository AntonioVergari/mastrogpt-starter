import os, requests as req
def test_sequenceauth():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/form/sequenceauth"
    res = req.get(url).json()
    assert res.get("output") == "sequenceauth"

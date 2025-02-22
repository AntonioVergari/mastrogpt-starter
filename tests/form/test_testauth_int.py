import os, requests as req
def test_testauth():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/form/testauth"
    res = req.get(url).json()
    assert res.get("output") == "testauth"

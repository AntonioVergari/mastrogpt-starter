import sys 
sys.path.append("packages/form/testauth")
import testauth

def test_testauth():
    res = testauth.testauth({})
    assert res["output"] == "testauth"

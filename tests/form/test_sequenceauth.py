import sys 
sys.path.append("packages/form/sequenceauth")
import sequenceauth

def test_sequenceauth():
    res = sequenceauth.sequenceauth({})
    assert res["output"] == "sequenceauth"

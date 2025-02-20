import re, os, requests as req
#MODEL = "llama3.1:8b"
MODEL = "phi4:14b"

FORM = [
  {
    "name": "queen",
    "label": "Add a queen",
    "type": "checkbox",
  },
  {
    "name": "bishop",
    "label": "Add bishops",
    "type": "checkbox",
  },
  {
    "name": "tower",
    "label": "Add towers",
    "type": "checkbox",
  },
  {
    "name": "knight",
    "label": "Add knights",
    "type": "checkbox",
  },
]

def chat(args, inp):
  host = args.get("OLLAMA_HOST", os.getenv("OLLAMA_HOST"))
  auth = args.get("AUTH", os.getenv("AUTH"))
  url = f"https://{auth}@{host}/api/generate"
  msg = { "model": MODEL, "prompt": inp, "stream": False}
  res = req.post(url, json=msg).json()
  out = res.get("response", "error")
  return  out
 
def extract_fen(out):
  pattern = r"([rnbqkpRNBQKP1-8]+\/){7}[rnbqkpRNBQKP1-8]+"
  fen = None
  m = re.search(pattern, out, re.MULTILINE)
  if m:
    fen = m.group(0)
  return fen

def puzzle(args):
  out = "If you want to see a chess puzzle, type 'puzzle'. To display a fen position, type 'fen <fen string>'."
  inp = args.get("input", "")
  res = {}
  print(f"primo:{inp}")
  if inp == "puzzle":
    inp = "generate a chess puzzle in FEN format"
    res["form"] = FORM
    handle_puzzle_gen(args, inp, res)
  # Adding form data check
  elif type(inp) is dict and "form" in inp:
    form_data = inp["form"]
    inp = "generate a chess puzzle in FEN format."
    if form_data["queen"] == "true":
      inp += "add a queen on each side."
    if form_data["knight"] == "true":
      inp += "add max two knight on each side."
    if form_data["tower"] == "true":
      inp += "add max two a tower on each side."
    if form_data["bishop"] == "true":
      inp += "add max two a bishop on each side."
    print(inp)
    handle_puzzle_gen(args, inp, res)
  elif inp.startswith("fen"):
    fen = extract_fen(inp)
    if fen:
       out = "Here you go."
       res['chess'] = fen
  elif inp != "":
    out = chat(args, inp)
    fen = extract_fen(out)
    print(out, fen)
    if fen:
      res['chess'] = fen

  res["output"] = out
  return res


def handle_puzzle_gen(args:dict, inp:str, res:dict):
  out = chat(args, inp)
  fen = extract_fen(out)
  if fen:
      print(fen)
      res['chess'] = fen
  else:
    out = "Bad FEN position."
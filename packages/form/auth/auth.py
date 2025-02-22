import os, redis

def check_auth(args):
  [user, secret] = args.get("token", "_:_").split(":")
  rd = redis.from_url(args.get("REDIS_URL", os.getenv("REDIS_URL")))
  check = rd.get(f"{args.get("REDIS_PREFIX", os.getenv("REDIS_PREFIX"))}TOKEN:{user}") or b''
  return check.decode("utf-8") != secret
  
def auth(args):
  print("Token:", args.get("token", "<none>"))
  result =  check_auth(args)
  if result:
    args["authorized"] = False
  else:
    args["authorized"] = True
  return args
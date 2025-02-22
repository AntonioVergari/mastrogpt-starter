#--kind python:default
#--web true
import testauth
def main(args):
  if(args["authorized"]):
    return { "body": testauth.testauth(args) }
  else:
    return {"body": {"output": "unauthorized"} }

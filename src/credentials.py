
from os.path import expanduser
import os, route53, os, sys

def get_credentials():
  #Check if aws credentials exist on the user home directory 
  fullname = os.path.abspath(os.path.join(expanduser("~"),".aws")) + "/credentials"
  aws_credentials=[]

  if os.path.isfile(fullname):
    for i in open(fullname):
      if "=" in i:
        aws_credentials.append(i.split("=")[1].rstrip("\n"))

 # If no credentials exist please prompt the user to enter credentials

  else:
    aws_credentials.append(input("Enter AWS Access Key ID: "))
    aws_credentials.append(input("Enter AWS Secret Access: "))
  return aws_credentials


def connection(aws_credentials):
  try:
    connect = route53.connect(
      aws_access_key_id=aws_credentials[0],
      aws_secret_access_key=aws_credentials[1],
    )
    return connect


  except:
    print("Invalid or Incorrect Credentials")
    sys.exit(1)    

  


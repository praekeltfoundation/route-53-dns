import route53
from credentials import get_credentials,connection
from exists import check
from verify import verify
import sys
 
if __name__=="__main__":
  passed_list=[word.lower() for word in sys.argv]
  print(passed_list)
  if len(passed_list)==1:
    verify(passed_list[1:])
  else:
    aws_credentials=get_credentials()
    verify(passed_list[1:])
  


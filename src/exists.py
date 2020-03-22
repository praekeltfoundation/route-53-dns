import route53

def check(conn,record):
  record=str(record.lower())

  if record[-1]!=".":
    record+="."
   
  for zone in conn.list_hosted_zones():
    for record_set in zone.record_sets:
      if record_set.name==record:
        print ("Real Truth")
        return True
   
  return False

    


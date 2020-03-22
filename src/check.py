import route53, sys
from credentials import connection, get_credentials

def common():
  aws_credentials=get_credentials()
  return connection(aws_credentials)

def check_domain(record_set, ip_address):
  no_hosted_zone=True
  list_ip_address=[]
  list_ip_address.append(ip_address)
  record=record_set[:-1].split(".")
  conn=common()
  
  for zone in conn.list_hosted_zones():
    no_hosted_zone=True
    domain=zone.name[:-1]
    if domain.split(".")==record[-2:] or domain.split(".")==record[-3:] or domain.split(".")==record[-4:] :
      try:
            
        new_record, change_info = zone.create_a_record(
          name=record_set,
          values=list_ip_address,
        )
        no_hosted_zone=False
        break
      except:
         print("Could not create A Record")

  msg="Could not Find the hosted zone for the record/Record Already exists" if no_hosted_zone==True else "Hosted zone found"
  print(msg) 
 
      
def list_records(parameter_to_list, control_variable):
  conn=common()
 
  if parameter_to_list=="record" or parameter_to_list=="record-set":
    for zone in conn.list_hosted_zones():
      for record_set in zone.record_sets:
        if  control_variable=="all" or control_variable=="a":
          print(record_set.name)
        else:
          if control_variable[-1]!=".":
            control_variable += "."
          if record_set.name == control_variable:
            print (record_set.name)        
            break

  elif parameter_to_list=="hosted-zone" or parameter_to_list=="hosted":
    for zone in conn.list_hosted_zones():
      if  control_variable=="all" or control_variable=="a":
        print (zone.name)
      else:
        if control_variable[-1]!=".":
          control_variable += "."
        if zone.name == control_variable:
          print (zone.name)
          break   
  
  else:
    print("Invalid Input")

def change_records(to_change,record,new):
  conn=common()
  control=False
  if to_change=="record" or to_change=="r":
    for zone in conn.list_hosted_zones():
      for record_set in zone.record_sets:
        if record_set.name == record:
          try:
            record_set.name = new
            record_set.save()
            control=True
            break
          except:
            print("Record found but could not be changed to the new value")
            break


  if to_change=="ip" or to_change=="ipaddr":
    for zone in conn.list_hosted_zones():
      for record_set in zone.record_sets:
        if record_set.name == record:
          list_new=[]
          list_new.append(new)
          try:
            record_set.values = list_new
            record_set.save()
            control=True
            break
          except:
            print("Could not change IP Address")
            break

  else:
    print("Invalid Input Entered")
    sys.exit(0)

  msg="Record/IP Successfully changed" if control==True else "Record not found"
  print(msg)

def  delete_records(record):
  conn=common()
  for zone in conn.list_hosted_zones():
    for record_set in zone.record_sets:
      if record_set.name == record:
        record_set.delete()

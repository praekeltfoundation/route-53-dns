import sys
from check import common
from check import check_domain, list_records, change_records, delete_records

def verify(argv):
  print(len(argv))
  help = '''route53 is a  tool for management of DNS Records\n\n
   Basic Commands: 
    Please add -h or --help for Assistance
    Options:
      create record/record-set x.x.x.x. 3.3.3.3    => Creates A Record[example create record/record-set example.domain.com. 7.7.7.7 ]
      create hosted/hosted-zone x.x.               => Creates Hosted Zone [Example create hosted/hosted-zone example.com. ]
      list hosted/hosted-zone[s] all               => Lists all Hosted Zones [Example list hosted/hosted-zone all]
      list  record/record-set[s] all               => Lists all Record Sets in Hosted Zones [Example list record/record-set all]
      list hosted/hosted-zone x.x.x.x.             => Lists  Hosted Zone x.x.x.x if present  [Example list hosted/hosted-zone example.com. ]
      list record/record-set x.x.x.x.              => Lists Record Set x.x.x.x in Hosted Zones if present [Example list record/record-set team.example.com]
      change => Change Record Set
      delete => Delete Record Set
               '''

  def create():
    comment= "Created hosted zone " +  argv[2] 
    count=argv[2].count(".")
    if argv[1].strip()=="hosted-zone" or argv[1].strip()=="h" or argv[1].strip()=="hosted" and count>=2 and len(argv)==3:
      if argv[2].strip()[-1]!=".":
        argv[2] += "."
      conn=common()
      try:
        new_zone, change_info = conn.create_hosted_zone(
          argv[2], comment=comment
        )
        print("Zone ID ", new_zone.id)

      except:
        print("Cannot create hosted zone")
        sys.exit(1)

    elif argv[1].strip()=="record" or argv[1].strip()=="record-set" and count>=2 and  len(argv)==4:
      if len(argv[3].split("."))==4:
        if argv[2][-1] != ".":
          argv[2] += "."
        check_domain(argv[2],argv[3])

      else:
        print("Enter IP Address as X.X.X.X") 
        sys.exit(1)
    else:
      print("Invalid Credentials Entered\n")
      print(help.split(":")[2] )
      sys.exit(1)
          
  def list():
    try:
      list_records(argv[1],argv[2])
    except:
      print("Error in number of variables entered")
      sys.exit(1)

  def change():
    try:
      if (argv[2][-1] != "."):
        argv[2] += "."
      if argv[3][-1] != "." and (argv[1]=="record" or argv[1]=="r"):
        argv[3] += "."
      change_records(argv[1],argv[2],argv[3])
    except:
      print("invalid credentials")
      sys.exit(1)

  def delete():
    try:
      if (argv[1][-1] != "."):
        argv[1] += "."
      delete_records(argv[1])
    except:
      print("Enter Valid Input")

  if len(argv)<1:
    print (help)
    sys.exit(0)

  if len(argv)==1:
    if str(argv[0].strip())=="-h" or str(argv[0].strip())=="--help":
      print(help.split(":")[2] )
      sys.exit(0)
      
    else:
      print(help.split(":")[2] )    

  elif argv[0].strip()=="create" or argv[0].strip()=="cr":
    create()
   
  elif argv[0].strip()=="list" or argv[0].strip()=="ls":
    list()

  elif argv[0].strip()=="change" or argv[0].strip()=="ch":
    change()
   
  elif str(argv[0].strip())=="delete" or str(argv[0].strip())=="dl":
    delete()

  else:
    print(help.split(":")[2] )
    sys.exit(1)

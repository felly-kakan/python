command=""
started=False
while True:
    command=(input(">: ")).lower()
    if command =="start":
       if started:
          print("car already started")
       else:
         started=True
         print("car started ...Ready to Go")
    elif command=="stop":
       if not started:
          print("car already stoped")
       else:
         started=False
         print("car stopped.")
    elif command=="help":
      print('''
start-car started
stop-car stopped
quit-to exit
           ''' )

    elif command=="quit":
       break
    else:
     print("I dont understand that......")    
  


def task():
    todo_list=[]
    print("===***welcome to the main menu of your todo list***===")

    total_task=int(input("ENTER HOW MANY TASK YOU WANT TO DO TODAY:"))
    for i in range(1,total_task+1):
     task_name =input(f"ENTER TASK{i}=")
     todo_list.append({
         "task":task_name,
         "status":"PENDING"
     })

    print("\nYOUR TODAY'S TASK: ",task_name)

    for index, task in enumerate(todo_list,1):
                      print(f"{index}:{task ['task']} -{task['status']}")



    while True:
        print("===== TODO MENU =====")
        print("1.ADD NEW TASK")
        print("2.VIEW THE TASK")
        print("3.REMOVE THE TASK")
        print("4.MArK THE TASK AS DONE")
        print("5.UPDATE THE TASK")
        print("6.EXIT")

        choice = input("ENTER YOUR CHOICE: ")

# ADD TASK
        if choice=="1":

          add=input("ENTER TASK YOU WANT TO ADD:")
          todo_list.append({
             "task":add,
             "status":"pending"
          })
    
          print("...TASK HAS BEEN SUCCESSFULLY ADDED...")


        elif choice=="2":
            
              if len(todo_list)==0:
                  print("NO PENDING TASK LEFT")
              else:
                print("\n YOUR TODO LIST:")
                for index, task in enumerate(todo_list,1):
                  print(f"{index}:{task ['task']} -{task['status']}")

# REMOVE TASK
        elif choice=="3":
        
          if len(todo_list)==0:
               print("\n LIST IS EMPTY")
          else:
               try: 
                   search_index=int(input("ENTER THE TASK NUMBER THAT YOU WANT TO REMOVE: "))-1
                   if 0<=search_index<len(todo_list):
                     remove_task=todo_list.pop(search_index)
                     print(f"TASK REMOVED IS: {remove_task['task']}")
                   else:
                    print("INVALID TASK NUMBER.")
               except ValueError:
                 print("PLEASE ENTER VALID TASK NUMBER")      

# /MARK AS DONE
        elif choice=="4":
           if len(todo_list)==0:
              print("\n LIST IS EMPTY")
           else:
            try: 
              search_index=int(input("ENTER THE TASK NUMBER THAT YOU WANT TO mark as done: "))-1
              if 0<=search_index<len(todo_list):
               todo_list[search_index]["status"]='done'
               print(f"TASK '{todo_list[search_index]['task']}'"" HAS BEEN MARKED AS DONE")
              else:
                print("INVALID TASK NUMBER.")
            except ValueError:
                print("PLEASE ENTER VALID TASK NUMBER")      

# UPDATE TASK 
        elif choice=="5":
           if len(todo_list)==0:
             print("\n LIST IS EMPTY")
           else:
            try:
                   search_index=int(input("ENTER THE NUMBER OF THE TASK YOU WANT TO UPDATE:"))-1
                   if 0<=search_index<len(todo_list):
                      up=input("enter the new task:")
                      todo_list[search_index]["TASK"]=up
                      print(f"updated task:{up}")
                   else:
                     print("INVALID TASK NUMBER.")
            except ValueError:
                print("PLEASE ENTER VALID TASK NUMBER.")

        elif choice=="6":
          print("closing the program...")
          break
        else:
         print("INVALID CHOICE,PLEASE ENTER 1-6")

task()

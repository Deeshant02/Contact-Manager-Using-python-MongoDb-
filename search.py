import pymongo
import datetime
from nextmenu import NextMenu

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["contact_manager"]
collection = db["contact_no"]

class SearchContact():
    def __init__(self):
        print('''1. Search Contact By Name
2. Search Contact By Contact No.
3. Search Contacts By Category''')

    def searchContactByName(self,name):
        self.name = name

        i = 1
        while(i<=111):
            print("-",end="")
            i+=1
        i=1
        while(i<=48):
            print(" ",end="")
            i+=1
        print("Search By Name ",end="")
        i=1
        while(i<=48):
            print(" ",end="")
            i+=1
        i = 1
        while(i<=111):
            print("-",end="")
            i+=1

        print("Sr no.",end="")

        i=1
        while(i<=5):
            print(" ",end="")
            i+=1
        print("Name",end="")
        i=1
        while(i<=26):
            print(" ",end="")
            i+=1
        
        i=1
        while(i<=2):
            print(" ",end="")
            i+=1
        print("Contact No.",end="")
        i=1
        while(i<=4):
            print(" ",end="")
            i+=1
        
        i=1
        while(i<=1):
            print(" ",end="")
            i+=1
        print("Category",end="")
        i=1
        while(i<=17):
            print(" ",end="")
            i+=1
        
        i=1
        while(i<=7):
            print(" ",end="")
            i+=1
        print("E-mail",end="")
        i=1
        while(i<=7):
            print(" ",end="")
            i+=1

        # lst = (collection.find({"first_name": self.name}))

        if(collection.find_one({"first_name": self.name}) != None):
            lst = (collection.find({"first_name": self.name}))
        else:
            lst = (collection.find({"last_name": self.name}))

        print()
        for i in lst:
            i
            srno = i["_id"]
            fname = i["first_name"]
            lname = i["last_name"]
            name = f"{fname} {lname}"
            mob = i["contact_no"]
            email = i["e_mail"]
            category = i["category"]

            print(srno,end="")
            strsrno = str(srno)
            for i in range(1,(7-len(strsrno))):
                print(" ",end="")
            
            print(name,end="")
            for i in range(1,(36-len(name))):
                print(" ",end="")
            
            print(f"+91 {mob}",end="")
            for i in range(1,5):
                print(" ",end="")
            
            print(category,end="")
            for i in range(1,(22-len(category))):
                print(" ",end="")
            
            print(email)

        input("Press 'Enter' to go back to main menu...")

    def searchContactByMob(self,mob):
        self.mob = mob
        i = 1
        while(i<=111):
            print("-",end="")
            i+=1
        i=1
        while(i<=45):
            print(" ",end="")
            i+=1
        print("Search By Contact No.",end="")
        i=1
        while(i<=45):
            print(" ",end="")
            i+=1
        i = 1
        while(i<=111):
            print("-",end="")
            i+=1

        print("Sr no.",end="")

        i=1
        while(i<=5):
            print(" ",end="")
            i+=1
        print("Name",end="")
        i=1
        while(i<=26):
            print(" ",end="")
            i+=1
        
        i=1
        while(i<=2):
            print(" ",end="")
            i+=1
        print("Contact No.",end="")
        i=1
        while(i<=4):
            print(" ",end="")
            i+=1
        
        i=1
        while(i<=1):
            print(" ",end="")
            i+=1
        print("Category",end="")
        i=1
        while(i<=17):
            print(" ",end="")
            i+=1
        
        i=1
        while(i<=7):
            print(" ",end="")
            i+=1
        print("E-mail",end="")
        i=1
        while(i<=7):
            print(" ",end="")
            i+=1

        # lst = (collection.find({"first_name": self.name}))

        lst = (collection.find({"contact_no": self.mob}))

        print()
        for i in lst:
            i
            srno = i["_id"]
            fname = i["first_name"]
            lname = i["last_name"]
            name = f"{fname} {lname}"
            mob = i["contact_no"]
            email = i["e_mail"]
            category = i["category"]

            print(srno,end="")
            strsrno = str(srno)
            for i in range(1,(7-len(strsrno))):
                print(" ",end="")
            
            print(name,end="")
            for i in range(1,(36-len(name))):
                print(" ",end="")
            
            print(f"+91 {mob}",end="")
            for i in range(1,5):
                print(" ",end="")
            
            print(category,end="")
            for i in range(1,(22-len(category))):
                print(" ",end="")
            
            print(email)

        input("Press 'Enter' to go back to main menu...")

    def searchByCategory(self,category):
        self.category = category
        i = 1
        while(i<=111):
            print("-",end="")
            i+=1
        i=1
        while(i<=46):
            print(" ",end="")
            i+=1
        print("Search By Category ",end="")
        i=1
        while(i<=46):
            print(" ",end="")
            i+=1
        i = 1
        while(i<=111):
            print("-",end="")
            i+=1

        print("Sr no.",end="")

        i=1
        while(i<=5):
            print(" ",end="")
            i+=1
        print("Name",end="")
        i=1
        while(i<=26):
            print(" ",end="")
            i+=1
        
        i=1
        while(i<=2):
            print(" ",end="")
            i+=1
        print("Contact No.",end="")
        i=1
        while(i<=4):
            print(" ",end="")
            i+=1
        
        i=1
        while(i<=1):
            print(" ",end="")
            i+=1
        print("Category",end="")
        i=1
        while(i<=17):
            print(" ",end="")
            i+=1
        
        i=1
        while(i<=7):
            print(" ",end="")
            i+=1
        print("E-mail",end="")
        i=1
        while(i<=7):
            print(" ",end="")
            i+=1

        # lst = (collection.find({"first_name": self.name}))

        lst = (collection.find({"category": self.category}))

        print()
        for i in lst:
            i
            srno = i["_id"]
            fname = i["first_name"]
            lname = i["last_name"]
            name = f"{fname} {lname}"
            mob = i["contact_no"]
            email = i["e_mail"]
            category = i["category"]

            print(srno,end="")
            strsrno = str(srno)
            for i in range(1,(7-len(strsrno))):
                print(" ",end="")
            
            print(name,end="")
            for i in range(1,(36-len(name))):
                print(" ",end="")
            
            print(f"+91 {mob}",end="")
            for i in range(1,5):
                print(" ",end="")
            
            print(category,end="")
            for i in range(1,(22-len(category))):
                print(" ",end="")
            
            print(email)

        input("Press 'Enter' to go back to main menu...")
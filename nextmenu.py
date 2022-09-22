import pymongo
import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["contact_manager"]
collection = db["contact_no"]

class NextMenu:
    def __init__(self):
        pass

    def addContact(self,fname,lname,mob,email,category,time):
        self.fname = fname
        self.lname = lname
        self.mob = mob
        self.email = email
        self.category = category
        self.time = time

        lst = collection.find()
        
        n=0
        for i in lst:
            if(i["contact_no"] == self.mob):
                fname = i["first_name"]
                lname = i["last_name"]
                name = f"{fname} {lname}"
                print(f"Given contact no. is already saved in contact list with name '{name}'")
                return
            n+=1

        srno = n+1

        while(collection.find_one({"_id": srno}) != None):
            srno+=1

        dictionary = {
            "_id": srno,
            "first_name": self.fname,
            "last_name": self.lname,
            "contact_no": self.mob,
            "e_mail": self.email,
            "category": self.category,
            "time_added": self.time
        }

        collection.insert_one(dictionary)

    def deleteContact(self,srno):
        self.srno = srno

        if(collection.find_one({"_id": srno}) == None):
            print(f"The contact of given serial no. '{self.srno}' does not exist !")
            return

        lst = collection.find()
        for i in lst:
            if(i["_id"] == self.srno):
                collection.delete_one({"_id": self.srno})
                return


    def listContact(self):
        i = 1
        while(i<=111):
            print("-",end="")
            i+=1
        i=1
        while(i<=48):
            print(" ",end="")
            i+=1
        print("List Of Contact",end="")
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

        lst = (collection.find())
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
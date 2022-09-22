import pymongo
import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["contact_manager"]
collection = db["contact_no"]

class MainMenu:
    def __init__(self):
        print("++++Main Menu++++")
        print('''1. Add New Contact
2. Delete Contact
3. List Contacts
4. Search Contact
5. Exit''')

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





if __name__ == "__main__":
    print("*****Welcome to Contact Manager****\n")
    print("-------Created By Dishant-------\n\n")
    while(1):
        wlcm = MainMenu()

        while(True):
            try:    
                choice = int(input("Enter your choice(1-5) : "))
                break
            except Exception as e:
                print("\nPlease enter you choice between 1-5 : ")
    
        mc = NextMenu()
    
        if(choice == 1):
            fname = input("Enter first name : ")
            lname = input("Enter last name : ")
            while(True):
                try:
                    mob = int(input("Enter 10 digit contact no. : "))
                    if(len(str(mob))==10):
                        break
                    else:
                        print("Invalid input !!!\nEnter only 10 digits mobile number !!!")
                except Exception as e:
                    print("Enter integers only !!!")
            
            while(True):
                email = input("Enter E-Mail address : ")
                if "@" in email and ".com" in email:
                    break
                else:
                    print("\nYour entered email id is wrong please type it again !")

            category = input("Enter category(family/frd/clg/home) : ")
            time = datetime.datetime.now()
    
            mc.addContact(fname.lower(),lname.lower(),mob,email.lower(),category.lower(),time)
        
        elif(choice == 2):
            srno = int(input("Enter sr. no. of contact : "))
    
            mc.deleteContact(srno)
    
        elif(choice == 3):
            mc.listContact()

        elif(choice == 4):
            src = SearchContact()

            choice = int(input("Enter your choice(1-3) : "))

            if(choice==1):
                name = input("Enter name : ")
                src.searchContactByName(name)
            elif(choice==2):
                mob = int(input("Enter contact no.(10 digit) : "))
                src.searchContactByMob(mob)
            elif(choice==3):
                category = input("Enter category(frd,family,clg,company) : ")
                src.searchByCategory(category)
    
        elif(choice == 5):
            exit()

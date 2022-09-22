import pymongo
import datetime
from nextmenu import NextMenu
from search import SearchContact

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

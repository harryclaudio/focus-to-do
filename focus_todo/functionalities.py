import datetime
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Functionalities:
    def __init__(self, option, accounts, email):
        self.email = email
        self.option = option
        self.accounts = accounts

    def save_data(self, filename, data):
        with open(filename, 'a') as file:
            file.write(data)
    
    def header(self):
        print("\n\t\t📒 Focus TO-DO 📒\n")
        print(f"👦 {self.accounts[self.email]['name']} {self.accounts[self.email]['lastname']}\n\n")
    
    def features_menu(self):
     self.header()
     print("\t\t1. 🚀 MY DAY")
     print("\t\t2. ⭐️ IMPORTANT")
     print("\t\t3. 📑 TASKS")
     print("\t\t4. 📚 NEW LIST")
     print("\t\t5. 🚶 EXIT")
     
     while(True):
         self.option = int(input("⏩ OPTION: "))
         
         if self.option >= 1 and self.option <= 5:
             break
         else :
             print("Invalid Option :(\n")
   
    def my_day_menu(self):
        self.header()
        print("\t\t🚀 MY DAY\n\n")
        print("\t\t1. ➕ Add Task")
        print("\t\t2. 👀 View Tasks")
        print("\t\t3. 🚶 Exit")
        print("-----------------------\n\n")
        self.option = int(input("⏩ OPTION: "))
   
    def validate_date(self):
        def validate_year(year):
            if year <= 2008 :
                return True
            else:
                return False
        
        def validate_month(month):
            if month >= 1 and month <= 12:
                return True
            else:
                return False
        
        def validate_day(day, month):
            if  month % 2 == 0:
                if day >= 1 and day <= 30:
                    return True
                else:
                    return False
            else:
                if day >= 1 and day <= 31:
                    return True
                else:
                    return False

        while(True):
            year = int(input("Year: "))
            if validate_year(year):
                break
        
        while(True):
            month = int(input("Month: "))
            if validate_month(month):
                break
        
        while(True): 
            day = int(input("Day: "))
            if validate_day(day, month):
                break
        
        due_date = datetime.date(year, month, day)  
        
        return due_date
   
    def validate_hour_and_minute(self):
        def validate_hour(hour):
            if hour >= 0 and hour <= 23:
                return True
            else:
                return False
        
        def validate_minute(minute):
            if minute >= 0 and minute <= 59:
                return True
            else:
                return False
        
        time = ""
        while(True):
            hour = int(input("Hour: "))
            if validate_hour(hour):
                break
            
        while(True):
            minute = int(input("Minute: "))
            if validate_minute(minute):
                break
        
        
        if minute >= 0 and minute <= 9 and hour >= 0 and hour <= 9:
            time = f"0{hour}:0{minute}"
        else:
            time = f"{hour}:{minute}"
            
        return time
   
   
    def due_date_task(self):
        due_date = "none-none-none"
        print("\n\n")
        print("\t\t📆 Due \n")
        print("1. TODAY")
        print("2. TOMORROW")
        print("3. NEXT WEEK")
        print("4. PICK a DATE")
        self.option = int(input("⏩ OPTION: "))
        
        current_date = datetime.datetime.now().date()
        
        if self.option == 1:
            due_date = current_date
        elif self.option == 2:
            due_date = current_date + datetime.timedelta(days=1)    
        elif self.option == 3:
            due_date = current_date + datetime.timedelta(weeks=1)
        else:
            due_date = self.validate_date()
        
        return due_date
    
    def reminder_task(self):
        reminder = "none, none"
        print("\n\n")
        print("\t\t⏰ Reminder \n")
        print("1. LATER TODAY")
        print("2. TOMORROW")
        print("3. NEXT WEEK")
        print("4. PICK a DATE & TIME")
        self.option = int(input("⏩ OPTION: "))
        
        current_time = datetime.datetime.now().time()
        new_time = datetime.datetime.combine(datetime.date.today(), current_time) + datetime.timedelta(hours=3)
        date = datetime.date.today
        if self.option == 1:
            reminder = f"{new_time.hour:02d}:{new_time.minute:02d}"
        elif self.option == 2:
            new_day = date + datetime.timedelta(days=1)
            reminder = f"{new_day.strftime('%A')}, {new_time.hour:02d}"
        elif self.option == 3:
            new_day = date + datetime.timedelta(weeks=1)
            reminder = f"{new_day.strftime('%A')}, {new_time.hour:02d}"
        else:
            custom_date = self.validate_date()
            custom_time = self.validate_hour_and_minute()
            
            reminder = f"{custom_date}, {custom_time}"
        
        return reminder
   
    def repeat_task(self):
        repeat = "none"
        print("\n\n")
        print("\t\t⭕ Repeat \n")
        print("1. DAILY")
        print("2. WEEKDAYS")
        print("3. WEEKLY")
        print("4. MONTHLY")
        print("4. YEARLY")
        self.option = int(input("⏩ OPTION: "))
        
        if self.option == 1:
            repeat = "Daily"
        elif self.option == 2:
            repeat = "Weekdays"
        elif self.option == 3:
            repeat = "Weekly"
        elif self.option == 4:
            repeat = "Monthly"
        elif self.option == 5:
            repeat = "Yearly"
        
        return repeat
   
    def my_day_functionality(self):
        
        while self.option != 3:
            self.my_day_menu()
        
            if self.option == 1:
                self.header()
                
                task_description = "none"
                answer = "none"
                due_date = "none-none-none"
                reminder = "none, none"
                repeat = "none"
                
                print("\t\t➕ Add Task\n")
                task_description = input("\t\tAdd a task: ")
                answer = input("\t\tAdd due date? [Yes:y / No:n]: ").lower()
                
                if answer == "y":
                    due_date = self.due_date_task()  
                else:
                    due_date = "NULL-NULL-NULL"
                
                answer = input("\n\n\t\tDo you want a reminder? [Yes:y / No:n]: ").lower()
                
                if answer == "y":
                    reminder = self.reminder_task()
                else:
                    reminder = "NULL, NULL"
                    
                answer = input("\n\n\t\tDo you want the task to be repeated? [Yes:y / No:n]: ").lower()

                if answer == "y":
                    repeat = self.repeat_task()
                else:
                    repeat = "none"
                
                answer = input("\n\n\t\tCreate task? [Yes:y / No:n]: ").lower()

                if answer == "y":
                    pass
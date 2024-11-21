
from datetime import datetime


class AttendanceSystem:


    def __init__(self):
        
        self.attendance_list = {}



    def mark_attendence(self, name):  


        date = datetime.now().strftime('%Y-%m-%d')

        if name in self.attendance_list:

            if date in self.attendance_list[name]:

                print(f"{name} is already marked present for today")

            else:

                self.attendence_list[name].append (date)

                print(f"{name} has been marked present for {date}.")

        else:

            self.attendance_list[name] = [date]

            print(f"{name} has been present for {date}")



    def view_attendence(self):

        if  not self.attendance_list:

            print("no attendence records found.")

        else:

            print("Attendance list: ")

            for name, dates in self.attendance_list.items():

                print(f'{name}: {','.join(dates)}')



    def view_specific_attendance(self, name):

        if name in self.attendance_list:

            dates = self.attendance_list

            print(f"{name} has been present on: {','.join(dates)}")

        else: 
            
            print(f"no attendance records found for {name}.")


    def run(self):

        while True:

            print("\nAttendance Management System")

            print("1. Mark Attendance")
            print("2. View Attendance")
            print("3. View Specific Attendance")
            print("4. Exit")


            choice = input("Enter your choice: ")

            
            if choice =="1":

                name = input("Enter the name of the student: ")

                self.mark_attendence(name)

            elif choice == "2":

                self.view_attendence()

        
            elif choice =="3":

                name = input("Enater the name of the student: ")

                self.view_specific_attendance(name)


            elif choice == "4":

                print("Exiting the system.")
                break

            else:

                print("Invalid choice. Please try again.")



if __name__ == "__main__":

    system = AttendanceSystem()

    system.run()

        


                


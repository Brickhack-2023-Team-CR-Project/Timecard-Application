#importing json library to read/write json file
import json 

#storing the maximum number of hours that the user can work
max_hours = 20 

#storing the user input in a dictionary
user_data = {}

#function to clock in to work
def clock_in():
  employee_id = input("Enter your employee ID: ")
  in_time = input("Enter your clock-in time: ")
  #check if the employee id already exists in the user data
  if employee_id in user_data:
    user_data[employee_id]["in"] = in_time
  else:
    user_data[employee_id] = {
      "in": in_time
    }
  #updating the json file with the new user data
  with open('user_data.json', 'w') as f:
    json.dump(user_data, f, indent=2)

#function to clock out of work
def clock_out():
  employee_id = input("Enter your employee ID: ")
  out_time = input("Enter your clock-out time: ")
  #check if the employee id already exists in the user data
  if employee_id in user_data:
    user_data[employee_id]["out"] = out_time
  else:
    user_data[employee_id] = {
      "out": out_time
    }
  #updating the json file with the new user data
  with open('user_data.json', 'w') as f:
    json.dump(user_data, f, indent=2)

#function to update the hours worked
def update_hours():
  employee_id = input("Enter your employee ID: ")
  hours = int(input("Enter the number of hours you worked: "))
  #check if the employee id already exists in the user data
  if employee_id in user_data:
    user_data[employee_id]["hours_worked"] = hours
  else:
    user_data[employee_id] = {
      "hours_worked": hours
    }
  #updating the json file with the new user data
  with open('user_data.json', 'w') as f:
    json.dump(user_data, f, indent=2)

#function to view the hours worked
def view_hours():
  employee_id = input("Enter your employee ID: ")
  #check if the employee id already exists in the user data
  if employee_id in user_data:
    hours_worked = user_data[employee_id].get("hours_worked", 0)
    hours_left = max_hours - hours_worked
    in_time = user_data[employee_id]["in"]
    out_time = user_data[employee_id]["out"]
    #calculate the total hours worked
    in_time_split = in_time.split(":")
    out_time_split = out_time.split(":")
    in_hour = int(in_time_split[0])
    in_min = int(in_time_split[1])
    out_hour = int(out_time_split[0])
    out_min = int(out_time_split[1])
    total_hours = (out_hour - in_hour) + ((out_min - in_min) / 60)
    hours_worked = total_hours if total_hours <= max_hours else max_hours
    hours_left = max_hours - hours_worked
    print(f"Employee with ID {employee_id} clocked in at {in_time} and clocked out at {out_time} and has worked {hours_worked} hours and has {hours_left} hours left to work this week.")
  else:
    print("Employee does not exist in the user data.")

#function to manually enter the hours worked
def manually_enter_hours():
  employee_id = input("Enter your employee ID: ")
  hours = int(input("Enter the number of hours you worked: "))
  #check if the employee id already exists in the user data
  if employee_id in user_data:
    user_data[employee_id]["hours_worked"] = hours
  else:
    user_data[employee_id] = {
      "hours_worked": hours
    }
  #updating the json file with the new user data
  with open('user_data.json', 'w') as f:
    json.dump(user_data, f, indent=2)

#main function which takes in user input
def main():
  while True:
    user_choice = input("What do you want to do? (1. Clock-in, 2. Clock-out, 3. Update hours, 4. View hours, 5. Manually enter hours, 6. Quit) ")
    if user_choice == "1":
      clock_in()
    elif user_choice == "2":
      clock_out()
    elif user_choice == "3":
      update_hours()
    elif user_choice == "4":
      view_hours()
    elif user_choice == "5":
      manually_enter_hours()
    elif user_choice == "6":
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()

import datetime
import json

# function to clock in
def clock_in(employee_id, description):
  # get the current time
  time_in = datetime.datetime.now()
  employees[employee_id] = {
    "time_in": time_in.strftime("%Y-%m-%d %H:%M:%S"),
    "description": description
  }
  print(f"Welcome {employee_id}, you have been successfully clocked in at {time_in.strftime('%H:%M:%S')}")

# function to clock out
def clock_out(employee_id):
  employee = employees[employee_id]
  if employee_id not in employees:
    print("Error: Employee has not been clocked in")
  else: 
  # get the current time
    time_out = datetime.datetime.now()
    # calculate the total hours worked
    total_hours = (time_out - datetime.datetime.strptime(employee[employee_id]["time_in"], "%Y-%m-%d %H:%M:%S")).total_seconds()/3600
    # calculate remaining hours
    remaining_hours = 20 - total_hours
    # add time out and total hours to the employee dictionary
    employees[employee_id]["time_out"] = time_out.strftime("%Y-%m-%d %H:%M:%S")
    employees[employee_id]["total_hours"] = total_hours
    # print the output
    print(f"Goodbye {employee_id}, you have been successfully clocked out at {time_out.strftime('%H:%M:%S')}. You have worked {total_hours:.2f} hours and you have {remaining_hours:.2f} hours left this week")

# function to view hours
def view_hours(employee_id):
  # get the time in, time out and total hours
  time_in = employees[employee_id]["time_in"]
  time_out = employees[employee_id]["time_out"]
  total_hours = employees[employee_id]["total_hours"]
  # print the output
  print(f"You clocked in at {time_in} and clocked out at {time_out}. You have worked {total_hours:.2f} hours")

# function to update hours
def update_hours(employee_id, description, time_in, time_out):
  # calculate the total hours
  total_hours = (datetime.datetime.strptime(time_out, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(time_in, "%Y-%m-%d %H:%M:%S")).total_seconds()/3600
  # calculate remaining hours
  remaining_hours = 20 - total_hours
  # update the employee dictionary
  employees[employee_id] = {
    "time_in": time_in,
    "time_out": time_out,
    "total_hours": total_hours,
    "description": description
  }
  # print the output
  print(f"The hours have been successfully updated. You have worked {total_hours:.2f} hours and you have {remaining_hours:.2f} hours left this week")

# function to manually enter hours
def manually_enter_hours(employee_id, description, time_in, time_out):
  # calculate the total hours
  total_hours = (datetime.datetime.strptime(time_out, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(time_in, "%Y-%m-%d %H:%M:%S")).total_seconds()/3600
  # calculate remaining hours
  remaining_hours = 20 - total_hours
  # add to the employee dictionary
  employees[employee_id] = {
    "time_in": time_in,
    "time_out": time_out,
    "total_hours": total_hours,
    "description": description
  }
  # print the output
  print(f"The hours have been successfully added. You have worked {total_hours:.2f} hours and you have {remaining_hours:.2f} hours left this week")

# global variable to store the employee data
employees = {}

def main():
  employee_id = input("Enter your employee id: ")
  description = input("Enter your description: ")
  option = input("Enter your option (clock in/clock out/view hours/update hours/manually enter hours): ")
  if option == "clock in":
    clock_in(employee_id, description)
  elif option == "clock out":
    clock_out(employee_id)
  elif option == "view hours":
    view_hours(employee_id)
  elif option == "update hours":
    time_in = input("Enter the time in: ")
    time_out = input("Enter the time out: ")
    update_hours(employee_id, description, time_in, time_out)
  elif option == "manually enter hours":
    time_in = input("Enter the time in: ")
    time_out = input("Enter the time out: ")
    manually_enter_hours(employee_id, description, time_in, time_out)
  # save the employee data to a json file
  with open("employees.json", "w") as f:
    json.dump(employees, f)

if __name__ == "__main__":
  main()
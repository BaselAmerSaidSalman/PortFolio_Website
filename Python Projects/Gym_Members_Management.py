import time
import os
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

# Project_Lists
gym_users = []
found_users = []
member_id = []

# Gym_Members_Class
class Gym_Members:
  def __init__ (self, first_name, last_name, member_ID, status = "inactive"):
    self.first_name = first_name
    self.last_name = last_name
    self.member_ID = member_ID
    self.status = status

  def print_member_info(self):
    print("-------------------------")
    print(f"First Name: {self.first_name}")
    print(f"Last Name: {self.last_name}")
    print(f"Member ID: {self.member_ID}")
    print(f"Status: {self.status}")

# Create_New_Member
def create_user():
  first_name = input("Enter your first name: ")
  while first_name == "":
    print("You didn't enter your first name.")
    first_name = input("Enter your first name: ")
    
  last_name = input("Enter your last name: ")
  while last_name == "":
    print("You didn't enter your last name.")
    last_name = input("Enter your last name: ")
    
  member_ID = input("Enter your member ID: ")
  while member_ID == "":
    print("You didn't enter your Member_ID.")
    member_ID = input("Enter your Member_ID: ")
  while member_ID in member_id:
    print("This Member_ID is already in use.")
    member_ID = input("Enter your Member_ID: ")
    
  status = input("Enter your status or press enter to continue without write: ")
  while status != "active" and status != "inactive" and status != "":
    print("Sorry, Invalid Status")
    status = input("Enter your status: ")
  if status == "":
    status = "inactive"
  else:
    status = status
    
  return Gym_Members(first_name, last_name, member_ID, status)


# Interface
def introduction():
  print("\nWelcome to the Gym Membership System!\n\n")
  # User_Choice
  print("Choose an Action: \n\n1. Add new member\n2. Display all members\n3. Search for a member\n4. Exit\n")
  user_choice = input("Enter your choice: ")
  # User_Choice_Validation
  while user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4":
    print("Sorry, Invalid Input. Please try again.")
    user_choice = input("Enter your choice: ")
  # Add_New_Member
  if user_choice == "1":
    clear_screen()
    gym_users.append(create_user())
    for x in gym_users:
      member_id.append(x.member_ID)
    print("Member added successfully!")
    time.sleep(1)
    clear_screen()
    time.sleep(0.5)
    introduction()
  # Display_All_Members
  elif user_choice == "2":
    if gym_users:
      clear_screen()
      print("Displaying all members......")
      for i in gym_users:
        i.print_member_info()
        print("-------------------------")
      time.sleep(3)
      clear_screen()
      time.sleep(0.5)
      introduction()
    else:
      print("Sorry, there are no members in the system.")
      time.sleep(2)
      clear_screen()
      time.sleep(0.5)
      introduction()
  # Search_For_Member
  elif user_choice == "3":
    clear_screen()
    print("Search by:\n\n1. Membership ID\n2. First_name\n3. Membership Status\n")
    search_choice = input("Enter your choice: ") 
    while search_choice != "1" and search_choice != "2" and search_choice != "3":
      print("Sorry, Invalid Input. Please try again.")
      search_choice = input("Enter your choice: ")
    # Search_By_Membership_ID
    if search_choice == "1":
      search_ID = input("Enter the member ID: ")
      if gym_users:
        for user in gym_users:
          if user.member_ID == search_ID:
           found_users.append(user)
        clear_screen()
        for x in found_users:
          x.print_member_info()
        print("-------------------------")
        time.sleep(3)
        clear_screen()
        time.sleep(0.5)
        introduction()
      else:
        print("Member not found.")
        time.sleep(1)
        clear_screen()
        time.sleep(0.5)
        introduction()
    # Search_By_First_Name
    elif search_choice == "2":
      search_first_name = input("Enter the First Name: ")
      if gym_users:
        for user in gym_users:
         if user.first_name == search_first_name:
          found_users.append(user)
        clear_screen()
        for x in found_users:
           x.print_member_info()
        print("-------------------------")
        time.sleep(3)
        clear_screen()
        time.sleep(0.5)
        introduction()
      else:
         print("Member not found.")
         time.sleep(1)
         clear_screen()
         time.sleep(0.5)
         introduction()
    # Search_By_Membership_Status
    else:
      search_member_status = input("Enter the Member Status: ")
      if gym_users:
        for user in gym_users:
          if user.status == search_member_status:
           found_users.append(user)
        clear_screen()
        for x in found_users:
          x.print_member_info()
        print("-------------------------")
        time.sleep(3)
        clear_screen()
        time.sleep(0.5)
        introduction()
      else:
         print("Member not found.")
         time.sleep(1)
         clear_screen()
         time.sleep(0.5)
         introduction()
  # Exit
  else:
    print("Thank you for using the Gym Membership System!")
    print("Exiting...........")
    time.sleep(2)

# Code
introduction()

    
    
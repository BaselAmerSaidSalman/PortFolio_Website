# import_Section
import time
import os 
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')



# Files_Library_Function
def files_Library():
  try:
    
    # User_Choice
    clear_screen()
    print("\n************ Welcome to the Files Library! ************\n\n")
    print("Choose an Action\n\n1.Create a new file\n2.Read your file\n3.Write something in your file\n4.Remove your file\n5.Exit\n")
    user_choice = input("Enter your choice (1,2,3,4,5): ")
    while user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4" and user_choice != "5":
      print("Sorry, Invalid input")
      user_choice = input("Please enter 1,2,3,4 or 5: ")
    
    # Create_New_File
    if user_choice == "1":
        clear_screen()
        time.sleep(0.5)
        print(r"Example: c:\Users\Vega Laptop\OneDrive\Desktop\your folder\yourfile.extension")
        user_file_name = input("Enter a file name & place to create it: ").strip()
        new_file = open(user_file_name, "w")
        new_file.close()
        print("Created Successfully!")
        time.sleep(2)
        clear_screen()
        time.sleep(0.5)
        files_Library()


    # Read_File
    elif user_choice == "2":
        clear_screen()
        time.sleep(0.5)
        print(r"Example: c:\Users\Vega Laptop\OneDrive\Desktop\Your folder\Yourfile.extension")
        name_file_read = input("Enter your file name & place to read it: ").strip()
        read_file = open(name_file_read, "r")
        clear_screen()
        time.sleep(0.5)
        print("\n************ The Information in your file ************\n")
        print(read_file.read())
        time.sleep(3)
        clear_screen()
        time.sleep(0.5)
        files_Library()


    # Write_in_File
    elif user_choice == "3":
        clear_screen()
        time.sleep(0.5)
        print("Choose an Action\n\n1.Writing something instead of what is written in the file\n2.Adding something to what is already written in the file.\n")
        user_choice_write = input("Enter your choice (1 or 2): ")
        while user_choice_write != "1" and user_choice_write != "2":
            print("Sorry, Invalid input")
            user_choice_write = input("Please enter your choice (1 or 2): ")
        
        # Write_instead_of_what_is_written
        if user_choice_write == "1":
            print(r"Example: c:\Users\Vega Laptop\OneDrive\Desktop\Your folder\Yourfile.extension")
            name_file_write_instead = input("Enter your file name & place to read it: ").strip()
            write_instead = input("Please Write what you want: ")
            file_write_instead = open(name_file_write_instead, "w")
            file_write_instead.write(write_instead)
            file_write_instead.close()
            print("Written Successfully!")
            time.sleep(2)
            clear_screen()
            time.sleep(0.5)
            files_Library()  

        # Write_Extra
        elif user_choice_write == "2":
            print(r"Example: c:\Users\Vega Laptop\OneDrive\Desktop\Your folder\Yourfile.extension")
            name_file_write_extra = input("Enter your file name & place to read it: ").strip()
            write_extra = input("Please write what you want: ")
            file_write_extra = open(name_file_write_extra, "a")
            file_write_extra.write(write_extra)
            file_write_extra.close()
            print("Written Successfully!")
            time.sleep(2)
            clear_screen()
            time.sleep(0.5)
            files_Library()

    # Remove_File
    elif user_choice == "4":
        clear_screen()
        time.sleep(0.5)
        print(r"Example: c:\Users\Vega Laptop\OneDrive\Desktop\Your folder\Yourfile.extension")
        remove_file = input("Enter your file name & place to remove it: ").strip()
        os.remove(remove_file)
        print("Removed Successfully!")
        time.sleep(2)
        clear_screen()
        time.sleep(0.5)
        files_Library()

    # Exit
    else:
        print("Thanks for using our library")
        print("Exiting........")
        time.sleep(2)

  # FileExistsError
  except FileExistsError:
        print("We had this file already!")
        time.sleep(2)
        clear_screen()
        time.sleep(0.5)
        files_Library()

  # FileNotFoundError
  except FileNotFoundError:
        print("We didn't have this file yet!")
        time.sleep(2)
        clear_screen()
        time.sleep(0.5)
        files_Library()

# Code   
files_Library()

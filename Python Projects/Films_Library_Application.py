# Import_Section
import sqlite3
import json
import time
import re
import os
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

# User_Info_Database
db = sqlite3.connect("users_info_in_films_library_app.db")
cr = db.cursor()
cr.execute("create table if not exists users_info (name text, email text, password text)")
cr.execute("select * from users_info")
users_info = cr.fetchall()
db.commit()

# User_Films_Database
db2 = sqlite3.connect("users_films_in_films_library_app.db")
cr2 = db2.cursor()
cr2.execute("create table if not exists users_films (email text, films text)")
cr2.execute("select * from users_films")
users_films = cr2.fetchall()
db2.commit()

# Application_Libraries
user_get = []
email_get = []
email_get_info = []
films_dic = {}
film_author_results = []
film_year_results = []

# Create_New_Film_Info
class Film:
  def __init__(self, type, name, author, year):
    self.type = type
    self.name = name
    self.author = author
    self.year = year

def add_film():
    film_type = input("Please enter your film type: ")
    film_name = input("Please enter your film name: ")
    film_author = input("Please enter your film author: ")
    film_year = input("Please enter the year that film was made: ")
    while int(film_year) > 2025:
        print("Wrong film year, We're still in 2025, Please try again")
        film_year = input("Please enter the year that film was made: ")
    while int(film_year) < 1887:
        print("Wrong film year, first film was made in 1888, Please try again")
        film_year = input("Please enter the year that film was made: ")
    if int(film_year) <= 2025: 
        return Film(film_type, film_name, film_author, film_year)


# Create_New_User
class User:
   def __init__(self, name, email, password):
      self.name = name
      self.email = email
      self.password = password

def create_user():
    while True:
        user_name = input("Please enter your name: ")
        user_email = input("Please enter your email: ")
        user_password = input("Please enter your password: ")
        if re.fullmatch(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", user_email):
            email_get_info.append(user_email) 
            return User(user_name, user_email, user_password)
        else:
            print("Invalid Email, Please try again.")
    
    







def films_library():
    global films_dic
    user_email = "".join(email_get_info[0])
    print("****************** Welcome to your films library! ******************\n")
    print("Choose an Action\n1. Create new film info\n2. See your films\n3. Search about film\n4. Exit\n")
    user_choice = input("Enter your choice (1,2,3 or 4): ")
    while user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4":
       print("Sorry, invalid choice")
       user_choice = input("Enter your choice (1,2,3 or 4) only: ")

    # Create_New_Film
    if user_choice == "1":
        clear_screen()
        time.sleep(0.5)
        create_new_film = add_film()
        if films_dic:
            if create_new_film.type in films_dic:
                if create_new_film.name in films_dic[create_new_film.type]:
                    print("We had this film already!")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    films_library()
                else:
                    films_dic[create_new_film.type][create_new_film.name] = {"Author" : create_new_film.author, "Year" : create_new_film.year}
                    json_data = json.dumps(films_dic)
                    cr2.execute(f"update users_films set films = '{json_data}' where email = '{user_email}'")
                    db2.commit()
                    print("Film Added")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    films_library()
            else:
                films_dic[create_new_film.type] = {create_new_film.name : {"Author" : create_new_film.author, "Year" : create_new_film.year}}
                json_data = json.dumps(films_dic)
                cr2.execute(f"update users_films set films = '{json_data}' where email = '{user_email}'")
                db2.commit()
                print("Film Added")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                films_library()
        else:
            films_dic[create_new_film.type] = {create_new_film.name : {"Author" : create_new_film.author, "Year" : create_new_film.year}}
            json_data = json.dumps(films_dic)
            cr2.execute(f"update users_films set films = '{json_data}' where email = '{user_email}'")
            db2.commit()
            print("Film Added")
            time.sleep(2)
            clear_screen()
            time.sleep(0.5)
            films_library()
    
    # Displaying_All_Films
    elif user_choice == "2":
        if films_dic:
            clear_screen()
            time.sleep(0.5)
            print("****************** Displaying all films ******************")
            cr2.execute(f"select films from users_films where email = '{user_email}'")
            results = cr2.fetchone()
            db2.commit()
            recieved_json = json.loads(results[0])
            films_dic = recieved_json
            for type in films_dic:
                print("---------------------------------")
                print(f"{type} => {films_dic[type]}")
            print("---------------------------------")
            time.sleep(2)
            clear_screen()
            time.sleep(0.5)
            films_library()
        else:
            print("We didn't have any films yet!")
            time.sleep(2)
            clear_screen()
            time.sleep(0.5)
            films_library()
        
    # Searching_About_Film
    elif user_choice == "3":
        cr2.execute(f"select films from users_films where email = '{user_email}'")
        results = cr2.fetchone()
        db2.commit()
        recieved_json = json.loads(results[0])
        films_dic = recieved_json
        clear_screen()
        time.sleep(0.5)
        print("****************** Searching about film ******************")
        print("\nSearching by\n1. Film Type\n2. Film Name\n3. Film Author\n4. Film Year\n")
        search_way = input("Enter your choice (1,2,3 or 4): ")
        while search_way != "1" and search_way != "2" and search_way != "3" and search_way != "4":
            print("Sorry, invalid choice")
            search_way = input("Enter your choice (1,2,3 or 4) only: ")
        
        # Searching_By_Using_Film_Type
        if search_way == "1":
            clear_screen()
            time.sleep(0.5)
            search_by_film_type = input("Please enter your film type: ")
            if films_dic:
                for type in films_dic:
                    if search_by_film_type == type:
                        clear_screen()
                        time.sleep(0.5)
                        print("****************** Your Search Results ******************")
                        print(f"{type} Films Information => {films_dic[type]}")
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        films_library()
                else:
                    print("We didn't have this film yet!")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    films_library()
            else:
                print("We didn't have any films yet!")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                films_library()

        # Searching_By_Using_Film_Name
        elif search_way == "2":
            if films_dic:
                clear_screen()
                time.sleep(0.5)
                search_by_film_name = input("Please enter your film name: ")
                for type in films_dic:
                    for name in films_dic[type]:
                        if search_by_film_name == name:
                            clear_screen()
                            time.sleep(0.5)
                            print("****************** Your Search Results ******************")
                            print(f"{name} => Type : {type} => Information : {films_dic[type][name]}")
                            time.sleep(2)
                            clear_screen()
                            time.sleep(0.5)
                            films_library()
                else:
                    print("We didn't have this film yet!")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    films_library()
            else:
                print("We didn't have any films yet!")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                films_library()
        
        # Searching_By_Using_Film_Author
        elif search_way == "3":
            if films_dic:
                clear_screen()
                time.sleep(0.5)
                search_by_film_author = input("Please enter your film author: ")
                film_author_results = []
                for type in films_dic:
                    for name in films_dic[type]:
                        if search_by_film_author == films_dic[type][name]['Author']:
                            film_author_results.append(f"{name} film => Type : {type} => Information : {films_dic[type][name]}")
                        else:
                            continue
                
                if film_author_results:
                    clear_screen()
                    time.sleep(0.5)
                    print("****************** Your Search Results ******************")
                    for i in film_author_results:
                        print("---------------------------------")
                        print(i)
                    print("---------------------------------")
                    time.sleep(3)
                    clear_screen()
                    time.sleep(0.5)
                    films_library()
                
                else:
                    print("We didn't have any film that made by this author")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    films_library()
                                
            else:
                print("We didn't have any films yet!")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                films_library()
        
        # Searching_By_Using_Film_Year
        elif search_way == "4":
            if films_dic:
                clear_screen()
                time.sleep(0.5)
                search_by_film_year = int(input("Please enter the year that film made in it: "))
                for type in films_dic:
                    for name in films_dic[type]:
                        if str(search_by_film_year) == films_dic[type][name]['Year']:
                            film_year_results.append(f"{name} film => Type : {type} => Information : {films_dic[type][name]}")
                        else:
                            continue

                if film_year_results:
                    clear_screen()
                    time.sleep(0.5)
                    print("****************** Your Search Results ******************")
                    for i in film_year_results:
                        print("---------------------------------")
                        print(i)
                    print("---------------------------------")
                    time.sleep(3)
                    clear_screen()
                    time.sleep(0.5)
                    films_library()
                else:
                    print("We didn't have films that made in this year yet!")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    films_library()
            else:
                print("We didn't have any films yet!")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                films_library()

    # Exit
    elif user_choice == "4":
        print("Thank you for using our films library application")
        print("Exiting.......")
        time.sleep(2)
        exit()








# User_Films
def user_films():
    global films_dic
    user_email = "".join(email_get_info[0])
    if users_films:
        for user_film in users_films:
            if "".join(email_get_info[0]) in user_film:
                email_get.append(user_film)
            else:
                continue
        if email_get:
            cr2.execute(f"select films from users_films where email = '{user_email}'")
            result = cr2.fetchone()
            db2.commit()
            recieved_json = json.loads(result[0])
            films_dic = recieved_json
            films_library()
        else:
            cr2.execute(f"insert into users_films (email, films) values ('{user_email}', 0)")
            db2.commit()
            films_library()
    else:
        cr2.execute(f"insert into users_films (email, films) values ('{user_email}', 0)")
        db2.commit()
        films_library()


                
            











def films_application():
        clear_screen()
        time.sleep(0.5)
        print("****************** Welcome to the film library app! ******************\n")
        print("Choose an Action\n1. Sign up\n2. Login\n")
        user_sign = input("Enter your choice (1 or 2): ")
        while user_sign != "1" and user_sign != "2":
           print("Sorry, invalid choice")
           user_sign = input("Enter your choice (1 or 2) only: ")

        
        # Sign up
        if user_sign == "1":
            clear_screen()
            time.sleep(0.5)
            create_new_user = create_user()
            if users_info == []:
                cr.execute(f"insert into users_info(name, email, password) values('{create_new_user.name}', '{create_new_user.email}', '{create_new_user.password}')")
                db.commit()
                print("Welcome to our films library app....")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                user_films()
            else:
                for user_info in users_info:
                    if create_new_user.email in user_info:
                        print("We have this user already, Please go to login")
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        films_application()
                    else:
                        continue
                else:
                    cr.execute(f"insert into users_info(name, email, password) values('{create_new_user.name}', '{create_new_user.email}', '{create_new_user.password}')")
                    db.commit()
                    print("Welcome to our films library app....")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    user_films()
        
        
        
        # Login
        elif user_sign == "2":
            clear_screen()
            time.sleep(0.5)
            create_new_user = create_user()
            if users_info:
                    for user_info in users_info:
                        if create_new_user.email in user_info:
                            if create_new_user.password in user_info:
                                if create_new_user.name in user_info:
                                    user_get.append(user_info)
                                else:
                                    print("You're name is wrong, please try again")
                                    time.sleep(2)
                                    clear_screen()
                                    time.sleep(0.5)
                                    films_application()
                            else:
                                print("You're password is wrong, please try again")
                                time.sleep(2)
                                clear_screen()
                                time.sleep(0.5)
                                films_application()
                        else:
                            continue

                    if user_get:
                        print("Login......")
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        user_films()
                    else:
                        print("We didn't have this user yet, please go to sign up")
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        films_application()
            else:
                print("We didn't have any user yet, please go to sign up")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                films_application()
        



        
        
films_application()
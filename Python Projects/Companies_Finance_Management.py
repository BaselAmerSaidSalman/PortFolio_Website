import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import json
import time
import re
import os
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')



df= pd.DataFrame({})

company_emails = []
company_names = []
company_places = []
company_months = []
company_years = []
company_sales_quantity = []
company_total_profits = []
places_get = []
months_get = []
years_get = []
finance_dic = {}
finance_dic_2 = {}
emails_get = []
user_get = []






db_signup_or_login = sqlite3.connect("companies_info.db")
cr_signup_or_login = db_signup_or_login.cursor()
cr_signup_or_login.execute("create table if not exists company_info(company_name text, company_email text, password text)")
cr_signup_or_login.execute("select * from company_info")
company_info = cr_signup_or_login.fetchall()
db_signup_or_login.commit()



db_finance_info = sqlite3.connect("companies_finance.db")
cr_finance_info = db_finance_info.cursor()
cr_finance_info.execute("create table if not exists finance_info(company_email text, company_finance text)")
cr_finance_info.execute("select * from finance_info")
companies_finance = cr_finance_info.fetchall()
db_finance_info.commit()



db_company_finance_info = sqlite3.connect("companies_finance_information.db")
cr_company_finance_info = db_company_finance_info.cursor()
cr_company_finance_info.execute("create table if not exists companies_finance_information(company_email text, year integer, month text, place text, sales integer, profit integer)")
cr_company_finance_info.execute("select * from companies_finance_information")
companies_finance_information = cr_company_finance_info.fetchall()
db_company_finance_info.commit()




class Finance:
    def __init__(self, place, month, year, sales_quantity, total_profits):
        self.place = place
        self.month = month
        self.year = year
        self.sales_quantity = sales_quantity
        self.total_profits = total_profits


def finance_information():
    place = input("Enter your finance place: ")
    company_places.append(place)
    month = input("Enter your finance month: ")
    company_months.append(month)
    year = int(input("Enter your finance year: "))
    while year > 2025:
        print("We are in 2025, year should be less than it, please try again")
        year = int(input("Enter your finance year: "))
    if year <= 2025:
        company_years.append(year)
        sales_quantity = int(input("Enter your sales quantity: "))
        company_sales_quantity.append(sales_quantity)
        total_profits = int(input("Enter your total profits: "))
        company_total_profits.append(total_profits)
        return Finance(place, month, year, sales_quantity, total_profits)



class User:
    def __init__(self, company_name, company_email, password):
       self.company_name = company_name
       self.company_email = company_email
       self.password = password

def create_user():
    while True:
        company_name = input("Enter your company name: ")
        company_names.append(company_name)
        company_email = input("Enter your company email: ")
        is_email = re.findall(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", company_email)
        while is_email == []:
            print("Invalid Email, please try again")
            company_email = input("Enter your company email: ")
            is_email = re.findall(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", company_email)
        if is_email != []:
            company_emails.append(company_email)
        password = input("Enter your password: ")
        return User(company_name, company_email, password)
    


def companies_finance_management():
  try:
    global finance_dic
    global finance_dic_2
    global df
    company_name = "".join(company_names[0])
    company_email = "".join(company_emails[0]) 
    place = "".join(company_places)
    month = "".join(company_months)
    for i in company_years:
        year = i
    for x in company_sales_quantity:
        sales_quantity = x
    for y in company_total_profits:
        total_profits = y

    print("**************************** Welcome to the finance management app ****************************")
    print("\n\nChoose an Action:\n1. Add a new finance informations\n2. See your finance informations\n3. Search about finance informations\n4. Data Analysis\n5. Finance Information Graph Line\n6. Exit\n")
    user_choice = input("Please enter your choice (1,2,3,4,5 or 6): ")
    while user_choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid Choice, please try again")
        user_choice = input("Please enter your choice (1,2,3,4,5 or 6) only: ")
    if user_choice == "1":
        clear_screen()
        time.sleep(0.5)
        new_finance_informations = finance_information()
        if finance_dic:
            if company_name in finance_dic:
                if str(new_finance_informations.year) in finance_dic[company_name]:
                    if new_finance_informations.month in finance_dic[company_name][str(new_finance_informations.year)]:
                        if new_finance_informations.place in finance_dic[company_name][str(new_finance_informations.year)][new_finance_informations.month]:
                            print("We have this month with this place & year already")
                            time.sleep(2)
                            clear_screen()
                            time.sleep(0.5)
                            companies_finance_management()
                        else:
                            finance_dic[company_name][str(new_finance_informations.year)][new_finance_informations.month][new_finance_informations.place] = {"Sales_quantity" : new_finance_informations.sales_quantity, "Total_profits" : new_finance_informations.total_profits}
                            json_data = json.dumps(finance_dic)
                            cr_finance_info.execute(f"update finance_info set company_finance = '{json_data}' where company_email = '{company_email}'")
                            db_finance_info.commit()

                            finance_dic_2 = {"Year" : new_finance_informations.year, "Month" : new_finance_informations.month, "Place" : new_finance_informations.place, "Sales" : new_finance_informations.sales_quantity, "Profit" : new_finance_informations.total_profits}
                            cr_company_finance_info.execute(f"insert into companies_finance_information(company_email, year, month, place, sales, profit) values('{company_email}', '{new_finance_informations.year}', '{new_finance_informations.month}', '{new_finance_informations.place}', '{new_finance_informations.sales_quantity}', '{new_finance_informations.total_profits}')")
                            db_company_finance_info.commit()
                            df = df._append(finance_dic_2, ignore_index=True)
                            print("Finance Informations Added")
                            time.sleep(2)
                            clear_screen()
                            time.sleep(0.5)
                            companies_finance_management()
                    else:
                        finance_dic[company_name][str(new_finance_informations.year)][new_finance_informations.month] = {new_finance_informations.place : {"Sales_quantity" : new_finance_informations.sales_quantity, "Total_profits" : new_finance_informations.total_profits}}
                        json_data = json.dumps(finance_dic)
                        cr_finance_info.execute(f"update finance_info set company_finance = '{json_data}' where company_email = '{company_email}'")
                        db_finance_info.commit()

                        finance_dic_2 = {"Year" : new_finance_informations.year, "Month" : new_finance_informations.month, "Place" : new_finance_informations.place, "Sales" : new_finance_informations.sales_quantity, "Profit" : new_finance_informations.total_profits}
                        cr_company_finance_info.execute(f"insert into companies_finance_information(company_email, year, month, place, sales, profit) values('{company_email}', '{new_finance_informations.year}', '{new_finance_informations.month}', '{new_finance_informations.place}', '{new_finance_informations.sales_quantity}', '{new_finance_informations.total_profits}')")
                        db_company_finance_info.commit()
                        df = df._append(finance_dic_2, ignore_index=True)
                        print("Finance Informations Added")
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        companies_finance_management()
                else:
                    finance_dic[company_name][str(new_finance_informations.year)] = {new_finance_informations.month : {new_finance_informations.place : {"Sales_quantity" : new_finance_informations.sales_quantity, "Total_profits" : new_finance_informations.total_profits}}}
                    json_data = json.dumps(finance_dic)
                    cr_finance_info.execute(f"update finance_info set company_finance = '{json_data}' where company_email = '{company_email}'")
                    db_finance_info.commit()

                    finance_dic_2 = {"Year" : new_finance_informations.year, "Month" : new_finance_informations.month, "Place" : new_finance_informations.place, "Sales" : new_finance_informations.sales_quantity, "Profit" : new_finance_informations.total_profits}
                    cr_company_finance_info.execute(f"insert into companies_finance_information(company_email, year, month, place, sales, profit) values('{company_email}', '{new_finance_informations.year}', '{new_finance_informations.month}', '{new_finance_informations.place}', '{new_finance_informations.sales_quantity}', '{new_finance_informations.total_profits}')")
                    db_company_finance_info.commit()
                    df = df._append(finance_dic_2, ignore_index=True)
                    print("Finance Informations Added")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
            else:
                finance_dic[company_name] = {str(new_finance_informations.year) : {new_finance_informations.month : {new_finance_informations.place : {"Sales_quantity" : new_finance_informations.sales_quantity, "Total_profits" : new_finance_informations.total_profits}}}}
                json_data = json.dumps(finance_dic)
                cr_finance_info.execute(f"update finance_info set company_finance = '{json_data}' where company_email = '{company_email}'")
                db_finance_info.commit()

                finance_dic_2 = {"Year" : new_finance_informations.year, "Month" : new_finance_informations.month, "Place" : new_finance_informations.place, "Sales" : new_finance_informations.sales_quantity, "Profit" : new_finance_informations.total_profits}
                cr_company_finance_info.execute(f"insert into companies_finance_information(company_email, year, month, place, sales, profit) values('{company_email}', '{new_finance_informations.year}', '{new_finance_informations.month}', '{new_finance_informations.place}', '{new_finance_informations.sales_quantity}', '{new_finance_informations.total_profits}')")
                db_company_finance_info.commit()
                df = df._append(finance_dic_2, ignore_index=True)
                print("Finance Informations Added")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                companies_finance_management()
        else:
            finance_dic[company_name] = {str(new_finance_informations.year) : {new_finance_informations.month : {new_finance_informations.place : {"Sales_quantity" : new_finance_informations.sales_quantity, "Total_profits" : new_finance_informations.total_profits}}}}
            json_data = json.dumps(finance_dic)
            cr_finance_info.execute(f"update finance_info set company_finance = '{json_data}' where company_email = '{company_email}'")
            db_finance_info.commit()

            finance_dic_2 = {"Year" : new_finance_informations.year, "Month" : new_finance_informations.month, "Place" : new_finance_informations.place, "Sales" : new_finance_informations.sales_quantity, "Profit" : new_finance_informations.total_profits}
            cr_company_finance_info.execute(f"insert into companies_finance_information(company_email, year, month, place, sales, profit) values('{company_email}', '{new_finance_informations.year}', '{new_finance_informations.month}', '{new_finance_informations.place}', '{new_finance_informations.sales_quantity}', '{new_finance_informations.total_profits}')")
            db_company_finance_info.commit()
            df = df._append(finance_dic_2, ignore_index=True)
            print("Finance Informations Added")
            time.sleep(2)
            clear_screen()
            time.sleep(0.5)
            companies_finance_management()


    elif user_choice == "2":
        if finance_dic_2:
            clear_screen()
            time.sleep(0.5)
            print("Choose the way that you want to see your finance informations with it\n1. See your finance informations here\n2. Make an excel sheet with your finance informations")
            display_finance_informations = input("please enter your choice (1 or 2): ")
            while display_finance_informations != "1" and display_finance_informations != "2":
                print("Invalid Choice, please try again")
                display_finance_informations = input("please enter your choice (1 or 2) only: ")
            if display_finance_informations == "1":
                clear_screen()
                time.sleep(0.5)
                print("**************************** Display All Finance Information ****************************")
                print(df)
                time.sleep(3)
                clear_screen()
                time.sleep(0.5)
                companies_finance_management()
            else:
                df.to_excel(f"{company_name}_finance_informations.xlsx", index=False)
                print("Excel File Created")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                companies_finance_management()
        else:
            print("We didn't have any finance informations yet")
            time.sleep(2)
            clear_screen()
            time.sleep(0.5)
            companies_finance_management()
    
    
    elif user_choice == "3":
        if finance_dic:
            clear_screen()
            time.sleep(0.5)
            print("Choose an Action\n1. Search about rows\n2. Search about columns\n3. finance data informations\n4. Other search ways")
            search_way = input("please enter your choice (1,2,3 or 4): ")
            while search_way not in ["1", "2", "3", "4"]:
                print("Invalid Choice, please try again")
                search_way = input("please enter your choice (1,2,3 or 4) only: ")
            if search_way == "1":
                clear_screen()
                time.sleep(0.5)
                print("Choose an Action\n1. All rows\n2. Head rows\n3. Random rows\n4. Specific rows\n5. Tail rows")
                search_row = input("please enter your choice (1,2,3,4 or 5): ")
                while search_row not in ["1", "2", "3", "4", "5"]:
                    print("Invalid Choice, please try again")
                    search_row = input("please enter your choice (1,2,3,4 or 5) only: ")
                if search_row == "1":
                    clear_screen()
                    time.sleep(0.5)
                    print("**************************** Display All Rows ****************************\n")
                    print(df)
                    time.sleep(3)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif search_row == "2":
                    clear_screen()
                    time.sleep(0.5)
                    number_of_rows = int(input("Enter number of rows: "))
                    while number_of_rows == 0 :
                        print("There is no row number equal to zero, please try again")
                        number_of_rows = int(input("Enter number of rows: "))
                    while number_of_rows < 0:
                        print("There is no negative row number, please try again")
                        number_of_rows = int(input("Enter number of rows: "))
                    while number_of_rows > len(df['Year']):
                        print("This number is bigger than the rows number of your data, please try again")
                        number_of_rows = int(input("Enter number of rows: "))
                    if number_of_rows > 0 and number_of_rows < len(df['Year']):
                        clear_screen()
                        time.sleep(0.5)
                        print("**************************** Display Head Rows ****************************\n")
                        print(df.head(number_of_rows))
                        time.sleep(3)
                        clear_screen()
                        time.sleep(0.5)
                        companies_finance_management()
                elif search_row == "3":
                    clear_screen()
                    time.sleep(0.5)
                    number_of_rows = int(input("Enter number of rows: "))
                    while number_of_rows == 0 :
                        print("There is no row number equal to zero, please try again")
                        number_of_rows = int(input("Enter number of rows: "))
                    while number_of_rows < 0:
                        print("There is no negative row number, please try again")
                        number_of_rows = int(input("Enter number of rows: "))
                    while number_of_rows > len(df['Year']):
                        print("This number is bigger than the rows number of your data, please try again")
                        number_of_rows = int(input("Enter number of rows: "))
                    if number_of_rows > 0 and number_of_rows < len(df['Year']):
                        clear_screen()
                        time.sleep(0.5)
                        print("**************************** Display Random Rows ****************************\n")
                        print(df.sample(number_of_rows))
                        time.sleep(3)
                        clear_screen()
                        time.sleep(0.5)
                        companies_finance_management()
                elif search_row == "4":
                    clear_screen()
                    time.sleep(0.5)
                    print("You should enter first & last row to give you rows that between their")
                    first_row_number = int(input("please enter the first row number: "))
                    while first_row_number == 0 :
                        print("There is no row number equal to zero, please try again")
                        first_row_number = int(input("please enter the first row number: "))
                    while first_row_number < 0:
                        print("There is no negative row number, please try again")
                        first_row_number = int(input("please enter the first row number: "))
                    while first_row_number > len(df['Year']):
                        print("This number is bigger than the rows number of your data, please try again")
                        first_row_number = int(input("please enter the first row number: "))
                    if first_row_number > 0 and first_row_number < len(df['Year']):
                        second_row_number = int(input("please enter the second row number: "))
                        while second_row_number == 0 :
                            print("There is no row number equal to zero, please try again")
                            second_row_number = int(input("please enter the second row number: "))
                        while second_row_number < 0:
                            print("There is no negative row number, please try again")
                            second_row_number = int(input("please enter the second row number: "))
                        while second_row_number > len(df['Year']):
                            print("This number is bigger than the rows number of your data, please try again")
                            second_row_number = int(input("please enter the second row number: "))
                        while second_row_number < first_row_number:
                            print("Second number should be greater than first number, please try again")
                            second_row_number = int(input("please enter the second row number: "))
                        if second_row_number > 0 and second_row_number < len(df['Year']) and second_row_number > first_row_number:
                            clear_screen()
                            time.sleep(0.5)
                            print(f"**************************** Display from {first_row_number} to {second_row_number} Rows ****************************\n")
                            print(df.iloc[first_row_number:second_row_number + 1])
                            time.sleep(3)
                            clear_screen()
                            time.sleep(0.5)
                            companies_finance_management()
                elif search_row == "5":
                    clear_screen()
                    time.sleep(0.5)
                    number_of_rows = int(input("Enter number of rows: "))
                    while number_of_rows == 0 :
                        print("There is no row number equal to zero, please try again")
                        number_of_rows = int(input("Enter number of rows: "))
                    while number_of_rows < 0:
                        print("There is no negative row number, please try again")
                        number_of_rows = int(input("Enter number of rows: "))
                    while number_of_rows > len(df['Year']):
                        print("This number is bigger than the rows number of your data, please try again")
                        number_of_rows = int(input("Enter number of rows: "))
                    if number_of_rows > 0 and number_of_rows < len(df['Year']):
                        clear_screen()
                        time.sleep(0.5)
                        print("**************************** Display Tail Rows ****************************\n")
                        print(df.tail(number_of_rows))
                        time.sleep(3)
                        clear_screen()
                        time.sleep(0.5)
                        companies_finance_management()
            
            elif search_way == "2":
                clear_screen()
                time.sleep(0.5)
                print("Choose an Action\n1. All columns\n2. Column name")
                search_column = input("please enter your choice (1 or 2): ")
                while search_column != "1" and search_column != "2":
                    print("Invalid Choice, please try again")
                    search_column = input("please enter your choice (1 or 2): ")
                if search_column == "1":
                    clear_screen()
                    time.sleep(0.5)
                    print("**************************** Display All Columns ****************************\n")
                    print(df.columns)
                    print("-------------------------------------------")
                    print(df)
                    time.sleep(3)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                else:
                    clear_screen()
                    time.sleep(0.5)
                    column_name = input("Enter your column name: ").capitalize()
                    clear_screen()
                    time.sleep(0.5)
                    print(f"**************************** Display {column_name} Column ****************************\n")
                    print(df[column_name])
                    time.sleep(3)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
            
            elif search_way == "3":
                clear_screen()
                time.sleep(0.5)
                print("**************************** Display All Finance Informations ****************************\n")
                print(df.info())
                time.sleep(3)
                clear_screen()
                time.sleep(0.5)
                companies_finance_management()

            else:
                clear_screen()
                time.sleep(0.5)
                print("Choose an Action\n\n1. Place finance\n2. Month finance\n3. Year finance\n")
                user_choice_2 = input("please enter your choice (1,2 or 3): ")
                while user_choice_2 != "1" and user_choice_2 != "2" and user_choice_2 != "3":
                    print("Invalid Choice, please try again")
                    user_choice_2 = input("please enter your choice (1,2 or 3) only: ")
                if user_choice_2 == "1":
                    clear_screen()
                    time.sleep(0.5)
                    company_place = input("please enter your company place: ")
                    for name in finance_dic:
                        for year in finance_dic[name]:
                            for month in finance_dic[name][year]:
                                if company_place in finance_dic[name][year][month]:
                                    places_get.append(f"{company_place} finance in {month} in {year} => {finance_dic[name][year][month][company_place]}")
                                else:
                                    continue

                    if places_get:
                        clear_screen()
                        time.sleep(0.5)
                        print(f"**************************** Display {company_place} Finance Informations ****************************\n")
                        for i in places_get:
                            print("----------------------------------------------")  
                            print(i)
                        print("----------------------------------------------")  
                        time.sleep(3)
                        clear_screen()
                        time.sleep(0.5)
                        companies_finance_management()
                    else:
                        print("We didn't have this place finance information yet")                              
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        companies_finance_management()

                elif user_choice_2 == "2":
                    clear_screen()
                    time.sleep(0.5)
                    company_month = input("please enter your company month: ")
                    for name in finance_dic:
                        for year in finance_dic[name]:
                            if company_month in finance_dic[name][year]:
                                months_get.append(f"{company_month} finance in {year} => {finance_dic[name][year][company_month]}")
                            else:
                                continue
                                
                    if months_get:
                        clear_screen()
                        time.sleep(0.5)
                        print(f"**************************** Display {company_month} Finance Informations ****************************\n")
                        for i in months_get:
                            print("----------------------------------------------")  
                            print(i)
                        print("----------------------------------------------")  
                        time.sleep(3)
                        clear_screen()
                        time.sleep(0.5)
                        companies_finance_management()
                    else:
                        print("We didn't have this month finance information yet")                              
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        companies_finance_management()

                elif user_choice_2 == "3":
                    years_get = [] 
                    clear_screen()
                    time.sleep(0.5)
                    company_year = input("please enter your company year: ")
                    for year in finance_dic[company_name]:
                        if company_year == year:
                            years_get.append(finance_dic[company_name][company_year])
                        else:
                            continue
                        
                            
                    if years_get:
                        clear_screen()
                        time.sleep(0.5)
                        print(f"**************************** Display {company_year} Finance Informations ****************************\n")
                        for i in years_get:
                            for x in i:
                                print("----------------------------------------------")  
                                print(f"{company_name} => {company_year} => {i[x]}")
                        print("----------------------------------------------") 
                        years_get = [] 
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        companies_finance_management()
                    else:
                        print("We didn't have this year finance information yet")                              
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        companies_finance_management()

        else:
            print("We didn't have any finance informations")
            time.sleep(2)
            clear_screen()
            time.sleep(0.5)
            companies_finance_management()
    
    elif user_choice == "4":
        if finance_dic:
            clear_screen()
            time.sleep(0.5)
            print("Choose a column that you want to analysis data from it\n1. Sales Quantity\n2. Total Profits")
            column_name = input("please enter your choice (1 or 2): ")
            while column_name != "1" and column_name != "2":
                print("Invalid Choice, please try again")
                column_name = input("please enter your choice (1 or 2) only: ")
            if column_name == "1":
                clear_screen()
                time.sleep(0.5)
                print("**************************** Sales Quantity Data Analysis ****************************\n")
                print(f"Min => {df['Sales'].min()}")
                print(f"Max => {df['Sales'].max()}")
                print(f"Mean => {df['Sales'].mean()}")
                print(f"Median => {df['Sales'].median()}")
                print(f"Sum => {df['Sales'].sum()}")
                index_choice = input("Do you want to see column that have min value?\nplease enter (yes or no): ").lower()
                while index_choice != "yes" and index_choice != "no":
                    print("Invalid Choice, please try again")
                    index_choice = input("please enter (yes or no) only: ")
                if index_choice == "yes":
                    clear_screen()
                    time.sleep(0.5)
                    print(print(df.iloc[df['Sales'].idxmin()]))
                    time.sleep(3)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                else:
                    index_choice = input("Do you want to see column that have max value?\nplease enter (yes or no): ").lower()
                    while index_choice != "yes" and index_choice != "no":
                        print("Invalid Choice, please try again")
                        index_choice = input("please enter (yes or no) only: ")
                    if index_choice == "yes":
                        clear_screen()
                        time.sleep(0.5)
                        print(print(df.iloc[df['Sales'].idxmax()]))
                        time.sleep(3)
                        clear_screen()
                        time.sleep(0.5)
                        companies_finance_management()
                    else:
                        print("Go to main page......")
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        companies_finance_management()     
            else:
                clear_screen()
                time.sleep(0.5)
                print("**************************** Total Profits Data Analysis ****************************\n")
                print(f"Min => {df['Profit'].min()}")
                print(f"Max => {df['Profit'].max()}")
                print(f"Mean => {df['Profit'].mean()}")
                print(f"Median => {df['Profit'].median()}")
                print(f"Sum => {df['Profit'].sum()}")
                index_choice = input("Do you want to see column that have min value?\nplease enter (yes or no): ").lower()
                while index_choice != "yes" and index_choice != "no":
                    print("Invalid Choice, please try again")
                    index_choice = input("please enter (yes or no) only: ")
                if index_choice == "yes":
                    clear_screen()
                    time.sleep(0.5)
                    print(df.iloc[df['Profit'].idxmin()])
                    time.sleep(3)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                else:
                    index_choice = input("Do you want to see column that have max value?\nplease enter (yes or no): ").lower()
                    while index_choice != "yes" and index_choice != "no":
                        print("Invalid Choice, please try again")
                        index_choice = input("please enter (yes or no) only: ")
                    if index_choice == "yes":
                        clear_screen()
                        time.sleep(0.5)
                        print(df.iloc[df['Profit'].idxmax()])
                        time.sleep(3)
                        clear_screen()
                        time.sleep(0.5)
                        companies_finance_management()
                    else:
                        print("Go to main page......")
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        companies_finance_management()
        else:
            print("We didn't have any finance informations yet")
            time.sleep(2)
            clear_screen()
            time.sleep(0.5)
            companies_finance_management()


    elif user_choice == "5":
        clear_screen()
        time.sleep(0.5)
        print("**************************** Show your finance information with graph & bar img ****************************\n")
        print("Choose your info show way:\n1. Graph Line\n2. Bar\n3. Pie\n4. Histogram\n5. Scatter")
        show_way = input("Please enter your choice (1,2,3,4 or 5): ")
        while show_way not in ["1", "2", "3", "4", "5"]:
            print("Invalid Choice, please try again")
            show_way = input("Please enter your choice (1,2,3,4 or 5) only: ")
        if show_way == "1":
            clear_screen()
            time.sleep(0.5)
            print("\nChoose your column:\n1. Year\n2. Month\n3. Place\n4. Sales\n5. Profits\n")
            column_show = input("Please enter your choice (1,2,3,4 or 5): ")
            while column_show not in ["1", "2", "3", "4", "5"]:
                print("Invalid Choice, please try again")
                column_show = input("Please enter your choice (1,2,3,4 or 5) only: ")
            if column_show == "1":
                clear_screen()
                time.sleep(0.5)
                plt.plot(df['Year'], df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Years Plot.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "2":
                clear_screen()
                time.sleep(0.5)
                plt.plot(df["Month"], df["Sales"])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Months Plot.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "3":
                clear_screen()
                time.sleep(2)
                plt.plot(df['Place'], df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Places Plot.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "4":
                clear_screen()
                time.sleep(2)
                plt.plot(df['Year'], df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Sales Plot.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "5":
                clear_screen()
                time.sleep(2)
                plt.plot(df['Year'], df['Profit'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Profits Plot.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

        elif show_way == "2":
            clear_screen()
            time.sleep(0.5)
            print("\nChoose your column:\n1. Year\n2. Month\n3. Place\n4. Sales\n5. Profits\n")
            column_show = input("Please enter your choice (1,2,3,4 or 5): ")
            while column_show not in ["1", "2", "3", "4", "5"]:
                print("Invalid Choice, please try again")
                column_show = input("Please enter your choice (1,2,3,4 or 5) only: ")
            if column_show == "1":
                clear_screen()
                time.sleep(0.5)
                plt.bar(df['Year'], df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Years Bar.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "2":
                clear_screen()
                time.sleep(0.5)
                plt.bar(df['Month'], df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Months Bar.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "3":
                clear_screen()
                time.sleep(2)
                plt.bar(df['Place'], df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Places Bar.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "4":
                clear_screen()
                time.sleep(2)
                plt.bar(df['Year'], df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Sales Bar.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "5":
                clear_screen()
                time.sleep(2)
                plt.bar(df['Year'], df['Profits'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Profits Bar.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

        elif show_way == "3":
            clear_screen()
            time.sleep(0.5)
            print("\nChoose your column:\n1. Year\n2. Month\n3. Place\n4. Sales\n5. Profits\n")
            column_show = input("Please enter your choice (1,2,3,4 or 5): ")
            while column_show not in ["1", "2", "3", "4", "5"]:
                print("Invalid Choice, please try again")
                column_show = input("Please enter your choice (1,2,3,4 or 5) only: ")
            if column_show == "1":
                clear_screen()
                time.sleep(0.5)
                plt.pie(df['Year'], df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Years Pie.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                
            elif column_show == "2":
                clear_screen()
                time.sleep(0.5)
                plt.pie(df['Month'], df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Months Pie.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "3":
                clear_screen()
                time.sleep(2)
                plt.pie(df['Place'], df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Places Pie.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "4":
                clear_screen()
                time.sleep(2)
                plt.pie(df['Year'], df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Sales Pie.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "5":
                clear_screen()
                time.sleep(2)
                plt.pie(df['Year'], df['Profit'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Profits Pie.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

        elif show_way == "4":
            clear_screen()
            time.sleep(0.5)
            print("\nChoose your column:\n1. Year\n2. Month\n3. Place\n4. Sales\n5. Profits\n")
            column_show = input("Please enter your choice (1,2,3,4 or 5): ")
            while column_show not in ["1", "2", "3", "4", "5"]:
                print("Invalid Choice, please try again")
                column_show = input("Please enter your choice (1,2,3,4 or 5) only: ")
            if column_show == "1":
                clear_screen()
                time.sleep(0.5)
                plt.hist(df['Year'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Years Histogram.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "2":
                clear_screen()
                time.sleep(0.5)
                plt.hist(df['Month'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Months Histogram.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "3":
                clear_screen()
                time.sleep(2)
                plt.hist(df['Place'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Places Histogram.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "4":
                clear_screen()
                time.sleep(2)
                plt.hist(df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Sales Histogram.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "5":
                clear_screen()
                time.sleep(2)
                plt.hist(df['Profit'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Profits Histogram.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

        elif show_way == "5":
            clear_screen()
            time.sleep(0.5)
            print("\nChoose your column:\n1. Year\n2. Month\n3. Place\n4. Sales\n5. Profits\n")
            column_show = input("Please enter your choice (1,2,3,4 or 5): ")
            while column_show not in ["1", "2", "3", "4", "5"]:
                print("Invalid Choice, please try again")
                column_show = input("Please enter your choice (1,2,3,4 or 5) only: ")
            if column_show == "1":
                clear_screen()
                time.sleep(0.5)
                plt.scatter(df['Year'], df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Years Scatter.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "2":
                clear_screen()
                time.sleep(0.5)
                plt.scatter(df['Month'], df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Months Scatter.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "3":
                clear_screen()
                time.sleep(2)
                plt.scatter(df['Place'], df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Places Scatter.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "4":
                clear_screen()
                time.sleep(2)
                plt.scatter(df['Year'], df['Sales'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Sales Scatter.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()

            elif column_show == "5":
                clear_screen()
                time.sleep(2)
                plt.scatter(df['Year'], df['Profit'])
                plt.show()
                time.sleep(2)
                save_image = input("Do you want to save this analysis? (yes, no): ").lower()
                while save_image != "yes" and save_image != "no":
                    print("Invalid Choice, please try again")
                    save_image = input("Do you want to save this analysis? (yes, no) only: ").lower()
                if save_image == "yes":
                    plt.savefig(f'{company_name} Profits Scatter.png')
                    print("Image Created")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()
                elif save_image == "no":
                    print("Ok, Go to the main page")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    companies_finance_management()




    elif user_choice == "6":
        print("Exiting.......")
        time.sleep(2)
        exit()


  except ValueError:
        print("You can't add letter here, only number, please try again")
        time.sleep(2)
        clear_screen()
        time.sleep(0.5)
        companies_finance_management()



def database_to_dic():
    global finance_dic
    global finance_dic_2
    global df
    company_email = "".join(company_emails)
    if company_info:
        for company in company_info:
            if "".join(company_emails) in company:
                emails_get.append("".join(company_emails))
            else:
                continue

        if emails_get:
            cr_finance_info.execute(f"select company_finance from finance_info where company_email = '{company_email}'")
            result = cr_finance_info.fetchone()
            db_finance_info.commit()
            json_data = json.loads(result[0])
            finance_dic = json_data

            cr_company_finance_info.execute(f"select year, month, place, sales, profit from companies_finance_information where company_email = '{company_email}'")
            result_2 = cr_company_finance_info.fetchall()
            db_company_finance_info.commit()
            if result_2:
                finance_dic_2 = result_2[1:]
                df = pd.DataFrame(finance_dic_2)
                df.columns = ["Year", "Month", "Place", "Sales", "Profit"]
                db_company_finance_info.commit()
                companies_finance_management()
            else:
                companies_finance_management()

        else:
            cr_finance_info.execute(f"insert into finance_info(company_email, company_finance) values('{company_email}', '0')")
            db_finance_info.commit()

            cr_company_finance_info.execute(f"insert into companies_finance_information(company_email, year, month, place, sales, profit) values('{company_email}', '0', '0', '0', '0', '0')")
            db_company_finance_info.commit()
            companies_finance_management()
    else:
        cr_finance_info.execute(f"insert into finance_info(company_email, company_finance) values('{company_email}', '0')")
        db_finance_info.commit()

        cr_company_finance_info.execute(f"insert into companies_finance_information(company_email, year, month, place, sales, profit) values('{company_email}', '0', '0', '0', '0', '0')")
        db_company_finance_info.commit()
        companies_finance_management()





def signup_and_login():
    clear_screen()
    time.sleep(0.5)
    print("**************************** Welcome to the companies finance management app ****************************\n")
    print("Choose an Action\n\n1. Signup\n2. Login\n")
    user_choice = input("please enter your choice (1 or 2): ")
    while user_choice != "1" and user_choice != "2":
        print("Invalid Choice, please try again")
        user_choice = input("please enter your choice (1 or 2) only: ")
    if user_choice == "1":
        clear_screen()
        time.sleep(0.5)
        create_new_user = create_user()
        if company_info == []:
            cr_signup_or_login.execute(f"insert into company_info(company_name, company_email, password) values('{create_new_user.company_name}', '{create_new_user.company_email}', '{create_new_user.password}')")
            db_signup_or_login.commit()
            print("Welcome to our finance management app..........")
            time.sleep(2)
            clear_screen()
            time.sleep(0.5)
            database_to_dic()
        else:
            for company in company_info:
                if create_new_user.company_email in company:
                    print("We have this user already, please go to login")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    signup_and_login()
                else:
                    cr_signup_or_login.execute(f"insert into company_info(company_name, company_email, password) values('{create_new_user.company_name}', '{create_new_user.company_email}', '{create_new_user.password}')")
                    db_signup_or_login.commit()
                    print("Welcome to our finance management app..........")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    database_to_dic()
            
    else:
        clear_screen()
        time.sleep(0.5)
        create_new_user = create_user()
        if company_info == []:
            print("We didn't have any user yet, please go to signup")
            time.sleep(2)
            clear_screen()
            time.sleep(0.5)
            signup_and_login()
        else:
            for company in company_info:
                if create_new_user.company_email in company:
                    if create_new_user.company_name in company:
                        if create_new_user.password in company:
                            user_get.append(company)
                        else:
                            print("Your password is wrong, please try again")
                            time.sleep(2)
                            clear_screen()
                            time.sleep(0.5)
                            signup_and_login()
                    else:
                        print("Your company name is wrong, please try again")
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        signup_and_login()
                else:
                    continue
            
            if user_get:
                print("Login........")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                database_to_dic()
            else:
                print("We didn't have this user, please try again")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                signup_and_login()
                            

            

signup_and_login()




            
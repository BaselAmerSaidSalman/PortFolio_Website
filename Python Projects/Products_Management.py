# Class_Products
class Products:
    def __init__ (self, name, price, type, amount):
        self.name = name
        self.price = price
        self.type = type
        self.amount = amount

# Create_New_Product_Info      
def create_product():
    product_type = input("Please enter the type of your product: ")
    product_name = input("Please enter the name of your product: ")
    product_price = int(input("Please enter the price of your product: "))
    product_amount = int(input("Please enter an amount of your product: "))
 
    return Products(product_name, product_price, product_type, product_amount)

# Interface
import time
import os
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

# Project_Lists_&_Dic
product_dic = {}
products_searched = []

# Project_Function
def products_management():
    try:
        # User_Choice
        clear_screen()
        time.sleep(0.5)
        print("****************** Welcome to the products management! ******************")
        print("\n\nChoose an Action!\n\n1.Add a new product\n2.See all products\n3.Search about products\n4.Exit\n")
        user_choice = input("Enter your choice (1,2,3 or 4): ")
        while user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4":
            print("Sorry, Invalid Choice")
            user_choice = input("Pleas enter your choice (1,2,3 or 4): ")

        # Add_New_Product
        if user_choice == "1":
            clear_screen()
            time.sleep(0.5)
            create_new_product = create_product()
            for type in product_dic:
                if create_new_product.name in product_dic[type]:
                    print("We had this product already")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    products_management()

            else:
                if create_new_product.type in product_dic:
                    product_dic[create_new_product.type][create_new_product.name] = {"Price" : str(create_new_product.price) + "$" , "Amount" : create_new_product.amount}
                    print("Added Successfully!")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    products_management()
                else:
                    product_dic[create_new_product.type] = {create_new_product.name : {"Price" : str(create_new_product.price) + "$" , "Amount" : create_new_product.amount}}
                    print("Added Successfully!")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    products_management()

        # Display_All_Products
        elif user_choice == "2":
            if product_dic:
                clear_screen()
                time.sleep(0.5)
                print("******************* All Products Information *******************")
                for x in product_dic:
                    print(f"{x} is {product_dic[x]}")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                products_management()
               
            else:
                print("We didn't have any products yet!")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                products_management()
            
        # Search_Product
        elif user_choice == "3":
            if product_dic:
                clear_screen()
                time.sleep(0.5)
                print("Search by\n\n1.Product_Type\n2.Product_Name\n3.Product_Price\n")
                search_way = input("Enter your choice (1, 2 or 3): ")
                while search_way != "1" and search_way != "2" and search_way != "3":
                    print("Sorry, Invalid input")
                    search_way = input("Enter your choice (1, 2 or 3): ")

                # Search_by_Product_Type
                if search_way == "1":
                    clear_screen()
                    time.sleep(0.5)
                    product_type_search = input("Enter the type of your product: ")
                    for type in product_dic:
                        if product_type_search in product_dic:
                            print(f"{product_type_search} Information: {product_dic[type]}")
                            time.sleep(2)
                            clear_screen()
                            time.sleep(0.5)
                            products_management()
                        else:
                            print("We didn't have this product type yet")
                            time.sleep(2)
                            clear_screen()
                            time.sleep(0.5)
                            products_management()

                # Search_by_Product_Name
                elif search_way == "2":
                    clear_screen()
                    time.sleep(0.5)
                    product_name_search = input("Please enter the name of your product: ")
                    for type in product_dic:
                        for name in product_dic[type]:
                            if product_name_search in product_dic[type]:
                                print(f"{product_name_search} Information: {product_dic[type][name]}")
                                time.sleep(2)
                                clear_screen()
                                time.sleep(0.5)
                                products_management()
                            else:
                                print("We didn't have this product name yet")
                                time.sleep(2)
                                clear_screen()
                                time.sleep(0.5)
                                products_management()

                # Search_by_Product_Price
                elif search_way == "3":
                    clear_screen()
                    time.sleep(0.5)
                    product_price_search = input("Please enter the price of your product: ")
                    for type in product_dic:
                        for name in product_dic[type]:     
                            if str(product_price_search) + "$" == product_dic[type][name]['Price']:
                                if product_dic[type][name] not in products_searched:
                                    products_searched.append(product_dic[type][name])
                                else:
                                    continue
                    if products_searched:
                        print("The Products that have same price are: ")
                        for type in product_dic:
                            for name in product_dic[type]:
                                if product_dic[type][name] in products_searched:
                                    print(f" Type => {type} : Name => {name} : Information => {product_dic[type][name]}")
                                else: 
                                    continue
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        products_management()
                    else:
                        print("We didn't find products that have this price")
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        products_management()
            else:
                print("We didn't have any products yet")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                products_management()

        # Exit
        elif user_choice == "4":
            print("\nThank you for using our products management library")
            print("Exiting..........")
            time.sleep(2) 
    # Errors           
    except:
        print("Sorry, Invalid input")
        time.sleep(2)
        clear_screen()
        time.sleep(0.5)
        products_management()
    
# Code
products_management()
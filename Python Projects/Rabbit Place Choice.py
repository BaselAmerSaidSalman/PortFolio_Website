print("Welcome to place the rabbit")
list_1 = ["🍀","🍀","🍀"]
list_2 = ["🍀","🍀","🍀"]
list_3 = ["🍀","🍀","🍀"]
print("""
""",list_1,"""
""",list_2,"""
""",list_3,"""
""")

place = input("Where should the rabbit go? 🐇\nPlease choose a row and a column: ")
while place == "":
  print("You didn't choose a row and a column")
  place = input("Please choose a row and a column🐇: ")
while int(place) > 33:
  print("Sorry, you should choose two numbers")
  place = input("Where should the rabbit go? 🐇\nPlease choose a row and a column: ")
if place == "11":
  list_1.remove("🍀")
  list_1.insert(0,"🐇")
elif place == "12":
  list_1.remove("🍀")
  list_1.insert(1,"🐇")
elif place == "13":
  list_1.remove("🍀")
  list_1.insert(2,"🐇")
elif place == "21":
  list_2.remove("🍀")
  list_2.insert(0,"🐇")
elif place == "22":
  list_2.remove("🍀")
  list_2.insert(1,"🐇")
elif place == "23":
  list_2.remove("🍀")
  list_2.insert(2,"🐇")
elif place == "31":
  list_3.remove("🍀")
  list_3.insert(0,"🐇")
elif place == "32":
  list_3.remove("🍀")
  list_3.insert(1,"🐇")
elif place == "33":
  list_3.remove("🍀")
  list_3.insert(2,"🐇")
print("""Success...\n
""",list_1,"""
""",list_2,"""
""",list_3,"""
""")


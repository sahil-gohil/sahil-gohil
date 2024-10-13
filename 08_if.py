# Exercise: Python If Condition
#1  Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
# i. Write a program that asks user to enter a city name and it should tell which country the city belongs to
# ii. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

# i
# city = input("input")
# if city in india:
#     print(f"{city} is in india")
# elif city in pakistan:
#     print(f"{city} is in pakistan")
# elif city in bangladesh:
#     print(f"{city} is in bangladesh")


#ii
# city_1 = input("enter city_1")
# city_2 = input("enter city_2")

# if city_1 and city_2 in india:
#     print("same countrey")

# elif city_1 and city_2 in pakistan:
#     print("same countrey")

# elif city_1 and city_2 in bangladesh:
#     print("same countrey")

# else :
#     print("not same countrey")

   
#2  Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# i. Ask user to enter his fasting sugar level
# ii. If it is below 80 to 100 range then print that sugar is low
# iii. If it is above 100 then print that it is high otherwise print that it is normal

sugar_lvl = int(input("Enter your sugar level: "))
if sugar_lvl < 80:
    print("your sugar level is low")
elif sugar_lvl > 100:
    print("your sugar level is high")
else:
    print("its normal")
# Exercise: String in Python


# 1 Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
street = "bakers street"
city = "london"
country = "uk"
address = street + '\n' + city + '\n' + country
print("using + opretor",address)

address = f'{street}\n{city}\n{country}'
print("using f opreteor",address)


# 2 Create a variable to store the string "Earth revolves around the sun"
# i Print "revolves" using slice operator
# ii Print "sun" using negative index

system = "Earth revolves around the sun"
print(system[6:13])
print(system[-3:])

# 3 Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

fruit = 4
veggie = 5
print(f"I eat {veggie} veggies and {fruit} fruits daily" )


# 4 I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.

s='maine 200 banana khaye'
s= s.replace("200","10").replace("banana","samosa")
print(s)
# Solution
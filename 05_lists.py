# Exercise: Python Lists
# 1 Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
expense= [2200,2350,2600,2130,2190]


# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
print("In Feb, how many dollars you spent extra ",expense[1]-expense[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
print("this is sum of 3 months exepense",expense[0]+expense[1]+expense[2])


# 3. Find out if you spent exactly 2000 dollars in any month
print("did i spend 2000 in any monrh", 2000 in expense)


# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expense.append(1980)
print(expense)

expense[2] = expense[2]-200

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list
# 

print("in april i got refund and my april expence is ",expense[3])



#2 You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

# 1. Length of the list
print(len(heros))
# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'

heros.remove("black panther")
heros.insert(3, 'black panther' )

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]=['doctor strange']
print(heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)
# Solution
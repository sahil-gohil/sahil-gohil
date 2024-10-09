# Exercise: Numbers in python






# SOLUTION

#1  You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
height = 92
wide = 48.8
area = height * wide

print(area)
# area of football feild is 4489.599999999999

#2 You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?

packets = 9
costs = 1.49
total = packets * costs
print(20 - total)

# sopkeeper return you 6.59 dollers

#3 You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)

length = 5.5 
area = length**2
print(area * 500)


#4 Print binary representation of number 17

print(bin(17))
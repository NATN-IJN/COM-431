print("Please enter the three people in your team")
people = [None] * 3
people[0] = input("Please enter the first person:")
people[1] = input("Please enter the second person:")
people[2] = input("Please enter the third person:")

print("The first person is " + people[0])
print("The second person is " + people[1])
print("The third person is " + people[2])

fourth = input("Please enter the fourth person:")
fifth = input("Please enter the fourth person:")
people.append(fourth)
people.append(fifth)
print("The fourth person is " + people[3])
print("The fifth person is " + people[4])
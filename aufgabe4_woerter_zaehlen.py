# Python3 code to demonstrate
# to count words in string

# initializing string
test_string = "Geeksforgeeks is best Computer Science Portal"

# printing original string
print("The original string is : " + test_string)

# to count words in string
res = test_string.count(" ") + 1

# printing result
print("The number of words in string are : " + str(res))

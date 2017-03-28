
# Ask for the user input
userNum = input("Tell me a number ")

# convert to float 
userNum = float(userNum)

# Do the computation
for i in range(2,10):
	answer = userNum * i
	print("{} times {} is {}.".format(userNum, i , answer))
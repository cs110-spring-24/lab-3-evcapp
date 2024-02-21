import random 

print("Options: 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10" ) 
run = input("Enter the problem you want run: ")
run = int(run)

if run == 1: 
    print("Running Problem 1: ")
    for count in range(1, 1001):
        print(count)
elif run == 2:
    print("Running Problem 2: ")
    for count in range(1, 1001):
        if count % 2 != 0:
            print(count) 
elif run == 3: 
    print("Running Problem 3: ")
    for count in range(1, 1001):
        if count % 3 == 0:
            print(count)
elif run == 4: 
    print("Running Problem 4: ")
    for count in range(1, 1001): 
        if count % 3 == 0 or count % 5 == 0:
            print(count) 
elif run == 5:
    print("Running Problem 5: ")
    user = int(input("Enter a number greater than 200:  "))
    for count in range(1, user): 
        if count % 11 == 0 or count % 13 == 0:
            print(count) 
elif run == 6: 
    print("Running Problem 6: ")
    string = input("Enter a word: ")
    for l in range(len(string)):
        print(string[l])
elif run == 7: 
    print("Running Problem 7: ")
    string = input("Enter a string that has more than 10 letters: ")
    if len(string) <= 10 :
        print("The string is less than 10 letters: ")
    else:
        for l in range(1, len(string), 2): 
            print(string[l])
elif run == 8: 
    print("Running Problem 8: ")
    ones = twos = threes = fours = fives = sixes = 0

    for roll in range(1000):
        dice = random.randint(1, 6)
        if dice == 1:
            print("One")
            ones += 1
        elif dice == 2: 
            print("Two")
            twos += 1 
        elif dice == 3:
            print("Three")
            threes += 1
        elif dice == 4:
            print("Four")
            fours += 1 
        elif dice == 5:
            print("Five")
            fives += 1
        elif dice == 6:
            print("Six")
            sixes += 1

    print(f"After 1000 rolls, we rolled {ones} ones, {twos} twos, {threes} threes, {fours} fours, {fives} fives, and {sixes} sixes")
elif run == 9:
    print("Running Problem 9: ")
    user = input ("Enter a number:  ")
    user = int(user) 
    if user > 1:
        for i in range(2, int(user/2)+1):
            if (user % i) == 0:
                print(user, "is not a prime number")
                break
        else:
            print(user, "is a prime number")
elif run == 10:
    print("Running Problem 10: ")
    print("Printing all Prime numbers less than 1000:")
    for num in range(2, 1000):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            print(num)



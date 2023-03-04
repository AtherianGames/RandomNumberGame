import random
import array as arr

def get_random_num(b):
    return random.randint(0,b)

def random_number_game():
    arrsize = 0
    while arrsize > 20 or arrsize < 2:
        arrsize = int(input("How many slots would you like?(Min: 2, Max:20) "))
    random_nums = arr.array("i",[-1] * arrsize)
    set_nums = arr.array("i",[-1] * arrsize)
    print("Select the upper bound for your random number game.")
    print("Lower Bound: 0")
    bound2 = 0
    while bound2 < 1 or bound2 > 999:
        bound2 = int(input("Upper Bound (Max 999): "))
    print("**** Game Start ****")
    roundcount = 0
    while roundcount < arrsize:
        random_nums[roundcount] = get_random_num(bound2)
        print(random_nums[roundcount])
        for x in set_nums:
            if x == -1:
                print("___", end=" ")
            else:
                print(x, end=" ")
        print("")
        slot = int(input("What slot would you like to put " + str(random_nums[roundcount]) + "? (Min: 1, Max: " + str(arrsize) + ") "))
        set_nums[(slot-1)] = random_nums[roundcount]
        lastx = set_nums[0]
        for x in set_nums:
            if x == -1:
                pass
            else:
                if x < lastx:
                    print("You have lost the game!")
                    return None
                else:
                    lastx = x
        roundcount += 1

def random_number_alg():
    arrsize = 0
    while arrsize > 20 or arrsize < 2:
        arrsize = int(input("How many slots would you like?(Min: 2, Max:20) "))
    random_nums = arr.array("i", [-1] * arrsize)
    set_nums = arr.array("i", [-1] * arrsize)
    print("Select the upper bound for your random number game.")
    print("Lower Bound: 0")
    bound2 = 0
    while bound2 < 1 or bound2 > 999:
        bound2 = int(input("Upper Bound (Max 999): "))
    print("**** Game Start ****")
    roundcount = 0
    slot = 1
    while roundcount < arrsize:
        random_nums[roundcount] = get_random_num(bound2)
        print(random_nums[roundcount])
        for x in set_nums:
            if x == -1:
                print("___", end=" ")
            else:
                print(x, end=" ")
        print("")
        slot = random.randint(1, arrsize)
        while not(set_nums[(slot-1)] == -1):
            slot = random.randint(1, arrsize)
        set_nums[(slot - 1)] = random_nums[roundcount]
        lastx = set_nums[0]
        for x in set_nums:
            if x == -1:
                pass
            else:
                if x < lastx:
                    for x in set_nums:
                        if x == -1:
                            print("___", end=" ")
                        else:
                            print(x, end=" ")
                    print("")
                    print("You have lost the game!")
                    return None
                else:
                    lastx = x
        roundcount += 1

while 1:
    print("******** Random Number Game ********")
    print("Would you like to play the game or see a computer algorithm?")
    print("1. Play a Game.")
    print("2. See a Computer Algorithm.")
    print("3. Exit")
    ch = int(input("Which option would you like to select? "))
    if (ch == 1):
        random_number_game()
    elif (ch == 2):
        random_number_alg()
    elif (ch == 3):
        exit()
    else:
        print("Invalid Selection.")
import random
import array as arr
import math

def get_random_num(b):
    return random.randint(0,b)

def set_bounds():
    arrsize = 0
    bound2 = 0
    while arrsize > 20 or arrsize < 2:
        arrsize = int(input("How many slots would you like?(Min: 2, Max:20) "))
    print("Select the upper bound for your random number game.")
    print("Lower Bound: 0")
    while bound2 < 1 or bound2 > 999:
        bound2 = int(input("Upper Bound (Max 999): "))
    return arrsize, bound2

def print_set_nums(set_nums):
    for x in set_nums:
        if x == -1:
            print("___", end=" ")
        else:
            print(x, end=" ")
    print("")

def random_number_game():
    bounds = set_bounds()
    arrsize = bounds[0]
    bound2 = bounds[1]
    random_nums = arr.array("i", [-1] * arrsize)
    set_nums = arr.array("i", [-1] * arrsize)
    print("**** Game Start ****")
    roundcount = 0
    while roundcount < arrsize:
        random_nums[roundcount] = get_random_num(bound2)
        print(random_nums[roundcount])
        print_set_nums(set_nums)
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

'''def optimal_percentile_game():
    bounds = set_bounds()
    arrsize = bounds[0]
    bound2 = bounds[1]
    random_nums = arr.array("i", [-1] * arrsize)
    set_nums = arr.array("i", [-1] * arrsize)
    print("**** Game Start ****")
    roundcount = 0
    slot = 1
    while roundcount < arrsize:
        random_nums[roundcount] = get_random_num(bound2)
        print(random_nums[roundcount])
        print_set_nums(set_nums)
        percentile = (bound2+1)/arrsize
        for n in range(arrsize):
            if set_nums[(n-1)] == -1:
                for m in range(1,(arrsize+1)):
                    if random_nums[roundcount] < (percentile*(m-n)):
                        set_nums[(n-1)] = random_nums[roundcount]
                        break
                    break
                break
            break
        break
        lastx = set_nums[0]
        for x in set_nums:
            if x == -1:
                pass
            else:
                if x < lastx:
                    print_set_nums(set_nums)
                    print("You have lost the game!")
                    return None
                else:
                    lastx = x
        roundcount += 1
    print_set_nums(set_nums)
    print("You won the game.")'''

def random_number_alg():
    bounds = set_bounds()
    arrsize = bounds[0]
    bound2 = bounds[1]
    random_nums = arr.array("i", [-1] * arrsize)
    set_nums = arr.array("i", [-1] * arrsize)
    print("**** Game Start ****")
    roundcount = 0
    slot = 1
    while roundcount < arrsize:
        random_nums[roundcount] = get_random_num(bound2)
        print(random_nums[roundcount])
        print_set_nums(set_nums)
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
                    print_set_nums(set_nums)
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
        print("What kind of computer algorithm would you like to see?")
        print("1. Random Placement")
        print("2. Percentile Exclusive Placement")
        print("3. Percentile & Bell Curve Distribution Placement")
        ch2 = int(input("Which option would you like to select? "))
        if ch2 == 1:
            random_number_alg()
        elif ch2 == 2:
            #optimal_percentile_game()
            print("Not Implemented Yet")
        elif ch2 == 3:
            print("Not Implemented Yet")
        else:
            print("Invalid Selection.")
    elif (ch == 3):
        exit()
    else:
        print("Invalid Selection.")
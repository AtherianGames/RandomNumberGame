import random
import array as arr
from collections import defaultdict
import math

class MenuInterface(object):
    def runUserSelectedOption(self, user_option):
        raise NotImplementedError()
    def displayMenu(self): #Virtual function - required to be overwritten by derived class
        raise NotImplementedError()
    def getUserOption(self):
        return int(input("Which option would you like to select? "))

    def runMenu(self):
        self.displayMenu()
        self.runUserSelectedOption(self.getUserOption())

    '''@staticmethod
    def runMenu(menu_interface):
        menu_interface.displayMenu()'''

def get_random_num(b):
    return random.randint(0,b)
class MainMenu(MenuInterface):
    def runUserSelectedOption(self, user_option):
        {
            1: random_number_game,
            2: display_alg_menu,
            3: exit
        }[user_option]()
    def displayMenu(self):
        print("******** Random Number Game ********")
        print("Would you like to play the game or see a computer algorithm?")
        print("1. Play a Game.")
        print("2. See a Computer Algorithm.")
        print("3. Exit")

def display_alg_menu():
    print("What kind of computer algorithm would you like to see?")
    print("1. Random Placement")
    print("2. Percentile Exclusive Placement")
    print("3. Percentile & Bell Curve Distribution Placement")
    ch2 = int(input("Which option would you like to select? "))
    return ch2

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

    #mydict = defaultdict(lambda: "___")

    #print(' '.join([mydict[x] for x in range(len(set_nums))]))

    print(' '.join(["___" if x == -1 else str(x) for x in set_nums]))

'''
    # for x in set_nums:
    #     if x == -1:
    #         print("___", end=" ")
    #     else:
    #         print(x, end=" ")
    # print("")
'''

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
                    print_set_nums(set_nums)
                    print("You have lost the game!")
                    return None
                else:
                    lastx = x
        roundcount += 1
    print_set_nums(set_nums)
    print("You won the game.")

def optimal_percentile_game():
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
    print("You won the game.")

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

def main():

    #holds values indefinitely
    main_menu = MainMenu()
    while 1:
        main_menu.runMenu()
        #MainMenu.runMenu(main_menu)
        '''ch = display_main_menu()
        if (ch == 1):
        # rename - Launching game instance
            random_number_game()
        # launch algorithm game
        elif (ch == 2):
            ch2 = display_alg_menu()
            if ch2 == 1:
                random_number_alg()
            elif ch2 == 2:
                optimal_percentile_game()
            elif ch2 == 3:
                print("Not Implemented Yet")
            else:
                print("Invalid Selection.")
        elif (ch == 3):
            exit()
        else:
            print("Invalid Selection.")'''

if __name__ == "__main__":
    main()
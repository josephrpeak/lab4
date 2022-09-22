########################################################################
##
## CS 101 Lab
## Program #4
## Name: Joe Peak
## Email: jrp3yp@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    play = input("Do you want to play again? ==> ")
    play = play.lower()

    if(play == 'y' or play == 'yes' or play == 'YES' or play == 'Y'):
        return True
    elif(play == 'n' or play == 'no' or play == 'NO' or play == 'N'):
        return False
    else:
        print("You must enter Y/YES/N/NO to continue. Please try again")
        play_again()
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager = int(input("How much would you like to wager? ==> "))

    while(wager < 0 or wager > bank):
        print("Invalid amount. Please try again.")
        wager = int(input("How much would you like to wager? ==> "))

    return wager            

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    r1,r2,r3 = random.randint(1,10), random.randint(1,10), random.randint(1,10)

    return (r1, r2, r3)

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''

    if(reela == reelb == reelc):
        return 3
    elif((reela == reelb) or (reelb == reelc) or (reela == reelc)):
        return 2
    else:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    bank = int(input("How many chips would you like to start with? ==> "))

    while(bank < 0 or bank > 100):
        print("Invalid amount. Please try again.")
        bank = int(input("How many chips would you like to start with? ==> "))

    return bank

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if(matches == 3):
        return wager * 10
    elif(matches == 2):
        return wager * 3
    else:
        return wager * -1


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while (bank > 0):  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()
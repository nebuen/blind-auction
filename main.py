from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")
bidders = {}

def bidding():
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bidders[name] = bid
  
  more_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if more_bidder == 'yes':
    clear()
    bidding()

bidding()
#print(bidders)
highest = ""
bid = 0
for key, value in bidders.items():
  temp = 0
  if value > temp:
    temp = value
    bid = temp
    highest = key

print(f"The winning bidder is: {highest}")
    
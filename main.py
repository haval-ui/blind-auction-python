import os
 


from art import logo


print(logo)
print("welcome to the secret auction program.")
def find_highest_bid(bidders_list):
  highest_bid=0
  for bidder in bidders_list:
    bid_amount=bidders_list[bidder]
    if int(bid_amount) > int(highest_bid):
      highest_bid=bid_amount
      winner=bidder
  print(f"the winner is {winner} with a bid of $ {highest_bid}")



bids={}
biding_finished= True
while biding_finished:
  name=input("what is your name ? ")
  price=input("what is your bid in usd ? ")
  bids[name]=price
  should_continue=input("are there any more bidders ? (yes) or (no)" )
  if should_continue=="no":
    biding_finished=False
    find_highest_bid(bids)
  elif should_continue=="yes":
    os.system('cls')


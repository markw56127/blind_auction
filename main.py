from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")
cont = True
name_lst = []
bid_lst = []
auct_dict = {}
while cont == True:
    name = input("What is your name?: ")
    name_lst.append(name)
  
    bid = int(input("What's your bid?: $"))
    bid_lst.append(bid)

    auct_dict["name"] = name_lst
    auct_dict["bid"] = bid_lst
  
    yn = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if yn == 'yes':
        clear()
    elif yn == 'no':
        cont = False

position = auct_dict["bid"].index(max(auct_dict["bid"]))
print("The winner is " + auct_dict["name"][position] + f" with a bid of ${bid_lst[position]}")

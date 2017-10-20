__author__ = 'cni12345'
# A program that tracks your total spending and number of items bought

def main():

    gift_card = 200
    items = 5
    spent = 0
    bought = 0

# While loop that will keep track of the value left in the gift card and how many items left that you can purchase
    while gift_card > 0 and items > 0:
        print("You can purchase up to", items, "items with $", end='')
        print(gift_card)
        price = input("Enter item price: ")
        if not price.isnumeric():
            print("Error: price must be an integer greater than 0")
            price = input("Enter a valid item price: ")
        if price.isnumeric():
            if int(price) > gift_card:
                print("You do not have enough funds\n")
            elif (0 < int(price) <= gift_card) and items > 0:
                if int(price) >= 50:
                    gift_card = (gift_card - int(price)) + 10
                else:
                    gift_card -= int(price)
                    items -= 1
                spent += int(price)
                bought += 1
                print("")

# Prints the total amount items bought and how much was spent purchasing those items
    print("You purchased", bought, "items totaling $", end='')
    print(spent)

# Call on function main
main()

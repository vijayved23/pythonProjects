menu = ["Pasta", "Pizza", "Chicken", "Pork", "Lo Mein"]
prices = [10,12,15,16,14, 14]
yourOrder = []
itemCost = []

def printElements():
    fmt = '{:<8}{:<20}{}'

    print(fmt.format('number', 'menu', 'prices'))
    for i, (menus, grade) in enumerate(zip(menu, prices)):
        print(fmt.format(i, menus, grade))

def ordering():
    cost = 0
    ordering = True
    while ordering:
        order = input("Please input the number of the order that you would like: ")
        print(menu[int(order)])
        cost = cost + prices[int(order)]
        print("That is going to cost ", prices[int(order)], " dollars")
        print("Your total cost is ", cost)
        yourOrder.append(menu[int(order)])
        itemCost.append(prices[int(order)])
        cont = input("If would would like to order again please type Y: ")
        if cont == "Y" or cont == "y":
            ordering = True
        else:
            ordering = False
            return cost

def endOrder(cost):
    print("\n")
    print("YOUR ORDER")
    fmt = '{:<8}{:<20}{}'
    print(fmt.format('Number', 'Your Items', 'Item Cost'))
    for i, (order, ordercost) in enumerate(zip(yourOrder, itemCost)):
        print(fmt.format(i, order, ordercost))
    print("Now that you have completed your order please pay",cost, "dollars")
    checkPay = input("Please type pay to complete your order: ")
    if checkPay == "pay":
        print("Enjoy!")
    else:
        print("Sorry that you couldn't order hopefully you come back")

def main():
    print("Welcome to Restaurant, Here is our menu")
    printElements()
    endOrder(ordering())
main()
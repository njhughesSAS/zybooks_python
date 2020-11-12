class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_description = 'none'
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        totalCost = self.item_quantity * self.item_price
        print('{} {} @ ${:.0f} = ${:.0f}'.format(self.item_name, self.item_quantity, self.item_price, totalCost))

    def print_item_description(self):
        print('{}: {}'.format(self.item_name, self.item_description))


class ShoppingCart:
    def __init__(self, customer_name, current_date):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for i in self.cart_items:
            if i.item_name == item_name:
                found = True
                self.cart_items.remove(i)
        if found == False:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, item):
        found = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                found = True
                self.cart_items[i].item_quantity = item.item_quantity
        if found == False:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        totalNumItems = 0
        for i in self.cart_items:
            totalNumItems += i.item_quantity
        return totalNumItems

    def get_cost_of_cart(self):
        totalCost = 0
        for i in self.cart_items:
            totalCost += (i.item_price * i.item_quantity)
        return totalCost

    def print_total(self):
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('Number of Items: {}\n'.format(self.get_num_items_in_cart()))
        if len(self.cart_items) > 0:
            for i in self.cart_items:
                i.print_item_cost()
        else:
            print('SHOPPING CART IS EMPTY')
        totalCost = self.get_cost_of_cart()
        print('\nTotal: ${:.0f}'.format(totalCost))

    def print_descriptions(self):
        print('{}\'s Shopping Cart - {}\n'.format(self.customer_name, self.current_date))
        print('Item Descriptions')
        if len(self.cart_items) > 0:
            for i in self.cart_items:
                i.print_item_description()
        else:
            print('SHOPPING CART IS EMPTY')


def print_menu(theCart):
    menuOp = ' '
    print('MENU');
    print('a - Add item to cart');
    print('r - Remove item from cart');
    print('c - Change item quantity');
    print('i - Output items\' descriptions');
    print('o - Output shopping cart');
    print('q - Quit\n');
    while menuOp != 'a' and menuOp != 'r' and menuOp != 'c' and menuOp != 'i' and menuOp != 'o' and menuOp != 'q':
        menuOp = input('Choose an option:\n')
        if menuOp == 'a':
            print('ADD ITEM TO CART')
            name = input('Enter the item name:\n')
            description = input('Enter the item description:\n')
            price = float(input('Enter the item price:\n'))
            quantity = int(input('Enter the item quantity:\n'))
            newItem = ItemToPurchase()
            newItem.item_name = name
            newItem.item_description = description
            newItem.item_price = price
            newItem.item_quantity = quantity
            theCart.add_item(newItem)
        elif menuOp == 'r':
            print('REMOVE ITEM FROM CART')
            name = input('Enter name of item to remove:\n')
            theCart.remove_item(name)
        elif menuOp == 'c':
            print('CHANGE ITEM QUANTITY')
            name = input('Enter the item name:\n')
            quantity = int(input('Enter the new quantity:\n'))
            item = ItemToPurchase()
            item.item_name = name
            item.item_quantity = quantity
            theCart.modify_item(item)
        elif menuOp == 'i':
            print('OUTPUT ITEMS\' DESCRIPTIONS')
            theCart.print_descriptions()
        elif menuOp == 'o':
            print('OUTPUT SHOPPING CART')
            theCart.print_total()
    return menuOp


if __name__ == "__main__":
    menuChoice = ' '
    custName = input('Enter customer\'s name:\n')
    dayDate = input('Enter today\'s date:\n')

    print('\nCustomer name: {}'.format(custName))
    print('Today\'s date: {}'.format(dayDate))

    myCart = ShoppingCart(custName, dayDate)

    while menuChoice != 'q':
        print('')
        menuChoice = print_menu(myCart)

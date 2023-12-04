from random import uniform


class ShoppingCart():
    
    def __init__(self):
        self.cart = {}
        self.totCost=0
        self.name = 'not declared'


    def shoppingCart(self):       
        self.name = input('Howdy! What\'s your name?\t')
        self.ask()


    def ask(self):
        while True:
            ask=input(f'Hey there {self.name}! What would you like to do in your shopping cart? Options: Add/Remove/Display/Quit\t')
            if ask == 'Add' or ask == 'add':
                self.add()
            elif ask == 'Remove' or ask == 'remove':
                self.remove()
            elif ask == 'Display' or ask == 'display':
                self.display()
            elif ask == 'Quit' or ask == 'quit':
                print('Have a nice day!')
                break
            else:
                print("Sorry! Please try again, selecting one of the available options\n")

                
    def add(self):
        item = input('What would you like to add to your cart?\t')
        num = input('How many would you like to add?\t')
        
        if item not in self.cart:
            self.cart[item]={'total':num,'price':(round(uniform(1.10, 4.59), 2))}
            print(f'Great, {num} {item} added!\n')
        else:
            self.cart[item]['total']+=num


    def remove(self):
        item = input('What would you like to remove from your cart?\t')
        
        if item in self.cart:
            num = input('How many would you like to remove?\t')
            self.cart[item]['total']=int(self.cart[item]['total'])-int(num)
            if self.cart[item]['total']<1:
                print(f"All {item}\'s removed from cart\n")
                del self.cart[item]
            else:
                print(f"{num} {item}\'s removed, {self.cart[item]['total']} remain\n")
        else:
            print(f"Sorry there are no {item}\'s in your cart.\nPlease try again\n")

            
    def cost(self):
        self.totCost=0
        for k in self.cart:
            self.totCost=float(self.totCost)+((int(self.cart[k]['total']))*(float(self.cart[k]['price'])))

            
    def display(self):
        self.cost()
        self.totCost="%.2f" % round(self.totCost, 2)
        print('\nYour cart contains:')
        for k in self.cart:
            print(f"{self.cart[k]['total']} {k}\'s for {self.cart[k]['price']} each")
        print(f'Your check out total is {self.totCost}.\n')



mine = ShoppingCart()   
mine.shoppingCart()
class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        dollars = int(input("How many dollars?: "))
        half_dollars = int(input("how many half dollars?: ")) * 0.5
        quarters = int(input("how many quarters?: ")) * 0.25
        nickels = int(input("how many nickels?: ")) * 0.05
        return dollars + half_dollars + quarters + nickels

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        else:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            print("Payment accepted.")
            return True
import cashier
import data
import sandwich_maker
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()



def main():
    is_on = True

    while is_on:
        choice = input("What size sandwich would you like? (small/medium/large) or 'off' to exit: ").lower()

        if choice == "off":
            is_on = False
            print("Turning off the machine...")
        elif choice in recipes:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)
        elif choice == "report":
            print(resources)
        else:
            print("Invalid selection.")

if __name__=="__main__":

    main()

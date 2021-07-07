class CoffeeMachine:

    def __init__(self):
        self.inventory = {'water': 400, 'milk': 540, 'coffee beans': 120, 'disposable cups': 9, 'money': 550}

    def state(self):
        print('The coffee machine has:')
        for item in self.inventory:
            print(f'{self.inventory[item]} of {item}')
        print()

    def action(self):
        action = input('Write action (buy, fill, take):\n')
        print()
        if action == 'buy':
            self.buy()
        elif action == 'fill':
            self.fill()
        else:
            self.take()

    def buy(self):
        espresso = {'water': 250, 'coffee beans': 16, 'disposable cups': 1, 'money': -4}
        latte = {'water': 350, 'milk': 75, 'coffee beans': 20, 'disposable cups': 1, 'money': -7}
        cappuccino = {'water': 200, 'milk': 100, 'coffee beans': 12, 'disposable cups': 1, 'money': -6}
        choices = [espresso, latte, cappuccino]
        choice = choices[int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')) - 1]
        for ingredient in self.inventory:
            if ingredient in choice:
                self.inventory[ingredient] -= choice[ingredient]
        print()
        self.state()

    def fill(self):
        self.inventory['water'] += int(input('Write how many ml of water you want to add:\n'))
        self.inventory['milk'] += int(input('Write how many ml of milk you want to add:\n'))
        self.inventory['coffee beans'] += int(input('Write how many grams of coffee beans you want to add:\n'))
        self.inventory['disposable cups'] += int(input('Write how many disposable coffee cups you want to add:\n'))
        print()
        self.state()

    def take(self):
        print(f'I gave you ${self.inventory["money"]}')
        self.inventory['money'] = 0
        print()
        self.state()


def main():
    on = CoffeeMachine()
    on.state()
    on.action()


main()

class CoffeeMachine:

    def __init__(self):
        self.inventory = {'water': 400, 'milk': 540, 'coffee beans': 120, 'disposable cups': 9, 'money': 550}

    def state(self):
        print('The coffee machine has:')
        for item in self.inventory:
            if item != 'money':
                print(f'{self.inventory[item]} of {item}')
            else:
                print(f'${self.inventory[item]} of {item}')
        print()
        self.action()

    def action(self):
        action = input('Write action (buy, fill, take, remaining, exit):\n')
        print()
        if action == 'buy':
            self.buy()
        elif action == 'fill':
            self.fill()
        elif action == 'take':
            self.take()
        elif action == 'remaining':
            self.state()
        else:
            exit()

    def buy(self):
        espresso = {'water': 250, 'coffee beans': 16, 'disposable cups': 1, 'money': -4}
        latte = {'water': 350, 'milk': 75, 'coffee beans': 20, 'disposable cups': 1, 'money': -7}
        cappuccino = {'water': 200, 'milk': 100, 'coffee beans': 12, 'disposable cups': 1, 'money': -6}
        choices = [espresso, latte, cappuccino]
        selection = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
        if selection == 'back':
            print()
            self.action()
        else:
            choice = choices[int(selection) - 1]
            for item in choice:
                if item in self.inventory and item != 'money':
                    if choice[item] > self.inventory[item]:
                        print(f'Sorry, not enough {item}!\n')
                        self.action()
                    else:
                        print('I have enough resources, making you a coffee!')
                        for item in self.inventory:
                            if item in choice:
                                self.inventory[item] -= choice[item]
                        print()
                        self.action()

    def fill(self):
        self.inventory['water'] += int(input('Write how many ml of water you want to add:\n'))
        self.inventory['milk'] += int(input('Write how many ml of milk you want to add:\n'))
        self.inventory['coffee beans'] += int(input('Write how many grams of coffee beans you want to add:\n'))
        self.inventory['disposable cups'] += int(input('Write how many disposable coffee cups you want to add:\n'))
        print()
        self.action()

    def take(self):
        print(f'I gave you ${self.inventory["money"]}')
        self.inventory['money'] = 0
        print()
        self.action()


def main():
    on = CoffeeMachine()
    on.action()


main()

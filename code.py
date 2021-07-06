water = int(input('Write how many ml of water the coffee machine has:\n'))
milk = int(input('Write how many ml of milk the coffee machine has:\n'))
beans = int(input('Write how many g of coffee beans the coffee machine has:\n'))
cups = int(input('Write how many cups of coffee you will need:\n'))
available = min(water // 200, milk // 50, beans // 15)

if cups == available:
    print('Yes, I can make that amount of coffee')
elif cups > available:
    print(f'No, I can make only {available} cups of coffee')
else:
    print(f'Yes, I can make that amount of coffee (and even {available - cups} more than that)')
    

gl_money = 550
gl_water = 400
gl_milk = 540
gl_beans = 120
gl_disposable = 9


def how_many():
    print()
    print("The coffee machine has:")
    print(gl_water, "of water")
    print(gl_milk, "of milk")
    print(gl_beans, "of coffee beans")
    print(gl_disposable, "of disposable cups")
    print("$" + str(gl_money), "of money")
    print()


def fill():
    print("Write how many ml of water the coffee machine has:")
    water = int(input("> "))
    print("Write how many ml of milk the coffee machine has:")
    milk = int(input("> "))
    print("Write how many grams of coffee beans the coffee machine has:")
    beans = int(input("> "))
    print("Write how many disposable cups of coffee do you want to add:")
    coffee_bean = int(input("> "))
    global gl_water
    global gl_milk
    global gl_beans
    global gl_disposable
    gl_water += water
    gl_milk += milk
    gl_beans += beans
    gl_disposable += coffee_bean


def check_resource(_water, _milk, _beans, _money, _disposable):
    global gl_water
    global gl_milk
    global gl_beans
    global gl_money
    global gl_disposable
    text = "Sorry, not enough "
    if _water < 0 < _milk and _beans > 0:
        text = text + "water!"
    elif _milk < 0 < _water and _beans > 0:
        text = text + "milk!"
    elif _beans < 0 < _water and _milk > 0:
        text = text + "coffee beans!"
    elif (_water < 0 and _milk < 0) or (_water < 0 and _beans < 0) or (_milk < 0 and _beans < 0):
        text = "Sorry, not enough "
    else:
        text = "I have enough resources, making you a coffee!"
        gl_water = _water
        gl_milk = _milk
        gl_beans = _beans
        gl_money = _money
        gl_disposable = _disposable
    print(text)


def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    coffee = input("> ")
    global gl_water
    global gl_milk
    global gl_beans
    global gl_disposable
    global gl_money
    _water = gl_water
    _milk = gl_milk
    _beans = gl_beans
    _disposable = gl_disposable
    _money = gl_money
    if coffee == 'back':
        pass
    elif int(coffee) == 1:
        _water = gl_water - 250
        _beans = gl_beans - 16
        _money = gl_money + 4
        _disposable = gl_disposable - 1
        check_resource(_water, _milk, _beans, _money, _disposable)
    elif int(coffee) == 2:
        _water = gl_water - 350
        _milk = gl_milk - 75
        _beans = gl_beans - 20
        _money = gl_money + 7
        _disposable = gl_disposable - 1
        check_resource(_water, _milk, _beans, _money, _disposable)
    elif int(coffee) == 3:
        _water = gl_water - 200
        _milk = gl_milk - 100
        _beans = gl_beans - 12
        _money = gl_money + 6
        _disposable = gl_disposable - 1
        check_resource(_water, _milk, _beans, _money, _disposable)


print("Write action (buy, fill, take, remaining, exit):")
action = input()
while True:
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        print("I gave you $" + str(gl_money))
        gl_money -= gl_money
    elif action == "remaining":
        how_many()
    elif action == "exit":
        break
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()

from decouple import config
def results(money):
    my_money = int(config('MY_MONEY'))
    # result = my_money - money
    if money > my_money:
        print(f'\033[32mYou earned {money - my_money}$\033[0m \n\033[33mYour remains: {money}$')
    elif money < my_money:
        print(f'\033[31mYou lose {my_money - money}$\033[0m \n\033[33mYour remains: {money}$')
    else:
        print(f'\033[33mYou don`t lost money! \nYour remails: {money}')
    return money

if __name__ == '__main__':
    results(1000)

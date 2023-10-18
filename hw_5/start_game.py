from random import randint
from decouple import config

def start():
    global money
    while True:
        number = input('\033[36mChoose the slot for rate: \033[0m')
        if number == '' or number == '0':
            print('\033[35mExiting...\n\033[0m')
            break
        rate = int(input('\033[36mChoose a sum for rate: \033[0m'))
        if int(number) > 0 and int(number) <= 30:
            if (money - rate) < 0:
                print(f'\033[31mRate more than remains!!! \n\033[33mRemains: {money}\033[0m')
                continue
        else:
            print('\033[31mDon`t existing slot.\033[0m\n')


        win_number = 7 #randint(1, 30)
        print(f'Winner number: {win_number}')
        if win_number == int(number):
            print(f'\033[32mYou win {rate* 2}$!!!\033[0m\n')
            money += rate * 2
            # print(f'Your remains: {money}\n')

        else:
            print(f'\033[31mYou lose {rate}$!!!\033[0m\n')
            money -= rate
            # print(f'Your remains: {money}\n')
        if money == 0:
            print('\033[33mYou money ended!!!\033[0m')
            break

        print('\033[33mDo you want to continue game?\033[0m')
    return money

list = list(range(1,31))
money = int(config('MY_MONEY'))
end_game = False
print(list)
start()
# while True:
#     number = input('Choose the slot for rate: ')
#     if number_for_rate == '' or number_for_rate == '0':
#         print('Exiting...')
#         break
#     rate = int(input('Choose a sum for rate: '))
#     start(number,rate)
# while True:
#     number_for_rate = input('Choose the slot for rate: ')
#
#     if number_for_rate == '' or number_for_rate == '0':
#         print('Exiting...')
#         break
#
#     rate = int(input('Choose a sum for rate: '))
#
#     if int(number_for_rate) > 0 and int(number_for_rate) <= 30:
#         if (money - rate) < 0:
#             print(f'Rate more than remains!!! \nRemains: {money}')
#             continue
#         if start(money, number_for_rate)==False:
#             money -= rate
#         else:
#             money += rate
#     else:
#         print('Don`t existing slot.\n')
#
#     if money <= 0:
#         print('You money ended!!!')
#         break
#
#     print('Do you want to continue game?')



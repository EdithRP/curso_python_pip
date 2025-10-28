import random

options = ['piedra', 'papel', 'tijera']
option_values = {
    'piedra': 1,
    'papel': 4,
    'tijera': 6
}
computer_wins = 0
user_wins = 0

rounds = 1

while True:
    print('*' * 10)
    print(f'Round {rounds}')
    rounds += 1

    user_option = input('piedra, papel o tijera => ').lower()

    if user_option not in options:
        print('Opción inválida. Intenta de nuevo.')
        continue

    computer_option = random.choice(options)
    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    user_value = option_values[user_option]
    computer_value = option_values[computer_option]
    difference = user_value - computer_value

    if difference == 0:
        print('Empate!')
    elif difference in [-5,3,2]:
        print('User gano!')
        user_wins += 1
    else:
        print('Computer gano!')
        computer_wins += 1

    if computer_wins == 2:
        print('El ganador es la computadora')
        break
    if user_wins == 2:
        print('El ganador es el usuario')
        break

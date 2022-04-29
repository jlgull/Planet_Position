#!/usr/bin/env python3
#
# Author: Tracy Baker

length_counter = 0
choice = ''

print('\n\nThis section will print all the prime numbers in a')
print('range you supply.')

start_number = int(input('\nPlease input starting number: '))
end_number = int(input('\nPlease input ending number: '))

print(f'\nThe prime numbers from {start_number} to {end_number} are:')

start_number = start_number - (start_number % 3)
if start_number % 2 == 0:
    start_number = start_number - 3


# input(f'\nstart_number = {start_number} . . . paused\n')

for i in range(start_number, end_number + 1, 2):

    num_factors = 0

    for j in range(3, i + 1, 2):
        if i % j == 0:
            num_factors += 1

            if num_factors > 1:
                break

    # Modified print to also print out the binary value of each prime.
    #   Also changed to divisor for length_counter to 8, from 15.
    if num_factors == 1:
        length_counter += 1
        print(f'{i:5} {bin(i):>16}', end=' ' if length_counter % 8 != 0 else '\n')

        if length_counter % 300 == 0:
            choice = input('\nPaused... press Enter to continue or Z to quit...\n').upper()
            if choice == 'Z':
                break

if choice != 'Z':
    input('\n\nFinished... press Enter...')

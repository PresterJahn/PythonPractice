
import random


def main():
    capitals = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Indiana': 'Indianapolis',
        'Maine': 'Augusta',
        'New Hampshire': 'Concord',
        'New York': 'Albany',
        'Ohio': 'Columbus',
        'Oregon': 'Salem',
        'Texas': 'Austin',
        'Wyoming': 'Cheyenne'
    }

    correct = 0
    incorrect = 0
    states = list(capitals.keys())

    while True:
        state = random.choice(states)
        answer = input('What is the capital of ' + state + '? (or enter 0 to quit): ')

        if answer == '0':
            break
        elif answer.strip().lower() == capitals[state].lower():
            print('That is correct.')
            correct += 1
        else:
            print('That is incorrect.')
            incorrect += 1

    print('You had', correct, 'correct responses and', incorrect, 'incorrect responses.')


if __name__ == '__main__':
    main()

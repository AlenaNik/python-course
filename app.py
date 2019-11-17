
secret = 9
i = 0
limit = 3
while i < limit:
    guess = int(input('Guess: '))
    i += 1
    if guess == secret:
        print('Number is ok')
        break
    else:
        print('Wrong number')
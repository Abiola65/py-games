print('Welcome to my computer quiz game!')

playing = input('Do you want to play? ')
if playing.lower() != 'yes':
    quit()
print('okay! Lets get started :)')
score = 0

answer = input('What does CPU stands for? ')
if answer.lower() == 'central processing unit':
    print('correct!')
    score += 1
else:
    print('oops incorrect! :(')

answer = input('What does GPU stand for? ')
if answer.lower()  == 'graphics processing unit':
    print('correct!')
    score += 1
else:
    print('oops incorrect! :(')

answer = input('What does RAM stand for? ')
if answer.lower()  == 'readom access memory':
    print('correct!')
    score += 1
else:
    print('oops incorrect! :(')

answer = input('What does ROM stand for? ')
if answer.lower()  == 'Read only memory':
    print('correct!')
    score += 1
else:
    print('oops incorrect! :(')

answer = input('What does HTML stands for? ')
if answer.lower()  == 'hyper text markup language':
    print('correct!')
    score += 1
else:
    print('oops incorrect! :(')

answer = input('What does HTTP stand for? ')
if answer.lower()  == 'hyper text transfer protocol':
    print('correct!')
    score += 1
else:
    print('oops incorrect! :(')

answer = input('What does GTA stand for? ')
if answer.lower()  == 'grand theft auto':
    print('correct!')
    score += 1
else:
    print('oops incorrect! :(')

answer = input('What does LDOE stands for? ')
if answer.lower()  == 'last day on earth':
    print('correct!')
    score += 1
else:
    print('oops incorrect! :(')

answer = input('What does CSS stands for? ')
if answer.lower()  == 'casscading style sheet':
    print('correct!')
    score += 1
else:
    print('oops incorrect! :(')

answer = input('What does MMM stands for? ' )
if answer.lower()  == 'mickery mockery madness':
    print('correct!')
    score += 1
else:
    print('oops incorrect! :(')

print('You got ' +str(score) + ' questions correct!')
print('You got ' +str((score / 10) *100) + '%.')
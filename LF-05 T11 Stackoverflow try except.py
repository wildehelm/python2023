

print('1) Blue')
print('2) Red')
print('3) Yellow')

while True:
    try:
        question = int(input('Out of these options\(1,2,3), which is your favourite?'))
        break
    except:
        print("That's not a valid option!")

if question == 1:
    print('Nice!')
elif question == 2:
    print('Cool')
elif question == 3:
    print('Awesome!')
else:
    print('That\'s not an option!')

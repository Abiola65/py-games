print('Welcome to Maznod Bank')
Trial = 3
Userpin = 1234

while Trial != 0:
    Pin = int(input('Pls Enter Your 4 Digit Pin: '))
    if Pin != Userpin:
       Trial -= 1
       print('Wrong pin number, you have',Trial, 'Trial left')
    else:
        UserChoice = input('d: Deposit, w: Withdraw:, s: Send: ')
        if UserChoice == 'd':
            UserDeposit = input('Enter the amount you will like to deposit: ')
            print(UserDeposit, '# Have Been Deposited To your account')
        elif UserChoice == 'w':
            UserWhithdraw = input('Enter The Amount you will like to withdraw: ')
            print(UserWhithdraw, '# Have been withdraw from your account')
        elif UserChoice == 's':
            Sender = input('Enter The Amount you want to send: ')
            Name = input('Enter the Name of the person you want to send the money to: ')
            print(Sender, 'Have been sent to ', Name)


    UserExit = input('Would you like to continue? (y/n): ')
    if UserExit == 'n':
        print('Thank u so much for using Maznod Bank')
        break
    else:
        continue
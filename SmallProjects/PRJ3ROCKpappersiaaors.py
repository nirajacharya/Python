import random
computer_score=0
user_score=0
while True:
    option=['rock', 'paper', 'scissor']
    computer_choosed_option=random.choice(option)

    user_input=input('''enter Your option
                     1)Rock
                     2)Paper
                     3)Scissor
                     press Q to Exit
                     Enter your value:'''
                     )
    print('computer choose',computer_choosed_option)
    if user_input.isdigit() == True:
        user_input=int(user_input)
        user_choosed_option=option[user_input-1]
        print(user_choosed_option)
        if computer_choosed_option == user_choosed_option:
            user_score=user_score
            computer_score=computer_score
        elif computer_choosed_option=="rock":
            if user_choosed_option=="paper":
                user_score = user_score+1
                computer_score=computer_score
            if user_choosed_option=="scissor":
                user_score=user_score
                computer_score = computer_score+1
        elif computer_choosed_option=="paper":
            if user_choosed_option=="scissor":
                user_score = user_score+1
                computer_score=computer_score
            if user_choosed_option=="rock":
                computer_score = computer_score+1
                user_score=user_score

        elif computer_choosed_option=="scissor":
            if user_choosed_option=="rock":
                user_score = user_score+1
            if user_choosed_option=="paper":
                computer_score = computer_score+1

        print("computerscore", computer_score)
        print("UserScore", user_score)

    else:
        if user_input=="q" or "Q":
            print("computerscore",computer_score)
            print("UserScore",user_score)
            if computer_score> user_score:
                print("computer wins")
            elif computer_score<user_score:
                print("User Wins")
            else:
                print("This game is Draw")
            exit()
        else:
            print("Enter only digits")
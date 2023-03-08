from Cards import Cards as game

res = 'Friend, do not believe in delusions,\n we ourselves are the creators of our destiny'
def few_questions():
    print('Hello friend, I heard you are looking for a seer?')
    if input('y/n ??? \n >---') == 'y':
        print('Do you believe in fortune telling?')
        if input('y/n ??? \n >---') == 'y':
            print('Then you are in luck,\n'
                  'because I know how to predict fate on cards')
            game.magic_cards()
            print ('I hope you understand my ' + res)
        else:
            print("I'm happy for you my " + res)
    else:
        print("That's good my " + res)

few_questions()
theboard={'1':' ','2':' ','3':' ',
          '4':' ','5':' ','6':' ',
          '7':' ','8':' ','9':' '}
boardkeys=[]
for key in (theboard):
    boardkeys.append(key)

def printboard(board):
    print(board['1']+'|'+board['2']+'|'+board['3'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['7']+'|'+board['8']+'|'+board['9'])

def game():
    
    turn='x'
    count=0

    for i in range (9):
        printboard(theboard)
        print('It\'s your turn '+turn+'. Where would you like to move to?')
        move=input()

        if theboard[move]==' ':
            theboard[move]=turn
            count+=1
        else:
            print('That space is already chosen. Choose somewhere else.')
        
        if count>=5:
            if theboard['1']==theboard['2']==theboard['3']!=' ':
                printboard(theboard)
                print('\nGame Over\n')
                print('-----'+turn+' won-----')
                break

            elif theboard['4']==theboard['5']==theboard['6']!=' ':
                printboard(theboard)
                print('\nGame Over\n')
                print('-----'+turn+' won-----')
                break

            elif theboard['7']==theboard['8']==theboard['9']!=' ':
                printboard(theboard)
                print('\nGame Over\n')
                print('-----'+turn+' won-----')
                break

            elif theboard['1']==theboard['4']==theboard['7']!=' ':
                printboard(theboard)
                print('\nGame Over\n')
                print('-----'+turn+' won-----')
                break

            elif theboard['2']==theboard['5']==theboard['8']!=' ':
                printboard(theboard)
                print('\nGame Over\n')
                print('-----'+turn+' won-----')
                break

            elif theboard['3']==theboard['6']==theboard['9']!=' ':
                printboard(theboard)
                print('\nGame Over\n')
                print('-----'+turn+' won-----')
                break

            elif theboard['1']==theboard['5']==theboard['9']!=' ':
                printboard(theboard)
                print('\nGame Over\n')
                print('-----'+turn+' won-----')
                break

            elif theboard['3']==theboard['5']==theboard['7']!=' ':
                printboard(theboard)
                print('\nGame Over\n')
                print('-----'+turn+' won-----')
                break
        if count==9:
            print('\nGame Over\n')
            print('-----It\'s a Draw-----')

        if turn=='x':
            turn='O'
        else:
            turn='x'

    restart=input('Do you want to replay the game? y or n\n')
    if restart=='y' or restart=='Y':
        for key in boardkeys:
            theboard[key]=" "

        game()

if __name__=="__main__":
    game()

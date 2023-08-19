print('Enter 1 for rock')
print('Enter 2 for paper')
print('Enter 3 for scissor')

p1=int(input('first player enter your choice :'))
p2=int(input('second player enter your choice :'))

if p1==p2:
    print('Draw')
elif p1==1 and p2==2 or p1==2 and p2==3 or p1==3 and p2==1:
    print('player 2 wins')
else:
    print("player 1 wins")
import random#the random command is used to initial the number
count=0# the count command is used to initial the number from 0
while count<=100: # it is initialzing the count value is less than equal to 100
    roll=input("press r to roll a die")# this suggest us to press r
    if roll=='r':# this tells us that roll is assigned to value r
     r=(random.randint(1,6))# it shuffles the number from 1 to 6
     print(r)# it prints the value of r
     count=count+r# the count is additing with r
     print("r is",r)# this tells that r is rolled 
     print("count is",count)# this tells that finally what number want to be in which block
     input("press any key to exit")# this ensure the loop will not come outside
     if count==8:
        count=37
        print("you've climbed the lader to 37")
        print("your count is",count)
     if count==13:
        count=34
        print("you've climbed the lader to 34")
        print("your count is",count)
     if count==38:
        count=9
        print("you've have been biten by the snake goto 9")
        print("your count is",count)
     if count==40:
        count=68
        print("you've climbed the lader to 68")
        print("your count is",count)
     if count==65:
        count=46
        print("you've have been biten by the snake goto 46")
        print("your count is",count)
     if count==52:
        count=81
        print("you've climbed the lader to 81")
        print("your count is",count)
    if count==89:
        count=70
        print("you've have been biten by the snake goto 70")
        print("your count is",count)
    if count==93:
        count=64
        print("you've have been biten by the snake goto 64")
        print("your count is",count)
    if count==97:
        count=100
        print("congratulation you won the game 100")# this tells that you reached number 100 and you won the game
        print("your count is",count)



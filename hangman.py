import random
import time
import string

def start():
    global n
    print("\t...welcome to hangman game...")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    print(time.ctime())
    print("...")
    time.sleep(2)
    n=input("enter name :")
    time.sleep(2)
    main()

def main():
    print("chose 1 to give word")
    print("chose 2 to guess word")
    print("choce 3 to restart game")
    print("chose 4 to exit")
    a=int(input("enter no. "))

    if a==1:
        giveword()
    elif a==2:
        guessword()
    elif a==3:
        start()
    elif a==4:
        exit()
    else:
        print("please enter valid input")
        main()


def giveword():
    m=input("enter word :")
    time.sleep(1)
    j=0
    for i in range(len(m)):
        p=random.choice(string.ascii_letters)
        q=m[i]
        r=q.lower()
        time.sleep(1)
        print(f"at {i+1} position computer choose {p}")
        if r==p:
            print("match")
        else:
            print("not match")
            j+=1
        
        if j==1:
            print("o")
        elif j==2:
            print("o")
            print("|")
        elif j==3:
            print(" o")
            print("-|")
        elif j==4:
            print(" o")
            print("-|-")
        elif j==5:
            print(" o")
            print("-|-")
            print("-")
        elif j==6:
            print(" o")
            print("-|-")
            print("- -")
            print(f"{n} wins")
            break
        else:
            continue
        time.sleep(3)
    if j!=6:
        print("computer wins")
    main()

def guessword():
    t=["golf","god","frog","art","wine","tree","machine"]
    y=random.choice(t)
    l="_"*len(y)
    m=[]
    print("_"*len(y))
    j=0
    for i in range(len(y)):
        b=input(f"enter {i+1} letter :")
        c=y[i]
        d=b.lower()
        if c==d:
            time.sleep(2)
            print("match")
        else:
            print("not match")
            j+=1
        #l.replace("_",c,1)
        m.append(c)
        print(m,"_"*(len(y)-i-1))
        #print(l)

        if j==1:
            print("o")
        elif j==2:
            print("o")
            print("|")
        elif j==3:
            print(" o")
            print("-|")
        elif j==4:
            print(" o")
            print("-|-")
        elif j==5:
            print(" o")
            print("-|-")
            print("-")
        elif j==6:
            print(" o")
            print("-|-")
            print("- -")
            print("computer wins")
            break
        else:
            continue
    if j!=6:
        print(f"{n} wins")

    main()

start()

    








import random
def main():
    global count
    global display
    global l
    global guess
    global word

    words=["word","hi","goalgdfg"]
    count=0
    word=random.choice(words)
    l=len(word)
    display="_"*l
    guess=[]
    start=""
    hangman()

def startgame():
    global playgame
    print("enter y to play or n to exit")
    playgame=input("do you to play y or n\n")
    while playgame!='y' and playgame!='Y' and playgame!='n' and playgame!='N':
        playgame=input("do you to play y or n\n")
    if playgame=='y' or playgame=='Y':
        main()
    elif playgame=='n' or playgame=='N':
        exit()

def man():
    global count
    if count==1:
        print("O")
    elif count==2:
        print("O")
        print("|")
        print("|")
        print("|")
    elif count==3:
        print("   O")
        print("---|---")
        print("   |")
        print("   |")
    elif count==4:
        print("   O")
        print("---|---")
        print("   |")
        print("___|")
    elif count==5:
        print("   O")
        print("---|---")
        print("   |")
        print("___|___")
        print("you lose")



def hangman():
    global count
    global display
    global l
    global guess
    global word
    limit=5
    for i in range(len(word)):
        g=input("this is hangman word :" + display + "enter your guess :\n")
        g=g.strip()
        if len(g)==0 or len(g)>=2:
            print("invalid input")
            hangman()    
        elif g in word:
            guess.extend([g])
            index=word.find(g)
            display=display[:index]+g+display[index+1:]
            print(display)
        elif g in guess:
            print("try another letter")
        else:
            print("not match")
            count+=1
            man()
    if word==display:
        print("you guess right")
    elif count>=5:
        print("sorry you loss")
    else:
        print("you win")



startgame()
    
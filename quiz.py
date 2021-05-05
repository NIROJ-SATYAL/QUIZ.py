#--------------------------------
def new_game():
    guesses=[]
    correct_guesses=0
    question_num=0
    

    for key in questions:
        print("--------------------------------")
        print(key)
        
        for i in answer[question_num]:
            print(i)
        
        
        guess=input("enter (A,B,C,D):  ").upper()  
        guesses.append(guess)
        correct_guesses+=check_answer(questions.get(key),guess)
        question_num+=1

    display_score(correct_guesses,guesses)
#--------------------------------
def check_answer(answer,guess):
    if answer==guess:
        print("correct:")
        return 1
    else:
        print("wrong:")
        return 0
    
#--------------------------------
def display_score(correct_guesses,guesses):
    print("--------------------------------")
    print("RESULTS")
    print("--------------------------------")
    
    print("guesses",end=" ")
    for i in guesses:
        print(i,end="  ")
    print()
    score=int(correct_guesses)
    print("your score is:",score)
    name=input("enter your name:  ")
    if score<=3:
        print("congratulation !!",name ,"you won the 3rd prize!!(3rd prize is 1000 rs)")
    elif score>3 or score<=5:
        print("congratulation!!",name," you won the second prize!!(second prize is 3000 rs)")
    else:
        print("congratulation !!",name," you won the first prize!!(first prize is 5000 rs)")


#--------------------------------
def play_again():
    
    responce=input("do you want to play again?(yes or no) ").lower()
    if responc=="yes":
        return True
    else:
        return False
    

questions={
    "who created python?":"A",
    "which one is the first search engine in internet":"C",
    "Number of bit used by the IPv6 address?":"C",
    "which one is the first web browser ibvented ib 1990?":"D",
    "which of the following programming language is used to create programs like applets?":"A",
    "First computer virus is known as?":"B",
    "firewall in computer is used for?":"A"
}




answer=[["A.guido van rossum","B.elon musk","c.bill gates","D.mark zuckerburg"],
["A.Google","B.WAIS","C.Archie","D.Altavista"],
["A.32 bit","B.64 bit","C.128 bit","D.256 bit"],
["A.Internet Explorer","B.Mosaic","C.Mozilla","D.Nexus"],
["A.Java","B.COBOL","C.C language","D.BASIC"],
["A.Rabbit","B.creeper virus","C.ELK cloner","D.SCA virus"],
["A.security","B.Data transmission","C.Authentication","D.Monitoring"]]
new_game()


while play_again():
    new_game()

print("BYEEEEEEEEE")


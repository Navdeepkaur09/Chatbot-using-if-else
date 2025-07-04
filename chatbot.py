def talk():
    mylist=["Fine,let's chit chat.Then I will ask you some questions and answer me.Type,exit to stop.","How is your day going","Fine,so what is your fav movie?","Great!What do you feel most happy about?"]
    while True:
        for i in mylist:
            print(f"{i}\n")
            user=input()
            if user=="exit":
                return
        break  

def questions():
    
    questions={"What is python":"Python is a object-oriented programming language","When and by whom python was made":"By Guido van Rossum in 1991",
               "What is a variable":"Variable is like a container that holds data","What is data type":"Data type specifies the type of value a variable holde"}
    lower_questions={k.lower():v for k,v in questions.items()}
    while True:
        print("ask question (wrie 'exit' to stop)\n")
        user=input().lower()
        if user in lower_questions:
            print(lower_questions[user])
        elif user=="exit":
            return
        else:
            print("Sorry,i don't understand that question.\n")
        
print("Hello")
print("How can i help you?")
print("1.Just a small talk\n2.Questions regarding Python\n3.Exit\nPress(1-3)\n")
choice=int(input())
if choice==1:
    talk()
elif choice==2:
    questions()
    print("Thanks for your questions")
else:
    print("Bye!")


       



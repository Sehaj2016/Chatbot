from chatterbot import ChatBot
from  chatterbot.trainers import ListTrainer
from tkinter import *
bot = ChatBot("My Bot")

conversation = [
    "Hello",
    "Hi there!",
 "what is your name?",
    "My name is Jasminder",
    "how are you doing?",
    "I am doing great!",
    "thank you!",
    "in which city you are?",
    "I am live in Mukerian",
    "in Which language you talk?",
    "I am talking in Punjabi"
]
trainer = ListTrainer(bot)
#  now training the bot with the help of trainer
trainer.train(conversation)

#answer= bot.get_response("what is your name?")
#print(answer)
#print("talk to bot")
#while True:print("talk to bot")
    #query = input()
    #if query=="exit":
        #break
    #answer = bot.get_response(query)
    #print(answer)

main = Tk()

main.geometry("300x300")

main.title('My Chatbot')
img= PhotoImage(file="my chatbot.png")
photo = Label(main, image=img)
photo.pack(pady=5)

def ask_from_bot():
    query=textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END,"you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END,"Bot : " + str(answer_from_bot))
    textF.delete(0, END)








frame=Frame(main)
sc=Scrollbar(frame)
msgs= Listbox(frame, width=80, height=20,)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
# creating text field

textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)

btn=Button(main,text="Ask from bot",font=("Verdana",20),command=ask_from_bot)
btn.pack()










main.mainloop()

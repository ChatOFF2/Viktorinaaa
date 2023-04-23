import turtle
import pandas as pd
ugadano=0

af=pd.read_csv("my_csv.csv", encoding="windows-1251")



turtle.title("The Game")
turtle.setup(1024,768)

turtle.addshape("gameimage.gif")
turtle.shape("gameimage.gif")
dicttt=[]
GameON=True
counter=0
flag=False
turtleerror=turtle.Turtle()
turtleerror.penup()
turtleerror.hideturtle()
turtleerror.goto(-150, 200)
while GameON:

    if ugadano==0:
        text=f"Введи закрашеные города"
    else:
        text=f"Сейчас угадано {ugadano} из 3 вопросов"
    answer = turtle.textinput(text, "город-")
    answer=answer.title()
    dataobj=af[af["state"]==answer]
    if dataobj.empty:
        pass
    else:
        if dataobj["state"].item() in dicttt:
            flag=True
            turtleerror.write(f"УЖЕ ЭТО ВВОДИЛ:\n{answer}", font=("Arial", 35, "bold"))
            continue
        else:
            turtleerror.clear()
            dicttt.append(dataobj["state"].item())
            answertext=turtle.Turtle()
            answertext.hideturtle()
            answertext.penup()
            answertext.goto(dataobj.iloc[0,1],dataobj.iloc[0,2]-10)
            answertext.write(dataobj.iloc[0,0], align="left", font=("Arial", 12, "normal"))
            ugadano+=1
            if ugadano==3:
                GameON=False









turtle.mainloop()
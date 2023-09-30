import turtle
import random
import time

turtle.bgcolor('light blue')

# cytat
cytat = turtle.Turtle()
cytat.color('black')
cytat.penup()
cytat.goto(-300,150)
cytat.write("'Który z żółwików wygra ten wyścig?'" , font=("Cambria", 30))
cytat.goto(-300,50)
time.sleep(0.5)
cytat.write("'Którego sen o zwycięstwie się ziści?'", font=("Cambria",30))
cytat.goto(-10,-50)
time.sleep(0.5)
cytat.write("'Małe żółwie' Wendy McLean", font=("Cambria",20))
cytat.hideturtle()
time.sleep(0.5)

# zawodnicy
yellow = turtle.Turtle()
yellow.penup()
yellow.goto(-200,-200)
yellow.shape('turtle')
yellow.color('yellow')

red = turtle.Turtle()
red.penup()
red.goto(0,-200)
red.shape('turtle')
red.color('red')

green = turtle.Turtle()
green.penup()
green.goto(200,-200)
green.shape('turtle')
green.color('green')

time.sleep(1)
cytat.clear()

# meta
meta = turtle.Turtle()
meta.color('black')
meta.penup()
meta.goto(260,220)
meta.write("META" , font=("Cambria",20))
meta.goto(300,200)
meta.pendown()
meta.goto(300,-200)
meta.hideturtle()

#zawodnicy na start
yellow.pensize(7)
yellow.penup()
yellow.goto(-300,100)
yellow.pendown()

red.pensize(7)
red.penup()
red.goto(-300,-100)
red.pendown()

green.pensize(7)
green.penup()
green.goto(-300, 0)
green.pendown()

# odliczanie
odliczanie = turtle.Turtle()
odliczanie.color('black')
odliczanie.penup()
odliczanie.goto(-320,200)
odliczanie.hideturtle()

for x in range(3):
    odliczanie.write(3-x, font=("Arial", 70, "bold"))
    time.sleep(1)
    odliczanie.clear()


odliczanie.write("'Wystartowały już wszystkie na sygnał!'", font=("Cambria", 20))
time.sleep(1)
odliczanie.clear()

#czy wygral
def sprawdz():
    if yellow.position()[0] >= 300:
        odliczanie.color('yellow')
        odliczanie.write('Wygrał ŻÓŁTY !!!', font=("Arial",40,'bold'))
        return True
    elif red.position()[0] >= 300:
        odliczanie.color('red')
        odliczanie.write('Wygrał CZERWONY !!!', font=("Arial",40,'bold'))
        return True
    elif green.position()[0] >= 300:
        odliczanie.color('green')
        odliczanie.write('Wygrał ZIELONY !!!', font=("Arial",40,'bold'))
        return True
    return False

# pętla główna
first = random.choice(['yellow','red', 'green'])

while True:
    if first == "red":
        red.forward(random.randint(0,50))
        if sprawdz(): break
        yellow.forward(random.randint(0,50))
        if sprawdz(): break
        green.forward(random.randint(0,50))
        if sprawdz(): break
    elif first == "yellow":
        yellow.forward(random.randint(0,50))
        if sprawdz(): break
        green.forward(random.randint(0,50))
        if sprawdz(): break
        red.forward(random.randint(0,50))
        if sprawdz(): break
    else:
        green.forward(random.randint(0,50))
        if sprawdz(): break
        red.forward(random.randint(0,50))
        if sprawdz(): break
        yellow.forward(random.randint(0,50))
        if sprawdz(): break
    time.sleep(0.3)

cytat.goto(-300, -270)
cytat.write("I to już koniec wyścigu, niestety", font=("Cambria", 30))
time.sleep(1)

turtle.exitonclick()

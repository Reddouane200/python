import turtle

ha = turtle.Screen()
ha.title('Hello...')
ha.setup(width=900, height=400)
ha.tracer(0)
ha.bgcolor("#00ff00")

kora = turtle.Turtle()
kora.speed(0)
kora.shape("circle")
kora.color('white')
kora.shapesize(stretch_len=1, stretch_wid=1)

kora.goto(x=0,y=0)
kora.penup()
#hada ta3 thrk l kora#
kora_dx, kora_dy = 3 ,3
kora_speed = .7

mam = turtle.Turtle()
mam.speed(0)
mam.shape('square')
mam.color('white')
mam.shapesize(stretch_len=.1, stretch_wid=25)
mam.penup()
mam.goto(0, 0)

d1 = turtle.Turtle()
d1.speed(0)
d1.shape('square')
d1.color('yellow')
d1.shapesize(stretch_len=1, stretch_wid=5)
d1.penup()
d1.goto(-600, 0)

d2 = turtle.Turtle()
d2.speed(0)
d2.shape('square')
d2.color('black')
d2.shapesize(stretch_len=1, stretch_wid=5)
d2.penup()
d2.goto(600, 0)

sc = turtle.Turtle()
sc.speed(0)
sc.color('purple')
sc.penup()
sc.goto(0, 350)
sc.write('wac: 0  kacm: 0', align="center", font=('Courier', 14, 'normal'))
sc.hideturtle()

#hada nta3 scor iban lik
bit_1, bit_2 = 0,0

#hada nta3 thrk l3ibat#

def p1_move_up():
    d1.sety(d1.ycor()+ 20)
def p1_move_down():
    d1.sety(d1.ycor()- 20)
def p2_move_up():
    d2.sety(d2.ycor()+ 20)
def p2_move_down():
    d2.sety(d2.ycor()- 20)

#hada nta3 bach tklki 3la hrf bach thrk l3ibs #
ha.listen()#hada tabch itjawb ila klkiti 3la chi haja#
ha.onkeypress( p1_move_up,'a')
ha.onkeypress( p1_move_down,'z')
ha.onkeypress( p2_move_up,'Up')
ha.onkeypress( p2_move_down,'Down')



while True:
    ha.update()
   # movement kora#
    kora.setx(kora.xcor() + (kora_dx * kora_speed))
    kora.sety(kora.ycor() + (kora_dy * kora_speed))


    #kora thbs tdrb fl lkhr bo trj3#
    if(kora.ycor()>350):
      kora.sety(350)
      kora_dy *= -1
    if(kora.ycor()<-350):
      kora.sety(-350)
      kora_dy *= -1
     #hada nta3 bach itla9a lkoram3a d2 o d2 bach i3tina harak tl3b
    if kora.xcor() < -550 and kora.xcor() > -600 and kora.ycor() > (d1.ycor()-60) and kora.ycor() < (d1.ycor()+60):
       kora.setx(-550)
       kora_dx *= -1
    if kora.xcor() > 550 and kora.xcor() < 600 and kora.ycor()>(d2.ycor()-60) and kora.ycor() < (d2.ycor()+60):
       kora.setx(550)
       kora_dx *= -1
     #hada nta3 bach ila tmarka lbit t3awd mn lwst#
    if (kora.xcor()> 600):
       kora.goto(0,0)
       kora_dx *= -1
       sc.clear()
       bit_1 += 1

       sc.write(f'wac: {bit_1} kacm: {bit_2}', align="center", font=('Courier', 14, 'normal'))
    if (kora.xcor()< -600):
       kora.goto(0,0)
       kora_dx *= -1
       sc.clear()
       bit_2 += 1
       sc.write(f'wac: {bit_1} kacm: {bit_2}', align="center", font=('Courier', 14, 'normal'))
   
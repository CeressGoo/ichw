
# coding: utf-8

# In[ ]:

import turtle
pingmu=turtle.Screen()

def stepmove(k):
    mcr.forward(1*k)
    mcr.left(1)
    vns.forward(2*k)
    vns.left(1)
    eth.forward(3*k)
    eth.left(1)
    mrs.forward(4*k)
    mrs.left(1)
    jpt.forward(5*k)
    jpt.left(1)
    stn.forward(6*k)
    stn.left(1)
    
pingmu.clear()

flame=turtle.Turtle()
flame.color('red')
flame.shape('blank')
flame.up()
flame.forward(15)
flame.down()
flame.begin_fill()
flame.fillcolor('orange')
flame.left(18)
for sctrl in range(5):
    flame.left(144)
    flame.forward(29)
flame.end_fill()
sun=turtle.Turtle()
sun.shape('circle')
sun.shapesize(0.8,0.8,0)
sun.color('yellow')
    
mcr=turtle.Turtle()
vns=turtle.Turtle()
eth=turtle.Turtle()
mrs=turtle.Turtle()
jpt=turtle.Turtle()
stn=turtle.Turtle()
mcr.shape('circle')
mcr.shapesize(0.2,0.2,0)
vns.shape('circle')
vns.shapesize(0.3,0.3,0)
eth.shape('circle')
eth.shapesize(0.4,0.4,0)
mrs.shape('circle')
mrs.shapesize(0.5,0.5,0)
jpt.shape('circle')
jpt.shapesize(0.6,0.6,0)
stn.shape('circle')
stn.shapesize(0.8,0.8,0)
mcr.color('gray')
vns.color('purple')
eth.color('sea green')
mrs.color('red')
jpt.color('orange')
stn.color('brown')
mcr.up()
vns.up()
eth.up()
mrs.up()
jpt.up()
stn.up()
mcr.speed(50)
vns.speed(50)
eth.speed(50)
mrs.speed(50)
jpt.speed(50)
stn.speed(50)
mcr.left(85)
vns.right(73)
eth.right(15)
mrs.left(208)
jpt.left(64)
stn.right(68)
mcr.forward(57)
vns.forward(115)
eth.forward(172)
mrs.forward(229)
jpt.forward(286)
stn.forward(344)
mcr.left(91)
vns.left(91)
eth.left(91)
mrs.left(91)
jpt.left(91)
stn.left(91)
mcr.down()
vns.down()
eth.down()
mrs.down()
jpt.down()
stn.down()

for n in range(2):
    for i in range(0,90,1):
        k=0.3+(i**2)*0.7/8100
        stepmove(k)
    for o in range(90,0,-1):
        k=0.3+(o**2)*0.7/8100
        stepmove(k)





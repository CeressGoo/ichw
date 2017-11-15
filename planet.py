
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
    
sun=turtle.Turtle()
sun.shape('circle')
sun.color('yellow')
    
mcr=turtle.Turtle()
vns=turtle.Turtle()
eth=turtle.Turtle()
mrs=turtle.Turtle()
jpt=turtle.Turtle()
stn=turtle.Turtle()
mcr.shape('circle')
vns.shape('circle')
eth.shape('circle')
mrs.shape('circle')
jpt.shape('circle')
stn.shape('circle')
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
        k=0.2+(i**2)*0.8/8100
        stepmove(k)
    for o in range(90,0,-1):
        k=0.2+(o**2)*0.8/8100
        stepmove(k)





# coding: utf-8

# In[ ]:

import turtle
pingmu=turtle.Screen()

def stepmove():
    mcr.forward(1)
    mcr.left(1)
    vns.forward(2)
    vns.left(1)
    eth.forward(3)
    eth.left(1)
    mrs.forward(4)
    mrs.left(1)
    jpt.forward(5)
    jpt.left(1)
    stn.forward(6)
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

for i in range(0,360,1):
    stepmove()



import math
import turtle

#===============================================================================
# LANDMARKS
#===============================================================================
def drawSpring(xpos,ypos):
     turtle.fillcolor(0.5,1,1)
     
     turtle.setpos(xpos,ypos)
     turtle.fill(True)
     turtle.circle(10)
     turtle.fill(False)
     turtle.setpos(xpos,ypos)
     return


def drawTown(xpos,ypos):
     turtle.fillcolor(1,0,0)
     turtle.fill(True)
     turtle.setpos(xpos,ypos)
     turtle.setpos(xpos-7,ypos)
     turtle.setpos(xpos-7,ypos+10)
     turtle.setpos(xpos-10,ypos+10)
     turtle.setpos(xpos,ypos+20)
     turtle.setpos(xpos+10,ypos+10)
     turtle.setpos(xpos+7,ypos+10)
     turtle.setpos(xpos+7,ypos)
     turtle.setpos(xpos,ypos)
     return

def drawCave(xpos,ypos):
     turtle.fillcolor(0.75,0.75,0.75)
     turtle.fill(True)
     turtle.setpos(xpos-10,ypos)
     turtle.setpos(xpos-10,ypos+15)
     turtle.setpos(xpos-5,ypos+20)
     turtle.setpos(xpos,ypos+20)
     turtle.setpos(xpos+5,ypos+20)
     turtle.setpos(xpos+10,ypos+15)
     turtle.setpos(xpos+10,ypos)
     turtle.setpos(xpos-10,ypos)
     turtle.fill(False)
     
     turtle.fillcolor(0,0,0)
     turtle.fill(True)
     turtle.setpos(xpos-5,ypos)
     turtle.setpos(xpos-5,ypos+10)
     turtle.setpos(xpos,ypos+15)
     turtle.setpos(xpos+5,ypos+10)
     turtle.setpos(xpos+5,ypos)
     turtle.setpos(xpos-5,ypos)
     turtle.fill(False)
     return


def drawRuin(xpos,ypos):


     turtle.fillcolor(0.95,0.95,0.95)
     turtle.fill(True)
     turtle.setpos(xpos-5,ypos)
     turtle.setpos(xpos-5,ypos+10)
     turtle.setpos(xpos,ypos+15)
     turtle.setpos(xpos+5,ypos+20)
     turtle.setpos(xpos+5,ypos)
     turtle.setpos(xpos-5,ypos)
     turtle.fill(False)
     turtle.setpos(xpos-10,ypos)
     turtle.setpos(xpos+10,ypos)
     

     return

def putSymbol(tuple):
     k=tuple[0]
     xpos=k[0]
     ypos=k[1]
     label=tuple[1]
     turtle.penup()
     turtle.fill(False)
     turtle.setpos(xpos,ypos)
     turtle.pendown();
     
     if (label=='ruin'):
          drawRuin(xpos,ypos)
     elif(label=='cave'):
          drawCave(xpos,ypos)
     elif(label=='town'):
          drawTown(xpos,ypos) 
     elif(label=='spring'):
          drawSpring(xpos,ypos)           
     return


def putSymbols(symbolSet):
     symbolType=symbolSet[0]
     for coords in symbolSet[1:]:
          putSymbol([coords,symbolType])          
     return


#===============================================================================
# BLOCKS OF COLOR
#===============================================================================


def fetchColor(label):
     color=(1,1,1)
     if (label=='ocean'):
          color=(0,0,1)
     elif (label=='shallow'):
          color=(0.5,0.5,1)
     elif (label=='sand'):
          color=(1,1,0.5)
     elif (label=='plain'):
          color=(0.5,1.0,0.5)
     elif (label=='forest'):
          color=(0,0.5,0)
     elif (label=='mountain'):
          color=(0.75,0.75,0.75)
     else:
          color=(1,0,0)
     return color

def putBlock(block):
     label=block[0]
     p=[]
     for coord in block[1:]:
          p=p+coord
          
     
     
     color=fetchColor(label)

     turtle.fill(True)
     turtle.fillcolor(color)
     turtle.penup()
     
     k=p[0]
     turtle.setpos(k[0],k[1])
     turtle.pendown()
     for i in range(0,len(p)):
          k=p[i]
          turtle.setpos(k[0],k[1])
     k=p[0]          
     turtle.setpos(k[0],k[1])        
     
     
     turtle.fill(False)
     turtle.penup()
 
     return

#===============================================================================
# MAPGRIDS
#===============================================================================
def drawCenter():
     for i in range(0,360,90):
          turtle.penup()
          turtle.setpos(0,0)
          turtle.setheading(i)
          turtle.pendown()
          turtle.forward(500)
     turtle.penup()
     turtle.setpos(0,0)
     turtle.setheading(0)
     return

def drawGrid():
     for i in range(360,-360,-20):
          turtle.penup()
          turtle.setpos(-500,i)
          turtle.pendown()
          turtle.setpos(500,i)
          
     for i in range(-500,500,20):
          turtle.penup()
          turtle.setpos(i,-360)
          turtle.pendown()
          turtle.setpos(i,360)          
          
     return
#===============================================================================
#MAIN
#===============================================================================

turtle.speed(0)
turtle.setup (width=1000, height=720)
turtle.hideturtle()
drawCenter()
#PUT BLOCKS OF COLOR HERE. ORDER IS IMPORTANT
drawGrid()

#PUT LANDMARKS

#PUT PATH TO TREASURE
turtle.exitonclick()


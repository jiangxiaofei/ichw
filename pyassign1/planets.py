#!/usr/bin/env python3

"""planets.py: Description of what foobar does.

__author__ = "Jiangxiaofei"
__pkuid__  = "1700012463"
__email__  = "jiangxiaofei@pku.edu.cn"
"""

import math
import turtle


def drawPolygon(a,t,l):
    for i in range(a):
        t.forward(l)
        t.left(360/180)


def drawCircle(a,t,r):
    drawPolygon(a,t,(2*math.pi*r)/180)


wn=turtle.Screen()
wn.bgcolor("black")


#the sun
sun=turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.stamp()


#the planets
def planet(a,p,speed,r):
    p.speed(speed)
    p.shape("circle")
    p.pensize("2")
    drawCircle(a,p,r)

  
def move(p,r):
    p.up()
    p.goto(0,-r*4/3)
    p.pendown()
    

mercury=turtle.Turtle()
venus=turtle.Turtle()
earth=turtle.Turtle()
mars=turtle.Turtle()
jupiter=turtle.Turtle()
saturn=turtle.Turtle()
uranus=turtle.Turtle()
neptune=turtle.Turtle()


def mercury_run():
    mercury.color("grey")
    planet(100,mercury,200,60)


def venus_run():
    venus.color("orange")
    planet(77,venus,15,100)


def earth_run():
    earth.color("lightgreen")
    planet(64,earth,10,130)


def mars_run():
    mars.color("red")
    planet(51,mars,2,170)


def jupiter_run():
    jupiter.color("brown")
    planet(40,jupiter,1.5,220)


def saturn_run():
    saturn.color("yellow")
    planet(28,saturn,1,280)


def uranus_run():
    uranus.color("lightblue")
    planet(22,uranus,1,340)


def neptune_run():
    neptune.color("blue")
    planet(16,neptune,1,400)


move(mercury,60)
move(venus,100)
move(earth,130)
move(mars,170)
move(jupiter,220)
move(saturn,280)
move(uranus,340)
move(neptune,400)


for i in range(20):
    mercury_run()
    venus_run()
    earth_run()
    mars_run()
    jupiter_run()
    saturn_run()
    uranus_run()
    neptune_run()


if __name__ == '__main__':
    main()

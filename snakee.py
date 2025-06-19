import turtle
import time
import random
import pygame

pygame.mixer.init()
pygame.mixer.music.load('chillsnake.mp3')
pygame.mixer.music.play()

planets = ['1.gif', '2.gif', '3.gif', '4.gif', '5.gif', '6.gif', '7.gif', '8.gif', '9.gif']
screen = turtle.Screen()
screen.bgcolor('black')
screen.addshape('blackhole.gif')
screen.addshape('star_.gif')


for p in planets:
	screen.addshape(p)

#p是指planets里的一个planet, 可以不写9次gif
#变量只可以由数字，字母和下划线组成，并且数字不能开头，可以A123，不可以123a，可以_123a

screen.tracer(0)
#没有trace

starlist = []

for i in range(100):
	s = turtle.Turtle()
	s.shape('star_.gif')
	s.penup()
	s.id = i
	s.goto(random.randint(-300, 300), random.randint(-300, 300))

	starlist.append(s)


head = turtle.Turtle()
head.penup()
head.shape('blackhole.gif')
head.direction = 'stop'
#put direction(with stop) in the "box"

foodlist = []

for p in planets:

	food = turtle.Turtle()
	food.penup()
	food.shape(p)
	food.imageName = p
	food.color('purple')
	food.goto(random.randint(-300, 300), random.randint(-300, 300))


	foodlist.append(food)


def move():
	global head
	if head.direction == 'Right':
		#==判断相等
		head.goto(head.xcor() + 40, head.ycor())

	if head.direction == 'Left':
		head.goto(head.xcor() - 40, head.ycor())

	if head.direction == 'Up':
		head.goto(head.xcor(), head.ycor() + 40)

	if head.direction == 'Down':
		head.goto(head.xcor(), head.ycor() - 40)

def bodymove():
	global head, bodylist

	if len(bodylist) > 1:

		for i in range(len(bodylist)-1, 0, -1):
		#0makes everyth. goes upside down, -1 rep (10,9,8,7,6..), -2 rep (10,8,6,4..)
		#(bl)-1 for index
			currbody = bodylist[i]
			currbody.goto(bodylist[i-1].xcor(), bodylist[i-1].ycor())



	if len(bodylist) > 0:
		#0 rep the number of body
		bodylist[0].goto(head.xcor(), head.ycor())

def eatfood():
	global head, foodlist, bodylist, wt, points

	for f in foodlist:

		if head.distance(f) < 50:
			print('collide')

			points = points + 1
			
			wt.undo()
			wt.write('Point: ' + str(points), move = True,align='right',font=('Arial',30,'bold'))
			#string makes numbers into texts
			f.goto(random.randint(-230, 230), random.randint(-230, 230))

			body = turtle.Turtle()
			body.shape(f.imageName)
			body.color('green')
			body.penup()

			bodylist.append(body)


def goright():
	global head
	#global找在外面的函数

	head.direction = 'Right'

def goleft():
	global head

	head.direction = 'Left'

def goup():
	global head

	head.direction = 'Up'

def godown():
	global head

	head.direction = 'Down'

screen.listen()

screen.onkey(goright, 'Right')
screen.onkey(goleft, 'Left')
screen.onkey(goup, 'Up')
screen.onkey(godown, 'Down')

bodylist = []

wt = turtle.Turtle()
wt.ht()
#hideturtle
wt.penup()
wt.goto(0, 220)
wt.color('white')
wt.write('Point: 0', move = True,align='right',font=('Arial',30,'bold'))

points = 0

loops = 0

while True:
#True一直循环

	if loops < 100:
		loops = loops + 1

	else:
		loops = 1

	for s in starlist:
		if s.id % loops < 10:
			#取余数的符号%
			s.ht()
			#hide
		else:
			s.st()
		
	bodymove()
	move()
	eatfood()


	print('loop')
	#repeat
	time.sleep(0.1)

	screen.update()

turtle.mainloop()


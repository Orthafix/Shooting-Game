from tkinter import*
from random import randint
from time import sleep, time
from math import sqrt

#THIS IS VERSION 1.1 OF SHOOTING GAME
#Includes:
#Player 1 and 2
#Points for player 1 and 2 
#Bonus for player 1 and 2
#Game over ending for player 1 and 2

#Game board
HEIGHT = 500
WIDTH = 800
window = Tk()
window.title('BUBBLE SHOW DOWN!')
c = Canvas(window, width=WIDTH, height=HEIGHT,bg='darkblue')
c.pack()

#Game player 1
SHIP_SPD1 = 10

#Create player 1
ship1_id = c.create_polygon(5,5,5,25,30,15, fill='red')
ship1_id2 = c.create_oval(0,0,30,30,outline='red')
SHIP_R1 = 15
MID_X1 = WIDTH/2
MID_Y1 = HEIGHT/2
c.move(ship1_id, MID_X1, MID_Y1)
c.move(ship1_id2, MID_X1, MID_Y1)

#Game player 2
SHIP_SPD2 = 10

# Create Player 2
ship2_id = c.create_polygon(5,5,5,25,30,15, fill='green')
ship2_id2 = c.create_oval(0,0,30,30,outline='green')
SHIP_R2 = 15
MID_X2 = WIDTH/2
MID_Y2 = HEIGHT/2
c.move(ship2_id, MID_X2, MID_Y2)
c.move(ship2_id2, MID_X2, MID_Y2)

def move_ship(event):
    #Player 1
    if event.keysym == 'Up':
        c.move(ship1_id,0,-SHIP_SPD1)
        c.move(ship1_id2,0,-SHIP_SPD1)
    elif event.keysym == 'Down':
        c.move(ship1_id,0, SHIP_SPD1)
        c.move(ship1_id2,0, SHIP_SPD1)
    elif event.keysym == 'Left':
        c.move(ship1_id,-SHIP_SPD1,0)
        c.move(ship1_id2,-SHIP_SPD1,0)
    elif event.keysym == 'Right':
        c.move(ship1_id, SHIP_SPD1,0)
        c.move(ship1_id2, SHIP_SPD1,0)
    #Player 2
    elif event.keysym == 'w':
        c.move(ship2_id,0,-SHIP_SPD2)
        c.move(ship2_id2,0,-SHIP_SPD2)
    elif event.keysym == 's':
        c.move(ship2_id,0, SHIP_SPD2)
        c.move(ship2_id2,0, SHIP_SPD2)
    elif event.keysym == 'a':
        c.move(ship2_id,-SHIP_SPD2,0)
        c.move(ship2_id2,-SHIP_SPD2,0)
    elif event.keysym == 'd':
        c.move(ship2_id, SHIP_SPD2,0)
        c.move(ship2_id2, SHIP_SPD2,0)
c.bind_all('<Key>', move_ship)

#Game targets
bub_id = list()
bub_r = list()
bub_speed = list()

MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SPD = 10
GAP = 100

    #Skapa bubblor
def create_bubble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x-r, y-r, x+r, y+r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1,MAX_BUB_SPD))

    #Röra bubblor
def move_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i],0)

BUB_CHANCE = 10
 
#Koordinater
def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2
    return x,y

#Ta bort bubblor
def del_bubble(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]

def clean_up_bubs():
    for i in range(len(bub_id)-1,-1,-1):
        x,y = get_coords(bub_id[i])
        if x < -GAP:
            del_bubble(i)

#Spräcker bubblor - räkna ut distans mellan objekten
def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1) **2)

#Pop bubbles player 1
def collision1():
    points = 0
    for bub in range(len(bub_id)-1, -1, -1):
        if distance(ship1_id2, bub_id[bub]) < (SHIP_R1 + bub_r[bub]):
            points += (bub_r[bub] + bub_speed[bub])
            del_bubble(bub)    
    return points

#Pop bubbles player 2
def collision2():
    points = 0
    for bub in range(len(bub_id)-1, -1, -1):
        if distance(ship2_id2, bub_id[bub]) < (SHIP_R2 + bub_r[bub]):
            points += (bub_r[bub] + bub_speed[bub])
            del_bubble(bub)
    return points

#14 Poäng spelare 1
c.create_text(50, 30, text='TID P1', fill='white')
c.create_text(150, 30, text='POÄNG P1', fill='white')
time_text1 = c.create_text(50, 50, fill='white')
score_text1 = c.create_text(150, 50, fill='white')

#14 Poäng spelare 2
c.create_text(350, 30, text='TID P2', fill='white')
c.create_text(450, 30, text='POÄNG P2', fill='white')
time_text2 = c.create_text(350, 50, fill='white')
score_text2 = c.create_text(450, 50, fill='white')

#14 Visa poäng spelare 1 och 2
def show_score(score1, score2):
    c.itemconfig(score_text1, text=str(score1))
    c.itemconfig(score_text2, text=str(score2))

# visa tid
def show_time(time_left1, time_left2):
    c.itemconfig(time_text1, text=str(time_left1))
    c.itemconfig(time_text2, text=str(time_left2))

#tidsgräns och extratid
BUB_CHANCE = 10
TIME_LIMIT = 30
BONUS_SCORE = 1000
score1 = 0
score2 = 0
bonus1 = 0
bonus2 = 0
end1 = time() + TIME_LIMIT
end2 = time() + TIME_LIMIT

#Huvudloopen
score1 = 0
score2 = 0

while time() < end1 and time()< end2:
    if randint(1, BUB_CHANCE) == 1:
        create_bubble()
    move_bubbles()
    clean_up_bubs()
    #Score for player 1
    score1+=collision1()

    #Score for player 2
    score2+=collision2()

    #bonus time player 1 and 2
    if(int(score1/BONUS_SCORE)) > bonus1:
        bonus1+=1
        end1+=TIME_LIMIT
    elif(int(score2/BONUS_SCORE)) > bonus2:
        bonus2+=1
        end2+=TIME_LIMIT
    #Visa poäng spelare 1 och 2    
    show_score(score1,score2)
    show_time(int(end1 - time()),int(end2 - time()))
    
    window.update()
    sleep(0.01)

#GAME OVER
c.create_text(MID_X1, MID_Y1, \
    text='GAME OVER', fill='white', font=('Helvetica',30))
if(score1>score2):
    c.create_text(MID_X1, MID_Y1+50, \
        text='PLAYER 1 WINS' + str(), fill='white', font=('Helvetica',15))
    c.create_text(MID_X1, MID_Y1 + 75, \
        text='Poäng: ' + str(score1), fill='white')
    c.create_text(MID_X1, MID_Y1 + 95, \
        text='Extratid: ' + str(bonus1*TIME_LIMIT), fill='white')
else:
    c.create_text(MID_X1, MID_Y1+ 50, \
        text='PLAYER 2 WINS' + str(), fill='white', font=('Helvetica',15))
    c.create_text(MID_X1, MID_Y1 + 75, \
        text='Poäng: ' + str(score2), fill='white')
    c.create_text(MID_X1, MID_Y1 + 95, \
        text='Extratid: ' + str(bonus2*TIME_LIMIT), fill='white')

#Omstartsknapp
#c.create_button(MID_X, MID_Y + 30 \
#text='START OVER', fill=white, font=('Helvetica', 12))


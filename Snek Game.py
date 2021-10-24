from tkinter import *
from tkinter import ttk
import random
import os

##GUI Settings
GAME_WIDTH = 800
GAME_HEIGHT = 800
PACE = 100
BLOCK_SIZE = 50
SNAKE_LENGTH = 3
SNAKE_COLOUR = "green"
SCORE_COLOUR = "red"
BACKGROUND_COLOUR = "black"

##Interactives
class Snake:
    def __init__(self):
        self.snake_length =  SNAKE_LENGTH
        self.coordinates = []
        self.squares = []

        for i in range(0, SNAKE_LENGTH):
            self.coordinates.append([0,0])
        
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,y,x+BLOCK_SIZE, y+BLOCK_SIZE, fill=SNAKE_COLOUR, tag="snake")
            self.squares.append(square)
    

class Score:
    def __init__(self):
        x = random.randint(0,(GAME_WIDTH/BLOCK_SIZE)-1) * BLOCK_SIZE
        y = random.randint(0,(GAME_HEIGHT/BLOCK_SIZE)-1) * BLOCK_SIZE

        self.coordinates = [x,y]

        canvas.create_rectangle(x,y,x+BLOCK_SIZE, y+BLOCK_SIZE, fill=SCORE_COLOUR, tag="score")

def next_move(snake, score):

    x, y = snake.coordinates[0]
    
    if direction == "up":
        y -= BLOCK_SIZE
    elif direction == "down":
         y += BLOCK_SIZE
    elif direction == "left":
         x -= BLOCK_SIZE
    elif direction == "right":
         x += BLOCK_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x,y,x+BLOCK_SIZE, y+BLOCK_SIZE, fill=SNAKE_COLOUR, tag="snake")

    snake.squares.insert(0,square)

    if x == score.coordinates[0] and y == score.coordinates[1]:
        
        global length
        
        length += 1
        
        label.config(text="Score:{}".format(length))

        canvas.delete("score")

        score = Score()
    
    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]
    
    if check_collisions(snake):
        
        game_over()
    
    else :
        
        window.after(PACE, next_move, snake, score)

def change_direction(new_direction):
    
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    
    x,y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:

        return TRUE
    
    elif y < 0 or y >= GAME_HEIGHT:

        return TRUE

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return TRUE

    return FALSE

def game_over():
    canvas.delete(ALL)

    new = Canvas(window, bg = "pink", height=GAME_HEIGHT, width=GAME_WIDTH)
    new.pack()
    
    label = Label(canvas, text= "GG", font= ('Helvetica 80 bold'))
    label.pack(pady= 30)
    
    ttk.Button(new, text='Restart',command = restart).pack()
    new.pack()

def restart():
    os.system("python 'Snek Game.py'")
    



window = Tk()
window.title("Snek Game")
window.resizable(False, False)

length = 0
direction = 'down'

label = Label(window, text="Score:{}".format(length), font=('Times', 40))
label.pack()

canvas = Canvas(window, bg = BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


window.update()

window.pack_propagate(False)

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

width = int((screen_width/2) - (window_width/2))
height = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{width}+{height}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
score = Score()

next_move(snake,score)

window.mainloop()
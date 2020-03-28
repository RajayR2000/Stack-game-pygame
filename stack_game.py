import pygame
pygame.init()

class Box:
    def __init__(self,width,height,speed,x,y):
        self.width=width
        self.height=height
        self.speed=speed
        self.x=x
        self.y=y

score=0
life=5
font1=pygame.font.SysFont('comicsans',50,True)
stackImg=pygame.image.load('final_stack.jpg')
win=pygame.display.set_mode((500,500))
pygame.display.set_caption('Stack game')
bg=pygame.image.load('stack_game_bg.png')
clock = pygame.time.Clock()
boxes=[]
initial_width=50
initial_height=50
start_box=Box(50,50,5,0,500-initial_height)
boxes.append(start_box)
run=True
tickval = 25


def redraw_window(score,box):
    win.blit(bg, (0, 0))
    text = font1.render('Score: ' +  str(score), 1, (0,0,0))

    if box.y+50<=0:
        font3 = pygame.font.SysFont('comicsans', 100)
        text = font3.render('You Won', 1, (0, 0, 255))
        win.blit(text, (250 - (text.get_width() // 2), 200))
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.quit()

    win.blit(text, (10, 10))


    for box in boxes:
        pygame.draw.rect(win, (100,100,100), (box.x, box.y, box.width, box.height))

    pygame.display.update()


while run:
    curr_box = boxes[len(boxes) - 1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] :
        print("in")
        if len(boxes) > 1:
            prev_box = boxes[len(boxes) - 2]

            prev_box_size = prev_box.x + prev_box.width

            curr_box_size = curr_box.x + curr_box.width

            if (curr_box.x > prev_box.x and curr_box.x < prev_box_size):
                score += 10
                new_width = prev_box.width - (curr_box_size - prev_box_size)
                print(prev_box.width, curr_box.width, new_width)
                curr_box.width = new_width
                curr_box = Box(new_width, curr_box.height, curr_box.speed, 0, curr_box.y - curr_box.height)
                tickval += 20
                boxes.append(curr_box)
                redraw_window(score, curr_box)

            elif (curr_box_size < prev_box_size and curr_box_size > prev_box.x):
                score += 10
                new_width = prev_box.width - abs(curr_box_size - prev_box_size)
                print(prev_box.width, curr_box.width, new_width)
                curr_box.width = new_width
                curr_box.x = prev_box.x
                curr_box = Box(new_width, curr_box.height, curr_box.speed, 0, curr_box.y - curr_box.height)
                tickval += 20
                boxes.append(curr_box)
                redraw_window(score, curr_box)

            elif curr_box.x == prev_box.x:
                score += 20
                curr_box = Box(curr_box.width, curr_box.height, curr_box.speed, 0, curr_box.y - curr_box.height)
                boxes.append(curr_box)
                redraw_window(score, curr_box)

            else:
                pygame.time.delay(500)
                life+=1
                redraw_window(score,curr_box)
        else:
            curr_box = Box(curr_box.width, curr_box.height, curr_box.speed, 0, curr_box.y - curr_box.height)
            tickval += 5
            boxes.append(curr_box)
            redraw_window(score, curr_box)

    if curr_box.x == 0:
        move_right = True

    elif curr_box.x + curr_box.width == 500:
        move_right = False

    if move_right == True:
        curr_box.x += curr_box.speed
    else:
        curr_box.x -= curr_box.speed

    clock.tick(tickval)
    keys = []
    redraw_window(score, curr_box)

pygame.quit()



import pygame
import random
import os

pygame.init()

HEIGHT = 600

WIDTH = 800

win = pygame.display.set_mode((WIDTH, HEIGHT))

os.chdir(r'C:\Users\juand\Documents\Old Projects\Game')

pygame.display.set_caption("Universo_2113")

SCOLOR = (250, 250, 0)

myFont = pygame.font.SysFont("comicsansms", 50)

Normal_BACKGRAUND = pygame.image.load(r'Background.png')

Normal_BACKGRAUND = pygame.transform.scale(Normal_BACKGRAUND, (WIDTH, HEIGHT))

Dark_BACKGRAUND = pygame.image.load(r'Dark.png')

Dark_BACKGRAUND = pygame.transform.scale(Dark_BACKGRAUND, (WIDTH, HEIGHT))

Darker_BACKGRAUND = pygame.image.load(r'Darker.png')

Darker_BACKGRAUND = pygame.transform.scale(Darker_BACKGRAUND, (WIDTH, HEIGHT))

BACKGRAUND = pygame.image.load(r'Darkest.png')

BACKGRAUND = pygame.transform.scale(BACKGRAUND, (WIDTH, HEIGHT))

YOU_WON = pygame.image.load(r'YOU_WIN.jpg')

YOU_WON = pygame.transform.scale(YOU_WON, (WIDTH, HEIGHT))

GAME_OVER = pygame.image.load(r'GAME_OVER.jpg')

GAME_OVER = pygame.transform.scale(GAME_OVER, (WIDTH, HEIGHT))

message = pygame.image.load(r'message.png')

message = pygame.transform.scale(message, (600, 150))

game_finished = False

JUAN = pygame.image.load(r"hero-1.png.png")

player = JUAN

player = pygame.transform.scale(player, (100, 100))

EMPTY = pygame.image.load(r"Empty.png")

BATTLEMUSIC = pygame.mixer.music.load(r"xDeviruchi - Decisive Battle (Loop).wav")






walkRight = [pygame.image.load(r"caminar derecha-1.png.png"), pygame.image.load(r"caminar derecha-2.png.png")]

walkLeft = [pygame.image.load(r"caminar izquierda-1.png.png"), pygame.image.load(r"caminar izquierda-2.png.png")]



walkRight[0] = pygame.transform.scale(walkRight[0], (100, 100))

walkRight[1] = pygame.transform.scale(walkRight[1], (100, 100))

walkLeft[0] = pygame.transform.scale(walkLeft[0], (100, 100))

walkLeft[1] = pygame.transform.scale(walkLeft[1], (100, 100))





walkUp = [pygame.image.load(r"caminar arriba-1.png.png"), pygame.image.load(r"caminar arriba-2.png.png"), 
          pygame.image.load(r"caminar arriba-1.png.png"), pygame.image.load(r"caminar arriba-4.png.png")]

walkDown = [pygame.image.load(r"hero-1.png.png"), pygame.image.load(r"hero-2.png.png"), 
            pygame.image.load(r"hero-1.png.png"), pygame.image.load(r"hero-4.png.png")]



walkUp[0] = pygame.transform.scale(walkUp[0], (100, 100))

walkUp[1] = pygame.transform.scale(walkUp[1], (100, 100))

walkUp[2] = pygame.transform.scale(walkUp[2], (100, 100))

walkUp[3] = pygame.transform.scale(walkUp[3], (100, 100))



walkDown[0] = pygame.transform.scale(walkDown[0], (100, 100))

walkDown[1] = pygame.transform.scale(walkDown[1], (100, 100))

walkDown[2] = pygame.transform.scale(walkDown[2], (100, 100))

walkDown[3] = pygame.transform.scale(walkDown[3], (100, 100))



AttacL = [pygame.image.load(r"ataque izquierda-1.png.png"), pygame.image.load(r"ataque izquierda-2.png.png"), 
          pygame.image.load(r"ataque izquierda-3.png.png")]

AttacR = [pygame.image.load(r"ataque derecha-1.png.png"), pygame.image.load(r"ataque derecha-2.png.png"), 
          pygame.image.load(r"ataque derecha-3.png.png")]

AttacU = [pygame.image.load(r"ataque arriba-1.png.png"), pygame.image.load(r"ataque arriba-2.png.png"), 
          pygame.image.load(r"ataque arriba-3.png.png"), pygame.image.load(r"ataque arriba-4.png.png")]

AttacD = [pygame.image.load(r"ataque abajo-1.png.png"), pygame.image.load(r"ataque abajo-2.png.png"), 
          pygame.image.load(r"ataque abajo-3.png.png"), pygame.image.load(r"ataque abajo-4.png.png")]


AttacL[0] = pygame.transform.scale(AttacL[0], (100, 100))
AttacL[1] = pygame.transform.scale(AttacL[1], (100, 100))
AttacL[2] = pygame.transform.scale(AttacL[2], (100, 100))

AttacR[0] = pygame.transform.scale(AttacR[0], (100, 100))
AttacR[1] = pygame.transform.scale(AttacR[1], (100, 100))
AttacR[2] = pygame.transform.scale(AttacR[2], (100, 100))

AttacU[0] = pygame.transform.scale(AttacU[0], (100, 100))
AttacU[1] = pygame.transform.scale(AttacU[1], (100, 100))
AttacU[2] = pygame.transform.scale(AttacU[2], (100, 100))
AttacU[3] = pygame.transform.scale(AttacU[3], (100, 100))

AttacD[0] = pygame.transform.scale(AttacD[0], (100, 100))
AttacD[1] = pygame.transform.scale(AttacD[1], (100, 100))
AttacD[2] = pygame.transform.scale(AttacD[2], (100, 100))
AttacD[3] = pygame.transform.scale(AttacD[3], (100, 100))


Dark_walkRight = [pygame.image.load(r"Him-1.png.png"), pygame.image.load(r"Him-2.png.png")]

Dark_walkLeft = [pygame.image.load(r"caminar izquierda Him -1.png.png"), pygame.image.load(r"caminar izquierda Him -2.png.png")]



Dark_walkRight[0] = pygame.transform.scale(Dark_walkRight[0], (100, 100))

Dark_walkRight[1] = pygame.transform.scale(Dark_walkRight[1], (100, 100))

Dark_walkLeft[0] = pygame.transform.scale(Dark_walkLeft[0], (100, 100))

Dark_walkLeft[1] = pygame.transform.scale(Dark_walkLeft[1], (100, 100))



Dark_walkUp = [pygame.image.load(r"caminar arriba him-1.png.png"), pygame.image.load(r"caminar arriba him-2.png.png"), 
               pygame.image.load(r"caminar arriba him-3.png.png"), pygame.image.load(r"caminar arriba him-4.png.png")]

Dark_walkDown = [pygame.image.load(r"him-1.png.png"), pygame.image.load(r"him-2.png.png"), 
                 pygame.image.load(r"him-3.png.png"), pygame.image.load(r"him-4.png.png")]



Dark_walkUp[0] = pygame.transform.scale(Dark_walkUp[0], (100, 100))

Dark_walkUp[1] = pygame.transform.scale(Dark_walkUp[1], (100, 100))

Dark_walkUp[2] = pygame.transform.scale(Dark_walkUp[2], (100, 100))

Dark_walkUp[3] = pygame.transform.scale(Dark_walkUp[3], (100, 100))



Dark_walkDown[0] = pygame.transform.scale(Dark_walkDown[0], (100, 100))

Dark_walkDown[1] = pygame.transform.scale(Dark_walkDown[1], (100, 100))

Dark_walkDown[2] = pygame.transform.scale(Dark_walkDown[2], (100, 100))

Dark_walkDown[3] = pygame.transform.scale(Dark_walkDown[3], (100, 100))


FINAL_ATTACK = [
pygame.image.load(r"Final attack\FINALATTACK_01.png"), 
pygame.image.load(r"Final attack\FINALATTACK_02.png"),
pygame.image.load(r"Final attack\FINALATTACK_03.png"),
pygame.image.load(r"Final attack\FINALATTACK_04.png"),
pygame.image.load(r"Final attack\FINALATTACK_05.png"),
pygame.image.load(r"Final attack\FINALATTACK_06.png"),
pygame.image.load(r"Final attack\FINALATTACK_07.png"),
pygame.image.load(r"Final attack\FINALATTACK_08.png"),
pygame.image.load(r"Final attack\FINALATTACK_09.png"),
pygame.image.load(r"Final attack\FINALATTACK_10.png"),
pygame.image.load(r"Final attack\FINALATTACK_11.png"),
pygame.image.load(r"Final attack\FINALATTACK_12.png"),
pygame.image.load(r"Final attack\FINALATTACK_13.png"),
pygame.image.load(r"Final attack\FINALATTACK_14.png"),
pygame.image.load(r"Final attack\FINALATTACK_15.png"),
pygame.image.load(r"Final attack\FINALATTACK_16.png"),
pygame.image.load(r"Final attack\FINALATTACK_17.png"),
pygame.image.load(r"Final attack\FINALATTACK_18.png"),
pygame.image.load(r"Final attack\FINALATTACK_19.png"),
pygame.image.load(r"Final attack\FINALATTACK_20.png"),
pygame.image.load(r"Final attack\FINALATTACK_21.png")
]

for i in range(21):
    FINAL_ATTACK[i] = pygame.transform.scale(FINAL_ATTACK[i], (100, 100))

FINAL_HIM = [
pygame.image.load(r"HIM\HIM_00.png"), 
pygame.image.load(r"HIM\HIM_01.png"),
pygame.image.load(r"HIM\HIM_02.png"), 
pygame.image.load(r"HIM\HIM_03.png"),
pygame.image.load(r"HIM\HIM_04.png"), 
pygame.image.load(r"HIM\HIM_05.png"),
pygame.image.load(r"HIM\HIM_06.png"), 
pygame.image.load(r"HIM\HIM_07.png"),
pygame.image.load(r"HIM\HIM_08.png"), 
pygame.image.load(r"HIM\HIM_09.png"),
pygame.image.load(r"HIM\HIM_10.png"), 
pygame.image.load(r"HIM\HIM_11.png"),
pygame.image.load(r"HIM\HIM_12.png")
]

for i in range(13):
    FINAL_HIM[i] = pygame.transform.scale(FINAL_HIM[i], (100, 100))



x = 342   

y = 250

"Dark_x = 500"

"Dark_y = 100"

Dark_Size = (64, 64)


player_WIDTH = 64

player_HEIGHT = 64

vel = 21

game_over = False

IsAttacking = False

left = False

right = False

up = False

down = False

WalkCountX = 0

WalkCountY = 0

Dark_WalkCountX = 0

Dark_WalkCountY = 0

IsLeft = False
IsRigth = False
IsUp = False
IsDown = True

score = 0


def draw_win():

    global IsLeft

    global IsRigth

    global IsUp

    global IsDown

    global WalkCountX

    global WalkCountY

    win.blit(BACKGRAUND, [0,0])



    if WalkCountX == 2:
        WalkCountX = 0


    if WalkCountY == 4:
        WalkCountY = 0

    if True:

        if left:
            win.blit(walkLeft[WalkCountX], (x,y))
            WalkCountX += 1
            IsLeft = True
            IsRigth = False
            IsUp = False
            IsDown = False

        elif right:
            win.blit(walkRight[WalkCountX], (x,y))
            WalkCountX += 1
            IsLeft = False
            IsRigth = True
            IsUp = False
            IsDown = False

        elif up:
            win.blit(walkUp[WalkCountY], (x,y))
            WalkCountY += 1
            IsLeft = False
            IsRigth = False
            IsUp = True
            IsDown = False

        elif down:
            win.blit(walkDown[WalkCountY], (x,y))
            WalkCountY += 1
            IsLeft = False
            IsRigth = False
            IsUp = False
            IsDown = True

        else:
            if IsLeft:
                win.blit(walkLeft[0], [x, y])

            if IsRigth:
                win.blit(walkRight[0], [x, y])

            if IsUp:
                win.blit(walkUp[0], [x, y])

            if IsDown:
                win.blit(walkDown[0], [x, y])

        pygame.display.update()



      
def attac():

    global x

    global y

    global Dark_x

    global Dark_y

    global game_over

    global score

    win.blit(BACKGRAUND, [0,0])
    

    if IsLeft:
        Delay_For_Background = 2


        for i in range(3):
            win.blit(AttacL[i], [x, y])

            if detect_sword_colision(x, y, Dark_x, Dark_y, "left"):
                print("Efective Attack")
                score = scoring(300, score)

            draw_Dark()
            if Dark_Direction == "right":
                Dark_x += 42

            if Dark_Direction == "left":
                Dark_x -= 42

            if Dark_Direction == "down":
                Dark_y += 42

            if Dark_Direction == "up":
                Dark_y -= 42

            pygame.display.update()
            pygame.time.delay(103)

            if Delay_For_Background > 0:
                win.blit(BACKGRAUND, [0,0])
                Delay_For_Background = Delay_For_Background - 1
       

    if IsRigth:
        Delay_For_Background = 2

        for i in range(3):
            win.blit(AttacR[i], [x, y])

            if detect_sword_colision(x, y, Dark_x, Dark_y, "left"):
                print("Efective Attack")
                score = scoring(300, score)

            draw_Dark()
            if Dark_Direction == "right":
                Dark_x += 42

            if Dark_Direction == "left":
                Dark_x -= 42

            if Dark_Direction == "down":
                Dark_y += 42

            if Dark_Direction == "up":
                Dark_y -= 42

            pygame.display.update()
            pygame.time.delay(103)


            if Delay_For_Background > 0:
                
                win.blit(BACKGRAUND, [0,0])
                Delay_For_Background = Delay_For_Background - 1

    if IsUp:
        Delay_For_Background = 3

        for i in range(4):
            win.blit(AttacU[i], [x, y])

            if detect_sword_colision(x, y, Dark_x, Dark_y, "left"):
                print("Efective Attack")
                score = scoring(300, score)

            draw_Dark()
            if Dark_Direction == "right":
                Dark_x += 42

            if Dark_Direction == "left":
                Dark_x -= 42

            if Dark_Direction == "down":
                Dark_y += 42

            if Dark_Direction == "up":
                Dark_y -= 42

            pygame.display.update()
            pygame.time.delay(103)

            if Delay_For_Background > 0:
                win.blit(BACKGRAUND, [0,0])
                Delay_For_Background = Delay_For_Background - 1
            

    if IsDown:
        Delay_For_Background = 3

        for i in range(4):
            win.blit(AttacD[i], [x, y])

            if detect_sword_colision(x, y, Dark_x, Dark_y, "left"):
                print("Efective Attack")
                score = scoring(300, score)


            draw_Dark()
            if Dark_Direction == "right":
                Dark_x += 42

            if Dark_Direction == "left":
                Dark_x -= 42

            if Dark_Direction == "down":
                Dark_y += 42

            if Dark_Direction == "up":
                Dark_y -= 42 
  
            pygame.display.update()
            pygame.time.delay(103)

            if Delay_For_Background > 0:
                win.blit(BACKGRAUND, [0,0])
                Delay_For_Background = Delay_For_Background - 1

    pygame.display.update()

def detect_colision(x, y, Dark_x, Dark_y):
    p_x = x
    p_y = y

    o_x = Dark_x
    o_y = Dark_y

    if (o_x >= p_x and o_x < (p_x + player_WIDTH)) or (p_x >= o_x and p_x < (o_x + Dark_Size[0])):
        if (o_y >= p_y and o_y < (p_y + player_HEIGHT)) or (p_y >= o_y and p_y < (o_y + Dark_Size[1])):
            return True
    return False

def detect_sword_colision(x, y, Dark_x, Dark_y, Direction):
    p_x = x
    p_y = y

    o_x = Dark_x
    o_y = Dark_y

    if Direction == "right":
        if (o_x >= p_x and o_x < (p_x + player_WIDTH*2)):
            if (o_y >= p_y and o_y < (p_y + player_HEIGHT)) or (p_y >= o_y and p_y < (o_y + Dark_Size[1])):
                print("golpe a la derecha")
                return True

    if Direction == "left":
        if (p_x >= o_x and p_x < (o_x + Dark_Size[0])):
            if (o_y >= p_y and o_y < (p_y + player_HEIGHT)) or (p_y >= o_y and p_y < (o_y + Dark_Size[1])):
                print("golpe a la izquierda")
                return True

    if Direction == "up":
        if (o_x >= p_x and o_x < (p_x + player_WIDTH)) or (p_x >= o_x and p_x < (o_x + Dark_Size[0])):
            if (p_y >= o_y and p_y < (o_y + Dark_Size[1])):
                print("golpe arriba")
                return True

    if Direction == "down":
        if (o_x >= p_x and o_x < (p_x + player_WIDTH)) or (p_x >= o_x and p_x < (o_x + Dark_Size[0])):
            if (o_y >= p_y and o_y < (p_y + player_HEIGHT + (player_HEIGHT/2))):
                print("golpe abajo")
                return True

    return False


def draw_Dark():

    global Dark_WalkCountX

    global Dark_WalkCountY

    global score

    if Dark_Direction == "right":

        if Dark_x > 790:
            Organize_Dirección_Dark()
            score = scoring(21, score)
        try:
            win.blit(Dark_walkRight[Dark_WalkCountX], [Dark_x, Dark_y])        

        except IndexError:
            Dark_WalkCountX = Dark_WalkCountX + 1 
        
    if Dark_Direction == "left":

        if Dark_x < -20:
            Organize_Dirección_Dark()
            score = scoring(21, score)

        try:
            win.blit(Dark_walkLeft[Dark_WalkCountX], [Dark_x, Dark_y])

        except IndexError:
            Dark_WalkCountX = Dark_WalkCountX + 1 

    if Dark_Direction == "down":

        if Dark_y > 500:
            Organize_Dirección_Dark()
            score = scoring(21, score)
        
        try:
            win.blit(Dark_walkDown[Dark_WalkCountY], [Dark_x, Dark_y])     

        except IndexError:
            Dark_WalkCountY = Dark_WalkCountY + 1 


    if Dark_Direction == "up":

        if Dark_y < -20: 
            Organize_Dirección_Dark()
            score = scoring(21, score)
        try:
            win.blit(Dark_walkUp[Dark_WalkCountY], [Dark_x, Dark_y])       

        except IndexError:
            Dark_WalkCountY = Dark_WalkCountY + 1 

    else:

        if Dark_Direction == "left":
            try:
                win.blit(Dark_walkLeft[Dark_WalkCountX], [Dark_x, Dark_y])      

            except IndexError:
                Dark_WalkCountX = Dark_WalkCountX + 1 

        if Dark_Direction == "right":
            try:
                win.blit(Dark_walkRight[Dark_WalkCountX], [Dark_x, Dark_y])      

            except IndexError:
                Dark_WalkCountX = Dark_WalkCountX + 1 

        if Dark_Direction == "up":
            try:
                win.blit(Dark_walkUp[Dark_WalkCountY], [Dark_x, Dark_y])       

            except IndexError:
                Dark_WalkCountY = Dark_WalkCountY + 1 

        if Dark_Direction == "down":
            try:
                win.blit(Dark_walkDown[Dark_WalkCountY], [Dark_x, Dark_y])     

            except IndexError:
                Dark_WalkCountY = Dark_WalkCountY + 1 

    "print(str(Dark_WalkCountX), str(Dark_WalkCountY))"

    score = scoring(0, score)

    pygame.display.update()


def Dark_Start_Point():
    global Dark_x
    global Dark_y

    if random.randint(0, 1) == 1:
        
        if random.randint(0, 1) == 1:
            Dark_x = 10
            Dark_y = random.randint(10, 590)
        else:
            Dark_x = 790
            Dark_y = random.randint(10, 590)

    else: 
        if random.randint(0, 1) == 1:
            Dark_x = random.randint(10, 790)
            Dark_y = 10
        else:
            Dark_x = random.randint(10, 790)
            Dark_y = 590


    Dark_Coordinates = (Dark_x, Dark_y)
    print(Dark_Coordinates)

    return Dark_Coordinates

def Organize_Dirección_Dark():

    global Dark_Direction

    Dark_Coordinates = Dark_Start_Point()
    Dark_x = Dark_Coordinates[0]
    Dark_y = Dark_Coordinates[1]

    if Dark_x == 10:
        print(" SE VA A LA DERECHA")
        Dark_Direction = "right"

    if Dark_x == 790:
        print(" SE VA A LA IZQUIERDA")
        Dark_Direction = "left"

    if Dark_y == 10:
        print(" SE VA ABAJO")
        Dark_Direction = "down"

    if Dark_y == 590:
        print(" SE VA ARRIBA")
        Dark_Direction = "up"   


def scoring(Value_to_add, score):

    score += Value_to_add

    return score

Organize_Dirección_Dark()

win.blit(Normal_BACKGRAUND, [0,0])
pygame.display.update()
pygame.time.delay(500)
win.blit(Dark_BACKGRAUND, [0,0])
pygame.display.update()
pygame.time.delay(500)
win.blit(Darker_BACKGRAUND, [0,0])
pygame.display.update()

pygame.time.delay(500)
pygame.mixer.music.play(13)

while not game_over:

    pygame.time.delay(100)

    text = "Score: " + str(score)
    label = myFont.render(text, 1, SCOLOR)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            game_over = True



    keys = pygame.key.get_pressed()



    if keys[pygame.K_LEFT] and x > 42:

        x -= vel

        left = True

    if keys[pygame.K_RIGHT] and x < WIDTH - player_WIDTH -vel -42:

        x += vel

        right = True

    if keys[pygame.K_UP] and y > 0: 

        y -= vel

        up = True

    if keys[pygame.K_DOWN] and y < HEIGHT - player_HEIGHT -vel -42:

        y += vel

        down = True

    if keys[pygame.K_SPACE] and y < HEIGHT - player_HEIGHT -vel:


        vel = 50
        attac()




    if False == keys[pygame.K_SPACE] and y < HEIGHT - player_HEIGHT -vel:

        vel = 21
        draw_win()
        win.blit(label, (WIDTH-300, HEIGHT- 90))


    if Dark_Direction == "right":
        Dark_x += 50

    if Dark_Direction == "left":
        Dark_x -= 50

    if Dark_Direction == "down":
        Dark_y += 50

    if Dark_Direction == "up":
        Dark_y -= 50

    Dark_WalkCountY += 1

    if Dark_WalkCountY >= 4:
        Dark_WalkCountY = 0


    Dark_WalkCountX += 1

    if Dark_WalkCountX >= 2:
        Dark_WalkCountX = 0



    draw_Dark()
    

    left = False

    right = False

    up = False

    down = False

    score = scoring(0, score)

    if score >= 300:

        distance = 50

        for i in range(11):

            win.blit(BACKGRAUND, [0,0])
            win.blit(FINAL_ATTACK[i], (210, 221))
            win.blit(FINAL_HIM[int(i/1.3)], (500, 270))
            pygame.time.delay(321)
            pygame.display.update()

        for i in range(10):

            win.blit(BACKGRAUND, [0,0])
            win.blit(FINAL_HIM[int(i/2)+7], (500, 270))
            win.blit(FINAL_ATTACK[i + 11], (242 + distance, 250))
            distance += 33
            pygame.time.delay(50)
            pygame.display.update()




        ENDMUSIC = pygame.mixer.music.load(r"xDeviruchi - Decisive Battle (End).wav")
        pygame.time.delay(1000)
        pygame.mixer.music.play(1)
        win.blit(YOU_WON, (0, 0))
        pygame.display.update()
        pygame.time.delay(3000)

        print("YOU WON")
        game_over = True


    if detect_colision(x, y, Dark_x, Dark_y):

        print("TE ATACO")

        pygame.time.delay(100)

        while not game_finished:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    game_finished = True

            keys = pygame.key.get_pressed()


            win.blit(GAME_OVER, (0, 0))
            win.blit(message, (100, 350))
            pygame.display.update()


            if keys[pygame.K_a]:
                print("reviving")
                score = 0
                x = 342
                y = 250
                Organize_Dirección_Dark()
                break

            if keys[pygame.K_x]:
                game_finished = True
                win.blit(GAME_OVER, (0, 0))
                pygame.time.delay(300)
                print("GAME OVER")
                game_over = True
            
pygame.quit()

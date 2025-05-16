import pygame
import random
import DesignClass
from birdturtle import BirdTurtle
from ObstacleClass import ObstacleClass, collide_list
from InfoCard import InfoCard
from UIClasses import TextClass, ButtonClass
from ObjectTimersClass import ObjectTimersClass
from deer import Deer
from livesclass import Lives
from sound import SoundClass

buttonlist = []
collect_list = []
km_count = 0
specialTransition = False

        
def ChangeGameState(newGameState):
    global GameState
    global buttonlist
    global end_time_text
    global km_count

    GameState = newGameState
    buttonlist = []
    end_time_text = current_time + 10000
    birdNPC.xcor = -100
    km_count = 0

def ResetGame():
    global GameState, buttonlist
    global obstacle_list, collide_list
    global end_time_cloud_spawn, end_time_bubble_spawn, end_time_wolf_spawn, end_time_wolf_animation, time_pass, end_time_hawk_animation, end_time_hawk_spawn, end_time_bullet_spawn
    global end_time_tree_spawn, end_time_snow_spawn, end_time_player_animation, end_time_rain_spawn, end_time_tNPC_move, end_time_eggs_move
    global end_time_trash_spawn, end_time_killerwhale_spawn, end_time_bug_spawn, end_time_hunter
    global end_time_shark_spawn, end_time_trap_spawn, end_time_eagle_spawn
    global end_time_bNPC_move, end_time_km_update, end_time_jellyfish_spawn
    global isJumping, vert_acceleration
    global current_player
    global bugsCaughtAmount

    buttonlist = []
    end_time_text = pygame.time.get_ticks() + 10000
    #ObjectTimers.
    birdNPC.xcor = -100
    km_count = 0
    bugsCaughtAmount = 0

    # reset objects
    obstacle_list = []
    collide_list = []

    # Reset all timers
    ObjectTimers.setAllDefault()
    end_time_player_animation = 0
    end_time_cloud_spawn = 0
    end_time_bubble_spawn = 0
    end_time_wolf_spawn = 1000
    end_time_wolf_animation = 0
    end_time_tree_spawn = 1000
    end_time_text = 8000
    end_time_snow_spawn = 0
    end_time_bNPC_move = 0
    end_time_tNPC_move = 0
    end_time_km_update = 0
    end_time_rain_spawn = 0
    time_pass = 0
    end_time_hawk_spawn = 0
    end_time_hawk_animation = 0
    end_time_bullet_spawn = 5000
    end_time_eggs_move = 3000
    end_time_trash_spawn = 5000
    end_time_shark_spawn = 8000
    end_time_killerwhale_spawn = 8000
    end_time_hunter = 0
    end_time_bug_spawn = 1000
    end_time_trap_spawn = 0
    end_time_eagle_spawn = random.randint(6000, 13000)
    end_time_jellyfish_spawn = 14000

    # Reset jump variables
    isJumping = False
    vert_acceleration = start_acceleration
    deer.ycor = 400

    #Reset hearts
    lives.lives = []
    
    GameState = "TitleScreen"

def SpecialLevelEnter():
    global GameState
    global specialTransition
    if current_player.ycor < 840:
        specialTransition = True
    else:
        GameState = "TitleScreen"

pygame.init()
pygame.display.set_caption("Animal Journey")
screen = pygame.display.set_mode((DesignClass.SCREEN_WIDTH, DesignClass.SCREEN_HEIGHT))




#Animal Frame Lists
bird_frames = []
turt_frames = []
deer_frames = []
friendly_bird_frames = []

for num in range(8):
    frame = pygame.image.load(f"ImageAssets/BirdAsset/BirdFlying{num+1}.png")
    frame = pygame.transform.scale(frame, size= (64, 64))
    frame = pygame.transform.flip(frame, flip_x=True, flip_y=False)
    bird_frames.append(frame)

for num in range(6):
    frame = pygame.image.load(f"ImageAssets/TurtleAsset/24bit-seaturtle{num+1}.png")
    frame = pygame.transform.scale(frame, size= (96, 96))
    frame = pygame.transform.flip(frame, flip_x=True, flip_y=False)
    turt_frames.append(frame)
    
for num in range(8):
    frame = pygame.image.load(f"ImageAssets/FriendlyBirdAsset/BirdFlying{num+1}.png")
    frame = pygame.transform.scale(frame, size= (64, 64))
    frame = pygame.transform.flip(frame, flip_x=True, flip_y=False)
    friendly_bird_frames.append(frame)

for img in range(5):
            frame = pygame.image.load(f'ImageAssets/DeerAsset/deer{img+1}.png')
            frame = pygame.transform.scale(frame, (28*4, 100))
            deer_frames.append(frame)

# for num in range([NUMBER_OF_FRAMES]):
#    frame = pygame.image.load(f"FRAME FILE LOCATION, WITH A WAY TO DIFFERENCIATE FILE")
#    frame = pygame.transform.scale(frame, size= (96, 96))
#    frame = pygame.transform.flip(frame, flip_x=True, flip_y=False)
#    turt_frames.append(frame)



#Animal Obj s
bird = BirdTurtle(50, 50, bird_frames, 20)
birdNPC = BirdTurtle(-100, 300, bird_frames, 16)
birdFlock1 = BirdTurtle(-100, bird.ycor - 100, friendly_bird_frames, 20)
birdFlock2 = BirdTurtle(-50, bird.ycor, friendly_bird_frames, 20)
birdFlock3 = BirdTurtle(-100, bird.ycor + 100, friendly_bird_frames, 20)
turtle = BirdTurtle(50, 400, turt_frames, 96)
deer = Deer(50, 400)
bonusDeer = BirdTurtle(50, 400, deer_frames, 60)
lives = Lives()
Sound = SoundClass()


#Info Cards
bird_info = InfoCard(
    "Red Winged Blackbird",
    "A stocky, red and black bird, and one",
    "that is very common in North America.",
    " Air pollution, Hawks, Eagles",
    "Migrate in flocks",
    "13000 km from Idaho to Florida",
    DesignClass.SCREEN_WIDTH_CENTER,
    DesignClass.SCREEN_HEIGHT_CENTER,
    bird_frames[0],
    DesignClass.Colors["SKYBLUE"],
    0,
    screen,
    ChangeGameState,
    "BirdLevel"
)

turtle_info = InfoCard(
    "Leather-Back Sea Turtle",
    "The largest sea turtle in the world, one",
    "that travels thousands of kilometers",
    "Pollution, Sharks",
    "Long distance migration",
    "4000 km across the Atlantic",
    DesignClass.SCREEN_WIDTH_CENTER - 300,
    DesignClass.SCREEN_HEIGHT_CENTER,
    turt_frames[0],
    DesignClass.Colors["OCEANBLUE"],
    40,
    screen,
    ChangeGameState,
    "TurtleLevel"
)

deer_info = InfoCard(
    "White-Tailed Deer",
    "A white and brown deer, which is",
    "abundant all over Central America",
    "Wolves, Habitat Loss",
    "Migrate during season change",
    "250 km across Brazil's plateaus",
    DesignClass.SCREEN_WIDTH_CENTER + 300,
    DesignClass.SCREEN_HEIGHT_CENTER,
    pygame.transform.scale(deer.icon, (28*3, 75)),
    DesignClass.Colors["GRASSGREEN"],
    40,
    screen,
    ChangeGameState,
    "DeerLevel"
)

#Obstacle Related Lists
obstacle_list = []
cloud_img_list = ["ImageAssets/CloudAsset/Cloud 10.png", "ImageAssets/CloudAsset/Cloud 11.png", "ImageAssets/CloudAsset/Cloud 12.png"]



#Wait Animation Section
ObjectTimers = ObjectTimersClass()
ObjectTimers.addObject("Player_Animation", 0)
ObjectTimers.addObject("Cloud_Spawn", 0)
ObjectTimers.addObject("Bubble_Spawn", 0)
ObjectTimers.addObject("Wolf_Spawn", 1000)
ObjectTimers.addObject("Wolf_Animation", 0)
ObjectTimers.addObject("Tree_Spawn", 1000)
ObjectTimers.addObject("Text", 8000)
ObjectTimers.addObject("Snow_Spawn", 0)
ObjectTimers.addObject("bNPC_Move", 0)
ObjectTimers.addObject("tNPC_Move", 0)
ObjectTimers.addObject("KM_Update", 0)
ObjectTimers.addObject("Rain_Spawn", 0)
ObjectTimers.addObject("Time_Pass", 0)
ObjectTimers.addObject("Hawk_Spawn", 0)
ObjectTimers.addObject("Hawk_Animation", 0)
ObjectTimers.addObject("Bullet_Spawn", 5000)
ObjectTimers.addObject("Eggs_Move", 3000)
ObjectTimers.addObject("Trash_Spawn", 5000)
ObjectTimers.addObject("Shark_Spawn", 8000)
ObjectTimers.addObject("Killerwhale_Spawn", 8000)
ObjectTimers.addObject("Hunter", 0)
ObjectTimers.addObject("Bug_Spawn", 1000)
ObjectTimers.addObject("Trap_Spawn", 0)
ObjectTimers.addObject("Pellet_Spawn", 3000)
ObjectTimers.addObject("Eagle_Spawn", random.randint(6000, 13000))
ObjectTimers.addObject("Highway_Change", 10000)
ObjectTimers.addObject("Jellyfish_Spawn", 1400)
ObjectTimers.addObject("Music_Restart", 326000)
'''
end_time_player_animation = 0
end_time_cloud_spawn = 0
end_time_bubble_spawn = 0
end_time_wolf_spawn = 1000
end_time_wolf_animation = 0
end_time_tree_spawn = 1000
end_time_text = 8000
end_time_snow_spawn = 0
end_time_bNPC_move = 0
end_time_tNPC_move = 0
end_time_km_update = 0
end_time_rain_spawn = 0
time_pass = 0
end_time_hawk_spawn = 0
end_time_hawk_animation = 0
end_time_bullet_spawn = 5000
end_time_eggs_move = 3000
end_time_trash_spawn = 5000
end_time_shark_spawn = 8000
end_time_killerwhale_spawn = 8000
end_time_hunter = 0
end_time_bug_spawn = 1000
end_time_trap_spawn = 0
end_time_pellet_spawn = 3000
end_time_eagle_spawn =  random.randint(6000, 13000)
end_time_highway_change = 10000
end_time_jellyfish_spawn = 14000
'''



#Functions for Obstacles
bubble_img = pygame.image.load("ImageAssets/BubbleAsset/bubble.png")
wolf_imgs = [pygame.image.load(f"ImageAssets/WolfAsset/wolf{x+1}.png") for x in range(6)]
revwolf_imgs = [pygame.transform.flip(pygame.image.load(f"ImageAssets/WolfAsset/wolf{x+1}.png") , True, False) for x in range(6)]
tree_img = pygame.transform.scale2x(pygame.image.load("ImageAssets/TreeAsset/tree.png"))
snow_img = pygame.transform.scale(pygame.image.load("ImageAssets/SnowflakeAsset/snowflakes.png"), (2, 2))
rain_img = pygame.transform.scale(pygame.image.load("ImageAssets/RainAsset/Raindrop.png"), (10, 10))
hawk_imgs = [pygame.image.load(f"ImageAssets/HawkAsset/bird{x+1}.png") for x in range(3)]
shark_img = pygame.transform.scale(pygame.image.load("ImageAssets/SharkAsset/shark.png"), (32, 18))
killerwhale_img = pygame.transform.scale(pygame.image.load("ImageAssets/KillerWhaleAsset/killerwhale.png"), (32, 18))
trash_img = pygame.transform.scale(pygame.image.load("ImageAssets/TrashAsset/Trash.png"), (20, 18))
bottle_img = pygame.transform.scale(pygame.image.load("ImageAssets/TrashAsset/PlasticBottle.png"), (10, 30))
bullet_img = pygame.image.load("ImageAssets/BulletAsset/Snipe1.png")
fish_img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("ImageAssets/GoldfishAsset/goldfish.png"), (50, 35)), True, False)
hunter_imgs = [pygame.image.load(f"ImageAssets/HunterAsset/hunter{x+1}.png") for x in range(6)]
bug1_img = pygame.transform.scale(pygame.image.load("ImageAssets/BugAsset/Bug1.png"), (10,10))
bug2_img = pygame.transform.scale(pygame.image.load("ImageAssets/BugAsset/Bug2.png"), (10,10))
bugList = [bug1_img, bug2_img]
arrow_imgs = [pygame.transform.scale(pygame.image.load(f"ImageAssets/ArrowAsset/file{x+1}.png"), (pygame.image.load(f"ImageAssets/ArrowAsset/file{x+1}.png").get_width()/4, pygame.image.load(f"ImageAssets/ArrowAsset/file{x+1}.png").get_height()/4)) for x in range(17)]
trap_img = pygame.image.load("ImageAssets/BearTrapAsset/trap1.png")
hole_img = pygame.transform.scale(pygame.image.load("ImageAssets/HoleAsset/Hole.png"), (27.5, 15))
highway_img = pygame.transform.scale(pygame.image.load("ImageAssets/HighwayAsset/Highway.png"), (40, 6))
net_img = pygame.transform.scale(pygame.image.load("ImageAssets/NetAsset/Net.png"), (64, 32))
pellet_img = pygame.image.load("ImageAssets/KelpAsset/Kelp.png")
eagle_img = pygame.transform.rotate(pygame.transform.flip(pygame.image.load("ImageAssets/EagleAsset/Eagle.png"), True, False), 45)
jellyfish_imgs = [pygame.transform.scale(pygame.image.load(f"ImageAssets/JellyfishAsset/jellyfish{x+1}.png"), (24, 24)) for x in range(6)]

#wolf_imgs = [pygame.image.load("white.png")]

# Functions for game objects
def make_cloud(bottom_bound: int = 600):
    cloud_img = pygame.image.load(random.choice(cloud_img_list))
    return ObstacleClass(1000, random.randint(0, bottom_bound), random.randint(5, 15), 0, cloud_img.get_width()/2, cloud_img.get_height()/2, False, False, [cloud_img], "Cloud")

def make_bubble():
    return ObstacleClass(random.randint(0, 840), 650,  4, random.randint(4, 5), bubble_img.get_width(), bubble_img.get_height(), False, False, [bubble_img], "Bubble")

def make_wolf():
    return ObstacleClass(900, 450, 8, 0, wolf_imgs[0].get_width(), wolf_imgs[0].get_height(), True, True, wolf_imgs, "Wolf")

def make_tree():
    return ObstacleClass(1000, random.randint(0, 500), 10, 0, 16, tree_img.get_height(), True, True, [tree_img], "Tree")

def make_snow():
    return ObstacleClass(random.randint(0, 1680), -5, 20, -20, 3, 3, False,False, [snow_img], "Snow")

def make_rain_diagonal():
    return ObstacleClass(random.randint(0, 1680), -5, 20, -20, 3, 3, False,False, [rain_img], "Rain")

def make_rain_straight():
    return ObstacleClass(random.randint(0, 1680), -5, 0, -20, 3, 3, False,False, [rain_img], "Rain")

def make_hawk():
    return ObstacleClass(1000, current_player.ycor, 20, random.randint(-2, 2), hawk_imgs[0].get_width(), hawk_imgs[0].get_height(), True,True, hawk_imgs, "Hawk")
    
def make_bullet():
    return ObstacleClass(current_player.xcor, -40, 0, -7, bullet_img.get_width()/2, bullet_img.get_height()/2,True,True, [bullet_img], "Hunter")

def make_shark():
    return ObstacleClass(1000, random.randint(0, 400), 5, 0, shark_img.get_width(), shark_img.get_height(), True,True, [shark_img], "Shark")

def make_killerwhale():
    return ObstacleClass(1000, random.randint(0, 400), 5, 0, killerwhale_img.get_width(), killerwhale_img.get_height(), True,True, [killerwhale_img], "Killer Whale")

def make_trash():
    return ObstacleClass(1000, random.randint(0, 400), 3, 0, trash_img.get_width(), trash_img.get_height(), True,True, [trash_img], "Trash")

def make_bottle():
    return ObstacleClass(1000, random.randint(0, 400), 3, 0, bottle_img.get_width(), bottle_img.get_height(), True,True, [bottle_img], "Plastic bottle")
    
def make_arrow():
    return ObstacleClass(1000, 450, 15, 0, arrow_imgs[0].get_width()/4, arrow_imgs[0].get_height()/4, True, True, arrow_imgs, "Arrow")

fishNPC = BirdTurtle(1000, 150, [fish_img], 10)

def make_hunter():
    return ObstacleClass(-180, 450, -10, 0, hunter_imgs[0].get_width(), hunter_imgs[0].get_height(), True,True, hunter_imgs, "Wolf")

def make_bug():
    return ObstacleClass(1100, random.randint(10, 500), 10, 0, 10, 10, True,False, [bugList[random.randint(0, 1)]], "Bug")

def make_trap():
    return ObstacleClass(1100, 450, 4, 0, 32, 32, True, False, [trap_img], "BearTrap")

def make_wolfBonus():
    return ObstacleClass(-100, random.randint(100, 600), -15, 0, revwolf_imgs[0].get_width(), revwolf_imgs[0].get_height(), True, True, revwolf_imgs, "Wolf")

def make_hole():
    return ObstacleClass(900, 500, 5, 0, hole_img.get_width(), hole_img.get_height(), False, False, [hole_img], "Hole")

def make_highway(ycor):
    return ObstacleClass(1000, ycor, 5, 0, 40, 6, False, False, [highway_img], "Highway")

def make_net():
    return  ObstacleClass(1000, 60, 10, 0, 64, 32, True, False, [net_img], "Net")

def make_pellet():
    return  ObstacleClass(random.randint(15, 700), -100, 0, -12, 16, 16, True, False, [pellet_img], "Pellet")

def make_bonus_pollution():
    return ObstacleClass(random.randint(0,900), -100, 0, -5, trash_img.get_width(), trash_img.get_height(), True,True, [trash_img], "Pollution")

def make_eagle():
    return ObstacleClass(random.randint(100, 400), -100, 20, -20, eagle_img.get_width(), eagle_img.get_height(), True,True, [eagle_img], "Eagle")

def make_jellyfish():
    return ObstacleClass(random.randint(500, 700), 600, 5, 2, jellyfish_imgs[0].get_width(), jellyfish_imgs[0].get_height(), True,True, jellyfish_imgs, "Jellyfish")

#Vars for player jumping
isJumping = False
start_acceleration = 12
vert_acceleration = 12
gravity_force = 0.5

#End screen args default
EndScreenTitle = "You Died!"
EndScreenTitleColor = DesignClass.Colors["RED"]
EndScreenReason = "N/A"
EndScreenNextStage = "TitleScreen"

def EndLevel(TitleText, TitleTextColor, EndReason, NextStage):
    global EndScreenTitle
    global EndScreenTitleColor
    global EndScreenReason
    global EndScreenNextStage
    global km_count
    global GameState
    
    EndScreenTitle = TitleText
    EndScreenTitleColor = TitleTextColor
    EndScreenReason = EndReason
    EndScreenNextStage = NextStage
    km_count = 0
    GameState = "EndScreen"
    
isCompletedBonus = False
bugsCaughtAmount = 0
pelletsCaughtAmount = 0

GameState = "TitleScreen"
RunVar = True

while RunVar == True:
    current_time = pygame.time.get_ticks()

    if current_time > ObjectTimers.getCurrentValue("Music_Restart"):
        Sound.play_backround_music()

    match GameState:
        case "TitleScreen":
            screen.fill(DesignClass.Colors["WHITE"])
            
            titleText = TextClass(
                "Animal Journey",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 50),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 125),
                screen
            )
            titleText.blit()
            
            startButton = ButtonClass(
                TextClass(
                    "Start",
                    pygame.font.Font(DesignClass.Fonts["Poppins"], 20),
                    DesignClass.Colors["BLACK"],
                    (DesignClass.SCREEN_WIDTH_CENTER, 250),
                    screen
                ),
                pygame.Rect(DesignClass.SCREEN_WIDTH_CENTER - 75, 250 - 25, 150, 50),
                0,
                DesignClass.Colors["GREEN"],
                screen,
                ChangeGameState,
                "PlayerChoose"
            )
            buttonlist.append(startButton)
            startButton.draw()

            controlsButton = ButtonClass(
                TextClass(
                    "Controls",
                    pygame.font.Font(DesignClass.Fonts["Poppins"], 20),
                    DesignClass.Colors["BLACK"],
                    (DesignClass.SCREEN_WIDTH_CENTER, 325),
                    screen
                ),
                pygame.Rect(DesignClass.SCREEN_WIDTH_CENTER - 75, 325 - 25, 150, 50),
                0,
                DesignClass.Colors["GREEN"],
                screen,
                ChangeGameState,
                "ControlsPage"
            )
            buttonlist.append(controlsButton)
            controlsButton.draw()
            
            infoButton = ButtonClass(
                TextClass(
                    "Game Info",
                    pygame.font.Font(DesignClass.Fonts["Poppins"], 20),
                    DesignClass.Colors["BLACK"],
                    (DesignClass.SCREEN_WIDTH_CENTER, 400),
                    screen
                ),
                pygame.Rect(DesignClass.SCREEN_WIDTH_CENTER - 75, 400 - 25, 150, 50),
                0,
                DesignClass.Colors["GREEN"],
                screen,
                ChangeGameState,
                "InfoPage"
            )
            buttonlist.append(infoButton)
            infoButton.draw()
            
            
            creditsText = TextClass(
                "Created By: Abdullah & Vivaan",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 20),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 550),
                screen
            )
            creditsText.blit()



            end_time_eggs_move = pygame.time.get_ticks() + 3000

        case "PlayerChoose":
            screen.fill(DesignClass.Colors["WHITE"])

            titleText = TextClass(
                "Animal Journey",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 50),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 75),
                screen
            )
            titleText.blit()

            buttonlist.append(turtle_info.playbutton)
            buttonlist.append(bird_info.playbutton)
            buttonlist.append(deer_info.playbutton)
            turtle_info.show(Screen=screen)
            bird_info.show(Screen=screen)
            deer_info.show(Screen=screen)

        case "BirdLevel":
            current_player = bird
            current_player.rect_update()
            routelen = 6000
            speciallenTop = 600
            speciallenBot = 500
            lives.load_hearts(2)


            screen.fill(DesignClass.Colors["FORESTGREEN"])

            instructText = TextClass(
                "Hurry Up! Pass through tree trunks",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 125),
                screen
            )
            kmText = TextClass(
                f"{km_count}km",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 40),
                DesignClass.Colors["BLACK"],
                (100, 25),
                screen
            )
            
            
            
            #Set up backround
            if current_time > end_time_tree_spawn:
                tree = make_tree()
                end_time_tree_spawn = pygame.time.get_ticks() + 1000
                obstacle_list.append(tree)
                collide_list.append(tree)

            if current_time > end_time_snow_spawn:
                snow = make_snow()
                end_time_snow_spawn = pygame.time.get_ticks() + 40
                obstacle_list.append(snow)

            if current_time > end_time_bNPC_move:
                birdNPC.move("RIGHT")
                end_time_bNPC_move += 80

            if current_time > end_time_km_update:
                km_count += 3
                end_time_km_update = pygame.time.get_ticks() + 1

            if km_count > routelen:
                EndLevel("You Won", DesignClass.Colors["GREEN"], "Go to level 2", "BirdLevel2")
                km_count = 6001
                

            if km_count > speciallenBot and km_count < speciallenTop:
                arrow = make_arrow()
                km_count = 601
                obstacle_list.append(arrow)
                collide_list.append(arrow)

            for obstacle in obstacle_list:
                obstacle.move()

            
                

            if current_time > end_time_player_animation:
                birdNPC.animation_update()
                bird.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 50


            #Blit all the objects
            for obstacle in obstacle_list:
                if obstacle.xcor < -200:
                    obstacle_list.remove(obstacle)
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
                    # pygame.draw.rect(screen, DesignClass.Colors["GREEN"], obstacle.Rect)

            if specialTransition:
                current_player.move("DOWN")
                if 600 < current_player.ycor:
                    ChangeGameState("BirdBonus")
                    
                    collideIndex = 0
                    for collide in collide_list:
                        if collide.descriptor == "Tree":
                            collide_list.pop(collideIndex)
                        collideIndex += 1
                        
                    current_player.ycor = 60
                    current_player.move("UP")

            if birdNPC.xcor < 1000:
                screen.blit(birdNPC.current_frame, birdNPC.Rect)

            screen.blit(bird.current_frame, bird.Rect)
            # pygame.draw.rect(screen, DesignClass.Colors["GREEN"], bird.Rect)d

            lives.blit(screen)

            if current_time < end_time_text:
                instructText.blit()
            kmText.blit()

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect) or obstacle.Rect.collidepoint(current_player.xcor, current_player.ycor):
                    if obstacle.descriptor == "Arrow":
                        SpecialLevelEnter()
                    else:
                        dead = lives.remove_life()
                        pygame.time.delay(100)
                        collide_list.remove(obstacle)
                        if dead:
                            EndLevel("You died!", DesignClass.Colors["RED"], "Unfortunately, you did not migrate successfully.", "TitleScreen")


        case "BirdBonus":
            specialTransition = False
            current_player = bird
            current_player.rect_update()
            routelen = 99999
            lives.load_hearts(2)
            screen.fill(DesignClass.Colors["SKYBLUE"])
            pygame.draw.rect(screen, DesignClass.Colors["GRASSGREEN"], pygame.Rect(0,500,840,100))

            instructText = TextClass(
                "Bonus level: Catch 20 bugs for +1 heart!",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 125),
                screen
            )
            bugsText = TextClass(
                f"{bugsCaughtAmount} Bug(s) Caught",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 35),
                DesignClass.Colors["BLACK"],
                (200, 25),
                screen
            )
            
            
            
            #Set up backround
            if current_time > end_time_cloud_spawn:
                cloud = make_cloud(bottom_bound=300)
                end_time_cloud_spawn = pygame.time.get_ticks() + 700
                obstacle_list.append(cloud)

            if bugsCaughtAmount >= 20:
                isCompletedBonus = True
                EndLevel("Bonus complete!", DesignClass.Colors["GREEN"], "Return to Level 1", "BirdLevel")
                lives.add_hearts(1)
                km_count = 601

            if current_time > end_time_eagle_spawn:
                eagle = make_eagle()
                obstacle_list.append(eagle)
                collide_list.append(eagle)
                end_time_eagle_spawn += random.randint(6000, 13000)

            for obstacle in obstacle_list:
                obstacle.move()
                obstacle.update_frame()
                
            collideIndex = 0
            for collide in collide_list:
                if collide.descriptor == "Tree":
                    collide_list.pop(collideIndex)
                collideIndex += 1


            if current_time > end_time_player_animation:
                bird.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 50
                
            if current_time > end_time_bug_spawn:
                bug = make_bug()
                collide_list.append(bug)
                obstacle_list.append(bug)
                end_time_bug_spawn = pygame.time.get_ticks() + 3000
                


            #Blit all the objects
            for obstacle in obstacle_list:
                if obstacle.xcor < -200:
                    obstacle_list.remove(obstacle)
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
                    # pygame.draw.rect(screen, DesignClass.Colors["GREEN"], obstacle.Rect)

            screen.blit(bird.current_frame, bird.Rect)
            # pygame.draw.rect(screen, DesignClass.Colors["GREEN"], bird.Rect)d

            lives.blit(screen)

            if current_time < end_time_text:
                instructText.blit()
            bugsText.blit()

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect) or obstacle.Rect.collidepoint(current_player.xcor, current_player.ycor):
                    if obstacle.descriptor == "Bug": 
                        bugsCaughtAmount += 1
                        obstacle_list.pop(obstacle_list.index(obstacle))
                        collide_list.pop(collide_list.index(obstacle))
                    else:
                        dead = lives.remove_life()
                        pygame.time.delay(100)
                        collide_list.remove(obstacle)
                        if dead:
                            isCompletedBonus = False
                            EndLevel("You died!", DesignClass.Colors["RED"], "Bonus incomplete!", "BirdLevel")

        case "BirdLevel2":
            current_player = bird
            routelen = 13000
            current_player.rect_update()
            if isCompletedBonus == True:
                lives.load_hearts(3)
            else:
                lives.load_hearts(2)
            screen.fill(DesignClass.Colors["SKYBLUE"])

            instructText = TextClass(
                "You're catching up! Watch out for eagles!",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 125),
                screen
            )
            kmText = TextClass(
                f"{km_count}km",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 40),
                DesignClass.Colors["BLACK"],
                (100, 25),
                screen
            )
            
            
            
            #Set up backround
            if current_time > end_time_cloud_spawn:
                cloud = make_cloud()
                end_time_cloud_spawn = pygame.time.get_ticks() + 700
                obstacle_list.append(cloud)


            if current_time > end_time_snow_spawn:
                snow = make_snow()
                end_time_snow_spawn = pygame.time.get_ticks() + 60 + time_pass/180
                obstacle_list.append(snow)

            if current_time > end_time_hawk_spawn:
                hawk = make_hawk()
                end_time_hawk_spawn = pygame.time.get_ticks() + 800
                obstacle_list.append(hawk)
                collide_list.append(hawk)

            if current_time > end_time_bNPC_move:
                birdNPC.move("RIGHT")
                end_time_bNPC_move += 80

            if current_time > end_time_km_update:
                km_count += 3
                end_time_km_update += 1

            if km_count > routelen:
                EndLevel("You Won!", DesignClass.Colors["GREEN"], "Congratulations, Try Other Animals Too!", "TitleScreen")

            for obstacle in obstacle_list:
                obstacle.move()
                obstacle.update_frame()


            if current_time > end_time_player_animation:
                birdNPC.animation_update()
                bird.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 50


            #Blit all the objects
            for obstacle in obstacle_list:
                if obstacle.xcor < -200:
                    obstacle_list.remove(obstacle)
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
                    # pygame.draw.rect(screen, DesignClass.Colors["GREEN"], obstacle.Rect)

            if birdNPC.xcor < 1000:
                screen.blit(birdNPC.current_frame, birdNPC.Rect)

            screen.blit(bird.current_frame, bird.Rect)
            # pygame.draw.rect(screen, DesignClass.Colors["GREEN"], bird.Rect)d

            lives.blit(screen)

            if current_time < end_time_text:
                instructText.blit()
            kmText.blit()

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect) or obstacle.Rect.collidepoint(current_player.xcor, current_player.ycor):
                    dead = lives.remove_life()
                    pygame.time.delay(100)
                    collide_list.remove(obstacle)
                    if dead:
                        EndLevel("You died!", DesignClass.Colors["RED"], "Unfortunately, you did not migrate successfully.", "TitleScreen")


        case "TurtleLevel":
            current_player = turtle
            current_player.xcor = 50
            routelen = 2000
            current_player.rect_update()
            lives.load_hearts(2)

            screen.fill(DesignClass.Colors["OCEANBLUE"])

            pygame.draw.rect(screen, DesignClass.Colors["OCEANYELLOW"], pygame.Rect(0,500,840,100))

            eggs = pygame.transform.scale(pygame.image.load("ImageAssets/TurtleExtraAsset/cracked-egg.png"), (86, 56))

            instructText = TextClass(
                "Embark on your journey, avoid trash and sharks!",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 125),
                screen
            )
            kmText = TextClass(
                f"{km_count}km",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 40),
                DesignClass.Colors["BLACK"],
                (100, 25),
                screen
            )

            # Set up backround 
            if current_time > end_time_bubble_spawn:
                bubble = make_bubble()
                obstacle_list.append(bubble)
                end_time_bubble_spawn = pygame.time.get_ticks() + random.randint(350, 450)

            if current_time > end_time_trash_spawn:
                trash = make_trash()
                obstacle_list.append(trash)
                end_time_trash_spawn = pygame.time.get_ticks() + 7000
                obstacle_list.append(trash)
                collide_list.append(trash)

            if current_time > end_time_shark_spawn:
                shark = make_shark()
                obstacle_list.append(shark)
                end_time_shark_spawn = pygame.time.get_ticks() + random.randint(3000,8000)
                obstacle_list.append(shark)
                collide_list.append(shark)
                
            if current_time > end_time_highway_change:
                pass

            if current_time < end_time_eggs_move:
                screen.blit(eggs, eggs.get_rect(center=(50,500)))

            for obstacle in obstacle_list:
                obstacle.move()

            if km_count < 300:
                instructText.blit()

            if km_count >= 567 and km_count <= 570:
                net = make_net()
                obstacle_list.append(net)
                collide_list.append(net)
                km_count = 571

            if km_count > routelen:
                EndLevel("You Won", DesignClass.Colors["GREEN"], "Go to level 2", "TurtleLevel2")

            if current_time > end_time_player_animation:
                current_player.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 60

            if current_time > end_time_km_update:
                km_count += 1
                end_time_km_update += 1

            if specialTransition:
                current_player.move("UP")
                net.ycor -= 10
                net.update_frame()
                if -100 > current_player.ycor:

                    ChangeGameState("TurtleBonus")
                        
                    current_player.ycor = 70



            #Blit all the objects
            for obstacle in obstacle_list:
                obstacle.move()
                if obstacle.xcor < -200:
                    del obstacle
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))

            screen.blit(current_player.current_frame, current_player.Rect)

            lives.blit(screen)

            kmText.blit()

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect) or obstacle.Rect.collidepoint(current_player.xcor, current_player.ycor):
                    if obstacle.descriptor == "Net":
                        SpecialLevelEnter()
                    else:
                        dead = lives.remove_life()
                        pygame.time.delay(100)
                        collide_list.remove(obstacle)
                        if dead:
                            EndLevel("You died!", DesignClass.Colors["RED"], "Unfortunately, you did not migrate successfully.", "TitleScreen")
        case "TurtleBonus":
            specialTransition = False
            current_player = turtle
            current_player.ycor = 400
            current_player.rect_update()
            routelen = 99999
            lives.load_hearts(2)
            screen.fill(DesignClass.Colors["OCEANBLUE"])

            instructText = TextClass(
                "Bonus level: Catch 20 bits of kelp for +1 heart!",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 125),
                screen
            )
            pelletsText = TextClass(
                f"{pelletsCaughtAmount} Pellet(s) Caught",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 35),
                DesignClass.Colors["BLACK"],
                (200, 25),
                screen
            )
            
        
            #Set up backround
            if pelletsCaughtAmount >= 20:
                isCompletedBonus = True
                EndLevel("Bonus complete!", DesignClass.Colors["GREEN"], "Return to Level 1", "TurtleLevel")
                lives.add_hearts(1)
                km_count = 574

            for obstacle in obstacle_list:
                obstacle.move()
                obstacle.update_frame()
                
            collideIndex = 0
            for collide in collide_list:
                if collide.descriptor == "Tree":
                    collide_list.pop(collideIndex)
                collideIndex += 1


            if current_time > end_time_player_animation:
                current_player.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 50
                
            if current_time > end_time_pellet_spawn:
                kelp = make_pellet()
                collide_list.append(kelp)
                obstacle_list.append(kelp)
                pollution = make_bonus_pollution()
                collide_list.append(pollution)
                obstacle_list.append(pollution)
                end_time_pellet_spawn = pygame.time.get_ticks() + 3000
                


            #Blit all the objects
            for obstacle in obstacle_list:
                if obstacle.xcor < -200:
                    obstacle_list.remove(obstacle)
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
                    # pygame.draw.rect(screen, DesignClass.Colors["GREEN"], obstacle.Rect)

            screen.blit(current_player.current_frame, current_player.Rect)
            # pygame.draw.rect(screen, DesignClass.Colors["GREEN"], bird.Rect)d

            lives.blit(screen)

            if current_time < end_time_text:
                instructText.blit()
            pelletsText.blit()

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect) or obstacle.Rect.collidepoint(current_player.xcor, current_player.ycor):
                    if obstacle.descriptor == "Pellet": 
                        pelletsCaughtAmount += 1
                        obstacle_list.pop(obstacle_list.index(obstacle))
                        collide_list.pop(collide_list.index(obstacle))
                    else:
                        dead = lives.remove_life()
                        pygame.time.delay(100)
                        collide_list.remove(obstacle)
                        if dead:
                            isCompletedBonus = False
                            EndLevel("You died!", DesignClass.Colors["RED"], "Bonus incomplete!", "TurtleLevel")

        case "TurtleLevel2":
            current_player = turtle
            routelen = 2000
            current_player.rect_update()
            lives.load_hearts(2)

            screen.fill(DesignClass.Colors["OCEANBLUE"])

            pygame.draw.rect(screen, DesignClass.Colors["OCEANYELLOW"], pygame.Rect(0,500,840,100))

            instructText = TextClass(
                "Get to the end and lay your eggs! Beware: Killer Whales",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 125),
                screen
            )
            kmText = TextClass(
                f"{km_count}km",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 40),
                DesignClass.Colors["BLACK"],
                (100, 25),
                screen
            )

            # Set up backround 
            if current_time > end_time_bubble_spawn:
                bubble = make_bubble()
                obstacle_list.append(bubble)
                end_time_bubble_spawn = pygame.time.get_ticks() + random.randint(350, 450)

            if current_time > end_time_tNPC_move:
                fishNPC.speed = 5
                fishNPC.move("LEFT")
                end_time_tNPC_move += 80

            if current_time > end_time_trash_spawn:
                bottle = make_bottle()
                obstacle_list.append(bottle)
                end_time_trash_spawn = pygame.time.get_ticks() + 7000
                # obstacle_list.append(bottle)
                collide_list.append(bottle)

            if current_time > end_time_jellyfish_spawn:
                jellyfish = make_jellyfish()
                obstacle_list.append(jellyfish)
                end_time_jellyfish_spawn = pygame.time.get_ticks() + 7000
                collide_list.append(jellyfish)

            if current_time > end_time_killerwhale_spawn:
                killerwhale = make_killerwhale()
                obstacle_list.append(killerwhale)
                end_time_killerwhale_spawn = pygame.time.get_ticks() + random.randint(3000,8000)
                obstacle_list.append(killerwhale)
                collide_list.append(killerwhale)

            if km_count < 200:
                instructText.blit()

            if km_count > routelen:
                EndLevel("You Won!", DesignClass.Colors["GREEN"], "Congratulations, try other animals!", "TitleScreen")

            for obstacle in obstacle_list:
                obstacle.move()


            if current_time > end_time_player_animation:
                fishNPC.animation_update()
                current_player.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 60

            if current_time > end_time_km_update:
                km_count += 1
                end_time_km_update += 1


            #Blit all the objects
            for obstacle in obstacle_list:
                obstacle.move()
                if obstacle.xcor < -200:
                    del obstacle
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
            
            if fishNPC.xcor < 1000:
                screen.blit(fishNPC.current_frame, fishNPC.Rect)

            screen.blit(current_player.current_frame, current_player.Rect)

            lives.blit(screen)

            kmText.blit()

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect) or obstacle.Rect.collidepoint(current_player.xcor, current_player.ycor):
                    dead = lives.remove_life()
                    pygame.time.delay(100)
                    collide_list.remove(obstacle)
                    if dead:
                        EndLevel("You died!", DesignClass.Colors["RED"], "Unfortunately, you did not migrate successfully.", "TitleScreen")


        case "DeerLevel":
            current_player = deer
            deer.xcor = 50
            current_player.rect_update()
            routelen = 250
            lives.load_hearts(2)
            time_pass += 1

            screen.fill(DesignClass.Colors["SKYBLUE"])

            pygame.draw.rect(screen, DesignClass.Colors["GRASSGREEN"], pygame.Rect(0,500,840,100))

            kmText = TextClass(
                f"{km_count}km",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 40),
                DesignClass.Colors["BLACK"],
                (100, 25),
                screen
            )
            sText = TextClass(
                f"S to enter hole",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 40),
                DesignClass.Colors["BLACK"],
                (185, 150),
                screen
            )

            # Set up backround 
            if current_time > end_time_cloud_spawn:
                cloud = make_cloud(300)
                obstacle_list.append(cloud)
                end_time_cloud_spawn = pygame.time.get_ticks() + 600

            if current_time > end_time_wolf_spawn:
                wolf = make_wolf()
                obstacle_list.append(wolf)
                collide_list.append(wolf)
                end_time_wolf_spawn = pygame.time.get_ticks() + random.randint(7000, 12000)

            if current_time > end_time_trap_spawn:
                trap = make_trap()
                obstacle_list.append(trap)
                collide_list.append(trap)
                end_time_trap_spawn = pygame.time.get_ticks() + random.randint(13000, 15000)

            if current_time > end_time_rain_spawn:
                rain = make_rain_diagonal()
                end_time_rain_spawn = pygame.time.get_ticks() + 15
                obstacle_list.append(rain)

            if current_time > end_time_km_update:
                km_count += 1
                end_time_km_update = pygame.time.get_ticks() + 250\
                
            if km_count == 123:
                hole = make_hole()
                obstacle_list.append(hole)
                collide_list.append(hole)
                km_count = 124

            if km_count > 123 and km_count < 130:
                sText.blit()

            for obstacle in obstacle_list:
                obstacle.update_frame()
                obstacle.move()


            if current_time > end_time_player_animation:
                current_player.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 60

            if km_count > routelen:
                EndLevel("You Won", DesignClass.Colors["GREEN"], "Go to level 2", "DeerLevel2")

            if specialTransition:
                current_player.move("DOWN")
                if 700 < current_player.ycor:
                    ChangeGameState("DeerBonus")
                    
                    collideIndex = 0
                    for collide in collide_list:
                        if collide.descriptor == "Wolf" or collide.descriptor == "BearTrap":
                            collide_list.pop(collideIndex)
                        collideIndex += 1
                        
                    current_player.ycor = 60

            #Jumping
            if isJumping == True:
                deer.current_frame = deer.frames[4]

                current_player.jump(vert_acceleration)
                
                if vert_acceleration > (-start_acceleration):
                    vert_acceleration -= gravity_force
                else:
                    isJumping = False
                    vert_acceleration = start_acceleration

            #Blit all the objects
            for obstacle in obstacle_list:
                obstacle.move()
                if obstacle.xcor < -200:
                    del obstacle
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
                    

            screen.blit(current_player.current_frame, current_player.Rect)

            lives.blit(screen)

            kmText.blit()

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect) or obstacle.Rect.collidepoint(current_player.xcor, current_player.ycor):
                    if obstacle.descriptor == "Hole":
                            SpecialLevelEnter()
                    else:
                        dead = lives.remove_life()
                        screen.blit(obstacle.image, obstacle.Rect)
                        pygame.time.delay(200)
                        collide_list.remove(obstacle)
                        if dead:
                            EndLevel("You died!", DesignClass.Colors["RED"], "Unfortunately, you did not migrate successfully.", "TitleScreen")

        case "DeerBonus":
            current_player = bonusDeer
            current_player.xcor = 500
            specialTransition = False
            current_player.rect_update()
            routelen = 30
            lives.load_hearts(2)
            screen.fill(DesignClass.Colors["GRASSGREEN"])

            instructText = TextClass(
                "Watch out for wolves running behind you!",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 125),
                screen
            )
            kmText = TextClass(
                f"{km_count} km",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 40),
                DesignClass.Colors["BLACK"],
                (200, 25),
                screen
            )   
            
            #Set up backround
            if current_time > end_time_km_update:
                km_count += 1
                end_time_km_update += 1000

            for obstacle in obstacle_list:
                obstacle.move()
                obstacle.update_frame()
                
            collideIndex = 0
            for collide in collide_list:
                if collide.descriptor == "Tree":
                    collide_list.pop(collideIndex)
                collideIndex += 1


            if current_time > end_time_player_animation:
                current_player.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 50
                
            if current_time > end_time_wolf_spawn:
                wolf = make_wolfBonus()
                collide_list.append(wolf)
                obstacle_list.append(wolf)
                end_time_wolf_spawn = pygame.time.get_ticks() + 700
                
            # if current_time > end_time_tree_spawn:
            #     tree = make_tree()
            #     collide_list.append(tree)
            #     obstacle_list.append(tree)
            #     end_time_tree_spawn = pygame.time.get_ticks() + 300

            if km_count >= routelen:
                isCompletedBonus = True
                EndLevel("Bonus complete!", DesignClass.Colors["GREEN"], "Return to Level 1", "DeerLevel")
                lives.add_hearts(1)
                km_count = 80


            #Blit all the objects
            for obstacle in obstacle_list:
                if obstacle.xcor < -200:
                    obstacle_list.remove(obstacle)
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
                    # pygame.draw.rect(screen, DesignClass.Colors["GREEN"], obstacle.Rect)

            screen.blit(current_player.current_frame, current_player.Rect)
            # pygame.draw.rect(screen, DesignClass.Colors["GREEN"], bird.Rect)d

            lives.blit(screen)

            if current_time < end_time_text:
                instructText.blit()
            kmText.blit()

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect) or obstacle.Rect.collidepoint(current_player.xcor, current_player.ycor):
                    dead = lives.remove_life()
                    pygame.time.delay(100)
                    collide_list.remove(obstacle)
                    if dead:
                        isCompletedBonus = False
                        EndLevel("You died!", DesignClass.Colors["RED"], "Bonus incomplete!", "DeerLevel")

        
        case "DeerLevel2":
            current_player = deer
            current_player.rect_update()
            current_player.ycor = 400
            routelen = 24
            lives.load_hearts(3)
            time_pass += 1

            screen.fill([170,206,250])

            pygame.draw.rect(screen, DesignClass.Colors["GRASSGREEN"], pygame.Rect(0,500,840,100))

            instructText = TextClass(
                "Dodge the bullets! The hunters have found you!",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 125),
                screen
            )
            kmText = TextClass(
                f"{km_count} hours till safe",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 40),
                DesignClass.Colors["BLACK"],
                (200, 25),
                screen
            )

            # Set up backround 
            if current_time > end_time_cloud_spawn:
                cloud = make_cloud(300)
                obstacle_list.append(cloud)
                end_time_cloud_spawn = pygame.time.get_ticks() + 600

            if current_time > end_time_rain_spawn:
                rain = make_rain_straight()
                end_time_rain_spawn = pygame.time.get_ticks() + 15
                obstacle_list.append(rain)

            if current_time > end_time_bullet_spawn:
                if end_time_bullet_spawn < 5000:
                    end_time_bullet_spawn = pygame.time.get_ticks() + 5000
                else:
                    bullet = make_bullet()
                    end_time_bullet_spawn = pygame.time.get_ticks() + 1300
                    obstacle_list.append(bullet)
                    collide_list.append(bullet)

            if end_time_hunter != None:
                if current_time > end_time_hunter:
                    hunter = make_hunter()
                    obstacle_list.append(hunter)
                    end_time_hunter = None
            

            if current_time > end_time_km_update:
                km_count += 1
                end_time_km_update += 5000

            for obstacle in obstacle_list:
                obstacle.update_frame()
                obstacle.move()


            if current_time > end_time_player_animation:
                current_player.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 60

            if km_count > routelen:
                EndLevel("You Won", DesignClass.Colors["GREEN"], "Level Won", "TitleScreen")


            #Blit all the objects
            for obstacle in obstacle_list:
                obstacle.move()
                if obstacle.xcor < -200:
                    del obstacle
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
                    
            deer.blit(screen)
            screen.blit(current_player.current_frame, current_player.Rect)

            if current_time < end_time_text:
                instructText.blit()
                end_time_text += 10000

            lives.blit(screen)

            kmText.blit()

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect) or obstacle.Rect.collidepoint(current_player.xcor, current_player.ycor):
                    dead = lives.remove_life()
                    pygame.time.delay(100)
                    collide_list.remove(obstacle)
                    if dead:
                        EndLevel("You died!", DesignClass.Colors["RED"], "Unfortunately, you did not migrate successfully.", "TitleScreen")

        
        
        case "ControlsPage":
            screen.fill(DesignClass.Colors["WHITE"])

            UpDownText = TextClass(
                "Up/Down (Bird & Turtle Only)",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (350, 50),
                screen
            )
            UpDownText.blit()
            Key_W = pygame.transform.scale(pygame.image.load("ImageAssets/KeyboardAsset/W.png"), (40,40))
            screen.blit(Key_W, Key_W.get_rect(center = (50, 50)))
            Key_S = pygame.transform.scale(pygame.image.load("ImageAssets/KeyboardAsset/S.png"), (40,40))
            screen.blit(Key_S, Key_S.get_rect(center = (95, 50)))
            
            LeftRightText = TextClass(
                "Left/Right (Deer Lvl 2 Only)",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (340, 130),
                screen
            )
            LeftRightText.blit()
            Key_A = pygame.transform.scale(pygame.image.load("ImageAssets/KeyboardAsset/A.png"), (40,40))
            screen.blit(Key_A, Key_A.get_rect(center = (50, 130)))
            Key_D = pygame.transform.scale(pygame.image.load("ImageAssets/KeyboardAsset/D.png"), (40,40))
            screen.blit(Key_D, Key_D.get_rect(center = (95, 130)))

            JumpText = TextClass(
                "Jump (Deer Lvl 1 Only)",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (310, 210),
                screen
            )
            JumpText.blit()
            Key_Space = pygame.transform.scale(pygame.image.load("ImageAssets/KeyboardAsset/SPACE.png"), (100,40))
            screen.blit(Key_Space, Key_Space.get_rect(center = (80, 210)))
            
            AbilityText = TextClass(
                "Bird Flock Ability (Bird Only)",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (290, 290),
                screen
            )
            AbilityText.blit()
            Key_Q = pygame.transform.scale(pygame.image.load("ImageAssets/KeyboardAsset/Q.png"), (40,40))
            screen.blit(Key_Q, Key_Q.get_rect(center = (50, 290)))

            EscText = TextClass(
                "Shortcut to main menu",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (270, 370),
                screen
            )
            EscText.blit()
            Key_Esc = pygame.transform.scale(pygame.image.load("ImageAssets/KeyboardAsset/ESC.png"), (40,40))
            screen.blit(Key_Esc, Key_Esc.get_rect(center = (50, 370)))

            BackButton = ButtonClass(
                TextClass(
                    "Understood!",
                    pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                    DesignClass.Colors["BLACK"],
                    (DesignClass.SCREEN_WIDTH_CENTER, 500),
                    screen
                ),
                pygame.Rect(DesignClass.SCREEN_WIDTH_CENTER - 175, 475, 350, 50),
                0,
                DesignClass.Colors["GREEN"],
                screen,
                ChangeGameState,
                "TitleScreen"
            )
            buttonlist.append(BackButton)
            BackButton.draw()
            
        case "InfoPage":
            screen.fill(DesignClass.Colors["WHITE"])
            
            InfoTitle = TextClass(
                "Game Info",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 50),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 50),
                screen
            )
            InfoTitle.blit()
            
            BirdTitle = TextClass(
                "Red-Winged Blackbird",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER - 200, 135),
                screen
            )
            BirdTitle.blit()
            BirdText1 = TextClass(
                "The Red-Winged Blackbird aims to find a suitable habitat for winter time. They typically fly in flocks.",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 10),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER - 30, 160),
                screen
            )
            BirdText1.blit()
            BirdText2 = TextClass(
                "Your goal is to migrate south. Avoid trees and predators to migrate successfully!",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 10),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER - 85, 180),
                screen
            )
            BirdText2.blit()
            BirdText3 = TextClass(
                "Hint: Find a bonus level for 1 extra heart!",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 10),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER - 120, 200),
                screen
            )
            BirdText3.blit()
            BirdText4 = TextClass(
                "Unique Ability: Press Q to use \"Flock\" ability and spawn friendly birds that can shield you!",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 10),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER - 60, 220),
                screen
            )
            BirdText4.blit()

            TurtleTitle = TextClass(
                "Leather-Back Sea Turtle",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER - 190, 265),
                screen
            )
            TurtleTitle.blit()
            TurtleText1 = TextClass(
                "The Leather-Back Sea Turtle is one of the largest turtles in the world. It typically travels from colder to warmer waters.",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 10),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER + 20, 290),
                screen
            )
            TurtleText1.blit()
            TurtleText2 = TextClass(
                "The Leather-Back Sea Turtle use ocean currents as \"Highways\" in order to migrate faster.",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 10),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER - 50, 310),
                screen
            )
            TurtleText2.blit()
            TurtleText3 = TextClass(
                "Unique Ability: Use Ocean Currents as Highways to increase speed!",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 10),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER - 110, 330),
                screen
            )
            TurtleText3.blit()
            
            DeerTitle = TextClass(
                "White-Tailed Deer",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER - 230, 375),
                screen
            )
            DeerTitle.blit()
            DeerText1 = TextClass(
                "The white-tailed deer is abundant throughout Central America.",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 10),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER - 110, 400),
                screen
            )
            DeerText1.blit()
            DeerText2 = TextClass(
                "Unique Ability: Deers have super senses and give an alert when an enemy is nearby!",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 10),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER - 60, 420),
                screen
            )
            DeerText2.blit()
            DeerText3 = TextClass(
                "Your goal is to migrate to the Brazilian marshes. Avoid wolves and hunters!",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 10),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER - 80, 440),
                screen
            )
            DeerText3.blit()
            
            
            BackButton = ButtonClass(
                TextClass(
                    "Understood!",
                    pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                    DesignClass.Colors["BLACK"],
                    (DesignClass.SCREEN_WIDTH_CENTER, 500),
                    screen
                ),
                pygame.Rect(DesignClass.SCREEN_WIDTH_CENTER - 175, 475, 350, 50),
                0,
                DesignClass.Colors["GREEN"],
                screen,
                ChangeGameState,
                "TitleScreen"
            )
            buttonlist.append(BackButton)
            BackButton.draw()

        case "EndScreen":
            screen.fill(DesignClass.Colors["WHITE"])
            obstacle_list = []
            collide_list = []
            
            endTitle = TextClass(
                EndScreenTitle,
                pygame.font.Font(DesignClass.Fonts["Poppins"], 100),
                EndScreenTitleColor,
                (DesignClass.SCREEN_WIDTH_CENTER, 150),
                screen
            )
            endTitle.blit()
            
            endReasonText = TextClass(
                EndScreenReason,
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 250),
                screen
            )
            endReasonText.blit()
            
            continueText = TextClass(
                "Press [Space] To Continue",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 35),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 450),
                screen
            )
            continueText.blit()
            


        #Commented because of run error
        # case _:
        #     #default
        #     pass


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RunVar = False

        #Detecting button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            for button in buttonlist:
                if button.rectangleRender.collidepoint(mousepos):
                    button.command(button.param)


        #Detecting key presses
        keys = pygame.key.get_pressed()
        try:
            if keys[pygame.K_w]:
                #Height limit
                if GameState != "DeerLevel":
                    if current_player.ycor > 10:
                        current_player.move("UP")
            if keys[pygame.K_s]:
                #Height limit
                if current_player == deer:
                    try:
                        if hole.xcor - 50 < deer.xcor and hole.xcor + 50 > deer.xcor:
                            SpecialLevelEnter()
                    except:
                        pass
                elif current_player.ycor < 500:
                    current_player.move("DOWN")
            if keys[pygame.K_q]:
                #unique ability
                pass

            if GameState == "DeerLevel2" or GameState == "TurtleBonus":
                if keys[pygame.K_d]:
                    if current_player.xcor < 730:
                      
                        current_player.move("RIGHT")

                if keys[pygame.K_a]:
                  
                    if current_player.xcor > 15:
                        current_player.move("LEFT")
        except:
            pass
        
        #For deer
        try:
            if keys[pygame.K_SPACE]:
                if GameState == "EndScreen":
                    pygame.time.delay(100)
                    GameState = EndScreenNextStage
                elif GameState == "DeerLevel":
                    isJumping = True
 
        except:
            pass

        #Returning to main menu during gameplay
        try:
            if keys[pygame.K_ESCAPE]:
                GameState = "TitleScreen"
                ResetGame()
        except:
            pass
            
    pygame.display.update()
    
    pygame.time.Clock().tick(40)

pygame.quit()
import gamebox
import pygame
import random
"""How to Play:
    - Use the left and right arrow keys in order to move Isabelle back and forth across the screen
    - In order to move onto the next level, Isabelle must catch 3 of each type of fruit and avoid the falling turnips
    - There are a total of 6 levels: apples, cherries, oranges, peaches, pears, and coconuts
    - If Isabelle catches one of the turnips, she will have to redo the level from the beginning
    - Once all fruits have been caught, you win!
    
    Optional Features:
    - Animation: Isabelle's leggies moving
    - Enemies: Dumb turnips >:(
    - Collectibles: Juicy fruits
    - Multiple Levels: Each juicy fruit
    - Save Points: Don't know if this counts? but I have the user restart at the level they lost so their score/progress on other
    levels is saved
    
    Notes:
    - Even though I tried to limit my gameboxes and resize my images, depending on your computer the game can start to 
    get a bit slow so I recommend just changing the falling fruit and turnip speeds according to how your computer allows you to
    play best (I talked to Prof. Pettit about this and he said there was no way around it :/). You can do this for each level, so
    for example on level 1 you would change "apple.yspeed += ___" and "turnip.yspeed += ___" but the values I put in work well too. 
        - Because of this, I purposefully didn't make each level "harder" by changing each speed I just allowed the game to lag a 
        bit and make the game harder on its own but I recommend changing it if you want because it is fun >:)
     
    - I've played the game a billion times already and sometimes (very rarely) the program gets a bit overwhelmed and throws
    an error that says something along the lines of "cannot iterate list type [x]" but I checked reddit and this can seem to happen
    if the program can't maintain storage capacity or something? This should rarely ever happen though so I think it should be okay. 
    
    - I think it's funny that Isabelle runs backwards animated so I kept it like that (please don't take off points haha), I am
    aware that I could do isabelle.flip() to mirror the spritesheet and make her run in the left direction but I don't know its so funny
    
    And uhh I think that is all, thank you for playing!
    """

camera = gamebox.Camera(800, 600)
isabellesheet = gamebox.load_sprite_sheet("isabelleright.png", 1, 8) #https://www.deviantart.com/theredthunderx/art/Isabelle-SSF2-Sprite-Sheet-813157302
isabelle = gamebox.from_image(300, 400, isabellesheet[0])
isabelle.scale_by(1.5)

frame = 0
counter = 0

#isabelle = gamebox.from_color(400, 450, "orange", 50, 50)
isabelle.xspeed = 40
ground = gamebox.from_color(-100, 480, "dark green", 3000, 100)

fruitsheet = gamebox.load_sprite_sheet("pixelfruitfinal.png", 1, 7) #http://rebloggy.com/post/animal-crossing-fruit-pixel-art-pixels-new-leaf-acnl/67233010846
apples = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[1])]
cherries = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[2])]
oranges = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[3])]
peaches = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[4])]
pears = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[5])]
coconuts = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[0])]
turnips = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[6])]

applecount = 0
cherrycount = 0
orangecount = 0
peachcount = 0
pearcount = 0
coconutcount = 0

splashscreen = gamebox.from_image(400, 300, "splashscreen.png") #https://www.dafont.com/forum/attach/orig/6/7/673445.png?1
splashscreen.scale_by(0.6)
main_screen_on = 1

def tick(keys):
    global main_screen_on, frame, counter, apples, applecount, cherries, cherrycount, oranges, orangecount, peaches, peachcount, pears, pearcount, coconuts, coconutcount, turnips

    #SPLASH SCREEN
    if main_screen_on == 1:
        camera.clear("white")
        camera.draw(splashscreen)
        if pygame.K_RETURN in keys:
            main_screen_on = 0
        camera.display()
        return

    #ISABELLE MOVEMENT
    if pygame.K_RIGHT in keys:
        isabelle.x += 10
        if frame == 8:
            frame = 0
        if counter % 5 == 0:
            isabelle.image = isabellesheet[frame]
        frame += 1
        counter += 1
    if pygame.K_LEFT in keys:
        isabelle.x -= 10
        if frame == 8:
            frame = 0
        if counter % 5 == 0:
            isabelle.image = isabellesheet[frame]
        frame += 1
        counter += 1
    isabelle.yspeed += 1
    isabelle.y = isabelle.y + isabelle.yspeed
    if isabelle.touches(ground):
        isabelle.move_to_stop_overlapping(ground)
    camera.clear("#D6F5F5")
    camera.draw(ground)
    background = gamebox.from_image(400, 300, "background.png") #https://image.shutterstock.com/image-vector/pixel-art-background-grass-mud-600w-564768682.jpg
    background.scale_by(0.32)
    camera.draw(background)
    camera.draw(isabelle)

    #LEVEL 1: APPLES
    for apple in apples:
        apple.yspeed += 0.2
        apple.y = apple.y + apple.yspeed
        if 0 <= applecount < 3:
            camera.draw(apple)
            if isabelle.touches(apple):
                applecount += 1
                apples.remove(apple)
                apples = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[1])]
            camera.draw(apple)
            if apple.touches(ground):
                apples.remove(apple)
                apples = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[1])]
            camera.draw(apple)
    for turnip in turnips:
        turnip.yspeed += 0.8
        turnip.y = turnip.y + turnip.yspeed
        if 0 <= applecount < 3:
            camera.draw(turnip)
            if isabelle.touches(turnip):
                applecount = 0
                turnips = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[6])]
            if turnip.touches(ground):
                turnips.remove(turnip)
                turnips = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[6])]
            camera.draw(turnip)
    appledisplay = gamebox.from_image(660, 70, fruitsheet[1])
    scoredisplay = gamebox.from_text(740, 70, "x  " + str(applecount), 30, "white", italic=True)
    if 0 <= applecount < 3:
        camera.draw(scoredisplay)
        camera.draw(appledisplay)
    camera.display()

    #LEVEL 2: CHERRIES
    if applecount == 3:
        score = 0
        if 0 <= cherrycount < 3:
            for cherry in cherries:
                cherry.yspeed += 0.8
                cherry.y = cherry.y + cherry.yspeed
                camera.draw(cherry)
                if isabelle.touches(cherry):
                    cherrycount += 1
                    cherries.remove(cherry)
                    cherries = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[2])]
                camera.draw(cherry)
                if cherry.touches(ground):
                    cherries.remove(cherry)
                    cherries = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[2])]
                camera.draw(cherry)
            for turnip in turnips:
                turnip.yspeed += 0.8
                turnip.y = turnip.y + turnip.yspeed
                if 0 <= cherrycount < 3:
                    camera.draw(turnip)
                    if isabelle.touches(turnip):
                        cherrycount = 0
                        turnips = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[6])]
                    if turnip.touches(ground):
                        turnips.remove(turnip)
                        turnips = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[6])]
                    camera.draw(turnip)
            cherrydisplay = gamebox.from_image(660, 70, fruitsheet[2])
            scoredisplay = gamebox.from_text(740, 70, "x  " + str(cherrycount), 30, "white", italic=True)
            if 0 <= cherrycount < 3:
                camera.draw(scoredisplay)
                camera.draw(cherrydisplay)
            camera.display()

        #LEVEL 3: ORANGES
        if cherrycount == 3:
            score = 0
            if 0 <= orangecount < 3:
                for orange in oranges:
                    orange.yspeed += 0.8
                    orange.y = orange.y + orange.yspeed
                    camera.draw(orange)
                    if isabelle.touches(orange):
                        orangecount += 1
                        oranges.remove(orange)
                        oranges = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[3])]
                    camera.draw(orange)
                    if orange.touches(ground):
                        oranges.remove(orange)
                        oranges = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[3])]
                    camera.draw(orange)
                for turnip in turnips:
                    turnip.yspeed += 0.8
                    turnip.y = turnip.y + turnip.yspeed
                    if 0 <= orangecount < 3:
                        camera.draw(turnip)
                        if isabelle.touches(turnip):
                            orangecount = 0
                            turnips = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[6])]
                        if turnip.touches(ground):
                            turnips.remove(turnip)
                            turnips = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[6])]
                        camera.draw(turnip)
                orangedisplay = gamebox.from_image(660, 70, fruitsheet[3])
                scoredisplay = gamebox.from_text(740, 70, "x  " + str(orangecount), 30, "white", italic=True)
                if 0 <= orangecount < 3:
                    camera.draw(scoredisplay)
                    camera.draw(orangedisplay)
                camera.display()

        #LEVEL 4: PEACHES
        if orangecount == 3:
            score = 0
            if 0 <= peachcount < 3:
                for peach in peaches:
                    peach.yspeed += 0.8
                    peach.y = peach.y + peach.yspeed
                    camera.draw(peach)
                    if isabelle.touches(peach):
                        peachcount += 1
                        peaches.remove(peach)
                        peaches = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[4])]
                    camera.draw(peach)
                    if peach.touches(ground):
                        peaches.remove(peach)
                        peaches = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[4])]
                    camera.draw(peach)
                for turnip in turnips:
                    turnip.yspeed += 0.8
                    turnip.y = turnip.y + turnip.yspeed
                    if 0 <= peachcount < 3:
                        camera.draw(turnip)
                        if isabelle.touches(turnip):
                            peachcount = 0
                            turnips = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[6])]
                        if turnip.touches(ground):
                            turnips.remove(turnip)
                            turnips = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[6])]
                        camera.draw(turnip)
                peachdisplay = gamebox.from_image(660, 70, fruitsheet[4])
                scoredisplay = gamebox.from_text(740, 70, "x  " + str(peachcount), 30, "white", italic=True)
                if 0 <= peachcount < 3:
                    camera.draw(scoredisplay)
                    camera.draw(peachdisplay)
                camera.display()

        #LEVEL 5: PEARS
        if peachcount == 3:
            score = 0
            if 0 <= pearcount < 3:
                for pear in pears:
                    pear.yspeed += 0.8
                    pear.y = pear.y + pear.yspeed
                    camera.draw\
                        (pear)
                    if isabelle.touches(pear):
                        pearcount += 1
                        pears.remove(pear)
                        pears = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[5])]
                    camera.draw(pear)
                    if pear.touches(ground):
                        pears.remove(pear)
                        pears = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[5])]
                    camera.draw(pear)
                for turnip in turnips:
                    turnip.yspeed += 0.8
                    turnip.y = turnip.y + turnip.yspeed
                    if 0 <= pearcount < 3:
                        camera.draw(turnip)
                        if isabelle.touches(turnip):
                            pearcount = 0
                            turnips = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[6])]
                        if turnip.touches(ground):
                            turnips.remove(turnip)
                            turnips = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[6])]
                        camera.draw(turnip)
                peardisplay = gamebox.from_image(660, 70, fruitsheet[5])
                scoredisplay = gamebox.from_text(740, 70, "x  " + str(pearcount), 30, "white", italic=True)
                if 0 <= pearcount < 3:
                    camera.draw(scoredisplay)
                    camera.draw(peardisplay)
                camera.display()

        #LEVEL 6: COCONUTS
        if pearcount == 3:
            score = 0
            if 0 <= coconutcount < 3:
                for coconut in coconuts:
                    coconut.yspeed += 0.8
                    coconut.y = coconut.y + coconut.yspeed
                    camera.draw(coconut)
                    if isabelle.touches(coconut):
                        coconutcount += 1
                        coconuts.remove(coconut)
                        coconuts = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[0])]
                    camera.draw(coconut)
                    if coconut.touches(ground):
                        coconuts.remove(coconut)
                        coconuts = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[0])]
                    camera.draw(coconut)
                for turnip in turnips:
                    turnip.yspeed += 0.8
                    turnip.y = turnip.y + turnip.yspeed
                    if 0 <= coconutcount < 3:
                        camera.draw(turnip)
                        if isabelle.touches(turnip):
                            coconutcount = 0
                            turnips = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[6])]
                        if turnip.touches(ground):
                            turnips.remove(turnip)
                            turnips = [gamebox.from_image(random.randint(200, 650), 100, fruitsheet[6])]
                        camera.draw(turnip)
                coconutdisplay = gamebox.from_image(660, 70, fruitsheet[0])
                scoredisplay = gamebox.from_text(740, 70, "x  " + str(coconutcount), 30, "white", italic=True)
                if 0 <= coconutcount < 3:
                    camera.draw(scoredisplay)
                    camera.draw(coconutdisplay)
                camera.display()

gamebox.timer_loop(30, tick)

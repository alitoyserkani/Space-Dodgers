################################################################

##     TITLE:            SPACE DODGERS
##     PROGRAMMER:       ALI TOYSERKANI

################################################################

from tkinter import *
from random import *
from time import *
from math import *
##from threading import Thread
##import subprocess
##
##class BackgroundMusic(Thread):
##    def run(self):
##        global process
##        process = subprocess.call(["afplay", "Original_Tetris_theme_Tetris_Soundtrack_.wav"])
##        process.terminate()
##        process.kill()
##bulletS = BackgroundMusic()
##bulletS.start()

#subprocess.call(["afplay", "Original_Tetris_theme_Tetris_Soundtrack_.wav"])

root = Tk()
screen = Canvas(root, width=1000, height=700, background = "black")
root.title('SPACE DODGERS')


#Imports all GIF files
def setImports():
    global spaceshipFiles,asteroidFiles,heart
    spaceshipFiles = []
    asteroidFiles = []

    for i in range(0,7):
        spaceshipFiles.append(PhotoImage(file = "spaceship-" + str(i) + ".gif"))
    for i in range(5,9):
        asteroidFiles.append(PhotoImage(file = "asteroid" + str(i) + ".gif"))

    heart = PhotoImage(file = "heart.gif")
    

    #print(len(spaceshipFiles),len(asteroidFiles))

# Whenever the mouse is clicked, the position is determined
def mouseClickHandler(event):
    global xMouse, yMouse
    
    screen.focus_set()
    
    xMouse = event.x
    yMouse = event.y
    #print(xMouse,yMouse)
    
# Checks to see if PLAY has been clicked
def PlayClickedDetector():
    global PlayClicked 

    if 300 < xMouse < 500 and 450 < yMouse < 550:
        PlayClicked = True

#Sets all inital values that will be used by other procedures
def setInitialValues():
    global xShip,yShip,shipSpeed,xMouse,yMouse,bullets,xBullets,yBullets,bulletSpeed
    global xSpeed,ySpeed,Qpressed,xAsteroid,yAsteroid,asteroids
    global asteroidSpeedX,asteroidSpeedY,score,lives,PlayClicked,CharactersDraw,ColorOptions,k
    global ChosenDifficulty,numAsteroids,AsteroidsHit,shipFile,gameOver,ScoreMultiplier,restartClicked

    #Starting position of spaceship   
    xShip = 400
    yShip = 400
    shipSpeed = 14

    #Starting speeds
    xSpeed = 0
    ySpeed = 0

    #Creating x and yMouse variables
    xMouse = 0
    yMouse = 0

    #Initialize arrays for the bullets
    bullets = []
    xBullets = []
    yBullets = []
    bulletSpeed = 15

    #Create arrays for the asteroids
    asteroids = []
    xAsteroid = []
    yAsteroid = []
    asteroidSpeedX = []
    asteroidSpeedY= []

    
    lives = 5   #Starting lives
    score = 0   #Initial score

    ScoreMultiplier = 2   #Sets initial multiplier for default normal difficulty
 
    Qpressed = False   #Becomes TRUE once Q is pressed
    PlayClicked = False      #Becomes TRUE once play is clicked in the menu       
    QuitClicked = False      #Becomes TRUE is exit is clicked on the screen
    gameOver = False      #Becomes TRUE once lives are depleted
    restartClicked = False #Sets the restart
    
    shipFile = 0       #Sets a default ship file for the game if player chooses not to change
    ChosenDifficulty = "Normal"    #Default difficulty
    numAsteroids = 15            #Default number of asteroids based on difficulty

    AsteroidsHit = 0    #Starting amount of asteroids hit

    CharactersDraw = []    #Creates empty array for the characters to be appended to later on
    ColorOptions = ["red","grey","gold","SkyBlue1","salmon4","purple","green"]  #Bullet color options
    

#Draws the background stars    
def createBackground():
    global stars,starX,starY

    stars = []
    starX = []
    starY = []

    for i in range(0,200):          #Adds coorinates for the stars to the array in a random fashion
        Xstar = randint(0,800)
        Ystar = randint(0,800)
        starX.append(Xstar)
        starY.append(Ystar)
        stars.append(0)

    for i in range(0,200):
        stars[i] = screen.create_oval(starX[i],starY[i],starX[i]+5,starY[i]+5,fill="white")    #Draws the stars


#Creates the menu system before the game
def createMenu():
    global PlayText,PlayTextRec,TitleText1,TitleText2,CharactersDraw,CharacterText
    global DifficultyRec,EasyDiffText,FirstDiffLine,NormalDiffText,SecondDiffLine,HardDiffText,ThirdDiffLine,InsaneDiffText,DifficultyText
    global QuoteText

    #Create Play Screen
    PlayTextRec = screen.create_rectangle(295,460,510,540,fill="red") 
    PlayText = screen.create_text(400,500,text="PLAY",activefill = "yellow",font="Helvetica 70 bold",fill="blue")

    #Draw title text
    TitleText1 = screen.create_text(400,125,text="SPACE",font="System 120 bold",fill="firebrick1")
    TitleText2 = screen.create_text(400,250,text="DODGERS",font="System 120 bold",fill="firebrick1")
    CharacterText = screen.create_text(400,600,text="click to change ship",font="System 30 bold",fill="purple1")

    #Create Difficulty Bars
    DifficultyRec = screen.create_rectangle(0,375,200,575,fill="gray30",outline="red",width=5)
    EasyDiffText = screen.create_text(100,400,text="EASY",activefill="yellow",fill="dodger blue",font="Helvetics 30 bold")
    FirstDiffLine = screen.create_line(0,425,200,425,fill="red",width=5)
    NormalDiffText = screen.create_text(100,450,text="NORMAL",activefill="yellow",font="Helvetics 30 bold",fill="dodger blue")
    SecondDiffLine = screen.create_line(0,475,200,475,fill="red",width=5)
    HardDiffText = screen.create_text(100,500,text="HARD",activefill="yellow",font="Helvetica 30 bold",fill="dodger blue")
    ThirdDiffLine = screen.create_line(0,525,200,525,fill="red",width=5)
    InsaneDiffText = screen.create_text(100,550,text="INSANE",activefill="yellow",font="Helvetica 30 bold",fill="dodger blue")
    DifficultyText = screen.create_text(100,350,text="choose difficulty",font="System 22 bold",fill="purple1")

    #Create quote
    QuoteText = screen.create_text(400,50,text="\"Dodge before you shoot\" ", fill='purple',font="Helvetica 30 bold")

    #Input the spaceships onto the screen
    x = 175
    for i in range(len(spaceshipFiles)):
        CharactersDraw.append(0)
    for i in range(len(CharactersDraw)):
        CharactersDraw[i] = screen.create_image(x,650,image=spaceshipFiles[i])
        x = x + 75
        
#Checks to see which character (spaceship) has been clicked
#Changes the character selected
def CharacterSelection():
    global SelectedCharacter,SelectedColor,shipFile

    if PlayClicked == False:
        
        if 150 < xMouse < 200 and 375 < yMouse < 425:     #Changes based on area clicked
            shipFile = 0
        elif 225 < xMouse < 275 and 625 < yMouse < 675:
            shipFile = 1
        elif 300 < xMouse < 350 and 625 < yMouse < 675:
            shipFile = 2
        elif 375 < xMouse < 425 and 625 < yMouse < 675:
            shipFile = 3
        elif 450 < xMouse < 500 and 625 < yMouse < 675:
            shipFile = 4
        elif 525 < xMouse < 575 and 625 < yMouse < 675:
            shipFile = 5
        elif 600 < xMouse < 650 and 625 < yMouse < 675:
            shipFile = 6

        SelectedCharacter = spaceshipFiles[shipFile]      #Alters the current selected spaceship
        SelectedColor = ColorOptions[shipFile]         #Assigns a color, depending on the chosen spaceship


#Changes the difficulty, by user decision
def DifficultyChoiceDetector():
    global ChosenDifficulty,numAsteroids,ScoreMultiplier

    if PlayClicked == False:

        if xMouse < 200 and 375 < yMouse < 425:    # Number of asteroids change relative to the difficulty chosen
            ChosenDifficulty = "Easy"
            numAsteroids = 8
            ScoreMultiplier = 1                  #Score multiplier increases as difficulty gets harder
        elif xMouse < 200 and 425 < yMouse < 475:
            ChosenDifficulty = "Normal"
            numAsteorids = 13
            ScoreMultiplier = 3
        elif xMouse < 200 and 475 < yMouse < 525:
            ChosenDifficulty = "Hard"
            numAsteroids = 18
            ScoreMultiplier = 5
        elif xMouse < 200 and 525 < yMouse < 575:
            ChosenDifficulty = "Insane"
            numAsteroids = 25
            ScoreMultiplier = 8

        #print(ChosenDifficulty,numAsteroids)
        
    
    
#Draws the scoreboard on the right side of the screen
def createScoreboard():
    global Sc1,Sc2,Sc3,Sc4,Sc5,Sc6,Sc7,Sc8,Sc9,Sc10,Sc11 
    #Creates scoreboard structure
    Sc1 = screen.create_line(800,0,800,700,fill = "blue", width = 8)
    Sc2 = screen.create_line(800,60,1000,60,fill="blue",width=8)
    Sc3 = screen.create_line(800,120,1000,120,fill="blue",width=8)
    Sc4 = screen.create_rectangle(800,120,1000,700,fill="blue",outline="blue")
    Sc5 = screen.create_rectangle(800,600,1000,700,fill="gray30",outline="red",width=8)

    #Inputs texts on the scoreboard
    Sc6 = screen.create_text(900,30,text="SCORE",font="Helvetica 36 bold",fill="white")
 #   screen.create_text(900,90,text=str(score),font="Helvetica 20 bold",fill="white")
    Sc7 = screen.create_text(900,150,text="LIVES",font="Helvetica 30 bold",fill="red")
    Sc8 = screen.create_text(900,270,text="ASTEROIDS HIT",font="Helvetica 22 bold",fill="sienna")
    Sc9 = screen.create_text(900,400,text="DIFFICULTY",font="Helvetica 25 bold",fill="DarkOrange1")
    Sc10 = screen.create_text(900,650,text="END",font = "Helvetica 50 bold",activefill="orange",fill="white")
    Sc11 = screen.create_text(900,500,text="MULTIPLIER",font = "Helivetica 25 bold",fill="green2")
                       
#Checks to see if certain keyboard buttons have been pressed
#If so, other procedures are called
#Sets x and y speeds based on the arrow key pressed
def keyDownHandler(event):
    global xShip, yShip, Qpressed,xSpeed,ySpeed,gamePaused

    if event.keysym == "Left" or event.keysym == "a":     #When LEFT arrow key or A is pressed, ship goes left
        xSpeed = -shipSpeed
    elif event.keysym == "Right" or event.keysym == "d" or event.keysym == "D":  #When RIGHT arrow key or D is pressed, ship goes right
        xSpeed = shipSpeed
    elif event.keysym == "Up" or event.keysym == "w" or event.keysym == "W":  #When UP arrow key  or W is pressed, ship goes up
        ySpeed = -shipSpeed
    elif event.keysym == "Down"or event.keysym == "s" or event.keysym == "S": #When DOWN arrow key or S is pressed, ship goes down
        ySpeed = shipSpeed
    elif event.keysym == "q" or event.keysym == "Q":     #When Q is pressed, it leads to ending the game session
        Qpressed = True
    elif event.keysym == "1" or event.keysym == "f" or event.keysym == "space":  #When 1 or F or SPACE is pressed, a bullet is created
        createNewBullet()

#Stops the spaceship when an arrow key is released
def keyUpHandler(event):
    global xSpeed,ySpeed

    xSpeed = 0
    ySpeed = 0

#Updates the ship's position using the current speed and direction, as well previous position
#Restricts player from moving off the screen
def updateShipPosition():
    global xShip,yShip

    if xShip <= 20:    #If the ship touches the edge of the screen, it stops it from further moving
        xShip = 21
    elif xShip >= 780:
        xShip = 779
    elif yShip <= 15:
        yShip = 16
    elif yShip >= 675:
        yShip = 674
    else:
        xShip = xShip + xSpeed       #Updates ship postion
        yShip = yShip + ySpeed

#Creates a new bullet everytime the spacebar,1,or f is pressed
#Removes 20 points from the score for every bullet creates
def createNewBullet():
    global bullets,xBullets,yBullets,score

    bullets.append(0)
    xBullets.append(xShip)
    yBullets.append(yShip)
    if PlayClicked == True:
        score = score - 20


#Makes the bullets move up the screen using bulletSpeed and the previous position of the bullet
def updateBulletPosition():
    global bullets,xBullets,yBullets

    for i in range(0,len(yBullets)):
        yBullets[i] = yBullets[i] - bulletSpeed

        #print(xBullets[i],yBullets[i])

    deleteBulletsFromArray()

#Removes the bullets from its array once the bullet exits the screen area
def deleteBulletsFromArray():
    j = 0

    while j < len(yBullets) < -1:
        if yBullets[j]<0:
            yBullets.pop(j)
            xBullets.pop(j)
            bullets.pop(j)
        else:
            j = j + 1

#Places the ship's image using its current position
def placeShip():
    global playerShip,xShip,yShip

    playerShip = screen.create_image(xShip,yShip, image = SelectedCharacter)

#Draws bullets based on current position
def drawBullets():
    for i in range(0,len(yBullets)):
        bullets[i] = screen.create_oval(xBullets[i]-5,yBullets[i]-5,xBullets[i]+5,yBullets[i]+5, fill = SelectedColor)

#Deletes Bullets from the screen once they exit the screen area
def deleteBullets():
    for i in range(0,len(yBullets)):
        screen.delete(bullets[i])



### CREATING AND CONTROLLOING THE ASTEROIDS

#Creates the initial asteroids
def createFirstAsteroids():
    global spawnAreaX,spawnAreaY,xAsteroid,yAsteroid,asteroids,asteroidSpeedX,asteroidSpeedY
    
    for i in range(0,numAsteroids+1):
        spawnAreaX = [-25,randint(10,790),825,randint(10,790)]     #Sets spawn areas for the asteroids outside the screen
        spawnAreaY = [randint(10,790),-25,randint(10,790),725]
        dependentSpeedX = [randint(2,8),randint(-2,2),randint(-8,-2),randint(-2,2)] #Sets random speeds for the asteroids based on their spawn area
        dependentSpeedY = [randint(-2,2),randint(2,8),randint(-2,2),randint(-8,-2)]

        xAsteroid.append(spawnAreaX[i%4])         #Adds initial postion sand speeds to asteroid arrays
        asteroidSpeedX.append(dependentSpeedX[i%4])
        yAsteroid.append(spawnAreaY[i%4])
        asteroidSpeedY.append(dependentSpeedY[i%4])
        asteroids.append(0)

        
#Updates the asteroids placement using its previous position and random speed
def updateAsteroidPosition():
    global asteroids,xAsteroid,yAsteroid 

    for i in range(0,len(asteroids)):
        xAsteroid[i] = xAsteroid[i] + asteroidSpeedX[i]
        yAsteroid[i] = yAsteroid[i] + asteroidSpeedY[i]

    deleteAsteroidsFromArray()


#Removes asteroids from its array whenever they go off the screen
def deleteAsteroidsFromArray():
    global asteroids,xAsteroid,yAsteroid
    
    for k in range(0,len(asteroids)):
        if xAsteroid[k] < -25:
            xAsteroid.pop(k)         #Removes the item at a certain point in the array, for all cases in procedure
            yAsteroid.pop(k)
            asteroids.pop(k)
            asteroidSpeedX.pop(k)
            asteroidSpeedY.pop(k)
            createNewAsteroid()
            #print(xAsteroid[k])
        elif xAsteroid[k] > 825:
            xAsteroid.pop(k)
            yAsteroid.pop(k)
            asteroids.pop(k)
            asteroidSpeedX.pop(k)
            asteroidSpeedY.pop(k)
            createNewAsteroid()
            #print(xAsteroid[k])
            
        elif yAsteroid[k] < -25:
            xAsteroid.pop(k)
            yAsteroid.pop(k)
            asteroids.pop(k)
            asteroidSpeedX.pop(k)
            asteroidSpeedY.pop(k)
            createNewAsteroid()
            #print(xAsteroid[k])
        elif yAsteroid[k] > 825:
            xAsteroid.pop(k)
            yAsteroid.pop(k)
            asteroids.pop(k)
            asteroidSpeedX.pop(k)
            asteroidSpeedY.pop(k)
            createNewAsteroid()
            #print(xAsteroid[k])
            

#Creates a new asteroid once one is deleted            
def createNewAsteroid():
    global spawnAreaX,spawnAreaY,xAsteroid,yAsteroid,asteroids,asteroidSpeedX,asteroidSpeedY
    
    IndexChoice = randint(0,3)     #Based a this random number, a random spawn area is chosen
    spawnAreaX = [-25,randint(10,790),825,randint(10,790)]     #Random spawn areas determined
    spawnAreaY = [randint(10,790),-25,randint(10,790),820]
    dependentSpeedX = [randint(2,10),randint(-2,2),randint(-10,-2),randint(-2,2)]   #Random speeds determined
    dependentSpeedY = [randint(-2,2),randint(2,10),randint(-2,2),randint(-10,-2)] 

    #print(spawnAreaX,spawnAreaY,dependentSpeedX,dependentSpeedY,IndexChoice)

    xAsteroid.append(spawnAreaX[IndexChoice])       #Adds initial positions and speeds to array
    asteroidSpeedX.append(dependentSpeedX[IndexChoice])
    yAsteroid.append(spawnAreaY[IndexChoice])
    asteroidSpeedY.append(dependentSpeedY[IndexChoice])
    asteroids.append(0)

#Draws asteroids on the screen using its x and y position
def drawAsteroids():
    global asteroids,xAsteroid,yAsteroid,asteroidFiles

    for i in range(0,len(asteroids)):
        if xAsteroid[i] < 805:   #To prevent asteroids from appearing on the scoreboard 
            asteroids[i] = screen.create_image(xAsteroid[i],yAsteroid[i],image = asteroidFiles[i%4])
        
        
#Deletes asteroids from the screen if they are off the screen
def deleteAsteroids():
    for i in range(0,len(asteroids)):
        screen.delete(asteroids[i])

#Detects if an asteroid has hit the spaceship
#Makes is so the asteroid goes off the screen and instantly deletes
def PlayerHitDetection():
    global xShip,yShip,xAsteroid,yAsteroid,asteroids,lives,score

    playerRadius = 23
    asteroidRadius = 23
    bulletRadius = 5

    for i in range(0,len(asteroids)):

        xDistancePlayerShip = abs(xAsteroid[i] - xShip)     #Calculates distance between the ship and a asteroid
        yDistancePlayerShip = abs(yAsteroid[i] - yShip)
        
        #Sends asteroid off screen to be deleted if the player hits the asteroid
        if xDistancePlayerShip <= 45 and yDistancePlayerShip <= 45:      

           xAsteroid[i] = 1000
           yAsteroid[i] = 1000
           lives = lives - 1    #A life is lost for every interaction


           
#Detects if a bullet has hit an asteroid
def BulletHitDetection():
    global bullets,xBullets,yBullets,asteroids,xAsteroid,yAsteroid,score,AsteroidsHit

    maxDist = 28    #Distance there is from the centre of the ball to the centre of the asteroid

    numBull = len(xBullets)     #Sets the number of bullets and asteroids to variables
    numAster = len(xAsteroid)

    for i in range(numBull):      
        for x in range(numAster):
            #If the distance between the bullet and the asteroid is within a range, the asteroid and the bullet move off the screen to get deleted
            if sqrt(((xBullets[i]-xAsteroid[x])**2)+((yBullets[i]-yAsteroid[x])**2)) <= maxDist:     
                CurrAstersHit = AsteroidsHit
                xAsteroid[x] = 1000
                yAsteroid[x] = 1000
                yBullets[i] = 0
                score = score + 120             #Adds to the score total for every asteroid hit (120 because of 20 point shot penalty)
                AsteroidsHit = AsteroidsHit + 1    #Updates the number of asteroids hit


#Updates the lives seen on the scoreboard
def updateLives():
    global livesDisplay,livesPicDisplay

    livesDisplay = screen.create_text(900,200,text=str(lives),font="Helvetica 30 bold",fill="white")

                
#Updates the score on the scoreboard
def updateScore():
    global scoreDisplay
    
    scoreDisplay = screen.create_text(900,90,text=str(score),font="Helvetica 20 bold",fill="white")

#Updates the number of asteroids hit on the scoreboar
def updateAsteroidsHit():
    global AsterHitDisplay

    AsterHitDisplay = screen.create_text(900,320,text=str(AsteroidsHit),font="Helvetica 30 bold",fill="white")
        
#Checks id the quit area has ben clicked       
def quitClickedDetector():
    global Qpressed

    if PlayClicked == True:
        if 815 < xMouse < 985 and 600 < yMouse:
            Qpressed = True
        

#Checks if user has hit restart area
def checkRestart():
    global restartClicked
    
    if 800 < xMouse < 1000 and yMouse > 600:
        if gameOver == True:
            restartClicked = True
    
#IF USER DESIRES TO END THE GAME
#Quits the game if the Q button is pressed
def quitGame():
    if Qpressed == True:
        return True
    else:
        return False


#Once the game ends, asteroids and ships are deleted, and an ending screen is made
def stopGame():
    global GameOver1,GameOver2,GameOver3,GameOver4
    
    screen.delete(playerShip)
    screen.delete(asteroids)

    GameOver1 = screen.create_text(400,400,text="Thanks for playing:",font="Helvetica 60 bold",fill="pink")
    GameOver2 = screen.create_text(400,500,text="Your final score:",font="Helvetica 50 bold",fill="pink")
    GameOver3 =  screen.create_text(400,600,text=str(score),font="Helvetica 60 bold",fill = "red")
    GameOver4 =  screen.create_text(400,250,text="GAME OVER",font = "Helvetica 100 bold",fill="red")

    

#RUNS THE GAME BY COMBINING ALL THE PROCEDURES
def runGame():
    global xShip,yShip,score,lives,scoreDisplay,gameOver,xMouse,yMouse

    setImports()
    createBackground()
    setInitialValues()
    createScoreboard()
    createMenu()

    screen.update()

    while PlayClicked == False:   #Keeps game on the menu until play is clicked
       CharacterSelection()
       updateShipPosition()
       updateBulletPosition()
       placeShip()
       drawBullets()

       screen.update()
       sleep(0.0001)

       screen.delete(playerShip)
       deleteBullets()
       DifficultyChoiceDetector()
       PlayClickedDetector()
       quitClickedDetector()

    createFirstAsteroids()

    screen.delete(PlayText,PlayTextRec,TitleText1,TitleText2,CharactersDraw,CharacterText)
    screen.delete(DifficultyRec,EasyDiffText,FirstDiffLine,NormalDiffText,SecondDiffLine,HardDiffText,ThirdDiffLine,InsaneDiffText,DifficultyText)
    screen.delete(QuoteText)
    for i in range(len(CharactersDraw)):
        screen.delete(CharactersDraw[i])

    ScreenDiff = screen.create_text(900,450,text=ChosenDifficulty,fill="white",font="Helvetica 25 bold")
    ScreenBoost = screen.create_text(900,550,text="X  " + str(ScoreMultiplier),fill="white",font="Helvetica 25 bold")
    GetReadyText = screen.create_text(400,350,text="GET READY",font="Helvetica 75 bold",fill="red")
    screen.update()
    for i in range(1,4):
        CountDownText = screen.create_text(400,500,text=4-i,font="Helvetica 80 bold",fill="green2")
        screen.update()
        sleep(1)
        screen.delete(CountDownText)
    screen.delete(GetReadyText)
    xShip = 400
    yShip = 400
    
    while Qpressed == False and lives > 0:  #Game runs until lives are depleted or QUIT, or Q is pressed
        updateLives()
        updateScore()
        updateAsteroidsHit()
        updateBulletPosition()
        updateShipPosition()
        updateAsteroidPosition()
        placeShip()
        drawBullets()
        drawAsteroids()

        screen.update()
        sleep(0.0001)
        screen.delete(playerShip)
        screen.delete(scoreDisplay)
        screen.delete(livesDisplay)
        
##        screen.delete(livesPicDisplay)
        

        PlayerHitDetection()
        deleteBullets()
        deleteAsteroids()
        BulletHitDetection()

        screen.delete(AsterHitDisplay)
        score = score + ScoreMultiplier

        quitClickedDetector()

    xMouse = 0    #Mouse position is reset to prevent the END button from triggering the MENU button
    yMouse = 0
    stopGame()

    RestartBox = screen.create_rectangle(800,600,1000,700,fill="gray30",outline="green2",width=8)
    RestartText = screen.create_text(900,650,text="MENU",fill="green2",activefill="orange",font="Helvetica 35 bold")
    
    while restartClicked == False:    #Remains on GAME OVER screen until MENU is pressed
        checkRestart()
        sleep(0.001)
        screen.update()
        gameOver=True

    screen.delete(Sc1,Sc2,Sc3,Sc4,Sc5,Sc6,Sc7,Sc8,Sc9,Sc10,Sc11)   #Deletes scoreboard before being redrawn
    for i in range(0,len(stars)):
        screen.delete(stars[i])
    screen.delete(GameOver1,GameOver2,GameOver3,GameOver4)
    screen.delete(RestartBox,RestartText)

    runGame()


#Runs the game
root.after(0,runGame)
#Detects when the mouse is clicked
screen.bind("<Button-1>",mouseClickHandler)\
#Detects when a key is pressed
screen.bind("<Key>", keyDownHandler)
#Detects when a key is released
screen.bind("<KeyRelease>", keyUpHandler)

#Creates screen
screen.pack()
root.mainloop()

#root.attributes("-fullscreen", True)

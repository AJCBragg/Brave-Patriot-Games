import random

print('GLORIOUS SOVIET ROCKET SPY') #This is the title of the game

print()

print('Greetings tovarisch cosmonaut! Your comrade, tovarisch spy, has been kill by \ncapitalist pigs! You must taking her documents and escape the moonbase in the \ninferior free-market spescraft.') #This explains the premise of the game to the user

G = random.randrange(1, 20) #Generate random numbers so that the game plays differently every time

W = random.randrange(1, 40) #Another random number to increase the complexity

R = G * W

print()

print('Gravity of capitalist moonbase is', G) #This gives one random number to the user so that they have something to base guesses on

print()

for c in range(0, 10): #This is a loop, which takes input from the user and checks to see if their guess is correct. If it is, the loop ends and the user wins. If they run out of guesses, they lose.
    F = int(input('Set takeoff velocity: '))
    if F > R:
        print('Velocity is too high, spaceship will make exploding!')
    if F < R:
        print('Velocity is too low, spaceship will do a crashed!')
    if F == R:
        print('Another glorious victory for the Motherland! Many praisings comrade, you will \nbe give a medal upon your returned.')
        takeOffSuccessful = bool(1) #This Boolean statement determines that, because F and R were equal, the takeOffSuccessful variable is set to 1 (true) and the user wins the game
        break
    if F != R and c < 9:
        print('Once more for the Motherland, comrade.')
        takeOffSuccessful = bool(0)

if takeOffSuccessful == bool(0):
    print('The capitalists got you! Use your patriotic cyanide pills!') #This string tells the user (more like loser) that they were not able to guess correctly and have run out of guesses.

input()
 ## this converts fantendo wiki to a game
import gradio


def Game_Generator(Game_Name, Game_Type, Game_Description, Game_Rules, Game_Setup, Game_Play, Game_End):
    Game_Name = input
    Game_Type = input
    Game_Description = input
    Game_Rules = input
    Game_Setup = input
    Game_Play = input
    Game_End = input
    Game_Generator = open(Game_Name + ".txt", "w")
    Game_Generator.write("Game Name: " + Game_Name + "\n")
    Game_Generator.write("Game Type: " + Game_Type + "\n")
    Game_Generator.write("Game Description: " + Game_Description + "\n")
    Game_Generator.write("Game Rules: " + Game_Rules + "\n")
    Game_Generator.write("Game Setup: " + Game_Setup + "\n")
    Game_Generator.write("Game Play: " + Game_Play + "\n")
    Game_Generator.write("Game End: " + Game_End + "\n")

    def Program_End():
        print("Program Ended")
        Game_Generator.close()
        exit()

        def Program_Start():
            print("Program Started")

def Client_Program():
    import gradio as gr
    import os
    import sys
    gradio.client = "800x800"
    gradio.clientsize= "800x800"
    gradio.launch(Game_Generator, "Game Generator")
    gradio.title= "Game Generator"

    gradio.game.gameinfo=input("Please input the game you would like to generate")
print("Please enter the size of the client")
gradio.clientsize=input()
print("Please enter the title of the game")
gradio.title=input()
gradio.export=input("Please enter the name of the file you would like to export to")
gradio.export=gradio.export+input()
gradio.launch(Game_Generator)
print("Done")
print(Game_Generator)

## play the game
def Game_Player():
    import gradio
    import os
    import sys
    gradio.client = "800x800"
    gradio.launch(Game_Generator, "Game Generator")
    gradio.clientsize= "800x800"
    gradio.launch(Game_Generator, "Game Generator")
    gradio.title= "Game Generator"
## write the game engine using pygame
def Game_Engine():
    import pygame
    import os
    import sys
    pygame.init()
    pygame.display.set_caption("Game Engine")
    screen = pygame.display.set_mode((800,800))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    if event.key == pygame.K_UP:
                        print("up")
                    if event.key == pygame.K_DOWN:
                        print("down")
                    if event.key == pygame.K_LEFT:
                        print("left")
                    if event.key == pygame.K_RIGHT:
                        print("right")
                    if event.key == pygame.K_SPACE:
                        print("space")
                    if event.key == pygame.K_RETURN:
                        print("enter")
print(Game_Generator)
print(Game_Engine)
print(Game_Player)

print(Client_Program)
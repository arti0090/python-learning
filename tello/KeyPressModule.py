import pygame
import time

def init():
    pygame.init()
    window = pygame.display.set_mode((1280, 720))

def getKey(keyName):
    answer = False

    for e in pygame.event.get():
        pass

    keyInput = pygame.key.get_pressed()
    # Looking for key in correct format e.g. K_LEFT
    key = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[key]:
        answer = True
    
    pygame.display.update()

    return answer

def main():
    print(getKey("a"))

if __name__ == "__main__":
    init()
    while True:
        main()
        time.sleep(0.1)
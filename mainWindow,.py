import sys
import  pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen= pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Aline Invasion")

    def run_game(self):#main loop game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit
            pygame.display.flip()
if __name__ == '__main__':
    gameAi = AlienInvasion()
    gameAi.run_game()
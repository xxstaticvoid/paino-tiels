
import pygame

from Row import Row
from Line import Line

from typing import List



SCREEN_WIDTH = 350
SCREEN_HEIGHT = 500


def main():

    #pygame setup
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    pygame.display.set_caption("Tiles")

    font = pygame.font.SysFont("Arial", 20)
    
    clock = pygame.time.Clock()
    running = True

    dt = 0
    player_score = 0

    list_of_rows: List[Row] = []
    row = Row()
    list_of_rows.append(row)

    line = Line()

    while running:

        if list_of_rows[-1].get_height() >= 0:
            row = Row()
            list_of_rows.append(row)

        if list_of_rows[0].get_height() >= SCREEN_HEIGHT:
            if not list_of_rows[0].is_killed():
                player_score -= 2
            del list_of_rows[0]

        #render game
        screen.fill("white")

        line.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Your final score was -> {player_score}")
                running = False
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_a: #A KEY
                    if list_of_rows[0].get_decided() == 0:
                        if not list_of_rows[0].is_killed():
                            if list_of_rows[0].get_height() in range(SCREEN_HEIGHT - 190, SCREEN_HEIGHT + 10):
                                player_score += 1
                                list_of_rows[0].kill_row()
                                list_of_rows[0].tiles[0].set_color("green")
                            
                elif event.key == pygame.K_s: #S KEY
                    if list_of_rows[0].get_decided() == 1:
                        if not list_of_rows[0].is_killed():
                            if list_of_rows[0].get_height() in range(SCREEN_HEIGHT - 190, SCREEN_HEIGHT + 10):
                                player_score += 1
                                list_of_rows[0].kill_row()
                                list_of_rows[0].tiles[1].set_color("green")
                            
                elif event.key == pygame.K_d: #D KEY
                    if list_of_rows[0].get_decided() == 2:
                        if not list_of_rows[0].is_killed():
                            if list_of_rows[0].get_height() in range(SCREEN_HEIGHT - 190, SCREEN_HEIGHT + 10):
                                player_score += 1
                                list_of_rows[0].kill_row()
                                list_of_rows[0].tiles[2].set_color("green")
                            
                elif event.key == pygame.K_f: #F KEY
                    if list_of_rows[0].get_decided() == 3:
                        if not list_of_rows[0].is_killed():
                            if list_of_rows[0].get_height() in range(SCREEN_HEIGHT - 190, SCREEN_HEIGHT + 10):
                                player_score += 1
                                list_of_rows[0].kill_row()
                                list_of_rows[0].tiles[3].set_color("green")
                    
        
        for row in list_of_rows:
            row.update()
            row.draw(screen)

        line.draw(screen)

        
        ###SCORE TEXT
        score_surface = font.render(f"Score: {player_score}", True, (255, 0, 0) )
        text_rect = score_surface.get_rect()
        text_rect.topright = (SCREEN_WIDTH - 10, 10)
        screen.blit(score_surface, text_rect)

        
        # flip() the display to put your work on screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000


    #close game
    pygame.quit()
    exit(0)




if __name__ == "__main__":
    main()

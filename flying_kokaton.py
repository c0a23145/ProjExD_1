import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    bird_img = pg.image.load("fig/3.png")
    bird_img = pg.transform.flip(bird_img, True, False)##鳥の左右反転
    bird_rct = bird_img.get_rect()
    bird_rct.center = 300, 200
    tmr = 0
    while True:
        
        key_lst = pg.key.get_pressed()

        for event in pg.event.get():
            
            if event.type == pg.QUIT: 
                return
        x = -(tmr%3200)
        screen.blit(bg_img, [(x), 0])
        screen.blit(bg_img2, [(x+1600), 0])
        screen.blit(bg_img, [(x+3200), 0])
        screen.blit(bg_img2, [(x+4800), 0])
        ##screen.blit(bird_img, [300-tmr,200])#  #screen Surfaiceに鳥のイメージ
        screen.blit(bird_img, bird_rct)
        dx, dy = 0, 0  
        if key_lst[pg.K_UP]:
            dy = -1
        if key_lst[pg.K_DOWN]:
            dy = 1
        if key_lst[pg.K_RIGHT]:
            dx = 1
        else :
            dx = -1
        if key_lst[pg.K_LEFT]:
            dx = -1

        bird_rct.move_ip(dx, dy)

        
       
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
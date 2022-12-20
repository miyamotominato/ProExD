import pygame as pg
import random
import sys


class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 

"""  ---攻撃手段製作途中---
class Bullet:
    def __init__(self,img_path, ratio, speed):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):

        if pg.K_SPACE:

        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()
"""

class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)                    


class Bomb:
    def __init__(self, img_path, ratio, vxy, scr:Screen):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate



def main():
    clock =pg.time.Clock()

    scr = Screen("逃げろ！こうかとん", (1600,900), "fig/pg_bg.jpg")

    kkt = Bird("fig/7.png", 2.0, (900,400))
    kkt.update(scr)

    #爆弾追加
    bkd_lst = []
    for i in range(5):
        #bkd = Bomb("fig/3.png", 1.5,  (+1, +1), scr)
        #bkd.update(scr)
        bkd_lst.append(Bomb("ex05/data/alien1.png", 1.0,  (+1, +1), scr))#"fig/3.png"

    while True:        
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.update(scr)

        for i in bkd_lst:
            i.update(scr)

            if kkt.rct.colliderect(i.rct):
                jikan = pg.time.get_ticks()
                fonto = pg.font.Font(None,80)
                txt = fonto.render(f"{int(jikan/1000)}seconds escape",True,(255,0,0))
                scr.sfc.blit(txt,(500,200))
                fonto = pg.font.Font(None,80)
                txt = fonto.render("Game Over",True,(255,0,0))
                scr.sfc.blit(txt,(500,400))
                pg.display.update()
                clock.tick(0.5)
                return 

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
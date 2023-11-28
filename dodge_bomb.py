import sys
import random
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    tmr = 0
    
    bb_img = pg.Surface((20,20))  #練習1：透明なsurfaceを作る
    bb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bb_img, (255,0,0),(10,10),10)  #練習1：赤い円を透明な正方形の中心(10,10)に描画
    bb_rct = bb_img.get_rect()
    bb_rct.centerx = random.randint(0, WIDTH)
    bb_rct.centery = random.randint(0, HEIGHT)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:#×ボタンを押されたらリターン　閉じる
                return

        screen.blit(bg_img, [0, 0])#写真をスクリーンに貼り付ける
        screen.blit(kk_img, [900, 400])#貼り付ける順番も大事
        screen.blit(bb_img, bb_rct)#rctで座標を
        pg.display.update()#スクリーンを更新する。変更を加えても更新しなければ意味が無い
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
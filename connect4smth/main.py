import pygame as py
py.init()
screen=py.display.set_mode((800,800))
py.display.set_caption("connect")
running=True
archer=py.image.load("connect4smth\\Screenshot_2026-08-03_184804-removebg-preview.png")
knight=py.image.load("connect4smth\\Screenshot_2026-08-03_184848-removebg-preview.png")
wizzard=py.image.load("connect4smth\\Screenshot_2026-08-03_184956-removebg-preview.png")

archer=py.transform.scale(archer, (100, 100))
knight=py.transform.scale(knight, (100, 100))
wizzard=py.transform.scale(wizzard, (100, 100))

wizzs=wizzard.get_rect()
knights=knight.get_rect()
arcs=archer.get_rect()


wand=py.image.load("connect4smth\\Screenshot_2026-08-10_180407-removebg-preview.png")
sword=py.image.load("connect4smth\\Screenshot_2026-08-10_180435-removebg-preview.png")
bow=py.image.load("connect4smth\\Screenshot_2026-08-10_180508-removebg-preview.png")

wand=py.transform.scale(wand, (100, 100))
sword=py.transform.scale(sword, (100, 100))
bow=py.transform.scale(bow, (100, 100))

wands=wand.get_rect()
swords=sword.get_rect() 
bows=bow.get_rect()


wizzs.center=(150, 100)
knights.center=(150, 250)
arcs.center=(150, 400)

wands.center=(450, 250)
swords.center=(450, 400)
bows.center=(450, 100)

l1=False
l2= False
l3= False

ww= False
ws= False
wb= False

kw= False
ks= False
kb= False

ab= False
asw= False
aw= False


while running:
    for events in py.event.get():
        if events.type==py.QUIT:
            running = False
    screen.fill ("light blue")
    screen.blit(sword, swords)
    screen.blit(archer, arcs)
    screen.blit(wizzard, wizzs)
    screen.blit(knight, knights)
    screen.blit(bow, bows)
    screen.blit(wand, wands)
    py.display.update()

py.quit()



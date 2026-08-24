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


font1= py.font.SysFont("Arial", 20)
font2= py.font.SysFont("Arial", 40)
text1= font1.render("instructions: match the following characters to their weapons/objects that correlate to their existance.",  "black", True)
text2= font2.render("result: ",  "black", True)

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
ars= False
aw= False


def mouseup(e):
    if swords.collidepoint(e):
        print ("swocket")
        if l1:
            kw= False
            kb= False
        if l2:
            ww= False
            wb= False
        if l3:
            aw= False
            ab= False
    if wands.collidepoint(e):
        print ("wand spell here")
        if l1:
            ks= False
            kb= False
        if l2:
            ws= False
            wb= False
        if l3:
            ars= False
            ab= False
    if bows.collidepoint(e):
        print ("the bowstring snapped")
        if l1:
            kw= False
            ks= False
        if l2:
            ww= False
            ws= False
        if l3:
            aw= False
            ars= False




while running:
    for events in py.event.get():
        if events.type==py.QUIT:
            running = False
        if events.type== py.MOUSEBUTTONDOWN:
            if knights.collidepoint(events.pos) and l1==False:
                kw= True
                ks=True
                kb=True
                l1=True
                print("kni")
            if wizzs.collidepoint(events.pos) and l2==False:
                ww= True
                ws=True
                wb=True
                l2=True
                print("wizzair")
            if arcs.collidepoint(events.pos) and l3==False:
                aw= True
                ars=True
                ab=True
                l3=True
                print("argh")

        if events.type==py.MOUSEBUTTONUP:
                if swords.collidepoint(events.pos):

                    print ("swocket")
                    if l1 and ks:
                        kw= False
                        kb= False
                     #   ks = True
                    if l2 and ws:
                        ww= False
                        wb= False
                      #  ws = True
                    if l3 and ars:
                        aw= False
                        ab= False
                     #   ars = True
                if wands.collidepoint(events.pos):
                    print ("wand spell here")
                    if l1 and kw:
                        ks= False
                        kb= False
                    #    kw= True
                    if l2 and ww:
                        ws= False
                        wb= False
                    #    ww= True
                    if l3 and aw:
                        ars= False
                        ab= False
                    #    aw= True
                if bows.collidepoint(events.pos):
                    print ("the bowstring snapped")
                    if l1 and kb:
                        kw= False
                        ks= False
                     #   kb= True
                    if l2 and wb:
                        ww= False
                        ws= False
                      #  wb= True
                    if l3 and ab:
                        aw= False
                        ars= False
                      #  ab= True


    screen.fill ("light blue")
    screen.blit(sword, swords)
    screen.blit(archer, arcs)
    screen.blit(wizzard, wizzs)
    screen.blit(knight, knights)
    screen.blit(bow, bows)
    screen.blit(wand, wands)
    screen.blit(text1, (30,530))
    screen.blit(text2, (30,600))
    if l1:
        #print ("11") #swoket
        if ks:
            py.draw.line(screen, "red", knights.center, swords.center, width=4)
        if kw:
            py.draw.line(screen, "blue", knights.center, wands.center, width=4)
        if kb:
            py.draw.line(screen, "green", knights.center, bows.center, width=4)
    if l2:
        #print ("12") #archer
        if ws:
            py.draw.line(screen, "red", wizzs.center, swords.center, width=4)
        if ww:
            py.draw.line(screen, "blue", wizzs.center, wands.center, width=4)
        if wb:
            py.draw.line(screen, "green", wizzs.center, bows.center, width=4)

    if l3:
        #print ("13") #wizzair

        if ars:
            py.draw.line(screen, "red", arcs.center, swords.center, width=4)
        if aw:
            py.draw.line(screen, "blue", arcs.center, wands.center, width=4)
        if ab:
            py.draw.line(screen, "green", arcs.center, bows.center, width=4)
    if l1 and l2 and l3:
      if ks and ww and ab: 
         text2= font2.render("result: 3/3 Well donwwee!11!",  "black", True)
      else:
         text2= font2.render("result: how stoopid can u b",  "black", True)
    
    

    py.display.update()

py.quit()



# -*- coding: utf-8 -*-
import pygame
from PIL import Image
from bs4 import BeautifulSoup
from pygame.locals import *
from defs import *
import time
import urllib.request

pygame.init()

infoObject = pygame.display.Info()

screen = pygame.display.set_mode((1024, 768)) #infoObject.current_w, infoObject.current_h
fpsClock = pygame.time.Clock()

FPS = 30

key = [False, False, False, False, False]

day = '7월 13일'
menu = '(블랙데이)자장면(&밥소량), 파인탕 수육, 단무지, 요구르트'
menu.strip()
menuNames = menu.split()
menuNumber = int(len(menuNames))

if menuNumber >= 4:
    m1 = school(menuNames[0])
    m2 = school(menuNames[1])
    m3 = school(menuNames[2])
    m4 = school(menuNames[3])
    allMenu = [m1, m2, m3, m4]
    if menuNumber >= 5:
        m5 = school(menuNames[4])
        allMenu.append(m5)
        if menuNumber >= 6:
            m6 = school(menuNames[5])
            allMenu.append(m6)
            if menuNumber >= 7:
                m7 = school(menuNames[6])
                allMenu.append(m7)



menuIm = Image.open('S/M.jpg')

size = (500, 400)
menuIm.thumbnail(size)

menuIm.save('S/menuImage.png')

menuImage = pygame.image.load('S/menuImage.png')

starZero = pygame.image.load("S/ZERO.png")
starOne = pygame.image.load("S/ONE.png")
starTwo = pygame.image.load("S/TWO.png")
starThree = pygame.image.load("S/THREE.png")
starFour = pygame.image.load("S/FOUR.png")
starFive = pygame.image.load("S/FIVE.png")


starImage = starZero
n = 0
x = 600
font = pygame.font.Font("BMHANNA_11yrs_ttf.ttf", 70)
fonts = pygame.font.Font("BMHANNA_11yrs_ttf.ttf", 40)



while True:
    one = 0
    screen.fill((255, 255, 255))

    screen.blit(menuImage, [50, 30])
    screen.blit(starImage, [162, 600])

    choiceManu = allMenu[n]

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:

            if event.key == K_a:
                school.average(m1)
                school.average(m2)
                school.average(m3)
                school.average(m4)
                if menuNumber >= 5:
                    school.average(m5)
                    if menuNumber >= 6:
                        school.average(m6)
                        if menuNumber >= 7:
                            school.average(m7)

            if event.key == K_KP1:
                starImage = starOne
                if one == 0:
                    choiceManu.allstar(int(1))
                    one = 1
                    if n == menuNumber-1:
                        n = 0
                    else:
                       n += 1


            if event.key == K_KP2:
                starImage = starTwo
                if one == 0:
                    choiceManu.allstar(int(2))
                    one = 1
                    if n == menuNumber-1:
                        n = 0
                    else:
                        n += 1


            if event.key == K_KP3:
                starImage = starThree
                if one == 0:
                    choiceManu.allstar(int(3))
                    one = 1
                    if n == menuNumber-1:
                        n = 0
                    else:
                        n += 1


            if event.key == K_KP4:
                starImage = starFour
                if one == 0:
                    choiceManu.allstar(int(4))
                    one = 1
                    if n == menuNumber-1:
                        n = 0
                    else:
                        n += 1


            if event.key == K_KP5:
                starImage = starFive
                if one == 0:
                    choiceManu.allstar(int(5))
                    one = 1
                    if n == menuNumber-1:
                        n = 0
                    else:
                        n += 1


        if event.type == pygame.KEYUP:

            if event.key == K_KP1:
                key[0] = False

            if event.key == K_KP2:
                key[1] = False

            if event.key == K_KP3:
                key[2] = False

            if event.key == K_KP4:
                key[3] = False

            if event.key == K_KP5:
                key[4] = False


    daytext = fonts.render('-' + day + '-', True, (0, 0, 0))
    daytextRect = daytext.get_rect()
    daytextRect.topleft = [x, 30]
    screen.blit(daytext, daytextRect)

    menu1text = fonts.render(menuNames[0], True, (0, 0, 0))
    menu1textRect = menu1text.get_rect()
    menu1textRect.topleft = [x, 90]
    screen.blit(menu1text, menu1textRect)

    menu2text = fonts.render(menuNames[1], True, (0, 0, 0))
    menu2textRect = menu2text.get_rect()
    menu2textRect.topleft = [x, 140]
    screen.blit(menu2text, menu2textRect)

    menu3text = fonts.render(menuNames[2], True, (0, 0, 0))
    menu3textRect = menu3text.get_rect()
    menu3textRect.topleft = [x, 190]
    screen.blit(menu3text, menu3textRect)

    menu4text = fonts.render(menuNames[3], True, (0, 0, 0))
    menu4textRect = menu4text.get_rect()
    menu4textRect.topleft = [x, 240]
    screen.blit(menu4text, menu4textRect)

    if menuNumber >= 5:
        menu5text = fonts.render(menuNames[4], True, (0, 0, 0))
        menu5textRect = menu5text.get_rect()
        menu5textRect.topleft = [x, 290]
        screen.blit(menu5text, menu5textRect)

        if menuNumber >= 6:
            menu6text = fonts.render(menuNames[5], True, (0, 0, 0))
            menu6textRect = menu6text.get_rect()
            menu6textRect.topleft = [x, 340]
            screen.blit(menu6text, menu6textRect)

            if menuNumber >= 7:
                menu7text = fonts.render(menuNames[6], True, (0, 0, 0))
                menu7textRect = menu7text.get_rect()
                menu7textRect.topleft = [x, 390]
                screen.blit(menu7text, menu7textRect)

    menuNametext = font.render("%s의" % (choiceManu.manuName), True, (0, 0, 0))
    menuNametextRect = menuNametext.get_rect()
    menuNametextRect.center = [512, 470]
    screen.blit(menuNametext, menuNametextRect)

    startext = font.render("별점은?", True, (0, 0, 0))
    startextRect = startext.get_rect()
    startextRect.center = [512, 550]
    screen.blit(startext, startextRect)

    pygame.display.update()
    fpsClock.tick(FPS)
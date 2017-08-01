# -*- coding: utf-8 -*-

import pygame
from PIL import Image
from pygame.locals import *
from defs import *
import time
from bs4 import BeautifulSoup
import datetime
import requests
import calendar
import urllib.request


def create_form():
    return {
        "access_token": access_token,
        "band_key": band_key,
        "content": content,
    }

def main():
    response = requests.post(request_url, data=create_form())

    print(response.status_code)


################################
today = datetime.datetime.now()
todayData = today.strftime('%Y-%m-%d').split('-')
yearData = int(todayData[0])
monthData = int(todayData[1])
dayData= int(todayData[2])


roopTrue = True
starRoopTrue = False
if dayData > 1:
    realDayData = dayData - 1
    realMonthData = monthData

else:
    realMonthData = monthData - 1
    realDayData = int(calendar.monthrange(yearData, monthData)[1])

while roopTrue:



    menuUrl = 'http://www.siheung.hs.kr/' \
              'main.php?menugrp=080702&master=' \
              'meal2&act=list&SearchYear=%s&' \
              'SearchMonth=%s&SearchDay=%s#diary_list' \
              %(yearData, realMonthData, realDayData)


    req = requests.get(menuUrl)
    html = req.text


    soup = BeautifulSoup(html, 'html.parser')

    my_titles = soup.select(
        "td"
    )

    menuPlusNumber = [None]
    for title in my_titles:
        if type(title.text) == str:
            menuPlusNumber.append(title.text)



    if menuPlusNumber[-1] == "등록된 식단 정보가 없습니다.":
        menuPlusNumber = [None]
        print(menuUrl)
        print('메뉴 없음')

        if realDayData > 1:
            realDayData = realDayData - 1

        else:
            realMonthData = realMonthData- 1
            realDayData = int(calendar.monthrange(yearData, realMonthData)[1])


    else:
        print(menuUrl)
        print("메뉴 찾음",menuPlusNumber[-1])
        menu = menuPlusNumber[-1]


        my_image = soup.select(
            "#meal_container > div.meal_content.col-md-7 > div > table > tbody > tr > td > p > img"
        )
        for link in my_image:
            imageUrl = 'http://www.siheung.hs.kr/'+link.get('src')

            headers = {'Referer': menuUrl}
            img_data = requests.get(imageUrl, headers=headers).content

            with open('S/M.jpg', 'wb') as f:
                f.write(img_data)

        starRoopTrue = True
        roopTrue = False


################################


pygame.init()

pygame.display.set_caption('School Meal Star v2.1')

infoObject = pygame.display.Info()
x, y = infoObject.current_w, infoObject.current_h

screen = pygame.display.set_mode((x, y),FULLSCREEN)
fpsClock = pygame.time.Clock()

FPS = 30

key = [False, False, False, False, False]

day = '%s월 %s일'%(realMonthData,realDayData)

menu.strip()
menuNames = menu.split()
menuNumber = int(len(menuNames))

menuAverage = [None]

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



menuImg = Image.open('S/M.jpg')
w, h = menuImg.size
if h > w:
    menuImg.transpose(Image.ROTATE_90)

size = (500/1024*x, 400/768*y)
menuImg.thumbnail(size)
menuImg.save('S/menuImage.png')

menuImage = pygame.image.load('S/menuImage.png')

star0Img = Image.open("S/0.png")
star1Img = Image.open("S/1.png")
star2Img = Image.open("S/2.png")
star3Img = Image.open("S/3.png")
star4Img = Image.open("S/4.png")
star5Img = Image.open("S/5.png")

starsize = (700/1024*x, 126/768*y)
star0Img.thumbnail(starsize)
star1Img.thumbnail(starsize)
star2Img.thumbnail(starsize)
star3Img.thumbnail(starsize)
star4Img.thumbnail(starsize)
star5Img.thumbnail(starsize)

star0Img.save('S/ZERO.png')
star1Img.save('S/ONE.png')
star2Img.save('S/TWO.png')
star3Img.save('S/THREE.png')
star4Img.save('S/FOUR.png')
star5Img.save('S/FIVE.png')

starZero = pygame.image.load("S/ZERO.png")
starOne = pygame.image.load("S/ONE.png")
starTwo = pygame.image.load("S/TWO.png")
starThree = pygame.image.load("S/THREE.png")
starFour = pygame.image.load("S/FOUR.png")
starFive = pygame.image.load("S/FIVE.png")

y6Img = Image.open('S/y6.png')
y6size = (800/1280*x, 600/800*y)
y6Img.thumbnail(y6size)
y6Img.save('S/y6s.png')

y6 = pygame.image.load("S/y6s.png")

Beep = pygame.mixer.Sound("S/Beep.wav")

starImage = starZero
n = 0
w = 600/1024 * x
font = pygame.font.Font("BMHANNA_11yrs_ttf.ttf", int(70/768*y))
fonts = pygame.font.Font("BMHANNA_11yrs_ttf.ttf", int(40/768*y))

imageIO = 0

intro = 0

while starRoopTrue:
    if intro == 0 :
        y6Rect = y6.get_rect()
        y6Rect.center = [1/2*x, 1/2*y]
        screen.fill((255, 255, 255))
        screen.blit(y6, y6Rect)
        pygame.display.update()
        fpsClock.tick(FPS)
        time.sleep(1)
        intro = 1



    starImageRect = starImage.get_rect()
    starImageRect.center = [1/2*x, 670/768*y]
    one = 0
    if imageIO == 0:
        starImage = starZero
    else:
        Beep.play()
        one = 1
        time.sleep(1)
        imageIO = 0




    screen.fill((255, 255, 255))

    screen.blit(menuImage, [50/1024 *x, 30/768 *y])
    screen.blit(starImage, starImageRect)

    choiceManu = allMenu[n]


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit(0)

            if event.key == K_a:
                request_url = "https://openapi.band.us/v2.2/band/post/create"
                access_token = "ZQAAAZblYVX0JXWqjhoOxCcugYjAGDaokeMUh4git3_XXHPmYRV1K-Qm20W" \
                               "OoyCndUSOaPAJEMtQMItw4XBHDAnF6P6_Qg210pa7Ux8ZXW6Ad6Pb"
                band_key = "AAAyMKZ4VCFpe92WMyTPFJrF"

                content = '%s월 %s일 급식\n\n' \
                          '1.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                          '2.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                          '3.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                          '4.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                          '홈페이지 : %s' \
                          % (realMonthData, realDayData,
                             menuNames[0], m1.allStar, m1.allPeolpe, round(m1.average,1),
                             menuNames[1], m2.allStar, m2.allPeolpe, round(m2.average,1),
                             menuNames[2], m3.allStar, m3.allPeolpe, round(m3.average,1),
                             menuNames[3], m4.allStar, m4.allPeolpe, round(m4.average,1),
                             menuUrl)
                if menuNumber >= 5:
                    content = '%s월 %s일 급식\n\n' \
                              '1.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                              '2.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                              '3.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                              '4.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                              '5.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                              '홈페이지 : %s' \
                              % (realMonthData, realDayData,
                                 menuNames[0], m1.allStar, m1.allPeolpe, round(m1.average,1),
                                 menuNames[1], m2.allStar, m2.allPeolpe, round(m2.average,1),
                                 menuNames[2], m3.allStar, m3.allPeolpe, round(m3.average,1),
                                 menuNames[3], m4.allStar, m4.allPeolpe, round(m4.average,1),
                                 menuNames[4], m5.allStar, m5.allPeolpe, round(m5.average,1),
                                 menuUrl)

                    if menuNumber >= 6:
                        content = '%s월 %s일 급식\n\n' \
                                  '1.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                                  '2.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                                  '3.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                                  '4.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                                  '5.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                                  '6.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                                  '홈페이지 : %s' \
                                  % (realMonthData, realDayData,
                                     menuNames[0], m1.allStar, m1.allPeolpe, round(m1.average,1),
                                     menuNames[1], m2.allStar, m2.allPeolpe, round(m2.average,1),
                                     menuNames[2], m3.allStar, m3.allPeolpe, round(m3.average,1),
                                     menuNames[3], m4.allStar, m4.allPeolpe, round(m4.average,1),
                                     menuNames[4], m5.allStar, m5.allPeolpe, round(m5.average,1),
                                     menuNames[5], m6.allStar, m6.allPeolpe, round(m6.average,1),
                                     menuUrl)
                        if menuNumber >= 7:
                            content = '%s월 %s일 급식\n\n' \
                                      '1.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                                      '2.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                                      '3.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                                      '4.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                                      '5.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                                      '6.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                                      '7.%s\n별합: %s,  투표자: %s,  평균별점: %s\n\n' \
                                      '홈페이지 : %s' \
                                      % (realMonthData, realDayData,
                                         menuNames[0], m1.allStar, m1.allPeolpe, round(m1.average,1),
                                         menuNames[1], m2.allStar, m2.allPeolpe, round(m2.average,1),
                                         menuNames[2], m3.allStar, m3.allPeolpe, round(m3.average,1),
                                         menuNames[3], m4.allStar, m4.allPeolpe, round(m4.average,1),
                                         menuNames[4], m5.allStar, m5.allPeolpe, round(m5.average,1),
                                         menuNames[5], m6.allStar, m6.allPeolpe, round(m6.average,1),
                                         menuNames[6], m7.allStar, m7.allPeolpe, round(m7.average,1),
                                         menuUrl)

                main()
                pygame.quit()
                exit(0)

            if event.key == K_KP1:
                starImage = starOne
                screen.blit(starImage, starImageRect)
                if one == 0:
                    choiceManu.allstar(int(1))
                    one = 1
                    if n == menuNumber - 1:
                        n = 0
                        imageIO = 1
                    else:
                        n += 1
                        imageIO = 1


            if event.key == K_KP2:
                starImage = starTwo
                screen.blit(starImage, starImageRect)
                if one == 0:
                    choiceManu.allstar(int(2))
                    one = 1
                    if n == menuNumber-1:
                        n = 0
                        imageIO = 1
                    else:
                        n += 1
                        imageIO = 1


            if event.key == K_KP3:
                starImage = starThree
                screen.blit(starImage, starImageRect)
                if one == 0:
                    choiceManu.allstar(int(3))
                    one = 1
                    if n == menuNumber-1:
                        n = 0
                        imageIO = 1
                    else:
                        n += 1
                        imageIO = 1


            if event.key == K_KP4:
                starImage = starFour
                screen.blit(starImage, starImageRect)
                if one == 0:
                    choiceManu.allstar(int(4))
                    one = 1
                    if n == menuNumber-1:
                        n = 0
                        imageIO = 1
                    else:
                        n += 1
                        imageIO = 1


            if event.key == K_KP5:
                starImage = starFive
                screen.blit(starImage, starImageRect)
                if one == 0:
                    choiceManu.allstar(int(5))
                    one = 1
                    if n == menuNumber-1:
                        n = 0
                        imageIO = 1
                    else:
                        n += 1
                        imageIO = 1


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
    daytextRect.topleft = [w, 30/768 *y]
    screen.blit(daytext, daytextRect)

    menu1text = fonts.render(menuNames[0], True, (0, 0, 0))
    menu1textRect = menu1text.get_rect()
    menu1textRect.topleft = [w, 90/768 *y]
    screen.blit(menu1text, menu1textRect)

    menu2text = fonts.render(menuNames[1], True, (0, 0, 0))
    menu2textRect = menu2text.get_rect()
    menu2textRect.topleft = [w, 140/768 *y]
    screen.blit(menu2text, menu2textRect)

    menu3text = fonts.render(menuNames[2], True, (0, 0, 0))
    menu3textRect = menu3text.get_rect()
    menu3textRect.topleft = [w, 190/768 *y]
    screen.blit(menu3text, menu3textRect)

    menu4text = fonts.render(menuNames[3], True, (0, 0, 0))
    menu4textRect = menu4text.get_rect()
    menu4textRect.topleft = [w, 240/768 *y]
    screen.blit(menu4text, menu4textRect)

    if menuNumber >= 5:
        menu5text = fonts.render(menuNames[4], True, (0, 0, 0))
        menu5textRect = menu5text.get_rect()
        menu5textRect.topleft = [w, 290/768 *y]
        screen.blit(menu5text, menu5textRect)

        if menuNumber >= 6:
            menu6text = fonts.render(menuNames[5], True, (0, 0, 0))
            menu6textRect = menu6text.get_rect()
            menu6textRect.topleft = [w, 340/768 *y]
            screen.blit(menu6text, menu6textRect)

            if menuNumber >= 7:
                menu7text = fonts.render(menuNames[6], True, (0, 0, 0))
                menu7textRect = menu7text.get_rect()
                menu7textRect.topleft = [w, 390/768 *y]
                screen.blit(menu7text, menu7textRect)

    menuNametext = font.render("%s의" % (choiceManu.manuName), True, (0, 0, 0))
    menuNametextRect = menuNametext.get_rect()
    menuNametextRect.center = [x/2, 490/768 *y]
    screen.blit(menuNametext, menuNametextRect)

    startext = font.render("별점은?", True, (0, 0, 0))
    startextRect = startext.get_rect()
    startextRect.center = [x/2, 570/768 *y]
    screen.blit(startext, startextRect)

    pygame.display.update()
    fpsClock.tick(FPS)
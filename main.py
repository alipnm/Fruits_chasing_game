from os.path import exists
from random import randint
from apple import Apple
from apricot import Apricot
from banana import Banana
from blackberry import Blackberry
from blueberry import Blueberry
from button import Button
from cherry import Cherry
from constants import *
from dragonfruit import Dragonfruit
from golden_apple import GoldenApple
from kiwi import Kiwi
from mango import Mango
from peach import Peach
from player import Player
money = 0
highmoney = 0
if exists("assets/highmoney.txt"):
    with open("assets/highmoney.txt", 'r') as f:
        highmoney = int(f.read())
shop_button = Button(150, 75, "Shop")
shop_button.rect.centerx = SCREEN_WIDTH / 4
money_text = GAME_FONT.render(f"Money:{money}$", True, (255,0,0))
money_rect = money_text.get_rect(centerx=SCREEN_WIDTH / 4 * 2)
highmoney_text = GAME_FONT.render(f"Highmoney:{highmoney}$", True, (255,0,0))
highmoney_rect = highmoney_text.get_rect(centerx=SCREEN_WIDTH / 4 * 3)
apple_group = pygame.sprite.Group()
golden_apple_group = pygame.sprite.Group()
banana_group = pygame.sprite.Group()
cherry_group = pygame.sprite.Group()
apricot_group = pygame.sprite.Group()
peach_group = pygame.sprite.Group()
kiwi_group = pygame.sprite.Group()
blackberry_group = pygame.sprite.Group()
mango_group = pygame.sprite.Group()
blueberry_group = pygame.sprite.Group()
dragonfruit_group = pygame.sprite.Group()
fruits_available = ['apple']
player = Player()
def check_collisions():
    global money, highmoney
    for apple in apple_group:
        if pygame.sprite.collide_mask(apple, player):
            score_sound.play()
            money += apple.price
            if money > highmoney:
                highmoney = money
            apple.kill()
    for golden_apple in golden_apple_group:
        if pygame.sprite.collide_mask(golden_apple, player):
            score_sound.play()
            money += golden_apple.price
            if money > highmoney:
                highmoney = money
            golden_apple.kill()
    for banana in banana_group:
        if pygame.sprite.collide_mask(banana, player):
            score_sound.play()
            money += banana.price
            if money > highmoney:
                highmoney = money
            banana.kill()
    for cherry in cherry_group:
        if pygame.sprite.collide_mask(cherry, player):
            score_sound.play()
            money += cherry.price
            if money > highmoney:
                highmoney = money
            cherry.kill()
    for apricot in apricot_group:
        if pygame.sprite.collide_mask(apricot, player):
            score_sound.play()
            money += apricot.price
            if money > highmoney:
                highmoney = money
            apricot.kill()
    for peach in peach_group:
        if pygame.sprite.collide_mask(peach, player):
            score_sound.play()
            money += peach.price
            if money > highmoney:
                highmoney = money
            peach.kill()
    for kiwi in kiwi_group:
        if pygame.sprite.collide_mask(kiwi, player):
            score_sound.play()
            money += kiwi.price
            if money > highmoney:
                highmoney = money
            kiwi.kill()
    for blackberry in blackberry_group:
        if pygame.sprite.collide_mask(blackberry, player):
            score_sound.play()
            money += blackberry.price
            if money > highmoney:
                highmoney = money
            blackberry.kill()
    for mango in mango_group:
        if pygame.sprite.collide_mask(mango, player):
            score_sound.play()
            money += mango.price
            if money > highmoney:
                highmoney = money
            mango.kill()
    for blueberry in blueberry_group:
        if pygame.sprite.collide_mask(blueberry, player):
            score_sound.play()
            money += blueberry.price
            if money > highmoney:
                highmoney = money
            blueberry.kill()
    for dragonfruit in dragonfruit_group:
        if pygame.sprite.collide_mask(dragonfruit, player):
            score_sound.play()
            money += dragonfruit.price
            if money > highmoney:
                highmoney = money
            dragonfruit.kill()
def shop():
    global running, money
    page = 1
    limit_p = 11
    hint_txt = GAME_FONT.render("Press key left or right to switch pages.", True, (255,0,0))
    hint_rct = hint_txt.get_rect(centerx=SCREEN_WIDTH / 2)
    page_txt = GAME_FONT.render(f"{page}", True, (255,0,0))
    page_rct = page_txt.get_rect(top=hint_rct.bottom + 20, centerx = hint_rct.centerx)
    exit_button = Button(150, 75, "Exit")
    exit_button.rect.bottom = SCREEN_HEIGHT
    exit_button.rect.centerx = SCREEN_WIDTH / 2
    store = True
    while store:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    store = False
                    running = False
                    with open("assets/highmoney.txt", 'w') as f:
                        f.write(str(highmoney))
                elif event.key == pygame.K_RIGHT:
                    if page < limit_p:
                        page += 1
                elif event.key == pygame.K_LEFT:
                    if page > 1:
                        page -= 1
        screen.fill((0,0,0))
        if exit_button.check_click():
            apple_group.empty()
            golden_apple_group.empty()
            banana_group.empty()
            cherry_group.empty()
            apricot_group.empty()
            peach_group.empty()
            kiwi_group.empty()
            blackberry_group.empty()
            mango_group.empty()
            blueberry_group.empty()
            dragonfruit_group.empty()
            store = False
        exit_button.draw()
        if page == 1:
            avail = False
            if not 'apple' in fruits_available:
                png = pygame.image.load("assets/Apple.png")
                apple_mask = pygame.mask.from_surface(png)
                png.fill((0,0,0))
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                pygame.draw.lines(png, (255,0,0), True, apple_mask.outline())
                screen.blit(png, rct)
            else:
                avail = True
                png = pygame.image.load("assets/Apple.png")
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                screen.blit(png, rct)
            if avail:
                a_text = GAME_FONT.render("Available", True, (0,255,0))
            else:
                a_text = GAME_FONT.render("Not available", True, (255,0,0))
            a_rect = a_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5 * 2))
            price_text = GAME_FONT.render("Cost: 1$ per one.", True, (0,0,255))
            price_rect = price_text.get_rect(top=a_rect.bottom + 10, centerx=a_rect.centerx)
            screen.blit(a_text, a_rect)
            screen.blit(price_text, price_rect)
            if not 'apple' in fruits_available:
                unlockp_text = GAME_FONT.render("Price to unlock: 10$", True, (255,255,255))
                unlockp_rect = unlockp_text.get_rect(top=price_rect.bottom + 10, centerx=a_rect.centerx)
                ymoney_text = GAME_FONT.render(f"Your money: {money}$", True, (255,255,255))
                ymoney_rect = ymoney_text.get_rect(top=unlockp_rect.bottom + 10, centerx = SCREEN_WIDTH / 2)
                buy_button = Button(150, 75, 'Buy')
                buy_button.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 * 2)
                if buy_button.check_click():
                    if money >= 10:
                        money -= 10
                        fruits_available.append('apple')
                screen.blit(unlockp_text, unlockp_rect)
                screen.blit(ymoney_text, ymoney_rect)
                buy_button.draw()
        elif page == 2:
            avail = False
            if not 'golden apple' in fruits_available:
                png = pygame.image.load("assets/Golden apple.png")
                golden_apple_mask = pygame.mask.from_surface(png)
                png.fill((0,0,0))
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                pygame.draw.lines(png, (255,0,0), True, golden_apple_mask.outline())
                screen.blit(png, rct)
            else:
                avail = True
                png = pygame.image.load("assets/Golden apple.png")
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                screen.blit(png, rct)
            if avail:
                a_text = GAME_FONT.render("Available", True, (0,255,0))
            else:
                a_text = GAME_FONT.render("Not available", True, (255,0,0))
            a_rect = a_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5 * 2))
            price_text = GAME_FONT.render("Cost: 2$ per one.", True, (0,0,255))
            price_rect = price_text.get_rect(top=a_rect.bottom + 10, centerx=a_rect.centerx)
            screen.blit(a_text, a_rect)
            screen.blit(price_text, price_rect)
            if not 'golden apple' in fruits_available:
                unlockp_text = GAME_FONT.render("Price to unlock: 20$", True, (255,255,255))
                unlockp_rect = unlockp_text.get_rect(top=price_rect.bottom + 10, centerx=a_rect.centerx)
                ymoney_text = GAME_FONT.render(f"Your money: {money}$", True, (255,255,255))
                ymoney_rect = ymoney_text.get_rect(top=unlockp_rect.bottom + 10, centerx = SCREEN_WIDTH / 2)
                buy_button = Button(150, 75, 'Buy')
                buy_button.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 * 2)
                if buy_button.check_click():
                    if money >= 20:
                        money -= 20
                        fruits_available.append('golden apple')
                screen.blit(unlockp_text, unlockp_rect)
                screen.blit(ymoney_text, ymoney_rect)
                buy_button.draw()
        elif page == 3:
            avail = False
            if not 'banana' in fruits_available:
                png = pygame.image.load("assets/Banana.png")
                banana_mask = pygame.mask.from_surface(png)
                png.fill((0,0,0))
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                pygame.draw.lines(png, (255,0,0), True, banana_mask.outline())
                screen.blit(png, rct)
            else:
                avail = True
                png = pygame.image.load("assets/Banana.png")
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                screen.blit(png, rct)
            if avail:
                a_text = GAME_FONT.render("Available", True, (0,255,0))
            else:
                a_text = GAME_FONT.render("Not available", True, (255,0,0))
            a_rect = a_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5 * 2))
            price_text = GAME_FONT.render("Cost: 3$ per one.", True, (0,0,255))
            price_rect = price_text.get_rect(top=a_rect.bottom + 10, centerx=a_rect.centerx)
            screen.blit(a_text, a_rect)
            screen.blit(price_text, price_rect)
            if not 'banana' in fruits_available:
                unlockp_text = GAME_FONT.render("Price to unlock: 40$", True, (255,255,255))
                unlockp_rect = unlockp_text.get_rect(top=price_rect.bottom + 10, centerx=a_rect.centerx)
                ymoney_text = GAME_FONT.render(f"Your money: {money}$", True, (255,255,255))
                ymoney_rect = ymoney_text.get_rect(top=unlockp_rect.bottom + 10, centerx = SCREEN_WIDTH / 2)
                buy_button = Button(150, 75, 'Buy')
                buy_button.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 * 2)
                if buy_button.check_click():
                    if money >= 40:
                        money -= 40
                        fruits_available.append('banana')
                screen.blit(unlockp_text, unlockp_rect)
                screen.blit(ymoney_text, ymoney_rect)
                buy_button.draw()
        elif page == 4:
            avail = False
            if not 'cherry' in fruits_available:
                png = pygame.image.load("assets/Cherry.png")
                cherry_mask = pygame.mask.from_surface(png)
                png.fill((0,0,0))
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                pygame.draw.lines(png, (255,0,0), True, cherry_mask.outline())
                screen.blit(png, rct)
            else:
                avail = True
                png = pygame.image.load("assets/Cherry.png")
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                screen.blit(png, rct)
            if avail:
                a_text = GAME_FONT.render("Available", True, (0,255,0))
            else:
                a_text = GAME_FONT.render("Not available", True, (255,0,0))
            a_rect = a_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5 * 2))
            price_text = GAME_FONT.render("Cost: 4$ per one.", True, (0,0,255))
            price_rect = price_text.get_rect(top=a_rect.bottom + 10, centerx=a_rect.centerx)
            screen.blit(a_text, a_rect)
            screen.blit(price_text, price_rect)
            if not 'cherry' in fruits_available:
                unlockp_text = GAME_FONT.render("Price to unlock: 80$", True, (255,255,255))
                unlockp_rect = unlockp_text.get_rect(top=price_rect.bottom + 10, centerx=a_rect.centerx)
                ymoney_text = GAME_FONT.render(f"Your money: {money}$", True, (255,255,255))
                ymoney_rect = ymoney_text.get_rect(top=unlockp_rect.bottom + 10, centerx = SCREEN_WIDTH / 2)
                buy_button = Button(150, 75, 'Buy')
                buy_button.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 * 2)
                if buy_button.check_click():
                    if money >= 80:
                        money -= 80
                        fruits_available.append('cherry')
                screen.blit(unlockp_text, unlockp_rect)
                screen.blit(ymoney_text, ymoney_rect)
                buy_button.draw()
        elif page == 5:
            avail = False
            if not 'apricot' in fruits_available:
                png = pygame.image.load("assets/Apricot.png")
                apricot_mask = pygame.mask.from_surface(png)
                png.fill((0,0,0))
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                pygame.draw.lines(png, (255,0,0), True, apricot_mask.outline())
                screen.blit(png, rct)
            else:
                avail = True
                png = pygame.image.load("assets/Apricot.png")
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                screen.blit(png, rct)
            if avail:
                a_text = GAME_FONT.render("Available", True, (0,255,0))
            else:
                a_text = GAME_FONT.render("Not available", True, (255,0,0))
            a_rect = a_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5 * 2))
            price_text = GAME_FONT.render("Cost: 5$ per one.", True, (0,0,255))
            price_rect = price_text.get_rect(top=a_rect.bottom + 10, centerx=a_rect.centerx)
            screen.blit(a_text, a_rect)
            screen.blit(price_text, price_rect)
            if not 'apricot' in fruits_available:
                unlockp_text = GAME_FONT.render("Price to unlock: 160$", True, (255,255,255))
                unlockp_rect = unlockp_text.get_rect(top=price_rect.bottom + 10, centerx=a_rect.centerx)
                ymoney_text = GAME_FONT.render(f"Your money: {money}$", True, (255,255,255))
                ymoney_rect = ymoney_text.get_rect(top=unlockp_rect.bottom + 10, centerx = SCREEN_WIDTH / 2)
                buy_button = Button(150, 75, 'Buy')
                buy_button.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 * 2)
                if buy_button.check_click():
                    if money >= 160:
                        money -= 160
                        fruits_available.append('apricot')
                screen.blit(unlockp_text, unlockp_rect)
                screen.blit(ymoney_text, ymoney_rect)
                buy_button.draw()
        elif page == 6:
            avail = False
            if not 'peach' in fruits_available:
                png = pygame.image.load("assets/Peach.png")
                peach_mask = pygame.mask.from_surface(png)
                png.fill((0,0,0))
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                pygame.draw.lines(png, (255,0,0), True, peach_mask.outline())
                screen.blit(png, rct)
            else:
                avail = True
                png = pygame.image.load("assets/Peach.png")
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                screen.blit(png, rct)
            if avail:
                a_text = GAME_FONT.render("Available", True, (0,255,0))
            else:
                a_text = GAME_FONT.render("Not available", True, (255,0,0))
            a_rect = a_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5 * 2))
            price_text = GAME_FONT.render("Cost: 6$ per one.", True, (0,0,255))
            price_rect = price_text.get_rect(top=a_rect.bottom + 10, centerx=a_rect.centerx)
            screen.blit(a_text, a_rect)
            screen.blit(price_text, price_rect)
            if not 'peach' in fruits_available:
                unlockp_text = GAME_FONT.render("Price to unlock: 320$", True, (255,255,255))
                unlockp_rect = unlockp_text.get_rect(top=price_rect.bottom + 10, centerx=a_rect.centerx)
                ymoney_text = GAME_FONT.render(f"Your money: {money}$", True, (255,255,255))
                ymoney_rect = ymoney_text.get_rect(top=unlockp_rect.bottom + 10, centerx = SCREEN_WIDTH / 2)
                buy_button = Button(150, 75, 'Buy')
                buy_button.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 * 2)
                if buy_button.check_click():
                    if money >= 320:
                        money -= 320
                        fruits_available.append('peach')
                screen.blit(unlockp_text, unlockp_rect)
                screen.blit(ymoney_text, ymoney_rect)
                buy_button.draw()
        elif page == 7:
            avail = False
            if not 'kiwi' in fruits_available:
                png = pygame.image.load("assets/Kiwi.png")
                kiwi_mask = pygame.mask.from_surface(png)
                png.fill((0,0,0))
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                pygame.draw.lines(png, (255,0,0), True, kiwi_mask.outline())
                screen.blit(png, rct)
            else:
                avail = True
                png = pygame.image.load("assets/Kiwi.png")
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                screen.blit(png, rct)
            if avail:
                a_text = GAME_FONT.render("Available", True, (0,255,0))
            else:
                a_text = GAME_FONT.render("Not available", True, (255,0,0))
            a_rect = a_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5 * 2))
            price_text = GAME_FONT.render("Cost: 7$ per one.", True, (0,0,255))
            price_rect = price_text.get_rect(top=a_rect.bottom + 10, centerx=a_rect.centerx)
            screen.blit(a_text, a_rect)
            screen.blit(price_text, price_rect)
            if not 'kiwi' in fruits_available:
                unlockp_text = GAME_FONT.render("Price to unlock: 410$", True, (255,255,255))
                unlockp_rect = unlockp_text.get_rect(top=price_rect.bottom + 10, centerx=a_rect.centerx)
                ymoney_text = GAME_FONT.render(f"Your money: {money}$", True, (255,255,255))
                ymoney_rect = ymoney_text.get_rect(top=unlockp_rect.bottom + 10, centerx = SCREEN_WIDTH / 2)
                buy_button = Button(150, 75, 'Buy')
                buy_button.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 * 2)
                if buy_button.check_click():
                    if money >= 410:
                        money -= 410
                        fruits_available.append('kiwi')
                screen.blit(unlockp_text, unlockp_rect)
                screen.blit(ymoney_text, ymoney_rect)
                buy_button.draw()
        elif page == 8:
            avail = False
            if not 'blackberry' in fruits_available:
                png = pygame.image.load("assets/Blackberry.png")
                blackberry_mask = pygame.mask.from_surface(png)
                png.fill((0,0,0))
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                pygame.draw.lines(png, (255,0,0), True, blackberry_mask.outline())
                screen.blit(png, rct)
            else:
                avail = True
                png = pygame.image.load("assets/Blackberry.png")
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                screen.blit(png, rct)
            if avail:
                a_text = GAME_FONT.render("Available", True, (0,255,0))
            else:
                a_text = GAME_FONT.render("Not available", True, (255,0,0))
            a_rect = a_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5 * 2))
            price_text = GAME_FONT.render("Cost: 8$ per one.", True, (0,0,255))
            price_rect = price_text.get_rect(top=a_rect.bottom + 10, centerx=a_rect.centerx)
            screen.blit(a_text, a_rect)
            screen.blit(price_text, price_rect)
            if not 'blackberry' in fruits_available:
                unlockp_text = GAME_FONT.render("Price to unlock: 500$", True, (255,255,255))
                unlockp_rect = unlockp_text.get_rect(top=price_rect.bottom + 10, centerx=a_rect.centerx)
                ymoney_text = GAME_FONT.render(f"Your money: {money}$", True, (255,255,255))
                ymoney_rect = ymoney_text.get_rect(top=unlockp_rect.bottom + 10, centerx = SCREEN_WIDTH / 2)
                buy_button = Button(150, 75, 'Buy')
                buy_button.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 * 2)
                if buy_button.check_click():
                    if money >= 500:
                        money -= 500
                        fruits_available.append('blackberry')
                screen.blit(unlockp_text, unlockp_rect)
                screen.blit(ymoney_text, ymoney_rect)
                buy_button.draw()
        elif page == 9:
            avail = False
            if not 'mango' in fruits_available:
                png = pygame.image.load("assets/Mango.png")
                mango_mask = pygame.mask.from_surface(png)
                png.fill((0,0,0))
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                pygame.draw.lines(png, (255,0,0), True, mango_mask.outline())
                screen.blit(png, rct)
            else:
                avail = True
                png = pygame.image.load("assets/Mango.png")
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                screen.blit(png, rct)
            if avail:
                a_text = GAME_FONT.render("Available", True, (0,255,0))
            else:
                a_text = GAME_FONT.render("Not available", True, (255,0,0))
            a_rect = a_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5 * 2))
            price_text = GAME_FONT.render("Cost: 9$ per one.", True, (0,0,255))
            price_rect = price_text.get_rect(top=a_rect.bottom + 10, centerx=a_rect.centerx)
            screen.blit(a_text, a_rect)
            screen.blit(price_text, price_rect)
            if not 'mango' in fruits_available:
                unlockp_text = GAME_FONT.render("Price to unlock: 700$", True, (255,255,255))
                unlockp_rect = unlockp_text.get_rect(top=price_rect.bottom + 10, centerx=a_rect.centerx)
                ymoney_text = GAME_FONT.render(f"Your money: {money}$", True, (255,255,255))
                ymoney_rect = ymoney_text.get_rect(top=unlockp_rect.bottom + 10, centerx = SCREEN_WIDTH / 2)
                buy_button = Button(150, 75, 'Buy')
                buy_button.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 * 2)
                if buy_button.check_click():
                    if money >= 700:
                        money -= 700
                        fruits_available.append('mango')
                screen.blit(unlockp_text, unlockp_rect)
                screen.blit(ymoney_text, ymoney_rect)
                buy_button.draw()
        elif page == 10:
            avail = False
            if not 'blueberry' in fruits_available:
                png = pygame.image.load("assets/Blueberry.png")
                blueberry_mask = pygame.mask.from_surface(png)
                png.fill((0,0,0))
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                pygame.draw.lines(png, (255,0,0), True, blueberry_mask.outline())
                screen.blit(png, rct)
            else:
                avail = True
                png = pygame.image.load("assets/Blueberry.png")
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                screen.blit(png, rct)
            if avail:
                a_text = GAME_FONT.render("Available", True, (0,255,0))
            else:
                a_text = GAME_FONT.render("Not available", True, (255,0,0))
            a_rect = a_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5 * 2))
            price_text = GAME_FONT.render("Cost: 10$ per one.", True, (0,0,255))
            price_rect = price_text.get_rect(top=a_rect.bottom + 10, centerx=a_rect.centerx)
            screen.blit(a_text, a_rect)
            screen.blit(price_text, price_rect)
            if not 'blueberry' in fruits_available:
                unlockp_text = GAME_FONT.render("Price to unlock: 875$", True, (255,255,255))
                unlockp_rect = unlockp_text.get_rect(top=price_rect.bottom + 10, centerx=a_rect.centerx)
                ymoney_text = GAME_FONT.render(f"Your money: {money}$", True, (255,255,255))
                ymoney_rect = ymoney_text.get_rect(top=unlockp_rect.bottom + 10, centerx = SCREEN_WIDTH / 2)
                buy_button = Button(150, 75, 'Buy')
                buy_button.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 * 2)
                if buy_button.check_click():
                    if money >= 875:
                        money -= 875
                        fruits_available.append('blueberry')
                screen.blit(unlockp_text, unlockp_rect)
                screen.blit(ymoney_text, ymoney_rect)
                buy_button.draw()
        elif page == 11:
            avail = False
            if not 'dragonfruit' in fruits_available:
                png = pygame.image.load("assets/Dragonfruit.png")
                dragonfruit_mask = pygame.mask.from_surface(png)
                png.fill((0,0,0))
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                pygame.draw.lines(png, (255,0,0), True, dragonfruit_mask.outline())
                screen.blit(png, rct)
            else:
                avail = True
                png = pygame.image.load("assets/Dragonfruit.png")
                rct = png.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
                screen.blit(png, rct)
            if avail:
                a_text = GAME_FONT.render("Available", True, (0,255,0))
            else:
                a_text = GAME_FONT.render("Not available", True, (255,0,0))
            a_rect = a_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5 * 2))
            price_text = GAME_FONT.render("Cost: 11$ per one.", True, (0,0,255))
            price_rect = price_text.get_rect(top=a_rect.bottom + 10, centerx=a_rect.centerx)
            screen.blit(a_text, a_rect)
            screen.blit(price_text, price_rect)
            if not 'dragonfruit' in fruits_available:
                unlockp_text = GAME_FONT.render("Price to unlock: 2000$", True, (255,255,255))
                unlockp_rect = unlockp_text.get_rect(top=price_rect.bottom + 10, centerx=a_rect.centerx)
                ymoney_text = GAME_FONT.render(f"Your money: {money}$", True, (255,255,255))
                ymoney_rect = ymoney_text.get_rect(top=unlockp_rect.bottom + 10, centerx = SCREEN_WIDTH / 2)
                buy_button = Button(150, 75, 'Buy')
                buy_button.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 * 2)
                if buy_button.check_click():
                    if money >= 2000:
                        money -= 2000
                        fruits_available.append('dragonfruit')
                screen.blit(unlockp_text, unlockp_rect)
                screen.blit(ymoney_text, ymoney_rect)
                buy_button.draw()
        hint_txt = GAME_FONT.render("Press key left or right to switch pages.", True, (255,0,0))
        hint_rct = hint_txt.get_rect(centerx=SCREEN_WIDTH / 2)
        page_txt = GAME_FONT.render(f"{page}", True, (255,0,0))
        page_rct = page_txt.get_rect(top=hint_rct.bottom + 20, centerx = hint_rct.centerx)
        screen.blit(hint_txt, hint_rct)
        screen.blit(page_txt, page_rct)
        pygame.display.update()
pygame.mixer.music.play(-1)
timer = pygame.time.get_ticks()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                with open("assets/highmoney.txt", 'w') as f:
                    f.write(str(highmoney))
    screen.fill((0,0,0))
    check_collisions()
    if pygame.time.get_ticks() - timer >= 900:
        timer = pygame.time.get_ticks()
        r = randint(1, len(fruits_available))
        if r == 1:
            if fruits_available[0] == 'apple':
                Apple(randint(0, 1472), 0, apple_group)
            elif fruits_available[0] == 'golden apple':
                GoldenApple(randint(0, 1472), 0, golden_apple_group)
            elif fruits_available[0] == 'banana':
                Banana(randint(0, 1472), 0, banana_group)
            elif fruits_available[0] == 'cherry':
                Cherry(randint(0, 1472), 0, cherry_group)
            elif fruits_available[0] == 'apricot':
                Apricot(randint(0, 1472), 0, apricot_group)
            elif fruits_available[0] == 'peach':
                Peach(randint(0, 1472), 0, peach_group)
            elif fruits_available[0] == 'kiwi':
                Kiwi(randint(0, 1472), 0, kiwi_group)
            elif fruits_available[0] == 'blackberry':
                Blackberry(randint(0, 1472), 0, blackberry_group)
            elif fruits_available[0] == 'mango':
                Mango(randint(0, 1472), 0, mango_group)
            elif fruits_available[0] == 'blueberry':
                Blueberry(randint(0, 1472), 0, blueberry_group)
            elif fruits_available[0] == 'dragonfruit':
                Dragonfruit(randint(0, 1472), 0, dragonfruit_group)
        elif r == 2:
            if fruits_available[1] == 'apple':
                Apple(randint(0, 1472), 0, apple_group)
            elif fruits_available[1] == 'golden apple':
                GoldenApple(randint(0, 1472), 0, golden_apple_group)
            elif fruits_available[1] == 'banana':
                Banana(randint(0, 1472), 0, banana_group)
            elif fruits_available[1] == 'cherry':
                Cherry(randint(0, 1472), 0, cherry_group)
            elif fruits_available[1] == 'apricot':
                Apricot(randint(0, 1472), 0, apricot_group)
            elif fruits_available[1] == 'peach':
                Peach(randint(0, 1472), 0, peach_group)
            elif fruits_available[1] == 'kiwi':
                Kiwi(randint(0, 1472), 0, kiwi_group)
            elif fruits_available[1] == 'blackberry':
                Blackberry(randint(0, 1472), 0, blackberry_group)
            elif fruits_available[1] == 'mango':
                Mango(randint(0, 1472), 0, mango_group)
            elif fruits_available[1] == 'blueberry':
                Blueberry(randint(0, 1472), 0, blueberry_group)
            elif fruits_available[1] == 'dragonfruit':
                Dragonfruit(randint(0, 1472), 0, dragonfruit_group)
        elif r == 3:
            if fruits_available[2] == 'apple':
                Apple(randint(0, 1472), 0, apple_group)
            elif fruits_available[2] == 'golden apple':
                GoldenApple(randint(0, 1472), 0, golden_apple_group)
            elif fruits_available[2] == 'banana':
                Banana(randint(0, 1472), 0, banana_group)
            elif fruits_available[2] == 'cherry':
                Cherry(randint(0, 1472), 0, cherry_group)
            elif fruits_available[2] == 'apricot':
                Apricot(randint(0, 1472), 0, apricot_group)
            elif fruits_available[2] == 'peach':
                Peach(randint(0, 1472), 0, peach_group)
            elif fruits_available[2] == 'kiwi':
                Kiwi(randint(0, 1472), 0, kiwi_group)
            elif fruits_available[2] == 'blackberry':
                Blackberry(randint(0, 1472), 0, blackberry_group)
            elif fruits_available[2] == 'mango':
                Mango(randint(0, 1472), 0, mango_group)
            elif fruits_available[2] == 'blueberry':
                Blueberry(randint(0, 1472), 0, blueberry_group)
            elif fruits_available[2] == 'dragonfruit':
                Dragonfruit(randint(0, 1472), 0, dragonfruit_group)
        elif r == 4:
            if fruits_available[3] == 'apple':
                Apple(randint(0, 1472), 0, apple_group)
            elif fruits_available[3] == 'golden apple':
                GoldenApple(randint(0, 1472), 0, golden_apple_group)
            elif fruits_available[3] == 'banana':
                Banana(randint(0, 1472), 0, banana_group)
            elif fruits_available[3] == 'cherry':
                Cherry(randint(0, 1472), 0, cherry_group)
            elif fruits_available[3] == 'apricot':
                Apricot(randint(0, 1472), 0, apricot_group)
            elif fruits_available[3] == 'peach':
                Peach(randint(0, 1472), 0, peach_group)
            elif fruits_available[3] == 'kiwi':
                Kiwi(randint(0, 1472), 0, kiwi_group)
            elif fruits_available[3] == 'blackberry':
                Blackberry(randint(0, 1472), 0, blackberry_group)
            elif fruits_available[3] == 'mango':
                Mango(randint(0, 1472), 0, mango_group)
            elif fruits_available[3] == 'blueberry':
                Blueberry(randint(0, 1472), 0, blueberry_group)
            elif fruits_available[3] == 'dragonfruit':
                Dragonfruit(randint(0, 1472), 0, dragonfruit_group)
        elif r == 5:
            if fruits_available[4] == 'apple':
                Apple(randint(0, 1472), 0, apple_group)
            elif fruits_available[4] == 'golden apple':
                GoldenApple(randint(0, 1472), 0, golden_apple_group)
            elif fruits_available[4] == 'banana':
                Banana(randint(0, 1472), 0, banana_group)
            elif fruits_available[4] == 'cherry':
                Cherry(randint(0, 1472), 0, cherry_group)
            elif fruits_available[4] == 'apricot':
                Apricot(randint(0, 1472), 0, apricot_group)
            elif fruits_available[4] == 'peach':
                Peach(randint(0, 1472), 0, peach_group)
            elif fruits_available[4] == 'kiwi':
                Kiwi(randint(0, 1472), 0, kiwi_group)
            elif fruits_available[4] == 'blackberry':
                Blackberry(randint(0, 1472), 0, blackberry_group)
            elif fruits_available[4] == 'mango':
                Mango(randint(0, 1472), 0, mango_group)
            elif fruits_available[4] == 'blueberry':
                Blueberry(randint(0, 1472), 0, blueberry_group)
            elif fruits_available[4] == 'dragonfruit':
                Dragonfruit(randint(0, 1472), 0, dragonfruit_group)
        elif r == 6:
            if fruits_available[5] == 'apple':
                Apple(randint(0, 1472), 0, apple_group)
            elif fruits_available[5] == 'golden apple':
                GoldenApple(randint(0, 1472), 0, golden_apple_group)
            elif fruits_available[5] == 'banana':
                Banana(randint(0, 1472), 0, banana_group)
            elif fruits_available[5] == 'cherry':
                Cherry(randint(0, 1472), 0, cherry_group)
            elif fruits_available[5] == 'apricot':
                Apricot(randint(0, 1472), 0, apricot_group)
            elif fruits_available[5] == 'peach':
                Peach(randint(0, 1472), 0, peach_group)
            elif fruits_available[5] == 'kiwi':
                Kiwi(randint(0, 1472), 0, kiwi_group)
            elif fruits_available[5] == 'blackberry':
                Blackberry(randint(0, 1472), 0, blackberry_group)
            elif fruits_available[5] == 'mango':
                Mango(randint(0, 1472), 0, mango_group)
            elif fruits_available[5] == 'blueberry':
                Blueberry(randint(0, 1472), 0, blueberry_group)
            elif fruits_available[5] == 'dragonfruit':
                Dragonfruit(randint(0, 1472), 0, dragonfruit_group)
        elif r == 7:
            if fruits_available[6] == 'apple':
                Apple(randint(0, 1472), 0, apple_group)
            elif fruits_available[6] == 'golden apple':
                GoldenApple(randint(0, 1472), 0, golden_apple_group)
            elif fruits_available[6] == 'banana':
                Banana(randint(0, 1472), 0, banana_group)
            elif fruits_available[6] == 'cherry':
                Cherry(randint(0, 1472), 0, cherry_group)
            elif fruits_available[6] == 'apricot':
                Apricot(randint(0, 1472), 0, apricot_group)
            elif fruits_available[6] == 'peach':
                Peach(randint(0, 1472), 0, peach_group)
            elif fruits_available[6] == 'kiwi':
                Kiwi(randint(0, 1472), 0, kiwi_group)
            elif fruits_available[6] == 'blackberry':
                Blackberry(randint(0, 1472), 0, blackberry_group)
            elif fruits_available[6] == 'mango':
                Mango(randint(0, 1472), 0, mango_group)
            elif fruits_available[6] == 'blueberry':
                Blueberry(randint(0, 1472), 0, blueberry_group)
            elif fruits_available[6] == 'dragonfruit':
                Dragonfruit(randint(0, 1472), 0, dragonfruit_group)
        elif r == 8:
            if fruits_available[7] == 'apple':
                Apple(randint(0, 1472), 0, apple_group)
            elif fruits_available[7] == 'golden apple':
                GoldenApple(randint(0, 1472), 0, golden_apple_group)
            elif fruits_available[7] == 'banana':
                Banana(randint(0, 1472), 0, banana_group)
            elif fruits_available[7] == 'cherry':
                Cherry(randint(0, 1472), 0, cherry_group)
            elif fruits_available[7] == 'apricot':
                Apricot(randint(0, 1472), 0, apricot_group)
            elif fruits_available[7] == 'peach':
                Peach(randint(0, 1472), 0, peach_group)
            elif fruits_available[7] == 'kiwi':
                Kiwi(randint(0, 1472), 0, kiwi_group)
            elif fruits_available[7] == 'blackberry':
                Blackberry(randint(0, 1472), 0, blackberry_group)
            elif fruits_available[7] == 'mango':
                Mango(randint(0, 1472), 0, mango_group)
            elif fruits_available[7] == 'blueberry':
                Blueberry(randint(0, 1472), 0, blueberry_group)
            elif fruits_available[7] == 'dragonfruit':
                Dragonfruit(randint(0, 1472), 0, dragonfruit_group)
        elif r == 9:
            if fruits_available[8] == 'apple':
                Apple(randint(0, 1472), 0, apple_group)
            elif fruits_available[8] == 'golden apple':
                GoldenApple(randint(0, 1472), 0, golden_apple_group)
            elif fruits_available[8] == 'banana':
                Banana(randint(0, 1472), 0, banana_group)
            elif fruits_available[8] == 'cherry':
                Cherry(randint(0, 1472), 0, cherry_group)
            elif fruits_available[8] == 'apricot':
                Apricot(randint(0, 1472), 0, apricot_group)
            elif fruits_available[8] == 'peach':
                Peach(randint(0, 1472), 0, peach_group)
            elif fruits_available[8] == 'kiwi':
                Kiwi(randint(0, 1472), 0, kiwi_group)
            elif fruits_available[8] == 'blackberry':
                Blackberry(randint(0, 1472), 0, blackberry_group)
            elif fruits_available[8] == 'mango':
                Mango(randint(0, 1472), 0, mango_group)
            elif fruits_available[8] == 'blueberry':
                Blueberry(randint(0, 1472), 0, blueberry_group)
            elif fruits_available[8] == 'dragonfruit':
                Dragonfruit(randint(0, 1472), 0, dragonfruit_group)
        elif r == 10:
            if fruits_available[9] == 'apple':
                Apple(randint(0, 1472), 0, apple_group)
            elif fruits_available[9] == 'golden apple':
                GoldenApple(randint(0, 1472), 0, golden_apple_group)
            elif fruits_available[9] == 'banana':
                Banana(randint(0, 1472), 0, banana_group)
            elif fruits_available[9] == 'cherry':
                Cherry(randint(0, 1472), 0, cherry_group)
            elif fruits_available[9] == 'apricot':
                Apricot(randint(0, 1472), 0, apricot_group)
            elif fruits_available[9] == 'peach':
                Peach(randint(0, 1472), 0, peach_group)
            elif fruits_available[9] == 'kiwi':
                Kiwi(randint(0, 1472), 0, kiwi_group)
            elif fruits_available[9] == 'blackberry':
                Blackberry(randint(0, 1472), 0, blackberry_group)
            elif fruits_available[9] == 'mango':
                Mango(randint(0, 1472), 0, mango_group)
            elif fruits_available[9] == 'blueberry':
                Blueberry(randint(0, 1472), 0, blueberry_group)
            elif fruits_available[9] == 'dragonfruit':
                Dragonfruit(randint(0, 1472), 0, dragonfruit_group)
        elif r == 11:
            if fruits_available[10] == 'apple':
                Apple(randint(0, 1472), 0, apple_group)
            elif fruits_available[10] == 'golden apple':
                GoldenApple(randint(0, 1472), 0, golden_apple_group)
            elif fruits_available[10] == 'banana':
                Banana(randint(0, 1472), 0, banana_group)
            elif fruits_available[10] == 'cherry':
                Cherry(randint(0, 1472), 0, cherry_group)
            elif fruits_available[10] == 'apricot':
                Apricot(randint(0, 1472), 0, apricot_group)
            elif fruits_available[10] == 'peach':
                Peach(randint(0, 1472), 0, peach_group)
            elif fruits_available[10] == 'kiwi':
                Kiwi(randint(0, 1472), 0, kiwi_group)
            elif fruits_available[10] == 'blackberry':
                Blackberry(randint(0, 1472), 0, blackberry_group)
            elif fruits_available[10] == 'mango':
                Mango(randint(0, 1472), 0, mango_group)
            elif fruits_available[10] == 'blueberry':
                Blueberry(randint(0, 1472), 0, blueberry_group)
            elif fruits_available[10] == 'dragonfruit':
                Dragonfruit(randint(0, 1472), 0, dragonfruit_group)
    player.move()
    for apple in apple_group:
        money = apple.update(money)
    for golden_apple in golden_apple_group:
        money = golden_apple.update(money)
    for banana in banana_group:
        money = banana.update(money)
    for cherry in cherry_group:
        money = cherry.update(money)
    for apricot in apricot_group:
        money = apricot.update(money)
    for peach in peach_group:
        money = peach.update(money)
    for kiwi in kiwi_group:
        money = kiwi.update(money)
    for blackberry in blackberry_group:
        money = blackberry.update(money)
    for mango in mango_group:
        money = mango.update(money)
    for blueberry in blueberry_group:
        money = blueberry.update(money)
    for dragonfruit in dragonfruit_group:
        money = dragonfruit.update(money)
    if shop_button.check_click():
        shop()
    player.draw()
    apple_group.draw(screen)
    golden_apple_group.draw(screen)
    banana_group.draw(screen)
    cherry_group.draw(screen)
    apricot_group.draw(screen)
    peach_group.draw(screen)
    kiwi_group.draw(screen)
    blackberry_group.draw(screen)
    mango_group.draw(screen)
    blueberry_group.draw(screen)
    dragonfruit_group.draw(screen)
    shop_button.draw()
    money_text = GAME_FONT.render(f"Money:{money}$", True, (255,0,0))
    money_rect = money_text.get_rect(centerx=SCREEN_WIDTH / 4 * 2)
    highmoney_text = GAME_FONT.render(f"Highmoney:{highmoney}$", True, (255,0,0))
    highmoney_rect = highmoney_text.get_rect(centerx=SCREEN_WIDTH / 4 * 3)
    screen.blit(money_text, money_rect)
    screen.blit(highmoney_text, highmoney_rect)
    pygame.display.update()
    clock.tick(FPS)
import sys
import time
import pygame
import requests
import threading

pygame.init()

width = 600
height = 600

TEXT = 'Hola'

def get_btc_price(url='https://api.bitso.com/v3/ticker/'):
    global TEXT

    while True:
        response = requests.get(url)

        if response.status_code == 200:
            payload = response.json().get('payload')[0]
            price = payload.get('last')

            TEXT = f'El precio actual del BTC es: ${price} MXN'

            time.sleep(1)

thread = threading.Thread(target=get_btc_price, daemon=True)
thread.start()

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Texto')

white = (255, 255, 255)
red = (115, 38, 80)
black = (0, 0, 0)

font = pygame.font.Font('Roboto/Roboto-Thin.ttf', 24)

while True:

    text = font.render(TEXT, True, black)
    rect = text.get_rect()
    rect.center = (width // 2, height//2)

    surface.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.blit(text, rect)

    pygame.display.update()

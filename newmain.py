import pygame
import os
from karakter import karakter
from silah_ekipman import *
from zirh_ekipman import *

# Oyun ayarları
WIDTH, HEIGHT = 800, 600
WHITE, BLACK, RED, BLUE, GRAY = (255, 255, 255), (0, 0, 0), (200, 0, 0), (0, 0, 200), (100, 100, 100)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Kart Savaş Oyunu")
clock = pygame.time.Clock()

def kazanankim(self,rakip):
    if rakip.can <= 0 and self.can <= 0:
                print("berabere!")
                exit()
    elif rakip.can <= 0:
                print(f"{self.adi}, kazandi!")
                exit()
    elif self.can <= 0:
                print(f"{rakip.adi}, kazandi!")
                exit()


class Card:
    def __init__(self, name, x, y, effect, cost):
        self.name = name
        self.x, self.y = x, y
        self.start_x, self.start_y = x, y  # Başlangıç pozisyonu
        self.effect = effect
        self.cost = cost
        self.dragging = False
        self.offset_x, self.offset_y = 0, 0

    def draw(self):
        pygame.draw.rect(screen, GRAY, (self.x, self.y, 120, 60))
        font = pygame.font.Font(None, 24)
        text = font.render(self.name, True, WHITE)
        screen.blit(text, (self.x + 10, self.y + 20))

    def check_activation(self):
        if self.y < self.start_y - 50:  # Kart yeterince yukarı kaldırıldıysa aktive olur
            return True
        return False



savasci = karakter(
                BLUE,150,250,
                "savasçi",
                can=200,
                kalkan_gücü=5
                )

hirsiz = karakter(
                RED,600,250,
                "hirsiz",
                can=150,
                silah=bıçak,
                kalkan_gücü=5
                )



# Kartları oluştur
attack_card = Card("Saldırı", 100, 500, "saldir", 5)
defense_card = Card("Savunma", 250, 500, "savun", 5)
inventory_card = Card("Envanter", 400, 500, "inventory", 0)

cards = [attack_card, defense_card, inventory_card]
selected_card = None

turn = "p1"

running = True
while running:
    screen.fill(BLACK)

    # Karakterleri çiz
    savasci.draw(screen)
    hirsiz.draw(screen)

    # Kartları çiz
    for card in cards:
        card.draw()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for card in cards:
                if card.x < event.pos[0] < card.x + 120 and card.y < event.pos[1] < card.y + 60:
                    selected_card = card
                    card.dragging = True
                    card.offset_x = event.pos[0] - card.x
                    card.offset_y = event.pos[1] - card.y

        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_card:
                if selected_card.check_activation() and turn == "p1":
                    if selected_card.effect == "saldir":
                        savasci.vur(hirsiz)
                    elif selected_card.effect == "savun":
                        savasci.savun()
                    turn = "p2"
                    print('sira p2 de')

                elif selected_card.check_activation() and turn == "p2":
                    if selected_card.effect == "saldir":
                        hirsiz.vur(savasci)
                    elif selected_card.effect == "savun":
                        hirsiz.savun()
                    turn = "p1"
                    print('sira p1 de')
                # Kartı eski yerine koy
                selected_card.x = selected_card.start_x
                selected_card.y = selected_card.start_y
                selected_card.dragging = False
                selected_card = None

        elif event.type == pygame.MOUSEMOTION:
            if selected_card and selected_card.dragging:
                selected_card.x = event.pos[0] - selected_card.offset_x
                selected_card.y = event.pos[1] - selected_card.offset_y


    clock.tick(30)

pygame.quit()
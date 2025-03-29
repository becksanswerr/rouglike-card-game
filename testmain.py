import pygame

# Oyun ayarları
WIDTH, HEIGHT = 800, 600
WHITE, BLACK, RED, BLUE, GRAY = (255, 255, 255), (0, 0, 0), (200, 0, 0), (0, 0, 200), (100, 100, 100)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Kart Savaş Oyunu")
clock = pygame.time.Clock()

# Karakter sınıfı
class Character:
    def __init__(self, name, x, y, color):
        self.name = name
        self.hp = 10
        self.energy = 5
        self.x, self.y = x, y
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 50))
        font = pygame.font.Font(None, 24)
        hp_text = font.render(f"HP: {self.hp} | Energy: {self.energy}", True, WHITE)
        screen.blit(hp_text, (self.x - 10, self.y - 30))

# Kart sınıfı
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

# Oyuncu ve düşman karakterleri
player = Character("Player", 600, 250, BLUE)
enemy = Character("Enemy", 150, 250, RED)

# Kartları oluştur
attack_card = Card("Saldırı", 100, 500, "attack", 2)
defense_card = Card("Savunma", 250, 500, "defense", 1)
inventory_card = Card("Envanter", 400, 500, "inventory", 0)

cards = [attack_card, defense_card, inventory_card]
selected_card = None

turn = "player"  # İlk tur oyuncunun

# Ana döngü
running = True
while running:
    screen.fill(BLACK)

    # Karakterleri çiz
    player.draw()
    enemy.draw()

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
                if selected_card.check_activation() and turn == "player":
                    if selected_card.effect == "attack" and player.energy >= selected_card.cost:
                        enemy.hp -= 3
                        player.energy -= selected_card.cost
                    elif selected_card.effect == "defense" and player.energy >= selected_card.cost:
                        player.energy -= selected_card.cost
                    turn = "enemy"
                
                # Kartı eski yerine koy
                selected_card.x = selected_card.start_x
                selected_card.y = selected_card.start_y
                selected_card.dragging = False
                selected_card = None

        elif event.type == pygame.MOUSEMOTION:
            if selected_card and selected_card.dragging:
                selected_card.x = event.pos[0] - selected_card.offset_x
                selected_card.y = event.pos[1] - selected_card.offset_y

    if turn == "enemy":
        if enemy.energy >= 2:
            player.hp -= 2
            enemy.energy -= 2
        turn = "player"
        player.energy = 5
        enemy.energy = 5

    clock.tick(30)

pygame.quit()

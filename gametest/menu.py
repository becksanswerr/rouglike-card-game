import pygame
import sys
import oyun  # Oyun dosyasını içe aktar

# Pygame'i başlat
pygame.init()

# Ekran boyutunu ayarla
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Oyun başlığı
pygame.display.set_caption("Oyun Menüsü")

# Saat objesi
clock = pygame.time.Clock()

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Yazı tipini ayarla
font = pygame.font.Font(None, 50)

# Menü seçenekleri
menu_options = ["Arena", "Karakter", "Ayarlar", "Çıkış"]
menu_rects = []

# Menü konumları
start_y = 200
for i, option in enumerate(menu_options):
    text_surface = font.render(option, True, BLACK)
    text_rect = text_surface.get_rect(center=(screen_width // 2, start_y + i * 80))
    menu_rects.append((text_surface, text_rect))

def main_menu():
    while True:
        # Olayları kontrol et
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i, (_, rect) in enumerate(menu_rects):
                    if rect.collidepoint(mouse_pos):
                        if i == 0:  # Arena
                            print("Arena seçildi!")
                            oyun.start_game(screen)  # Arena seçildiğinde oyun başlar
                        elif i == 1:  # Karakter
                            print("Karakter seçildi!")
                        elif i == 2:  # Ayarlar
                            print("Ayarlar seçildi!")
                        elif i == 3:  # Çıkış
                            pygame.quit()
                            sys.exit()

        # Ekranı temizle
        screen.fill(WHITE)

        # Menü seçeneklerini çiz
        for text_surface, text_rect in menu_rects:
            if text_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, GRAY, text_rect.inflate(10, 10))
            screen.blit(text_surface, text_rect)

        # Ekranı güncelle
        pygame.display.flip()

        # FPS'yi sabitle
        clock.tick(60)

if __name__ == "__main__":
    main_menu()

import pygame
import sys

# Renkler
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Oyuncu kare (x, y, genişlik, yükseklik)
player = pygame.Rect(100, 100, 50, 50)

# Yazı tipini ayarla
font = pygame.font.Font(None, 50)

def draw_text(screen, text, y):
    """Ekrana metin yazmak için yardımcı fonksiyon."""
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, y))
    screen.blit(text_surface, text_rect)

def pause_menu(screen):
    """Pause menüsü."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # ESC'ye basıldığında oyuna dön
                    return
                elif event.key == pygame.K_q:  # Q'ya basıldığında çıkış yap
                    pygame.quit()
                    sys.exit()

        # Ekranı temizle
        screen.fill(GRAY)

        # Pause menüsü seçenekleri
        draw_text(screen, "Oyun Duraklatıldı", 200)
        draw_text(screen, "ESC - Devam Et", 300)
        draw_text(screen, "Q - Çıkış", 400)

        # Ekranı güncelle
        pygame.display.flip()

def start_game(screen):
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # ESC'ye basıldığında pause menüsü aç
                    pause_menu(screen)
        
        # Oyuncu hareketi
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.y -= 5
        if keys[pygame.K_DOWN]:
            player.y += 5
        if keys[pygame.K_LEFT]:
            player.x -= 5
        if keys[pygame.K_RIGHT]:
            player.x += 5
        
        # Ekranı temizle
        screen.fill(WHITE)

        # Oyuncu karakterini çiz
        pygame.draw.rect(screen, BLUE, player)

        # Ekranı güncelle
        pygame.display.flip()

        # FPS'yi sabitle
        clock.tick(60)

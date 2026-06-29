import pygame
import sys

from typeosarus_gui import run_typeosarus
from rhythm_game import run_rhythm_game
from login import run_login

pygame.init()

# -------------------------
# LOGIN FIRST
# -------------------------
run_login()

# -------------------------
# SCREEN
# -------------------------
WIDTH, HEIGHT = 1450, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typeosarus")

clock = pygame.time.Clock()

# -------------------------
# FONTS
# -------------------------
title_font = pygame.font.SysFont("consolas", 72, bold=True)
font = pygame.font.SysFont("consolas", 32)
small_font = pygame.font.SysFont("consolas", 22)

# -------------------------
# COLOURS - Cream Theme
# -------------------------
BG_TOP = (250, 248, 240)
BG_BOTTOM = (240, 235, 220)

PANEL = (245, 240, 230)
TEXT = (100, 120, 90)
ACCENT = (60, 100, 50)  # Deep green
ACCENT_LIGHT = (100, 140, 80)

BUTTON = (235, 228, 215)
BUTTON_HOVER = (225, 218, 205)

# -------------------------
# BUTTONS - Centered with proper sizing
# -------------------------
button_width = 350
button_height = 80
button_spacing = 25

total_height = button_height * 3 + button_spacing * 2
start_y = (HEIGHT - total_height) // 2

type_button = pygame.Rect((WIDTH - button_width) // 2, start_y, button_width, button_height)
rhythm_button = pygame.Rect((WIDTH - button_width) // 2, start_y + button_height + button_spacing, button_width, button_height)
exit_button = pygame.Rect((WIDTH - button_width) // 2, start_y + (button_height + button_spacing) * 2, button_width, button_height)

# -------------------------
# BACKGROUND
# -------------------------
def draw_background():
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(BG_TOP[0] * (1-ratio) + BG_BOTTOM[0] * ratio)
        g = int(BG_TOP[1] * (1-ratio) + BG_BOTTOM[1] * ratio)
        b = int(BG_TOP[2] * (1-ratio) + BG_BOTTOM[2] * ratio)
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

# -------------------------
# BUTTON DRAW - Fixed text fitting
# -------------------------
def draw_button(rect, text, icon=""):
    mouse = pygame.mouse.get_pos()
    colour = BUTTON_HOVER if rect.collidepoint(mouse) else BUTTON
    
    pygame.draw.rect(screen, colour, rect, border_radius=16)
    pygame.draw.rect(screen, ACCENT, rect, 3, border_radius=16)
    
    # Auto-scale font size to fit button
    font_size = 32
    temp_font = pygame.font.SysFont("consolas", font_size, bold=True)
    text_surface = temp_font.render(text, True, ACCENT)
    
    # Reduce font size until text fits in button (with padding)
    while text_surface.get_width() > rect.width - 40 and font_size > 16:
        font_size -= 2
        temp_font = pygame.font.SysFont("consolas", font_size, bold=True)
        text_surface = temp_font.render(text, True, ACCENT)
    
    txt_x = rect.x + rect.width//2 - text_surface.get_width()//2
    txt_y = rect.y + rect.height//2 - text_surface.get_height()//2
    screen.blit(text_surface, (txt_x, txt_y))

# -------------------------
# MAIN LOOP
# -------------------------
running = True

while running:
    clock.tick(60)
    draw_background()
    
    # Main panel - Centered
    panel_width = 550
    panel_height = 500
    panel_x = (WIDTH - panel_width) // 2
    panel_y = (HEIGHT - panel_height) // 2 - 50
    
    pygame.draw.rect(screen, PANEL, (panel_x, panel_y, panel_width, panel_height), border_radius=25)
    pygame.draw.rect(screen, ACCENT, (panel_x, panel_y, panel_width, panel_height), 3, border_radius=25)
    
    # Title - Centered
    title = title_font.render("Typeosarus", True, ACCENT)
    title_x = WIDTH//2 - title.get_width()//2
    title_y = panel_y + 60
    screen.blit(title, (title_x, title_y))
    
    # Subtitle - Centered
    subtitle = small_font.render("Choose Your Game Mode", True, TEXT)
    subtitle_x = WIDTH//2 - subtitle.get_width()//2
    subtitle_y = title_y + title.get_height() + 20
    screen.blit(subtitle, (subtitle_x, subtitle_y))
    
    # Buttons
    draw_button(type_button, "Typeosarus")
    draw_button(rhythm_button, "Rhythm Game")
    draw_button(exit_button, "Exit")
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if type_button.collidepoint(event.pos):
                run_typeosarus()
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                draw_background()
                
            elif rhythm_button.collidepoint(event.pos):
                run_rhythm_game()
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                draw_background()
                
            elif exit_button.collidepoint(event.pos):
                running = False

pygame.quit()
sys.exit()
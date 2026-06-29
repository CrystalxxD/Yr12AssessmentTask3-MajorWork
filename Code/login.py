import pygame
import sys
import os
from cryptography.fernet import Fernet

pygame.init()

# -------------------------
# SCREEN
# -------------------------
WIDTH, HEIGHT = 1450, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Login System")

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
INPUT_BG = (235, 228, 215)
ERROR = (200, 80, 70)

# -------------------------
# FILE SETUP
# -------------------------
ACCOUNTS_DIR = "Code/accounts"

if not os.path.exists(ACCOUNTS_DIR):
    os.makedirs(ACCOUNTS_DIR)

KEY_FILE = f"{ACCOUNTS_DIR}/key.key"

if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "rb") as f:
        key = f.read()
else:
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

cipher = Fernet(key)

# -------------------------
# SAVE ACCOUNT
# -------------------------
def save_account(username, password):
    data = f"{username}:{password}".encode()
    encrypted = cipher.encrypt(data)
    with open(f"{ACCOUNTS_DIR}/{username}.dat", "wb") as f:
        f.write(encrypted)

# -------------------------
# CHECK LOGIN
# -------------------------
def check_login(username, password):
    file_path = f"{ACCOUNTS_DIR}/{username}.dat"
    if not os.path.exists(file_path):
        return False
    try:
        with open(file_path, "rb") as f:
            encrypted = f.read()
        decrypted = cipher.decrypt(encrypted).decode()
        stored_user, stored_pass = decrypted.split(":")
        return stored_user == username and stored_pass == password
    except:
        return False

# -------------------------
# UI ELEMENTS - Centered
# -------------------------
panel_width = 720
panel_height = 600
panel_x = (WIDTH - panel_width) // 2
panel_y = (HEIGHT - panel_height) // 2 - 50

# Input boxes - Centered
box_width = 350
box_height = 55
box_x = (WIDTH - box_width) // 2

username_box = pygame.Rect(box_x, panel_y + 150, box_width, box_height)
password_box = pygame.Rect(box_x, panel_y + 260, box_width, box_height)

# Buttons - Centered
button_main = pygame.Rect((WIDTH - 250) // 2, panel_y + 380, 250, 60)
switch_button = pygame.Rect((WIDTH - 250) // 2, panel_y + 460, 250, 45)

username = ""
password = ""

active_box = None

message = ""
message_colour = TEXT

mode = "login"  # login OR create

# -------------------------
# BACKGROUND
# -------------------------
def draw_background():
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(BG_TOP[0] * (1 - ratio) + BG_BOTTOM[0] * ratio)
        g = int(BG_TOP[1] * (1 - ratio) + BG_BOTTOM[1] * ratio)
        b = int(BG_TOP[2] * (1 - ratio) + BG_BOTTOM[2] * ratio)
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

# -------------------------
# MAIN LOGIN LOOP
# -------------------------
def run_login():
    global username, password, active_box, message, message_colour, mode

    while True:
        clock.tick(60)
        draw_background()
        
        # Main panel - Centered
        pygame.draw.rect(screen, PANEL, (panel_x, panel_y, panel_width, panel_height), border_radius=25)
        pygame.draw.rect(screen, ACCENT, (panel_x, panel_y, panel_width, panel_height), 3, border_radius=25)
        
        # Title - Centered
        title_text = "LOGIN" if mode == "login" else "CREATE ACCOUNT"
        title = title_font.render(title_text, True, ACCENT)
        title_x = WIDTH//2 - title.get_width()//2
        title_y = panel_y + 50
        screen.blit(title, (title_x, title_y))
        
        # Labels - Centered
        username_label = small_font.render("USERNAME", True, TEXT)
        username_label_x = WIDTH//2 - username_label.get_width()//2
        screen.blit(username_label, (username_label_x, panel_y + 120))
        
        password_label = small_font.render("PASSWORD", True, TEXT)
        password_label_x = WIDTH//2 - password_label.get_width()//2
        screen.blit(password_label, (password_label_x, panel_y + 230))
        
        # Input boxes
        pygame.draw.rect(screen, INPUT_BG, username_box, border_radius=12)
        pygame.draw.rect(screen, INPUT_BG, password_box, border_radius=12)
        
        # Input box borders
        username_border_color = ACCENT if active_box == "username" else (200, 195, 185)
        password_border_color = ACCENT if active_box == "password" else (200, 195, 185)
        
        pygame.draw.rect(screen, username_border_color, username_box, 3, border_radius=12)
        pygame.draw.rect(screen, password_border_color, password_box, 3, border_radius=12)
        
        # Input text - Centered inside boxes
        username_text = font.render(username, True, ACCENT)
        username_text_x = username_box.x + (username_box.width - username_text.get_width()) // 2
        username_text_y = username_box.y + (username_box.height - username_text.get_height()) // 2
        screen.blit(username_text, (username_text_x, username_text_y))
        
        password_display = "*" * len(password)
        password_text = font.render(password_display, True, ACCENT)
        password_text_x = password_box.x + (password_box.width - password_text.get_width()) // 2
        password_text_y = password_box.y + (password_box.height - password_text.get_height()) // 2
        screen.blit(password_text, (password_text_x, password_text_y))
        
        # Main button
        btn_text = "LOGIN" if mode == "login" else "CREATE"
        pygame.draw.rect(screen, ACCENT, button_main, border_radius=14)
        btn_surface = font.render(btn_text, True, (245, 240, 230))
        btn_x = button_main.x + button_main.width//2 - btn_surface.get_width()//2
        btn_y = button_main.y + button_main.height//2 - btn_surface.get_height()//2
        screen.blit(btn_surface, (btn_x, btn_y))
        
        # Switch button
        switch_text = "Create Account" if mode == "login" else "Back to Login"
        pygame.draw.rect(screen, INPUT_BG, switch_button, border_radius=10)
        pygame.draw.rect(screen, ACCENT_LIGHT, switch_button, 2, border_radius=10)
        switch_surface = small_font.render(switch_text, True, TEXT)
        switch_x = switch_button.x + switch_button.width//2 - switch_surface.get_width()//2
        switch_y = switch_button.y + switch_button.height//2 - switch_surface.get_height()//2
        screen.blit(switch_surface, (switch_x, switch_y))
        
        # Message - Centered
        if message:
            msg_surface = small_font.render(message, True, message_colour)
            msg_x = WIDTH//2 - msg_surface.get_width()//2
            msg_y = panel_y + panel_height - 40
            screen.blit(msg_surface, (msg_x, msg_y))
        
        pygame.display.update()
        
        # -------------------------
        # EVENTS
        # -------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if username_box.collidepoint(event.pos):
                    active_box = "username"
                elif password_box.collidepoint(event.pos):
                    active_box = "password"
                elif switch_button.collidepoint(event.pos):
                    mode = "create" if mode == "login" else "login"
                    message = ""
                    username = ""
                    password = ""
                elif button_main.collidepoint(event.pos):
                    if mode == "login":
                        if check_login(username, password):
                            return True
                        else:
                            message = "Invalid login"
                            message_colour = ERROR
                    else:
                        if username and password:
                            save_account(username, password)
                            message = "Account created!"
                            message_colour = ACCENT
                            return True
                        else:
                            message = "Please enter username and password"
                            message_colour = ERROR
            
            # keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if active_box == "username":
                        username = username[:-1]
                    elif active_box == "password":
                        password = password[:-1]
                elif event.key == pygame.K_RETURN:
                    if mode == "login":
                        if check_login(username, password):
                            return True
                        else:
                            message = "Invalid login"
                            message_colour = ERROR
                    else:
                        if username and password:
                            save_account(username, password)
                            return True
                        else:
                            message = "Please enter username and password"
                            message_colour = ERROR
                elif event.key == pygame.K_TAB:
                    if active_box == "username":
                        active_box = "password"
                    elif active_box == "password":
                        active_box = "username"
                else:
                    if active_box == "username" and len(username) < 20:
                        username += event.unicode
                    if active_box == "password" and len(password) < 20:
                        password += event.unicode
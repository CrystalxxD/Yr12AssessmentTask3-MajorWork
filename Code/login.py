import pygame
import sys
import os
from cryptography.fernet import Fernet

pygame.init()

# -------------------------
# SCREEN
# -------------------------
WIDTH, HEIGHT = 1450, 800 # Set the window size to 1450x800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Login System") # Set the window title to "Login System"

clock = pygame.time.Clock()

# -------------------------
# FONTS
# -------------------------
title_font = pygame.font.SysFont("consolas", 72, bold=True) # Set the title font to Consolas, size 72, bold
font = pygame.font.SysFont("consolas", 32) # Set the main font to Consolas, size 32
small_font = pygame.font.SysFont("consolas", 22) # Set the small font to Consolas, size 22

# -------------------------
# COLOURS - Cream Theme
# -------------------------
BG_TOP = (250, 248, 240) # Set the top background color to a light cream color
BG_BOTTOM = (240, 235, 220) # Set the bottom background color to a slightly darker cream color

PANEL = (245, 240, 230) # Set the panel color to a light cream color
TEXT = (100, 120, 90) # Set the text color to a dark greenish color
ACCENT = (60, 100, 50)  # Deep green
ACCENT_LIGHT = (100, 140, 80) # Set the accent light color to a lighter green color
INPUT_BG = (235, 228, 215) # Set the input box background color to a light cream color
ERROR = (200, 80, 70) # Set the error color to a reddish color

# -------------------------
# FILE SETUP
# -------------------------
ACCOUNTS_DIR = "Code/accounts" # Set the accounts directory to "Code/accounts"

if not os.path.exists(ACCOUNTS_DIR): # If the accounts directory does not exist, create it
    os.makedirs(ACCOUNTS_DIR)

KEY_FILE = f"{ACCOUNTS_DIR}/key.key" # Set the key file path to "Code/accounts/key.key"

if os.path.exists(KEY_FILE): # If the key file exists, read the key from it
    with open(KEY_FILE, "rb") as f: # Read the key from the key file
        key = f.read()
else:
    key = Fernet.generate_key() # Generate a new key if the key file does not exist
    with open(KEY_FILE, "wb") as f: # Write the new key to the key file
        f.write(key)

cipher = Fernet(key)

# -------------------------
# SAVE ACCOUNT
# -------------------------
def save_account(username, password): # Save the account information to a file
    data = f"{username}:{password}".encode() # Encode the username and password as bytes
    encrypted = cipher.encrypt(data) # Encrypt the data using the cipher
    with open(f"{ACCOUNTS_DIR}/{username}.dat", "wb") as f: # Write the encrypted data to a file named after the username in the accounts directory
        f.write(encrypted)

# -------------------------
# CHECK LOGIN
# -------------------------
def check_login(username, password): # Check if the login information is correct
    file_path = f"{ACCOUNTS_DIR}/{username}.dat" # Set the file path to the account file for the given username
    if not os.path.exists(file_path): # If the account file does not exist, return False
        return False 
    try:
        with open(file_path, "rb") as f: # Read the encrypted data from the account file
            encrypted = f.read() #  Decrypt the data using the cipher
        decrypted = cipher.decrypt(encrypted).decode() # Split the decrypted data into the stored username and password
        stored_user, stored_pass = decrypted.split(":") # Split the decrypted data into the stored username and password
        return stored_user == username and stored_pass == password # Return True if the stored username and password match the input username and password, otherwise return False
    except:
        return False

# -------------------------
# UI ELEMENTS - Centered
# -------------------------
panel_width = 720 # Set the panel width to 720
panel_height = 600 # Set the panel height to 600
panel_x = (WIDTH - panel_width) // 2 # Center the panel horizontally by calculating the x-coordinate based on the window width and panel width
panel_y = (HEIGHT - panel_height) // 2 - 50 # Center the panel vertically by calculating the y-coordinate based on the window height and panel height, with an offset of -50 to move it slightly up

# Input boxes - Centered
box_width = 350 # Set the input box width to 350
box_height = 55 # Set the input box height to 55 
box_x = (WIDTH - box_width) // 2 # Center the input boxes horizontally by calculating the x-coordinate based on the window width and box width

username_box = pygame.Rect(box_x, panel_y + 150, box_width, box_height) # Set the username input box position and size using a pygame Rect object, with the x-coordinate centered and the y-coordinate offset from the panel's y-coordinate by 150 pixels
password_box = pygame.Rect(box_x, panel_y + 260, box_width, box_height) # Set the password input box position and size using a pygame Rect object, with the x-coordinate centered and the y-coordinate offset from the panel's y-coordinate by 260 pixels

# Buttons - Centered
button_main = pygame.Rect((WIDTH - 250) // 2, panel_y + 380, 250, 60) # Set the main button position and size using a pygame Rect object, with the x-coordinate centered and the y-coordinate offset from the panel's y-coordinate by 380 pixels
switch_button = pygame.Rect((WIDTH - 250) // 2, panel_y + 460, 250, 45) # Set the main button and switch button positions and sizes using pygame Rect objects, with the x-coordinates centered and the y-coordinates offset from the panel's y-coordinate by 380 pixels and 460 pixels respectively

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
    for y in range(HEIGHT): # Loop through each pixel row in the window height
        ratio = y / HEIGHT
        r = int(BG_TOP[0] * (1 - ratio) + BG_BOTTOM[0] * ratio) # Calculate the red component of the gradient color based on the ratio of the current pixel row to the total height
        g = int(BG_TOP[1] * (1 - ratio) + BG_BOTTOM[1] * ratio) # Calculate the green component of the gradient color based on the ratio of the current pixel row to the total height
        b = int(BG_TOP[2] * (1 - ratio) + BG_BOTTOM[2] * ratio) # Calculate the blue component of the gradient color based on the ratio of the current pixel row to the total height
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y)) # Draw a horizontal line across the window at the current pixel row with the calculated gradient color
 
# -------------------------
# MAIN LOGIN LOOP
# -------------------------
def run_login():
    global username, password, active_box, message, message_colour, mode # Declare the global variables to be used in the function

    while True:
        clock.tick(60) # Limit the frame rate to 60 frames per second
        draw_background() # Draw the background gradient
        
        # Main panel - Centered
        pygame.draw.rect(screen, PANEL, (panel_x, panel_y, panel_width, panel_height), border_radius=25) # Draw the main panel rectangle with the specified color, position, size, and border radius
        pygame.draw.rect(screen, ACCENT, (panel_x, panel_y, panel_width, panel_height), 3, border_radius=25) # Draw the border of the main panel rectangle with the specified color, position, size, border thickness, and border radius
        
        # Title - Centered
        title_text = "LOGIN" if mode == "login" else "CREATE ACCOUNT" # Set the title text based on the current mode (login or create account)
        title = title_font.render(title_text, True, ACCENT) # Render the title text using the title font and accent color
        title_x = WIDTH//2 - title.get_width()//2 # Calculate the x-coordinate to center the title text horizontally in the window
        title_y = panel_y + 50 # Set the title position to be centered horizontally and offset from the panel's y-coordinate by 50 pixels
        screen.blit(title, (title_x, title_y)) # Draw the title text on the screen at the calculated position
        
        # Labels - Centered
        username_label = small_font.render("USERNAME", True, TEXT) # Render the username label text using the small font and text color
        username_label_x = WIDTH//2 - username_label.get_width()//2 # Calculate the x-coordinate to center the username label text horizontally in the window
        screen.blit(username_label, (username_label_x, panel_y + 120)) # Draw the username label text on the screen at the calculated position, offset from the panel's y-coordinate by 120 pixels
        
        password_label = small_font.render("PASSWORD", True, TEXT) # Render the password label text using the small font and text color
        password_label_x = WIDTH//2 - password_label.get_width()//2 # Calculate the x-coordinate to center the password label text horizontally in the window
        screen.blit(password_label, (password_label_x, panel_y + 230)) # Draw the password label text on the screen at the calculated position, offset from the panel's y-coordinate by 230 pixels
        
        # Input boxes
        pygame.draw.rect(screen, INPUT_BG, username_box, border_radius=12) # Draw the username input box rectangle with the specified color, position, size, and border radius
        pygame.draw.rect(screen, INPUT_BG, password_box, border_radius=12) # Draw the password input box rectangle with the specified color, position, size, and border radius
        
        # Input box borders
        username_border_color = ACCENT if active_box == "username" else (200, 195, 185) # Set the border color of the username input box to accent color if it is active, otherwise set it to a light gray color
        password_border_color = ACCENT if active_box == "password" else (200, 195, 185) # Set the border color of the password input box to accent color if it is active, otherwise set it to a light gray color
        
        pygame.draw.rect(screen, username_border_color, username_box, 3, border_radius=12) # Draw the border of the username input box rectangle with the specified color, position, size, border thickness, and border radius
        pygame.draw.rect(screen, password_border_color, password_box, 3, border_radius=12) # Draw the border of the password input box rectangle with the specified color, position, size, border thickness, and border radius
        
        # Input text - Centered inside boxes
        username_text = font.render(username, True, ACCENT) # Render the username input text using the main font and accent color
        username_text_x = username_box.x + (username_box.width - username_text.get_width()) // 2 # Calculate the x-coordinate to center the username input text horizontally inside the username input box
        username_text_y = username_box.y + (username_box.height - username_text.get_height()) // 2 # Calculate the y-coordinate to center the username input text vertically inside the username input box
        screen.blit(username_text, (username_text_x, username_text_y)) # Draw the username input text on the screen at the calculated position
        
        password_display = "*" * len(password) # Create a string of asterisks to represent the password input text, with the same length as the actual password
        password_text = font.render(password_display, True, ACCENT) # Render the password input text (asterisks) using the main font and accent color
        password_text_x = password_box.x + (password_box.width - password_text.get_width()) // 2 # Calculate the x-coordinate to center the password input text horizontally inside the password input box  
        password_text_y = password_box.y + (password_box.height - password_text.get_height()) // 2 # Calculate the y-coordinate to center the password input text vertically inside the password input box
        screen.blit(password_text, (password_text_x, password_text_y)) # Draw the password input text (asterisks) on the screen at the calculated position
        
        # Main button
        btn_text = "LOGIN" if mode == "login" else "CREATE" # Set the main button text based on the current mode (login or create account)
        pygame.draw.rect(screen, ACCENT, button_main, border_radius=14) # Draw the main button rectangle with the specified color, position, size, and border radius
        btn_surface = font.render(btn_text, True, (245, 240, 230)) # Render the main button text using the main font and a light cream color
        btn_x = button_main.x + button_main.width//2 - btn_surface.get_width()//2 # Calculate the x-coordinate to center the main button text horizontally inside the main button
        btn_y = button_main.y + button_main.height//2 - btn_surface.get_height()//2 # Calculate the y-coordinate to center the main button text vertically inside the main button
        screen.blit(btn_surface, (btn_x, btn_y)) # Draw the main button text on the screen at the calculated position
        
        # Switch button
        switch_text = "Create Account" if mode == "login" else "Back to Login" # Set the switch button text based on the current mode (login or create account)
        pygame.draw.rect(screen, INPUT_BG, switch_button, border_radius=10) # Draw the switch button rectangle with the specified color, position, size, and border radius
        pygame.draw.rect(screen, ACCENT_LIGHT, switch_button, 2, border_radius=10) # Draw the border of the switch button rectangle with the specified color, position, size, border thickness, and border radius
        switch_surface = small_font.render(switch_text, True, TEXT) # Render the switch button text using the small font and text color
        switch_x = switch_button.x + switch_button.width//2 - switch_surface.get_width()//2 # Calculate the x-coordinate to center the switch button text horizontally inside the switch button
        switch_y = switch_button.y + switch_button.height//2 - switch_surface.get_height()//2 # Calculate the y-coordinate to center the switch button text vertically inside the switch button
        screen.blit(switch_surface, (switch_x, switch_y)) # Draw the switch button text on the screen at the calculated position
        
        # Message - Centered
        if message:
            msg_surface = small_font.render(message, True, message_colour) # Render the message text using the small font and the specified message color
            msg_x = WIDTH//2 - msg_surface.get_width()//2 # Calculate the x-coordinate to center the message text horizontally in the window
            msg_y = panel_y + panel_height - 40 # Calculate the x-coordinate to center the message text horizontally in the window and the y-coordinate to position it 40 pixels above the bottom of the panel
            screen.blit(msg_surface, (msg_x, msg_y)) # Draw the message text on the screen at the calculated position
        
        pygame.display.update()
        
        # -------------------------
        # EVENTS
        # -------------------------
        for event in pygame.event.get(): # Handle events in the event queue
            if event.type == pygame.QUIT: # If the user clicks the close button on the window, quit the program
                pygame.quit()
                sys.exit()
            
            # mouse
            if event.type == pygame.MOUSEBUTTONDOWN: # If the user clicks the mouse button, check if they clicked on any of the input boxes or buttons
                if username_box.collidepoint(event.pos):
                    active_box = "username"
                elif password_box.collidepoint(event.pos): # If the user clicks on the password input box, set the active box to "password"
                    active_box = "password"
                elif switch_button.collidepoint(event.pos): # If the user clicks on the switch button, toggle the mode between "login" and "create account", reset the message, username, and password
                    mode = "create" if mode == "login" else "login"
                    message = ""
                    username = ""
                    password = ""
                elif button_main.collidepoint(event.pos): # If the user clicks on the main button, check if they are in "login" or "create account" mode and validate the input accordingly
                    if mode == "login":
                        if check_login(username, password): # If the login is successful, return True to exit the login loop
                            return True
                        else:
                            message = "Invalid login" # If the login is unsuccessful, set the message to "Invalid login" and set the message color to ERROR
                            message_colour = ERROR
                    else:
                        if username and password: # If the user is in "create account" mode and both the username and password fields are filled, save the account information and set the message to "Account created!" with the message color set to ACCENT, then return True to exit the login loop
                            save_account(username, password) # Save the account information to a file using the save_account function
                            message = "Account created!"
                            message_colour = ACCENT
                            return True
                        else:
                            message = "Please enter username and password" # If the user is in "create account" mode and either the username or password field is empty, set the message to "Please enter username and password" and set the message color to ERROR
                            message_colour = ERROR
            
            # keyboard
            if event.type == pygame.KEYDOWN: # If the user presses a key on the keyboard, check if they are in an active input box and handle the input accordingly
                if event.key == pygame.K_BACKSPACE: # If the user presses the backspace key, remove the last character from the active input box (username or password)
                    if active_box == "username": # If the active input box is "username", remove the last character from the username string
                        username = username[:-1] 
                    elif active_box == "password": # If the active input box is "password", remove the last character from the password string
                        password = password[:-1] 
                elif event.key == pygame.K_RETURN: # If the user presses the return/enter key, check if they are in "login" or "create account" mode and validate the input accordingly
                    if mode == "login":
                        if check_login(username, password): # If the login is successful, return True to exit the login loop
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
                    if active_box == "username" and len(username) < 20: # If the active input box is "username" and the username string is less than 20 characters, append the typed character to the username string
                        username += event.unicode
                    if active_box == "password" and len(password) < 20: # If the active input box is "password" and the password string is less than 20 characters, append the typed character to the password string
                        password += event.unicode
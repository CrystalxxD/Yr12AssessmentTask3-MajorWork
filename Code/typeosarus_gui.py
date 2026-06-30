import pygame  # Import pygame for game development
import random  # Import random for generating random words
import time  # Import time for timing typing tests
import os  # Import os for file operations

pygame.init()  # Initialize pygame modules

class SentenceGenerator:
    """Class to generate random sentences from word bank"""
    def __init__(self, file_path="wordbank.txt"):
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory
        full_path = os.path.join(base_dir, file_path)  # Build full file path
        try:
            # Load words from file
            with open(full_path, "r", encoding="utf-8") as f:
                self.words = [w.strip() for w in f if w.strip()]
            print(f"Loaded {len(self.words)} words")
        except:
            # Use default words if file not found
            self.words = ["code", "typing", "system", "python", "speed"]

    def generate(self, count):
        """Generate a list of random words"""
        return [random.choice(self.words) for _ in range(count)]


def run_typeosarus():
    """Main function for the Typeosarus typing game"""
    WIDTH, HEIGHT = 1450, 800  # Window dimensions
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create window
    pygame.display.set_caption("Typeosarus")  # Set window title
    clock = pygame.time.Clock()  # Create clock object

    # Create fonts of different sizes
    FONT = pygame.font.SysFont("consolas", 42, bold=True)
    SMALL = pygame.font.SysFont("consolas", 24)
    SMALLER = pygame.font.SysFont("consolas", 16)

    gen = SentenceGenerator()  # Create sentence generator

    # -------------------------
    # THEMES
    # -------------------------
    themes = {
        "cream": {
            "bg_top": (250, 248, 240), "bg_bottom": (240, 235, 220),
            "text": (160, 150, 130), "subtext": (140, 130, 110),
            "correct": (60, 100, 50), "incorrect": (200, 80, 70),
            "current": (200, 100, 50), "current_bg": (235, 225, 205),
            "particle": (200, 190, 170), "caret": (200, 100, 50), "caret_blink": (60, 100, 50),
            "button_bg": (235, 228, 215), "panel_bg": (245, 240, 230), "stats_bg": (248, 244, 235),
        }
    }
    current_theme = "cream"  # Currently active theme

    # -------------------------
    # STATE
    # -------------------------
    state = "menu"  # Current game state
    words, full_text, typed = [], "", ""  # Word list, full text, and typed text
    start_time, end_time = None, None  # Timing variables
    word_count = 30  # Default word count
    wpm = accuracy = raw_wpm = 0  # Statistics
    scroll_offset = max_scroll_offset = 0  # Scroll position variables

    # -------------------------
    # BACKGROUND PARTICLES
    # -------------------------
    particles = [[random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 3)] for _ in range(80)]

    # -------------------------
    # CAT FRAME ANIMATION
    # -------------------------
    cat_frames, current_frame = [], 0  # Cat animation frames and current frame
    cat_x, cat_y = 120, HEIGHT - 160  # Cat position
    base_path = os.path.join(os.path.dirname(__file__), "bongo")  # Path to cat images

    try:
        # Load cat animation frames from folder
        if os.path.exists(base_path):
            for f in sorted(os.listdir(base_path)):
                if f.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    img = pygame.image.load(os.path.join(base_path, f)).convert_alpha()
                    cat_frames.append(pygame.transform.scale(img, (150, 100)))  # Scale images
    except:
        pass

    if not cat_frames:
        cat_frames = [None]  # Placeholder if no images found

    def advance_cat_frame():
        """Advance to next cat animation frame"""
        nonlocal current_frame
        if cat_frames and len(cat_frames) > 1:
            current_frame = (current_frame + 1) % len(cat_frames)  # Loop animation

    # -------------------------
    # MENU BUTTONS
    # -------------------------
    back_button = pygame.Rect(20, 20, 180, 45)  # Back button rectangle
    menu_buttons = {}  # Dictionary for menu buttons

    # -------------------------
    # SCROLL FUNCTIONS
    # -------------------------
    def get_visible_chars():
        """Calculate how many characters fit on screen"""
        return (WIDTH - 300) // FONT.size("W")[0]  # Rough estimate

    def update_scroll():
        """Update scroll offset based on cursor position"""
        nonlocal scroll_offset, max_scroll_offset
        visible_chars = get_visible_chars()
        cursor_pos = len(typed)
        target = visible_chars - 15  # Keep cursor away from edges
        if cursor_pos < scroll_offset:
            scroll_offset = max(0, cursor_pos - 5)  # Scroll left
        elif cursor_pos >= scroll_offset + target:
            scroll_offset = min(max_scroll_offset, cursor_pos - target + 5)  # Scroll right
        scroll_offset = max(0, min(scroll_offset, max_scroll_offset))

    # -------------------------
    # START TEST
    # -------------------------
    def start_test(n):
        """Start a new typing test with n words"""
        nonlocal words, full_text, typed, start_time, end_time, state, word_count, scroll_offset, max_scroll_offset, current_frame
        word_count = n  # Set word count
        words = gen.generate(n)  # Generate random words
        full_text = " ".join(words)  # Join words into text
        typed = ""  # Reset typed text
        start_time = end_time = None  # Reset timing
        scroll_offset = current_frame = 0  # Reset scroll and animation
        state = "test"  # Switch to test state
        max_scroll_offset = max(0, len(full_text) - get_visible_chars())  # Calculate max scroll

    # -------------------------
    # RESULTS
    # -------------------------
    def calculate_results():
        """Calculate typing statistics"""
        nonlocal wpm, accuracy, raw_wpm, end_time
        if start_time is None:
            return
        end_time = time.time()  # Record end time
        elapsed = max(end_time - start_time, 0.001)  # Calculate elapsed time
        # Count correctly typed characters
        correct = sum(1 for i in range(min(len(typed), len(full_text))) if typed[i] == full_text[i])
        accuracy = (correct / len(full_text)) * 100  # Calculate accuracy percentage
        wpm = ((correct / 5) / elapsed) * 60  # Calculate WPM
        raw_wpm = ((len(typed) / 5) / elapsed) * 60  # Calculate raw WPM

    # -------------------------
    # BACKGROUND
    # -------------------------
    def draw_background():
        """Draw gradient background with particles"""
        theme = themes[current_theme]
        # Draw vertical gradient
        for y in range(HEIGHT):
            r = int(theme["bg_top"][0] * (1 - y / HEIGHT) + theme["bg_bottom"][0] * (y / HEIGHT))
            g = int(theme["bg_top"][1] * (1 - y / HEIGHT) + theme["bg_bottom"][1] * (y / HEIGHT))
            b = int(theme["bg_top"][2] * (1 - y / HEIGHT) + theme["bg_bottom"][2] * (y / HEIGHT))
            pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))
        # Draw floating particles
        for p in particles:
            p[1] += p[2] * 0.2  # Float upward
            if p[1] > HEIGHT:  # Reset at top
                p[0], p[1] = random.randint(0, WIDTH), 0
            pygame.draw.circle(screen, theme["particle"], (int(p[0]), int(p[1])), p[2])

    # -------------------------
    # DRAW CAT
    # -------------------------
    def draw_cat():
        """Draw the cat character or a simple cat shape"""
        if cat_frames and cat_frames[current_frame] is not None:
            screen.blit(cat_frames[current_frame], (cat_x, cat_y))  # Draw animated cat
        else:
            # Draw simple cat shape if no images
            theme = themes[current_theme]
            pygame.draw.ellipse(screen, (100, 120, 80), (cat_x, cat_y + 10, 50, 40))  # Body
            pygame.draw.circle(screen, (100, 120, 80), (cat_x + 45, cat_y + 15), 18)  # Head
            pygame.draw.circle(screen, (255, 255, 255), (cat_x + 52, cat_y + 10), 4)  # Eye white
            pygame.draw.circle(screen, (0, 0, 0), (cat_x + 53, cat_y + 10), 2)  # Eye pupil
            pygame.draw.arc(screen, (0, 0, 0), (cat_x + 42, cat_y + 15, 12, 8), 0, 3.14, 2)  # Mouth
            pygame.draw.line(screen, (100, 120, 80), (cat_x + 35, cat_y + 25), (cat_x + 50, cat_y + 30), 6)  # Tail
            pygame.draw.line(screen, (100, 120, 80), (cat_x + 20, cat_y + 45), (cat_x + 15, cat_y + 55), 6)  # Leg
            pygame.draw.line(screen, (100, 120, 80), (cat_x + 35, cat_y + 45), (cat_x + 30, cat_y + 55), 6)  # Leg
            pygame.draw.line(screen, (100, 120, 80), (cat_x + 10, cat_y + 25), (cat_x - 10, cat_y + 35), 4)  # Arm

    # -------------------------
    # DRAW MENU
    # -------------------------
    def draw_menu():
        """Draw the main menu screen"""
        nonlocal menu_buttons
        draw_background()  # Draw background
        theme = themes[current_theme]
        
        # Draw title
        title = FONT.render("Typeosarus", True, theme["correct"])
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 80))
        subtitle = SMALL.render("Select word count", True, theme["subtext"])
        screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, 180))

        # Create word count buttons
        btn_w, btn_h, btn_spacing = 120, 60, 25
        total_w = (btn_w * 5) + (btn_spacing * 4)
        start_x = (WIDTH - total_w) // 2
        start_y = 250
        
        menu_buttons = {
            10: pygame.Rect(start_x, start_y, btn_w, btn_h),
            15: pygame.Rect(start_x + btn_w + btn_spacing, start_y, btn_w, btn_h),
            30: pygame.Rect(start_x + (btn_w + btn_spacing) * 2, start_y, btn_w, btn_h),
            60: pygame.Rect(start_x + (btn_w + btn_spacing) * 3, start_y, btn_w, btn_h),
            100: pygame.Rect(start_x + (btn_w + btn_spacing) * 4, start_y, btn_w, btn_h),
        }
        
        # Draw each button
        for n, rect in menu_buttons.items():
            pygame.draw.rect(screen, theme["button_bg"], rect, border_radius=8)
            pygame.draw.rect(screen, theme["correct"], rect, 2, border_radius=8)
            fs = 24
            tf = pygame.font.SysFont("consolas", fs, bold=True)
            ts = tf.render(str(n), True, theme["correct"])
            # Adjust font size if text doesn't fit
            while ts.get_width() > rect.width - 20 and fs > 12:
                fs -= 2
                tf = pygame.font.SysFont("consolas", fs, bold=True)
                ts = tf.render(str(n), True, theme["correct"])
            screen.blit(ts, (rect.centerx - ts.get_width() // 2, rect.centery - ts.get_height() // 2))

        # Draw back button
        pygame.draw.rect(screen, theme["button_bg"], back_button, border_radius=10)
        pygame.draw.rect(screen, theme["correct"], back_button, 2, border_radius=10)
        back_text = SMALLER.render("Back to Main Menu", True, theme["correct"])
        screen.blit(back_text, (back_button.x + back_button.width // 2 - back_text.get_width() // 2, back_button.y + 13))
        draw_cat()  # Draw cat

    # -------------------------
    # DRAW TEST
    # -------------------------
    def draw_test():
        """Draw the typing test screen"""
        draw_background()  # Draw background
        theme = themes[current_theme]
        update_scroll()  # Update scroll position

        # Get visible portion of text
        visible_chars, start_idx = get_visible_chars(), scroll_offset
        end_idx = min(scroll_offset + visible_chars, len(full_text))
        visible_text = full_text[start_idx:end_idx]
        text_x = (WIDTH - FONT.size(visible_text)[0]) // 2  # Center text
        text_y = HEIGHT // 2 - 30

        x = text_x  # Start drawing from left
        for i, char in enumerate(visible_text):
            g_idx = start_idx + i  # Global index
            if g_idx < len(typed):
                # Draw typed character (correct or incorrect)
                colour = theme["correct"] if typed[g_idx] == char else theme["incorrect"]
            elif g_idx == len(typed):
                # Draw current character with caret
                colour = theme["current"]
                cs = FONT.render(char, True, colour)
                screen.blit(cs, (x, text_y))
                # Draw underline
                pygame.draw.line(screen, theme["current"], (x, text_y + FONT.get_height() + 2), (x + cs.get_width(), text_y + FONT.get_height() + 2), 3)
                x += cs.get_width()
                continue
            else:
                # Draw future character
                colour = theme["text"]
            cs = FONT.render(char, True, colour)
            screen.blit(cs, (x, text_y))
            x += cs.get_width()

        # Draw blinking caret
        if len(typed) < len(full_text) and pygame.time.get_ticks() % 800 < 400 and start_idx <= len(typed) < end_idx:
            cx = text_x + sum(FONT.size(visible_text[i])[0] for i in range(len(typed) - start_idx))
            caret_color = theme["caret_blink"] if pygame.time.get_ticks() % 400 < 200 else theme["caret"]
            pygame.draw.line(screen, caret_color, (cx, text_y - 5), (cx, text_y + FONT.get_height() + 5), 4)

        # Draw statistics panel
        if start_time and state == "test":
            elapsed = time.time() - start_time
            mins = max(elapsed / 60, 0.001)  # Convert to minutes
            correct = sum(1 for i in range(min(len(typed), len(full_text))) if typed[i] == full_text[i])
            cur_acc = (correct / max(len(full_text), 1)) * 100 if len(typed) > 0 else 0
            cur_wpm = (correct / 5) / mins if elapsed > 0 else 0

            # Stats panel background
            sr = pygame.Rect(30, 40, 300, 220)
            pygame.draw.rect(screen, theme["stats_bg"], sr, border_radius=15)
            pygame.draw.rect(screen, theme["correct"], sr, 2, border_radius=15)

            # WPM display
            wpm_t = FONT.render(f"{int(cur_wpm)}", True, theme["correct"])
            screen.blit(wpm_t, (50, 60))
            screen.blit(SMALL.render("wpm", True, theme["subtext"]), (50 + wpm_t.get_width() + 5, 85))

            # Accuracy display
            acc_t = FONT.render(f"{int(cur_acc)}%", True, theme["correct"])
            screen.blit(acc_t, (50, 130))
            screen.blit(SMALL.render("accuracy", True, theme["subtext"]), (50 + acc_t.get_width() + 5, 155))

            # Progress bar
            prog = len(typed) / len(full_text)
            pygame.draw.rect(screen, (220, 215, 200), (50, 210, 240, 8), border_radius=4)
            pygame.draw.rect(screen, theme["correct"], (50, 210, 240 * prog, 8), border_radius=4)
            screen.blit(SMALLER.render(f"{len(typed)}/{len(full_text)} chars", True, theme["subtext"]), (50, 190))

            # Timer display
            tr = pygame.Rect(WIDTH - 180, 40, 150, 60)
            pygame.draw.rect(screen, theme["stats_bg"], tr, border_radius=10)
            pygame.draw.rect(screen, theme["correct"], tr, 2, border_radius=10)
            screen.blit(SMALL.render(f"{elapsed:.1f}s", True, theme["correct"]), (WIDTH - 160, 60))

        draw_cat()  # Draw cat
        # Position indicator and instructions
        pos_text = SMALLER.render(f"Char {len(typed)}/{len(full_text)}", True, theme["subtext"])
        screen.blit(pos_text, (WIDTH - 150, HEIGHT - 60))
        inst = SMALLER.render("ESC: Exit | Backspace: Delete | Each key advances cat & scrolls", True, theme["subtext"])
        screen.blit(inst, (WIDTH // 2 - inst.get_width() // 2, HEIGHT - 30))

    # -------------------------
    # DRAW RESULTS
    # -------------------------
    def draw_results():
        """Draw the results screen"""
        draw_background()  # Draw background
        theme = themes[current_theme]
        
        # Results panel
        panel_width = 700
        panel_height = 480
        panel_x = (WIDTH - panel_width) // 2
        panel_y = (HEIGHT - panel_height) // 2 - 30
        
        pygame.draw.rect(screen, theme["stats_bg"], (panel_x, panel_y, panel_width, panel_height), border_radius=25)
        pygame.draw.rect(screen, theme["correct"], (panel_x, panel_y, panel_width, panel_height), 3, border_radius=25)
        
        # Title
        title = FONT.render("Test Complete!", True, theme["correct"])
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, panel_y + 30))
        
        # Stats grid - 2x3 layout
        box_width = 200
        box_height = 90
        box_spacing = 30
        start_x = WIDTH // 2 - box_width - box_spacing // 2
        start_y = panel_y + 90
        
        # Row 1: WPM and Raw WPM
        wpm_box = pygame.Rect(start_x, start_y, box_width, box_height) # Draw a rectangle for the "WPM" box
        pygame.draw.rect(screen, (248, 244, 235), wpm_box, border_radius=15) # Draw a filled rectangle for the "WPM" box
        pygame.draw.rect(screen, theme["correct"], wpm_box, 2, border_radius=15) # Draw a border around the "WPM" box
        wpm_v = FONT.render(f"{int(wpm)}", True, theme["correct"]) # Render the WPM value as text
        screen.blit(wpm_v, (wpm_box.centerx - wpm_v.get_width() // 2, wpm_box.y + 15)) # Draw the WPM value centered in the "WPM" box
        wpm_label = SMALL.render("WPM", True, theme["subtext"]) # Render the label "WPM" as text
        screen.blit(wpm_label, (wpm_box.centerx - wpm_label.get_width() // 2, wpm_box.y + 60)) # Draw the label "WPM" centered in the "WPM" box
        
        raw_box = pygame.Rect(start_x + box_width + box_spacing, start_y, box_width, box_height) # Draw a rectangle for the "Raw WPM" box
        pygame.draw.rect(screen, (248, 244, 235), raw_box, border_radius=15) # Draw a filled rectangle for the "Raw WPM" box
        pygame.draw.rect(screen, theme["correct"], raw_box, 2, border_radius=15) # Draw a border around the "Raw WPM" box
        raw_v = FONT.render(f"{int(raw_wpm)}", True, theme["correct"]) # Render the Raw WPM value as text
        screen.blit(raw_v, (raw_box.centerx - raw_v.get_width() // 2, raw_box.y + 15)) # Draw the Raw WPM value centered in the "Raw WPM" box
        raw_label = SMALL.render("RAW WPM", True, theme["subtext"]) # Render the label "RAW WPM" as text
        screen.blit(raw_label, (raw_box.centerx - raw_label.get_width() // 2, raw_box.y + 60)) # Draw the label "RAW WPM" centered in the "Raw WPM" box
        
        # Row 2: Accuracy and Time
        start_y = panel_y + 90 + box_height + box_spacing
        acc_box = pygame.Rect(start_x, start_y, box_width, box_height)
        pygame.draw.rect(screen, (248, 244, 235), acc_box, border_radius=15)
        pygame.draw.rect(screen, theme["correct"], acc_box, 2, border_radius=15)
        acc_v = FONT.render(f"{int(accuracy)}%", True, theme["correct"])
        screen.blit(acc_v, (acc_box.centerx - acc_v.get_width() // 2, acc_box.y + 15))
        acc_label = SMALL.render("ACCURACY", True, theme["subtext"])
        screen.blit(acc_label, (acc_box.centerx - acc_label.get_width() // 2, acc_box.y + 60))
        
        elapsed = end_time - start_time if start_time and end_time else 0
        time_box = pygame.Rect(start_x + box_width + box_spacing, start_y, box_width, box_height)
        pygame.draw.rect(screen, (248, 244, 235), time_box, border_radius=15)
        pygame.draw.rect(screen, theme["correct"], time_box, 2, border_radius=15)
        time_v = SMALL.render(f"{elapsed:.1f}s", True, theme["correct"])
        screen.blit(time_v, (time_box.centerx - time_v.get_width() // 2, time_box.y + 15))
        time_label = SMALL.render("TIME", True, theme["subtext"])
        screen.blit(time_label, (time_box.centerx - time_label.get_width() // 2, time_box.y + 60))
        
        # Row 3: Characters and Completion
        start_y = panel_y + 90 + (box_height + box_spacing) * 2
        char_box = pygame.Rect(start_x, start_y, box_width, box_height)
        pygame.draw.rect(screen, (248, 244, 235), char_box, border_radius=15)
        pygame.draw.rect(screen, theme["correct"], char_box, 2, border_radius=15)
        char_v = SMALL.render(f"{len(full_text)}", True, theme["correct"])
        screen.blit(char_v, (char_box.centerx - char_v.get_width() // 2, char_box.y + 15))
        char_label = SMALL.render("CHARACTERS", True, theme["subtext"])
        screen.blit(char_label, (char_box.centerx - char_label.get_width() // 2, char_box.y + 60))
        
        typed_chars = len(typed)
        total_chars = len(full_text)
        completion = (typed_chars / total_chars * 100) if total_chars > 0 else 0
        comp_box = pygame.Rect(start_x + box_width + box_spacing, start_y, box_width, box_height)
        pygame.draw.rect(screen, (248, 244, 235), comp_box, border_radius=15)
        pygame.draw.rect(screen, theme["correct"], comp_box, 2, border_radius=15)
        comp_v = SMALL.render(f"{completion:.0f}%", True, theme["correct"])
        screen.blit(comp_v, (comp_box.centerx - comp_v.get_width() // 2, comp_box.y + 15))
        comp_label = SMALL.render("COMPLETION", True, theme["subtext"])
        screen.blit(comp_label, (comp_box.centerx - comp_label.get_width() // 2, comp_box.y + 60))
        
        click_msg = SMALLER.render("Click anywhere to return to menu", True, theme["subtext"]) # Instruction to return to menu
        msg_x = WIDTH // 2 - click_msg.get_width() // 2 # Center horizontally
        msg_y = panel_y + panel_height + 30  # Position below the panel
        screen.blit(click_msg, (msg_x, msg_y)) # Draw instruction message

        draw_cat()  # Draw cat

    # -------------------------
    # MAIN LOOP
    # -------------------------
    running = True
    while running:
        clock.tick(60)  # Limit to 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return

            # Handle menu mouse clicks
            if state == "menu" and event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return  # Go back to main menu
                for n, rect in menu_buttons.items():
                    if rect.collidepoint(event.pos):
                        start_test(n)  # Start test with selected word count

            # Handle results click to return to menu
            if state == "results" and event.type == pygame.MOUSEBUTTONDOWN:
                state = "menu"
                current_frame = 0

            # Handle typing test keyboard input
            if state == "test" and event.type == pygame.KEYDOWN:
                if start_time is None:
                    start_time = time.time()  # Start timing on first key press
                if event.key == pygame.K_BACKSPACE:
                    if typed:
                        typed = typed[:-1]  # Remove last character
                        advance_cat_frame()  # Animate cat
                elif event.key == pygame.K_ESCAPE:
                    state = "menu"  # Exit to menu
                    current_frame = start_time = end_time = 0
                elif event.unicode and len(typed) < len(full_text) and event.unicode.isprintable():
                    typed += event.unicode  # Add character
                    advance_cat_frame()  # Animate cat
                if len(typed) >= len(full_text):
                    calculate_results()  # Calculate final stats
                    state = "results"  # Show results

        # Draw based on current state
        if state == "menu":
            draw_menu()
        elif state == "test":
            draw_test()
        elif state == "results":
            draw_results()
        pygame.display.update()  # Update screen

    pygame.quit()  # Quit pygame
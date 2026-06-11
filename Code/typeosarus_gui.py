import pygame
import random
import time
import os

pygame.init()

# -------------------------
# WORD GENERATOR
# -------------------------
class SentenceGenerator:
    def __init__(self, file_path="wordbank.txt"):

        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, file_path)

        try:
            with open(full_path, "r", encoding="utf-8") as f:
                self.words = [w.strip() for w in f if w.strip()]
        except:
            self.words = ["code", "typing", "system", "python", "speed"]

    def generate(self, count):
        return [random.choice(self.words) for _ in range(count)]


# -------------------------
# MAIN GAME
# -------------------------
def run_typeosarus():

    WIDTH, HEIGHT = 1450, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Typeosarus")

    clock = pygame.time.Clock()

    FONT = pygame.font.SysFont("consolas", 36)
    SMALL = pygame.font.SysFont("consolas", 24)
    SMALLER = pygame.font.SysFont("consolas", 16)

    gen = SentenceGenerator()

    # -------------------------
    # THEMES
    # -------------------------
    themes = {
        "cream_green": {
            "bg_top": (245, 240, 225),
            "bg_bottom": (220, 230, 210),
            "text": (60, 90, 60),
            "subtext": (90, 120, 90),
            "correct": (60, 90, 60),
            "incorrect": (180, 80, 80),
            "current": (40, 60, 40),
            "particle": (120, 160, 120),
        }
    }

    current_theme = "cream_green"

    # -------------------------
    # STATE
    # -------------------------
    state = "menu"

    words = []
    full_text = ""
    typed = ""

    start_time = None
    word_count = 30

    wpm = 0
    accuracy = 0

    # -------------------------
    # BACKGROUND PARTICLES
    # -------------------------
    particles = []
    for _ in range(80):
        particles.append([random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 3)])

    # -------------------------
    # CAT ANIMATION
    # -------------------------
    cat_frames = []
    cat_index = 0
    cat_timer = 0
    cat_speed = 120

    cat_x = 120
    cat_bob = 0

    base_path = os.path.join(os.path.dirname(__file__), "bongo")

    try:
        for f in sorted(os.listdir(base_path)):
            img = pygame.image.load(os.path.join(base_path, f)).convert_alpha()
            img = pygame.transform.scale(img, (60, 60))
            cat_frames.append(img)
    except:
        cat_frames = []

    # -------------------------
    # MENU BUTTONS
    # -------------------------
    back_button = pygame.Rect(20, 20, 160, 45)
    buttons = {
        10: pygame.Rect(200, 200, 120, 60),
        15: pygame.Rect(340, 200, 120, 60),
        30: pygame.Rect(480, 200, 120, 60),
        60: pygame.Rect(620, 200, 120, 60),
        100: pygame.Rect(760, 200, 120, 60),
    }

    back_btn = pygame.Rect(WIDTH//2 - 80, 450, 160, 50)

    # -------------------------
    # START TEST
    # -------------------------
    def start_test(n):
        nonlocal words, full_text, typed, start_time, state, word_count

        word_count = n
        words = gen.generate(n)
        full_text = " ".join(words)

        typed = ""
        start_time = None
        state = "test"

    # -------------------------
    # RESULTS
    # -------------------------
    def calculate_results():
        nonlocal wpm, accuracy

        elapsed = max(time.time() - start_time, 0.001)

        typed_words = typed.split()
        original_words = full_text.split()

        correct = 0
        for i in range(min(len(typed_words), len(original_words))):
            if typed_words[i] == original_words[i]:
                correct += 1

        accuracy = (correct / len(original_words)) * 100
        wpm = (len(typed_words) / elapsed) * 60

    # -------------------------
    # BACKGROUND
    # -------------------------
    def draw_background():

        theme = themes[current_theme]

        for i in range(HEIGHT):
            ratio = i / HEIGHT

            r = int(theme["bg_top"][0] * (1 - ratio) + theme["bg_bottom"][0] * ratio)
            g = int(theme["bg_top"][1] * (1 - ratio) + theme["bg_bottom"][1] * ratio)
            b = int(theme["bg_top"][2] * (1 - ratio) + theme["bg_bottom"][2] * ratio)

            pygame.draw.line(screen, (r, g, b), (0, i), (WIDTH, i))

        for p in particles:
            p[1] += p[2] * 0.2

            if p[1] > HEIGHT:
                p[0] = random.randint(0, WIDTH)
                p[1] = 0

            pygame.draw.circle(screen, theme["particle"], (int(p[0]), int(p[1])), p[2])

    # -------------------------
    # DRAW MENU
    # -------------------------
    def draw_menu():

        draw_background()

        theme = themes[current_theme]

        title = FONT.render("Typeosarus", True, theme["text"])
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))

        subtitle = SMALL.render("Select word count", True, theme["subtext"])
        screen.blit(subtitle, (WIDTH//2 - subtitle.get_width()//2, 150))

        for n, rect in buttons.items():
            pygame.draw.rect(screen, (235, 230, 210), rect, border_radius=8)
            pygame.draw.rect(screen, (120, 140, 120), rect, 2, border_radius=8)

            txt = SMALL.render(str(n), True, theme["text"])
            screen.blit(txt, (rect.centerx - txt.get_width()//2,
                              rect.centery - txt.get_height()//2))
            
        pygame.draw.rect(screen, (60, 70, 65), back_button, border_radius=10)
        pygame.draw.rect(screen, (130, 255, 170), back_button, 2, border_radius=10)

        back_text = SMALLER.render("Back to Menu", True, (230, 230, 230))
        screen.blit(back_text, (
            back_button.x + back_button.width//2 - back_text.get_width()//2,
            back_button.y + 10
        ))
    # -------------------------
    # DRAW TEST
    # -------------------------
    def draw_test():

        nonlocal cat_index, cat_timer, cat_bob

        draw_background()

        theme = themes[current_theme]

        x, y = 100, 250

        for i, char in enumerate(full_text):

            if i < len(typed):
                colour = theme["correct"] if typed[i] == char else theme["incorrect"]
            elif i == len(typed):
                colour = theme["current"]
            else:
                colour = (120, 120, 120)

            surf = FONT.render(char, True, colour)
            screen.blit(surf, (x, y))
            x += surf.get_width()

            if x > WIDTH - 100:
                x = 100
                y += 60

        # cat animation
        if cat_frames:
            cat_timer += clock.get_time()

            if cat_timer > cat_speed:
                cat_index = (cat_index + 1) % len(cat_frames)
                cat_timer = 0

            cat_bob *= 0.85
            screen.blit(cat_frames[cat_index], (cat_x, 520 + cat_bob))

    # -------------------------
    # DRAW RESULTS
    # -------------------------
    def draw_results():

        draw_background()

        theme = themes[current_theme]

        title = FONT.render("Results", True, theme["text"])
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 120))

        w = SMALL.render(f"WPM: {int(wpm)}", True, theme["text"])
        a = SMALL.render(f"Accuracy: {int(accuracy)}%", True, theme["text"])

        screen.blit(w, (WIDTH//2 - w.get_width()//2, 220))
        screen.blit(a, (WIDTH//2 - a.get_width()//2, 260))

        pygame.draw.rect(screen, (235, 230, 210), back_btn, border_radius=8)
        pygame.draw.rect(screen, (120, 140, 120), back_btn, 2, border_radius=8)

        txt = SMALL.render("Back to Menu", True, theme["text"])
        screen.blit(txt, (back_btn.centerx - txt.get_width()//2,
                          back_btn.centery - txt.get_height()//2))

    # -------------------------
    # LOOP
    # -------------------------
    running = True

    while running:
        clock.tick(60)

        if state == "menu":
            draw_menu()
        elif state == "test":
            draw_test()
        elif state == "results":
            draw_results()

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if state == "menu" and event.type == pygame.MOUSEBUTTONDOWN:
                for n, rect in buttons.items():
                    if rect.collidepoint(event.pos):
                        start_test(n)

            if state == "results" and event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.collidepoint(event.pos):
                    state = "menu"

            if state == "test" and event.type == pygame.KEYDOWN:

                if start_time is None:
                    start_time = time.time()

                if event.key == pygame.K_BACKSPACE:
                    typed = typed[:-1]
                else:
                    typed += event.unicode
                    cat_bob = -8

                if len(typed) >= len(full_text):
                    calculate_results()
                    state = "results"
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_button.collidepoint(event.pos):
                return   # THIS sends you back to main menu
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state = "menu" 

    pygame.quit()
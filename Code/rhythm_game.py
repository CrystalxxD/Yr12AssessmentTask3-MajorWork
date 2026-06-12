import pygame
import random
import sys
import os

def run_osu_game():
    pygame.init()
    pygame.mixer.init()

    # -------------------------
    # SCREEN
    # -------------------------
    WIDTH, HEIGHT = 900, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("OSU")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 28)
    big_font = pygame.font.SysFont("consolas", 48)

    # -------------------------
    # SONGS + BEATMAPS
    # -------------------------
    SONGS = {
        "1": {
            "name": "Suzume",
            "audio": "Code/music/1music.mp3",
            "beatmap": "Code/beatmaps/1music.map"
        },
        "2": {
            "name": "White Keys",
            "audio": "Code/music/2music.mp3",
            "beatmap": "Code/beatmaps/2music.map"
        },
        "3": {
            "name": "Prairies",
            "audio": "Code/music/3music.mp3",
            "beatmap": "Code/beatmaps/3music.map"
        }
    }

    selected_song = "1"
    song_length_ms = 0  # Will store the song length

    # -------------------------
    # STATE
    # -------------------------
    state = "song_select"

    # -------------------------
    # LANES (8 KEYS)
    # -------------------------
    KEYS = ["a", "s", "d", "f", "h", "j", "k", "l"]
    LANE_COUNT = len(KEYS)
    LANE_WIDTH = WIDTH // LANE_COUNT
    lanes_x = [i * LANE_WIDTH for i in range(LANE_COUNT)]

    HIT_LINE_Y = 520

    # -------------------------
    # GAME VALUES
    # -------------------------
    notes = []
    beatmap = []
    spawn_index = 0

    score = 0
    combo = 0

    perfect_hits = 0
    good_hits = 0
    misses = 0
    accuracy = 0

    judgement_text = ""
    judgement_timer = 0
    
    # Track note hit status
    hit_note_index = None

    running = True

    # -------------------------
    # NOTE CLASS
    # -------------------------
    class Note:
        def __init__(self, lane):
            self.lane = lane
            self.x = lanes_x[lane]
            self.y = -50
            self.key = KEYS[lane]
            self.hit = False  # Track if note has been hit (Perfect/Good)
            self.missed = False  # Track if note was missed

        def update(self):
            if not self.hit:  # Only move if not hit
                self.y += 6

        def draw(self):
            # Different colors for hit/miss status
            if self.hit:
                # Fade out effect for hit notes (will be removed after animation)
                color = (100, 255, 100)
            elif self.missed:
                color = (255, 80, 80)
            else:
                color = (0, 200, 255)
            
            pygame.draw.rect(
                screen,
                color,
                (self.x + 8, self.y, LANE_WIDTH - 16, 25),
                border_radius=6
            )
            
            # Draw key letter on note
            key_text = font.render(self.key.upper(), True, (255, 255, 255))
            screen.blit(key_text, (self.x + LANE_WIDTH//2 - key_text.get_width()//2, self.y + 5))

    # -------------------------
    # GET SONG LENGTH
    # -------------------------
    def get_song_length(song_key):
        try:
            # Load the music file to get its length
            pygame.mixer.music.load(SONGS[song_key]["audio"])
            # pygame doesn't have a direct way to get length, so we'll track time
            return None
        except:
            return None

    # -------------------------
    # LOAD BEATMAP
    # -------------------------
    def load_beatmap(song_key):
        path = SONGS[song_key]["beatmap"]
        data = []

        try:
            with open(path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        t, lane = line.split(",")
                        data.append((int(t), int(lane)))
        except Exception as e:
            print("Missing beatmap:", path, e)

        return data

    # -------------------------
    # RESET GAME
    # -------------------------
    def reset_game():
        nonlocal notes, score, combo
        nonlocal perfect_hits, good_hits, misses
        nonlocal judgement_text, judgement_timer
        nonlocal spawn_index, beatmap, hit_note_index

        notes = []
        score = 0
        combo = 0

        perfect_hits = 0
        good_hits = 0
        misses = 0

        judgement_text = ""
        judgement_timer = 0

        spawn_index = 0
        hit_note_index = None
        beatmap = load_beatmap(selected_song)

    # -------------------------
    # START SONG
    # -------------------------
    def start_song(song_key):
        nonlocal beatmap, spawn_index

        beatmap = load_beatmap(song_key)
        spawn_index = 0

        try:
            pygame.mixer.music.load(SONGS[song_key]["audio"])
            pygame.mixer.music.play()
        except Exception as e:
            print("Error playing music:", e)

    # -------------------------
    # HIT SYSTEM (MS BASED)
    # Notes only disappear on PERFECT/GOOD hits
    # MISS hits count as miss but note stays visible
    # -------------------------
    def check_hit(key_pressed):
        nonlocal score, combo
        nonlocal judgement_text, judgement_timer
        nonlocal perfect_hits, good_hits, misses

        PERFECT_WINDOW = 50
        GOOD_WINDOW = 100

        best = None
        best_diff = 9999
        best_index = -1

        # Find the closest note in the correct lane that hasn't been hit yet
        for i, n in enumerate(notes):
            if n.key == key_pressed and not n.hit and not n.missed:
                diff = abs(n.y - HIT_LINE_Y)
                if diff < best_diff:
                    best = n
                    best_diff = diff
                    best_index = i

        if best is None:
            # No note to hit - this is a miss (but no note disappears)
            combo = 0
            misses += 1
            judgement_text = "MISS"
            judgement_timer = 400
            return

        # Hit the note
        if best_diff <= PERFECT_WINDOW:
            score += 300 * (1 + combo // 10)  # Bonus for higher combo
            combo += 1
            perfect_hits += 1
            judgement_text = "PERFECT"
            best.hit = True  # Mark as hit (will be removed)
            
        elif best_diff <= GOOD_WINDOW:
            score += 150 * (1 + combo // 10)
            combo += 1
            good_hits += 1
            judgement_text = "GOOD"
            best.hit = True  # Mark as hit (will be removed)
            
        else:
            # Hit outside timing window - miss, note stays
            combo = 0
            misses += 1
            judgement_text = "MISS"
            best.missed = True  # Mark as missed but keep visible

        judgement_timer = 400

    # -------------------------
    # MENU
    # -------------------------
    def draw_menu():
        screen.fill((10, 10, 15))

        title = font.render("Select Song", True, (220, 220, 220))
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 120))

        songs = [
            "1 - Suzume",
            "2 - White Keys",
            "3 - Prairies"
        ]

        y = 220
        for s in songs:
            txt = font.render(s, True, (180, 180, 180))
            screen.blit(txt, (WIDTH//2 - txt.get_width()//2, y))
            y += 60
            
        instr = font.render("Press 1, 2, or 3 to select", True, (100, 100, 120))
        screen.blit(instr, (WIDTH//2 - instr.get_width()//2, HEIGHT - 80))

    # -------------------------
    # DRAW RESULTS SCREEN
    # -------------------------
    def draw_results():
        screen.fill((10, 10, 15))
        
        results_title = big_font.render("Results", True, (220, 220, 220))
        screen.blit(results_title, (WIDTH//2 - results_title.get_width()//2, 100))
        
        score_text = font.render(f"Final Score: {score}", True, (220, 220, 220))
        screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 200))
        
        acc_text = font.render(f"Accuracy: {accuracy:.2f}%", True, (220, 220, 220))
        screen.blit(acc_text, (WIDTH//2 - acc_text.get_width()//2, 250))
        
        perfect_text = font.render(f"Perfect: {perfect_hits}", True, (0, 255, 120))
        screen.blit(perfect_text, (WIDTH//2 - perfect_text.get_width()//2, 310))
        
        good_text = font.render(f"Good: {good_hits}", True, (255, 200, 0))
        screen.blit(good_text, (WIDTH//2 - good_text.get_width()//2, 350))
        
        miss_text = font.render(f"Miss: {misses}", True, (255, 80, 80))
        screen.blit(miss_text, (WIDTH//2 - miss_text.get_width()//2, 390))
        
        max_combo_text = font.render(f"Max Combo: {max_combo}", True, (220, 220, 220))
        screen.blit(max_combo_text, (WIDTH//2 - max_combo_text.get_width()//2, 450))
        
        cont_text = font.render("Press ESC to return to menu", True, (100, 100, 120))
        screen.blit(cont_text, (WIDTH//2 - cont_text.get_width()//2, HEIGHT - 60))

    # -------------------------
    # MAIN LOOP
    # -------------------------
    results_display_time = 0
    max_combo = 0
    game_ended = False
    music_start_time = 0
    
    while running:
        clock.tick(60)

        # -------------------------
        # MENU STATE
        # -------------------------
        if state == "song_select":
            draw_menu()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        selected_song = "1"
                        start_song("1")
                        reset_game()
                        state = "game"
                        game_ended = False
                        music_start_time = pygame.time.get_ticks()
                        max_combo = 0

                    elif event.key == pygame.K_2:
                        selected_song = "2"
                        start_song("2")
                        reset_game()
                        state = "game"
                        game_ended = False
                        music_start_time = pygame.time.get_ticks()
                        max_combo = 0

                    elif event.key == pygame.K_3:
                        selected_song = "3"
                        start_song("3")
                        reset_game()
                        state = "game"
                        game_ended = False
                        music_start_time = pygame.time.get_ticks()
                        max_combo = 0

                    elif event.key == pygame.K_ESCAPE:
                        running = False

            continue

        # -------------------------
        # RESULTS STATE
        # -------------------------
        if state == "results":
            draw_results()
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        state = "song_select"
                        game_ended = False
                        pygame.mixer.music.stop()

            continue

        # -------------------------
        # GAME LOGIC
        # -------------------------
        screen.fill((15, 15, 20))

        current_time = pygame.mixer.music.get_pos()
        
        # Check if music has ended (get_pos returns -1 when no music playing or ended)
        if pygame.mixer.music.get_busy() == False and not game_ended and state == "game":
            if current_time == -1 or (pygame.time.get_ticks() - music_start_time > 1000):
                # Music has ended - show results
                state = "results"
                game_ended = True
                # Calculate final accuracy
                total = perfect_hits + good_hits + misses
                if total > 0:
                    accuracy = ((perfect_hits * 100) + (good_hits * 50)) / (total * 100) * 100
                continue

        # Only process game logic if music is playing
        if pygame.mixer.music.get_busy():
            current_time = pygame.mixer.music.get_pos()
            
            # beatmap spawn - infinite (keeps spawning all notes, loop continues until music ends)
            while spawn_index < len(beatmap):
                t, lane = beatmap[spawn_index]

                if current_time >= t:
                    notes.append(Note(lane))
                    spawn_index += 1
                else:
                    break

        # Draw lanes
        for i in range(LANE_COUNT):
            pygame.draw.rect(screen, (25, 25, 35),
                             (lanes_x[i], 0, LANE_WIDTH, HEIGHT))
            # Draw lane dividers
            pygame.draw.line(screen, (40, 40, 50),
                             (lanes_x[i], 0),
                             (lanes_x[i], HEIGHT), 2)
            # Draw key labels at bottom
            key_label = font.render(KEYS[i].upper(), True, (80, 80, 90))
            screen.blit(key_label, (lanes_x[i] + LANE_WIDTH//2 - key_label.get_width()//2, HEIGHT - 35))

        # Hit line
        pygame.draw.line(screen, (0, 255, 120),
                         (0, HIT_LINE_Y),
                         (WIDTH, HIT_LINE_Y), 4)
        
        # Draw glow effect on hit line
        for i in range(3):
            alpha = 100 - i * 30
            pygame.draw.line(screen, (0, 255, 120, alpha),
                             (0, HIT_LINE_Y - i * 2),
                             (WIDTH, HIT_LINE_Y - i * 2), 1)

        # Update and draw notes
        for n in notes[:]:
            n.update()
            n.draw()

            # Check if note passed the hit line without being hit
            if n.y > HIT_LINE_Y + 30 and not n.hit and not n.missed:
                notes.remove(n)
                combo = 0
                misses += 1
                judgement_text = "MISS"
                judgement_timer = 400
                continue
            
            # Remove hit notes after they've been drawn (for animation effect)
            if n.hit and n.y > HIT_LINE_Y + 20:
                notes.remove(n)
            elif n.missed and n.y > HEIGHT:
                notes.remove(n)

        # Update max combo
        if combo > max_combo:
            max_combo = combo

        # Judgement text
        if judgement_timer > 0:
            if judgement_text == "PERFECT":
                color = (0, 255, 120)
                # Add bouncing effect
                scale = 1 + (judgement_timer / 400) * 0.5
            elif judgement_text == "GOOD":
                color = (255, 200, 0)
                scale = 1 + (judgement_timer / 400) * 0.3
            else:
                color = (255, 80, 80)
                scale = 1
            
            text = font.render(judgement_text, True, color)
            # Center text
            text_x = WIDTH//2 - text.get_width()//2
            text_y = 200 - (400 - judgement_timer) // 10
            screen.blit(text, (text_x, text_y))
            
            # Show combo counter for Perfect/Good
            if judgement_text in ["PERFECT", "GOOD"] and combo > 1:
                combo_text = font.render(f"{combo}x", True, (220, 220, 220))
                screen.blit(combo_text, (WIDTH//2 - combo_text.get_width()//2, text_y + 40))
            
            judgement_timer -= clock.get_time()

        # Update accuracy (real-time)
        total = perfect_hits + good_hits + misses
        if total > 0:
            accuracy = ((perfect_hits * 100) + (good_hits * 50)) / (total * 100) * 100

        # Draw note hit indicators on lanes
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if key in KEYS:
                    # Flash effect on lane when key pressed
                    lane_idx = KEYS.index(key)
                    flash_rect = pygame.Rect(lanes_x[lane_idx], HIT_LINE_Y - 10, LANE_WIDTH, 20)
                    pygame.draw.rect(screen, (0, 255, 120, 100), flash_rect)

        # UI
        score_text = font.render(f"Score: {score}", True, (220, 220, 220))
        screen.blit(score_text, (20, 20))
        
        combo_text = font.render(f"Combo: {combo}", True, (220, 220, 220))
        screen.blit(combo_text, (20, 55))
        
        acc_text = font.render(f"Acc: {accuracy:.1f}%", True, (220, 220, 220))
        screen.blit(acc_text, (20, 90))
        
        # Show remaining notes
        notes_left = len(beatmap) - spawn_index
        if notes_left > 0:
            notes_text = font.render(f"Left: {notes_left}", True, (150, 150, 160))
            screen.blit(notes_text, (20, 125))

        pygame.display.update()

        # -------------------------
        # INPUT HANDLING
        # -------------------------
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)

                if key in KEYS:
                    check_hit(key)

                if key == "escape" and state == "game":
                    pygame.mixer.music.stop()
                    state = "song_select"
                    
                # Debug: skip to results
                if key == "r" and state == "game":
                    state = "results"
                    total = perfect_hits + good_hits + misses
                    if total > 0:
                        accuracy = ((perfect_hits * 100) + (good_hits * 50)) / (total * 100) * 100

    pygame.quit()
    sys.exit()
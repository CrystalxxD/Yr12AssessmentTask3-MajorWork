import pygame  # Import pygame library for game development
import sys  # Import sys for system operations and exiting
import os  # Import os for file path operations
import math  # Import math for mathematical functions
import random  # Import random for generating random numbers

# Define the main function that runs the rhythm game
def run_rhythm_game():
    pygame.init()  # Initialize all pygame modules
    pygame.mixer.init()  # Initialize the sound mixer module
    
    # Set up the game window dimensions
    WIDTH, HEIGHT = 1450, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the game window
    pygame.display.set_caption("Rhythm Game")  # Set the window title
    clock = pygame.time.Clock()  # Create a clock object to control frame rate
    font = pygame.font.SysFont("consolas", 28)  # Create main font
    big_font = pygame.font.SysFont("consolas", 48)  # Create large font
    small_font = pygame.font.SysFont("consolas", 16)  # Create small font

    # -------------------------
    # PARTICLE CLASSES
    # -------------------------
    class Particle:
        """Class for creating visual particle effects"""
        def __init__(self, x, y, color, vel, ptype="circle"):
            # Initialize particle position, color, and velocity
            self.x, self.y, self.color = x, y, color
            self.vx, self.vy = vel[0], vel[1]  # Velocity in x and y directions
            self.life, self.size = 255, random.randint(3, 8)  # Alpha life and size
            self.type = ptype  # Particle type (circle, spark, glow)
            self.rot = random.uniform(0, 360)  # Random rotation angle
            self.rot_speed = random.uniform(-5, 5)  # Rotation speed
            
        def update(self):
            """Update particle position, life, and size each frame"""
            self.x += self.vx  # Move particle horizontally
            self.y += self.vy  # Move particle vertically
            self.vy += 0.2  # Apply gravity
            self.vx *= 0.98  # Apply air resistance
            self.life -= 8  # Reduce particle life
            self.size = max(1, self.size - 0.15)  # Shrink particle
            self.rot += self.rot_speed  # Update rotation
            
        def draw(self, screen):
            """Draw the particle on the screen"""
            if self.life <= 0:  # Skip if particle is dead
                return
            c = self.color  # Get particle color
            
            # Draw based on particle type
            if self.type == "circle":
                pygame.draw.circle(screen, c, (int(self.x), int(self.y)), int(self.size))
            elif self.type == "spark":
                # Draw a line spark effect
                ex = self.x + math.cos(math.radians(self.rot)) * self.size * 2
                ey = self.y + math.sin(math.radians(self.rot)) * self.size * 2
                pygame.draw.line(screen, c, (self.x, self.y), (ex, ey), max(1, int(self.size / 2)))
            elif self.type == "glow":
                # Draw a glowing circle with alpha
                surf = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
                pygame.draw.circle(surf, (*c, self.life), (self.size, self.size), self.size)
                screen.blit(surf, (self.x - self.size, self.y - self.size))

    class NoteHitEffect:
        """Class for creating hit effects when notes are struck"""
        def __init__(self, x, y, color, hit_type):
            self.life = 30  # Effect lifetime
            self.particles = []  # List of particles
            # Number of particles based on hit quality
            num = 25 if hit_type == "perfect" else 15 if hit_type == "good" else 10
            
            for _ in range(num):
                # Random velocity in circular pattern
                a = random.uniform(0, 2 * math.pi)
                s = random.uniform(2, 8)
                vx = math.cos(a) * s
                vy = math.sin(a) * s - 3
                
                # Choose particle type and color based on hit quality
                if hit_type == "perfect":
                    pt = random.choice(["circle", "spark", "glow"])
                    pc = (random.randint(100, 255), random.randint(200, 255), random.randint(100, 200))
                elif hit_type == "good":
                    pt = random.choice(["circle", "spark"])
                    pc = (random.randint(200, 255), random.randint(150, 220), random.randint(50, 150))
                else:
                    pt = "circle"
                    pc = (random.randint(200, 255), random.randint(50, 100), random.randint(50, 100))
                
                self.particles.append(Particle(x, y, pc, (vx, vy), pt))
                
        def update(self):
            """Update all particles in the effect"""
            self.life -= 1  # Decrease effect life
            for p in self.particles[:]:
                p.update()  # Update each particle
                if p.life <= 0:  # Remove dead particles
                    self.particles.remove(p)
            return len(self.particles) > 0  # Return True if effect is still alive
            
        def draw(self, screen):
            """Draw all particles in the effect"""
            for p in self.particles:
                p.draw(screen)

    class AmbientParticle:
        """Class for background ambient particles"""
        def __init__(self):
            # Initialize at random position
            self.x = random.randint(0, WIDTH)
            self.y = random.randint(0, HEIGHT)
            self.size = random.randint(1, 3)  # Small size
            self.speed = random.uniform(0.5, 2)  # Float up speed
            self.alpha = random.randint(30, 100)  # Transparency
            self.color = random.choice([(100, 150, 255), (150, 100, 255), (100, 255, 150)])
            
        def update(self):
            """Float upward and reset when off screen"""
            self.y -= self.speed
            if self.y < 0:  # Reset to bottom when reaching top
                self.y = HEIGHT
                self.x = random.randint(0, WIDTH)
                
        def draw(self, screen):
            """Draw the ambient particle with transparency"""
            if self.alpha > 0:
                surf = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
                pygame.draw.circle(surf, (*self.color, self.alpha), (self.size, self.size), self.size)
                screen.blit(surf, (self.x - self.size, self.y - self.size))

    # -------------------------
    # GAME STATE VARIABLES
    # -------------------------
    hit_effects = []  # List of active hit effects
    ambient_particles = [AmbientParticle() for _ in range(50)]  # Create 50 ambient particles
    lane_glows = [0] * 8  # Glow intensity for each lane
    key_cooldown = {}  # Cooldown timer for each key
    COOLDOWN_MS = 100  # Cooldown duration in milliseconds

    # -------------------------
    # SONGS + BEATMAPS
    # -------------------------
    SONGS = {
        # Dictionary of available songs with their metadata
        "1": {"name": "Suzume", "audio": "Code/music/1music.mp3", "beatmap": "Code/beatmaps/1music.map", "duration": 270, "theme_color": (100, 150, 255)},
        "2": {"name": "White Keys", "audio": "Code/music/2music.mp3", "beatmap": "Code/beatmaps/2music.map", "duration": 144, "theme_color": (255, 200, 100)},
        "3": {"name": "Prairies", "audio": "Code/music/3music.mp3", "beatmap": "Code/beatmaps/3music.map", "duration": 191, "theme_color": (100, 255, 150)}
    }
    selected_song = "1"  # Currently selected song
    state = "song_select"  # Current game state

    # -------------------------
    # LANES
    # -------------------------
    KEYS = ["a", "s", "d", "f", "h", "j", "k", "l"]  # Keys for each lane
    LANE_COUNT = 8  # Number of lanes
    LANE_WIDTH = WIDTH // LANE_COUNT  # Width of each lane
    lanes_x = [i * LANE_WIDTH for i in range(LANE_COUNT)]  # X positions of lanes
    HIT_LINE_Y = 700  # Y position of hit line
    NOTE_SPEED = 4.5  # Speed at which notes fall

    # -------------------------
    # GAME VALUES
    # -------------------------
    notes = []  # List of active notes
    beatmap = []  # Loaded beatmap data
    spawn_index = 0  # Current index in beatmap
    score = 0  # Player's score
    combo = 0  # Current combo count
    max_combo = 0  # Maximum combo achieved
    perfect_hits = 0  # Count of perfect hits
    good_hits = 0  # Count of good hits
    misses = 0  # Count of misses
    accuracy = 0  # Current accuracy percentage
    judgement_text = ""  # Text to display for judgement
    judgement_timer = 0  # Timer for displaying judgement
    judgement_scale = 1.0  # Scale animation for judgement text
    running = True  # Main game loop flag
    game_ended = False  # Flag for game ending
    music_start_time = 0  # Time when music started
    music_length_ms = 0  # Length of current song in milliseconds
    screen_flash = 0  # Screen flash intensity

    # -------------------------
    # BUTTONS
    # -------------------------
    buttons = {
        "back": pygame.Rect(20, 20, 120, 40),  # Back button
        "exit": pygame.Rect(WIDTH - 140, 20, 120, 35),  # Exit button
        "results": pygame.Rect(WIDTH // 2 - 100, HEIGHT - 70, 200, 45)  # Results button
    }
    song_hover = {1: False, 2: False, 3: False}  # Track hover state for song buttons

    # -------------------------
    # NOTE CLASS
    # -------------------------
    class Note:
        __slots__ = ('lane', 'x', 'y', 'key', 'hit', 'missed', 'target_time', 'hit_animation', 'glow_intensity', 'trail')
        # __slots__ optimizes memory usage by defining fixed attributes
        
        def __init__(self, lane, time_ms):
            self.lane = lane  # Lane index
            self.x = lanes_x[lane]  # X position based on lane
            self.y = -50  # Start above the screen
            self.key = KEYS[lane]  # Associated key
            self.hit = False  # Has been hit
            self.missed = False  # Has been missed
            self.target_time = time_ms  # Target time for hitting
            self.hit_animation = 0  # Animation progress when hit
            self.glow_intensity = 0  # Glow effect intensity
            self.trail = []  # Trail positions for visual effect
            
        def update(self):
            """Update note position and effects"""
            if not self.hit and not self.missed:
                self.y += NOTE_SPEED  # Move note down
                # Add position to trail
                self.trail.append((self.x + LANE_WIDTH // 2, self.y + 12))
                if len(self.trail) > 5:  # Limit trail length
                    self.trail.pop(0)
                # Animate glow intensity
                self.glow_intensity = abs(math.sin(pygame.time.get_ticks() * 0.01)) * 3
                
        def draw_trail(self):
            """Draw the trail behind the note"""
            for i, (tx, ty) in enumerate(self.trail):
                a = int(100 * (i / len(self.trail)))  # Alpha based on position in trail
                s = 4 - i * 0.5  # Size decreases along trail
                if s > 0:
                    surf = pygame.Surface((s * 2, s * 2), pygame.SRCALPHA)
                    pygame.draw.circle(surf, (0, 200, 255, a), (s, s), s)
                    screen.blit(surf, (tx - s, ty - s))
                    
        def draw(self):
            """Draw the note on screen"""
            if self.hit:
                # Draw hit animation (shrinking green rectangle)
                a = max(0, 255 - self.hit_animation * 20)
                rw = int((LANE_WIDTH - 16) * max(0.3, 1 - self.hit_animation / 20))
                rx = self.x + 8 + (LANE_WIDTH - 16 - rw) // 2
                gs = pygame.Surface((rw + 10, 35), pygame.SRCALPHA)
                pygame.draw.rect(gs, (100, 255, 100, a // 2), (0, 0, rw + 10, 35), border_radius=8)
                screen.blit(gs, (rx - 5, self.y - 5))
                pygame.draw.rect(screen, (100, 255, 100), (rx, self.y, rw, 25), border_radius=6)
                
            elif self.missed:
                # Draw miss indicator (red rectangle with X)
                pygame.draw.rect(screen, (255, 80, 80), (self.x + 8, self.y, LANE_WIDTH - 16, 25), border_radius=6)
                cx = self.x + LANE_WIDTH // 2
                cy = self.y + 12
                pygame.draw.line(screen, (255, 255, 255), (cx - 8, cy - 6), (cx + 8, cy + 6), 2)
                pygame.draw.line(screen, (255, 255, 255), (cx + 8, cy - 6), (cx - 8, cy + 6), 2)
                
            else:
                # Draw normal note with 3D effect and key label
                for i in range(3):
                    pygame.draw.rect(screen, (0, 100 + i * 50, 150, 100 - i * 30),
                                     (self.x + 8 - i, self.y - i, LANE_WIDTH - 16 + i * 2, 25 + i * 2), border_radius=6)
                pygame.draw.rect(screen, (0, 200, 255), (self.x + 8, self.y, LANE_WIDTH - 16, 25), border_radius=6)
                pygame.draw.rect(screen, (255, 255, 255), (self.x + 8, self.y, LANE_WIDTH - 16, 25), border_radius=6, width=2)
                # Render key label on note
                kt = font.render(self.key.upper(), True, (255, 255, 255))
                screen.blit(kt, (self.x + LANE_WIDTH // 2 - kt.get_width() // 2, self.y + 5))

    # -------------------------
    # LOAD BEATMAP
    # -------------------------
    def load_beatmap(song_key):
        """Load beatmap data from file or generate default pattern"""
        path = SONGS[song_key]["beatmap"]
        data = []
        
        # If file doesn't exist, generate default beatmap
        if not os.path.exists(path):
            dur = SONGS[song_key]["duration"] * 1000
            return [(t, (t // 500) % 8) for t in range(0, int(dur), 500)]
        
        try:
            # Read beatmap file
            with open(path, 'r') as f:
                for l in f:
                    l = l.strip()
                    if l and ',' in l:
                        p = l.split(',')
                        if len(p) >= 2:
                            try:
                                data.append((int(p[0]), int(p[1])))  # (time, lane)
                            except:
                                continue
            print(f"Loaded {len(data)} notes")
        except:
            pass
        
        # If loading failed or empty, generate default pattern
        if not data:
            dur = SONGS[song_key]["duration"] * 1000
            data = [(t, (t // 400) % 8) for t in range(0, int(dur), 400)]
            
        return data

    # -------------------------
    # CREATE HIT EFFECT
    # -------------------------
    def create_hit_effect(x, y, ht, lane):
        """Create and return a hit effect at specified position"""
        tc = SONGS[selected_song]["theme_color"]  # Theme color for song
        e = NoteHitEffect(x, y, tc, ht)  # Create the effect
        
        # Add extra spark particles for perfect hits
        if ht == "perfect":
            for _ in range(8):
                a = random.uniform(0, 2 * math.pi)
                vx = math.cos(a) * random.uniform(3, 6)
                vy = math.sin(a) * random.uniform(3, 6) - 2
                e.particles.append(Particle(x, y, (255, 215, 0), (vx, vy), "spark"))
            lane_glows[lane] = 20  # Activate lane glow
            
        return e

    # -------------------------
    # HIT SYSTEM
    # -------------------------
    def check_hit(key):
        """Check if a key press hits a note"""
        # Use nonlocal to modify outer scope variables
        nonlocal score, combo, max_combo, screen_flash, judgement_scale
        nonlocal judgement_text, judgement_timer, perfect_hits, good_hits, misses
        
        now = pygame.time.get_ticks()
        # Check cooldown to prevent multiple hits
        if key in key_cooldown and now - key_cooldown[key] < COOLDOWN_MS:
            return
        key_cooldown[key] = now
        
        idx = KEYS.index(key)  # Get lane index for key
        best = None  # Best matching note
        best_diff = 9999  # Best difference from hit line
        best_i = -1  # Index of best note
        
        # Find closest note in the same lane
        for i, n in enumerate(notes):
            if n.key == key and not n.hit and not n.missed and n.y <= HIT_LINE_Y + 80:
                d = abs(n.y - HIT_LINE_Y)
                if d < best_diff:
                    best = n
                    best_diff = d
                    best_i = i
                    
        # If no note found, count as miss
        if not best:
            combo = 0
            misses += 1
            judgement_text = "MISS"
            judgement_timer = 400
            judgement_scale = 1.2
            hit_effects.append(create_hit_effect(lanes_x[idx] + LANE_WIDTH // 2, HIT_LINE_Y, "miss", idx))
            return
            
        hx = best.x + LANE_WIDTH // 2
        hy = HIT_LINE_Y
        
        # Judge accuracy based on distance from hit line
        if best_diff <= 55:  # Perfect
            score += 300 * (1 + combo // 15)  # Bonus points for combo
            combo += 1
            perfect_hits += 1
            judgement_text = "PERFECT"
            hit_effects.append(create_hit_effect(hx, hy, "perfect", idx))
            screen_flash = 5
            
        elif best_diff <= 110:  # Good
            score += 150 * (1 + combo // 15)
            combo += 1
            good_hits += 1
            judgement_text = "GOOD"
            hit_effects.append(create_hit_effect(hx, hy, "good", idx))
            
        else:  # Miss
            combo = 0
            misses += 1
            judgement_text = "MISS"
            best.missed = True
            hit_effects.append(create_hit_effect(hx, hy, "miss", idx))
            
        # Update max combo if current combo is higher
        if combo > max_combo:
            max_combo = combo
            
        # Remove the hit note
        if best_i != -1 and best_i < len(notes):
            notes.pop(best_i)
            
        # Start judgement display
        judgement_timer = 400
        judgement_scale = 1.2

    # -------------------------
    # RESET GAME
    # -------------------------
    def reset_game():
        """Reset all game state for a new round"""
        nonlocal notes, score, combo, max_combo, perfect_hits, good_hits, misses
        nonlocal judgement_text, judgement_timer, spawn_index, beatmap, game_ended
        nonlocal hit_effects, key_cooldown
        
        notes = []  # Clear notes
        score = 0  # Reset score
        combo = 0  # Reset combo
        max_combo = 0  # Reset max combo
        perfect_hits = 0  # Reset perfect count
        good_hits = 0  # Reset good count
        misses = 0  # Reset misses
        judgement_text = ""  # Clear judgement text
        judgement_timer = 0  # Reset timer
        spawn_index = 0  # Reset spawn index
        game_ended = False  # Reset game ended flag
        hit_effects = []  # Clear hit effects
        key_cooldown = {}  # Clear cooldowns
        beatmap = load_beatmap(selected_song)  # Load beatmap for selected song

    # -------------------------
    # START SONG
    # -------------------------
    def start_song(song_key):
        """Start playing the selected song"""
        nonlocal beatmap, spawn_index, music_start_time, music_length_ms
        
        beatmap = load_beatmap(song_key)  # Load beatmap
        spawn_index = 0  # Reset spawn index
        music_start_time = pygame.time.get_ticks()  # Record start time
        music_length_ms = int(SONGS[song_key]["duration"] * 1000)  # Get song duration
        
        try:
            # Load and play audio file
            if os.path.exists(SONGS[song_key]["audio"]):
                pygame.mixer.music.load(SONGS[song_key]["audio"])
                pygame.mixer.music.play()
        except:
            pass

    # -------------------------
    # DRAW FUNCTIONS
    # -------------------------
    def draw_gradient_bg():
        """Draw a gradient background based on song theme"""
        tc = SONGS[selected_song]["theme_color"]
        # Draw vertical gradient lines
        for y in range(HEIGHT):
            r = int(10 + (tc[0] - 10) * (y / HEIGHT) * 0.3)
            g = int(10 + (tc[1] - 10) * (y / HEIGHT) * 0.3)
            b = int(20 + (tc[2] - 20) * (y / HEIGHT) * 0.3)
            pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

    # -------------------------
    # MAIN LOOP
    # -------------------------
    while running:
        clock.tick(60)  # Limit frame rate to 60 FPS
        
        # Update particles
        for p in ambient_particles:
            p.update()  # Update ambient particles
            
        for e in hit_effects[:]:
            if not e.update():  # Update and check if effect is dead
                hit_effects.remove(e)  # Remove dead effects
                
        if screen_flash > 0:
            screen_flash -= 1  # Decrease flash intensity
        if judgement_scale > 1.0:
            judgement_scale -= 0.05  # Shrink judgement text back to normal
        if judgement_timer > 0:
            judgement_timer -= clock.get_time()  # Decrease judgement timer

        # -------------------------
        # SONG SELECT STATE
        # -------------------------
        if state == "song_select":
            draw_gradient_bg()  # Draw background
            
            for p in ambient_particles:
                p.draw(screen)  # Draw ambient particles
                
            mouse = pygame.mouse.get_pos()  # Get mouse position
            
            # Draw song selection buttons
            for i in range(1, 4):
                r = pygame.Rect(WIDTH // 2 - 200, 230 + (i - 1) * 72, 400, 52)  # Button rectangle
                song_hover[i] = r.collidepoint(mouse)  # Check hover
                c = (40, 40, 60) if song_hover[i] else (20, 20, 30)  # Color based on hover
                pygame.draw.rect(screen, c, r, border_radius=10)  # Draw button
                
                colors = [(100, 150, 255), (255, 200, 100), (100, 255, 150)]  # Theme colors
                border_width = 4 if song_hover[i] else 2
                pygame.draw.rect(screen, colors[i - 1], r, border_width, border_radius=10)  # Border
                
                song_names = ['Suzume', 'White Keys', 'Prairies']  # Song names
                txt = font.render(f"{i} - {song_names[i - 1]}", True, (220, 220, 220))
                screen.blit(txt, (WIDTH // 2 - txt.get_width() // 2, 233 + (i - 1) * 72))  # Draw name
                
                durations = ["4:30", "2:24", "3:11"]  # Durations
                dur = small_font.render(durations[i - 1], True, (150, 150, 150))
                screen.blit(dur, (WIDTH // 2 - dur.get_width() // 2, 260 + (i - 1) * 72))  # Draw duration
                
            # Draw back button
            pygame.draw.rect(screen, (40, 40, 50), buttons["back"], border_radius=10)
            pygame.draw.rect(screen, (200, 200, 200), buttons["back"], 2, border_radius=10)
            screen.blit(small_font.render("Main Menu", True, (220, 220, 220)), (buttons["back"].x + 10, buttons["back"].y + 12))
            
            # Draw title
            title = big_font.render("RHYTHM GAME", True, (0, 200, 255))
            screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 80))
            
            pygame.display.update()  # Update screen
            
            # Handle events in song select
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return  # Exit game
                    
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if buttons["back"].collidepoint(e.pos):
                        return  # Return to main menu
                        
                    # Check song button clicks
                    for i in range(1, 4):
                        rect = pygame.Rect(WIDTH // 2 - 200, 230 + (i - 1) * 70, 400, 50)
                        if rect.collidepoint(e.pos):
                            selected_song = str(i)
                            state = "game"  # Switch to game state
                            reset_game()  # Reset game
                            start_song(str(i))  # Start selected song
                            
                # Keyboard shortcuts for song selection
                if e.type == pygame.KEYDOWN and e.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                    selected_song = str(e.key - pygame.K_1 + 1)
                    state = "game"
                    reset_game()
                    start_song(selected_song)
                    
            continue  # Skip rest of loop

        # -------------------------
        # RESULTS STATE
        # -------------------------
        if state == "results":
            draw_gradient_bg()  # Draw background
            
            for p in ambient_particles:
                p.draw(screen)  # Draw ambient particles
            for e in hit_effects:
                e.draw(screen)  # Draw remaining hit effects
            
            # Draw results panel
            panel = pygame.Rect(WIDTH // 2 - 350, 100, 700, 520)
            pygame.draw.rect(screen, (20, 20, 30), panel, border_radius=20)
            pygame.draw.rect(screen, (0, 200, 255), panel, 3, border_radius=20)
            
            # Draw title
            title = big_font.render("RESULTS", True, (0, 200, 255))
            screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 120))
            
            # Draw score
            score_text = big_font.render(f"{score}", True, (255, 215, 0))
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 175))
            score_label = small_font.render("SCORE", True, (150, 150, 160))
            screen.blit(score_label, (WIDTH // 2 - score_label.get_width() // 2, 225))
            
            # Divider line
            pygame.draw.line(screen, (60, 60, 80), (WIDTH // 2 - 250, 255), (WIDTH // 2 + 250, 255), 2)
            
            # Draw stats in two columns
            # Left column
            perfect_text = font.render(f"PERFECT: {perfect_hits}", True, (0, 255, 120))
            screen.blit(perfect_text, (WIDTH // 2 - 180, 280))
            
            good_text = font.render(f"GOOD: {good_hits}", True, (255, 200, 0))
            screen.blit(good_text, (WIDTH // 2 - 180, 325))
            
            miss_text = font.render(f"MISS: {misses}", True, (255, 80, 80))
            screen.blit(miss_text, (WIDTH // 2 - 180, 370))
            
            # Right column
            accuracy_text = font.render(f"ACCURACY", True, (180, 180, 190))
            screen.blit(accuracy_text, (WIDTH // 2 + 20, 280))
            acc_value = font.render(f"{accuracy:.2f}%", True, (220, 220, 220))
            screen.blit(acc_value, (WIDTH // 2 + 20, 310))
            
            combo_text = font.render(f"MAX COMBO", True, (180, 180, 190))
            screen.blit(combo_text, (WIDTH // 2 + 20, 355))
            combo_value = font.render(f"{max_combo}", True, (220, 220, 220))
            screen.blit(combo_value, (WIDTH // 2 + 20, 385))
            
            # Divider
            pygame.draw.line(screen, (60, 60, 80), (WIDTH // 2 - 250, 420), (WIDTH // 2 + 250, 420), 2)
            
            # Calculate and draw grade
            if accuracy >= 95:
                grade = "SS"
                gc = (255, 215, 0)
            elif accuracy >= 90:
                grade = "S"
                gc = (255, 215, 0)
            elif accuracy >= 80:
                grade = "A"
                gc = (0, 255, 120)
            elif accuracy >= 70:
                grade = "B"
                gc = (255, 200, 0)
            elif accuracy >= 60:
                grade = "C"
                gc = (255, 100, 100)
            else:
                grade = "D"
                gc = (255, 80, 80)
            
            grade_text = big_font.render(grade, True, gc)
            screen.blit(grade_text, (WIDTH // 2 - grade_text.get_width() // 2, 440))
            
            grade_label = small_font.render("GRADE", True, (150, 150, 160))
            screen.blit(grade_label, (WIDTH // 2 - grade_label.get_width() // 2, 490))
            
            # Draw exit button
            mouse = pygame.mouse.get_pos()
            exit_btn = pygame.Rect(WIDTH // 2 - 120, panel.y + panel.height - 60, 240, 45)
            c = (60, 60, 80) if exit_btn.collidepoint(mouse) else (40, 40, 50)
            pygame.draw.rect(screen, c, exit_btn, border_radius=12)
            
            border_color = (255, 100, 100) if exit_btn.collidepoint(mouse) else (200, 200, 200)
            border_width = 3 if exit_btn.collidepoint(mouse) else 2
            pygame.draw.rect(screen, border_color, exit_btn, border_width, border_radius=12)
            
            exit_text = font.render("Exit", True, (220, 220, 220))
            screen.blit(exit_text, (exit_btn.x + exit_btn.width // 2 - exit_text.get_width() // 2, exit_btn.y + 12))
            
            pygame.display.update()
            
            # Handle events in results
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return
                    
                if e.type == pygame.MOUSEBUTTONDOWN and exit_btn.collidepoint(e.pos):
                    state = "song_select"  # Return to song select
                    game_ended = False
                    pygame.mixer.music.stop()  # Stop music
                    
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    state = "song_select"
                    game_ended = False
                    pygame.mixer.music.stop()
                    
            continue  # Skip rest of loop

        # -------------------------
        # GAME STATE
        # -------------------------
        elapsed = pygame.time.get_ticks() - music_start_time  # Time since song started
        
        # Check if song has ended
        if not game_ended and elapsed >= music_length_ms + 1000:
            game_ended = True
            state = "results"  # Show results
            total = perfect_hits + good_hits + misses
            if total > 0:
                # Calculate final accuracy
                accuracy = ((perfect_hits * 100) + (good_hits * 50)) / (total * 100) * 100
            continue

        draw_gradient_bg()  # Draw background
        
        for p in ambient_particles:
            p.draw(screen)  # Draw ambient particles
            
        cur = pygame.mixer.music.get_pos()  # Get current music position
        if cur < 0 or not pygame.mixer.music.get_busy():
            cur = elapsed  # Use elapsed time if music isn't playing
            
        # Spawn notes from beatmap
        if not game_ended and beatmap:
            while spawn_index < len(beatmap):
                t, l = beatmap[spawn_index]
                if cur >= t:  # Time to spawn note
                    notes.append(Note(l, t))
                    spawn_index += 1
                else:
                    break

        # Draw lanes
        for i in range(LANE_COUNT):
            pygame.draw.rect(screen, (25, 25, 35), (lanes_x[i], 0, LANE_WIDTH, HEIGHT))
            pygame.draw.line(screen, (40, 40, 50), (lanes_x[i], 0), (lanes_x[i], HEIGHT), 2)
            
        # Draw key labels
        for i, k in enumerate(KEYS):
            kl = font.render(k.upper(), True, (100, 100, 120))
            screen.blit(kl, (lanes_x[i] + LANE_WIDTH // 2 - kl.get_width() // 2, HEIGHT - 35))
            
        # Draw hit line
        for i in range(5):
            pygame.draw.line(screen, (0, 255, 120, 100 - i * 20), (0, HIT_LINE_Y - i), (WIDTH, HIT_LINE_Y - i), 3)
        pygame.draw.line(screen, (0, 255, 120), (0, HIT_LINE_Y), (WIDTH, HIT_LINE_Y), 4)
        
        # Draw lane glows
        for i, intensity in enumerate(lane_glows):
            if intensity > 0:
                s = pygame.Surface((LANE_WIDTH, HEIGHT), pygame.SRCALPHA)
                pygame.draw.rect(s, (255, 255, 255, min(200, intensity * 15)), (0, 0, LANE_WIDTH, HEIGHT))
                screen.blit(s, (lanes_x[i], 0))
                lane_glows[i] -= 1  # Decrease glow intensity

        # Update and draw notes
        for n in notes[:]:
            n.update()  # Update note position
            n.draw_trail()  # Draw trail
            n.draw()  # Draw note
            
            # Check if note was missed (passed hit line)
            if not n.hit and not n.missed and n.y > HIT_LINE_Y + 50:
                combo = 0  # Reset combo
                misses += 1  # Increment misses
                judgement_text = "MISS"
                judgement_timer = 400
                judgement_scale = 1.2
                hit_effects.append(create_hit_effect(lanes_x[n.lane] + LANE_WIDTH // 2, HIT_LINE_Y, "miss", n.lane))
                notes.remove(n)  # Remove missed note

        # Draw hit effects
        for e in hit_effects:
            e.draw(screen)
            
        # Draw judgement text
        if judgement_timer > 0:
            # Set color based on judgement type
            if "PERFECT" in judgement_text:
                c = (0, 255, 120)
            elif "GOOD" in judgement_text:
                c = (255, 200, 0)
            else:
                c = (255, 80, 80)
                
            # Render with scaling animation
            sf = pygame.font.SysFont("consolas", int(28 * judgement_scale))
            t = sf.render(judgement_text, True, c)
            screen.blit(t, (WIDTH // 2 - t.get_width() // 2, 200 - (400 - judgement_timer) // 10))
            
            # Show combo count on perfect/good hits
            if ("PERFECT" in judgement_text or "GOOD" in judgement_text) and combo > 1:
                ct = sf.render(f"{combo}x", True, (220, 220, 220))
                screen.blit(ct, (WIDTH // 2 - ct.get_width() // 2, 200 - (400 - judgement_timer) // 10 + 50))
                
        # Update accuracy
        total = perfect_hits + good_hits + misses
        if total > 0:
            accuracy = ((perfect_hits * 100) + (good_hits * 50)) / (total * 100) * 100

        # Draw UI
        screen.blit(font.render(f"Score: {score}", True, (220, 220, 220)), (20, 20))
        screen.blit(font.render(f"Combo: {combo}", True, (220, 220, 220)), (20, 55))
        screen.blit(font.render(f"Acc: {accuracy:.1f}%", True, (220, 220, 220)), (20, 90))

        # Draw exit button
        mouse = pygame.mouse.get_pos()
        c = (60, 60, 80) if buttons["exit"].collidepoint(mouse) else (40, 40, 50)
        pygame.draw.rect(screen, c, buttons["exit"], border_radius=8)

        border_color = (255, 100, 100) if buttons["exit"].collidepoint(mouse) else (200, 200, 200)
        border_width = 3 if buttons["exit"].collidepoint(mouse) else 2
        pygame.draw.rect(screen, border_color, buttons["exit"], border_width, border_radius=8)

        exit_text = small_font.render("Exit", True, (220, 220, 220))
        screen.blit(exit_text, (buttons["exit"].x + buttons["exit"].width // 2 - 20, buttons["exit"].y + 10))

        # Draw progress bar
        prog = min(1.0, elapsed / music_length_ms) if music_length_ms > 0 else 0
        progress_width = 400
        progress_x = (WIDTH - progress_width) // 2
        pygame.draw.rect(screen, (40, 40, 50), (progress_x, 20, progress_width, 10))
        pygame.draw.rect(screen, (0, 200, 255), (progress_x, 20, progress_width * prog, 10))

        # Draw timer
        tl = max(0, (music_length_ms - elapsed) / 1000)
        timer_text = font.render(f"{int(tl // 60)}:{int(tl % 60):02d}", True, (200, 200, 210))
        screen.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, 45))
        
        # Draw screen flash
        if screen_flash > 0:
            fs = pygame.Surface((WIDTH, HEIGHT))
            fs.fill((255, 255, 255))
            fs.set_alpha(screen_flash * 10)
            screen.blit(fs, (0, 0))
            
        pygame.display.update()  # Update screen

        # Handle input
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return  # Exit game
                
            if e.type == pygame.MOUSEBUTTONDOWN and buttons["exit"].collidepoint(e.pos):
                pygame.mixer.music.stop()  # Stop music
                state = "song_select"  # Return to song select
                
            if e.type == pygame.KEYDOWN:
                # Check if key press matches a lane
                if pygame.key.name(e.key) in KEYS:
                    check_hit(pygame.key.name(e.key))  # Process hit
                    
                if pygame.key.name(e.key) == "escape":
                    pygame.mixer.music.stop()
                    state = "song_select"
                    
                if pygame.key.name(e.key) == "r" and state == "game":
                    # Force results with 'r' key
                    state = "results"
                    total = perfect_hits + good_hits + misses
                    if total > 0:
                        accuracy = ((perfect_hits * 100) + (good_hits * 50)) / (total * 100) * 100
                        
    pygame.quit()  # Quit pygame
    sys.exit()  # Exit the program
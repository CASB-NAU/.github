import math
from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path

# Config
WIDTH = 1200
HEIGHT = 400
FPS = 20
DURATION_SEC = 3
TOTAL_FRAMES = FPS * DURATION_SEC  # 60 frames for a 3-second loop
OUT_GIF = Path("/Users/jason/workplace/NAU/casb-github/profile/assets/animation.gif")

# Color palette (Futuristic SynthBio neon)
BG_COLOR = (5, 11, 20)          # Deep space dark blue
NEON_TEAL = (13, 148, 136)       # #0d9488
NEON_GREEN = (52, 211, 153)      # #34d399
NEON_PURPLE = (167, 139, 250)    # #a78bfa
GLOW_COLOR = (20, 184, 166, 40)  # Transparent teal for glow effect

# Network Nodes: (x, y, color, size_range)
NODES = [
    (200, 200, NEON_TEAL, (10, 16)),
    (400, 120, NEON_GREEN, (8, 14)),
    (400, 280, NEON_PURPLE, (8, 14)),
    (600, 200, NEON_TEAL, (12, 20)),
    (800, 120, NEON_PURPLE, (8, 14)),
    (800, 280, NEON_GREEN, (8, 14)),
    (1000, 200, NEON_TEAL, (10, 16)),
]

# Network Edges: (from_node_idx, to_node_idx, flow_color)
EDGES = [
    (0, 1, NEON_GREEN),
    (0, 2, NEON_PURPLE),
    (1, 3, NEON_TEAL),
    (2, 3, NEON_TEAL),
    (3, 4, NEON_PURPLE),
    (3, 5, NEON_GREEN),
    (4, 6, NEON_TEAL),
    (5, 6, NEON_TEAL),
    (1, 2, NEON_PURPLE),
    (4, 5, NEON_GREEN),
]

def draw_glow_circle(draw, x, y, r, color):
    # Draw nested layers to create a soft glow effect
    for i in range(4):
        alpha = int(60 / (i + 1))
        layer_color = color + (alpha,)
        draw.ellipse([x - r - i*3, y - r - i*3, x + r + i*3, y + r + i*3], fill=layer_color)

def generate_animation():
    OUT_GIF.parent.mkdir(parents=True, exist_ok=True)
    frames = []

    for f_idx in range(TOTAL_FRAMES):
        # Progress from 0.0 to 1.0
        progress = f_idx / TOTAL_FRAMES
        angle = progress * 2 * math.pi

        # Create base image with transparency support
        img = Image.new("RGBA", (WIDTH, HEIGHT), BG_COLOR + (255,))
        draw = ImageDraw.Draw(img, "RGBA")

        # 1. Draw connecting metabolic pathways (edges)
        for u_idx, v_idx, edge_color in EDGES:
            u = NODES[u_idx]
            v = NODES[v_idx]
            
            # Base pathway line
            draw.line([u[0], u[1], v[0], v[1]], fill=edge_color + (50,), width=2)
            
            # Flowing pulse particle along path
            # Pulse position offsets to create a continuous stream
            for pulse_offset in [0.0, 0.5]:
                t = (progress + pulse_offset) % 1.0
                px = u[0] + (v[0] - u[0]) * t
                py = u[1] + (v[1] - u[1]) * t
                
                # Glowing pulse particle
                draw.ellipse([px - 5, py - 5, px + 5, py + 5], fill=edge_color + (200,))
                draw.ellipse([px - 8, py - 8, px + 8, py + 8], fill=edge_color + (60,))

        # 2. Draw metabolic nodes
        for idx, (nx, ny, n_color, (min_s, max_s)) in enumerate(NODES):
            # Pulsing size based on sine wave
            phase_shift = idx * 0.8
            pulse_size = min_s + (max_s - min_s) * (0.5 + 0.5 * math.sin(angle * 2 + phase_shift))
            
            # Draw glow
            draw_glow_circle(draw, nx, ny, pulse_size, n_color)
            # Solid core
            draw.ellipse([nx - pulse_size/2, ny - pulse_size/2, nx + pulse_size/2, ny + pulse_size/2], fill=n_color + (255,))

        # 3. Add overlay decoration representing data matrix/grid
        grid_space = 40
        for gx in range(0, WIDTH, grid_space):
            for gy in range(0, HEIGHT, grid_space):
                # Subtle matrix dots
                draw.point((gx, gy), fill=(255, 255, 255, 10))

        # Add text label "IN SILICO CELL SIMULATION" in bottom right
        # Using simple line draws to draw a retro status line
        draw.line([50, HEIGHT - 40, WIDTH - 50, HEIGHT - 40], fill=NEON_TEAL + (100,), width=1)
        draw.rectangle([50, HEIGHT - 45, 150, HEIGHT - 35], fill=NEON_TEAL + (50,))
        
        # Add dynamic loading bar
        bar_w = int((WIDTH - 100) * progress)
        draw.line([50, HEIGHT - 40, 50 + bar_w, HEIGHT - 40], fill=NEON_GREEN + (220,), width=2)

        # Convert back to RGB for gif optimization
        frames.append(img.convert("RGB"))

    # Save frames as an animated GIF
    frames[0].save(
        OUT_GIF,
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=int(1000 / FPS),  # milliseconds per frame (50ms)
        loop=0                     # 0 means loop infinitely
    )
    print(f"Animation saved to {OUT_GIF} (file size: {OUT_GIF.stat().st_size / 1024:.2f} KB)")

if __name__ == "__main__":
    generate_animation()

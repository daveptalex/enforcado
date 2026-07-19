#!/usr/bin/env python3
"""Generate icons for Enforcado 3D PWA/TWA"""
from PIL import Image, ImageDraw, ImageFont
import os

SIZES = [72, 96, 128, 144, 152, 192, 384, 512]
BG_COLOR = (10, 6, 18)
ACCENT_COLOR = (0, 243, 255)
TEXT_COLOR = (255, 255, 255)

def create_icon(size, output_path):
    img = Image.new('RGB', (size, size), BG_COLOR)
    draw = ImageDraw.Draw(img)

    center = size // 2

    # Draw hanging rope
    rope_width = max(2, size // 48)
    rope_length = size // 3
    draw.line(
        [(center, 0), (center, rope_length)],
        fill=(200, 173, 127),
        width=rope_width
    )

    # Draw stickman head (circle)
    head_radius = size // 8
    head_center = center
    head_y = rope_length + head_radius + rope_width
    draw.ellipse(
        [head_center - head_radius, head_y - head_radius,
         head_center + head_radius, head_y + head_radius],
        fill=ACCENT_COLOR
    )

    # Draw X eyes
    eye_size = max(2, size // 24)
    eye_offset_x = head_radius // 2
    eye_y_offset = head_radius // 4
    eye_color = (255, 0, 68)

    # Left eye X
    lx = head_center - eye_offset_x
    ly = head_y - eye_y_offset
    draw.line([(lx - eye_size, ly - eye_size), (lx + eye_size, ly + eye_size)], fill=eye_color, width=max(1, size // 48))
    draw.line([(lx - eye_size, ly + eye_size), (lx + eye_size, ly - eye_size)], fill=eye_color, width=max(1, size // 48))

    # Right eye X
    rx = head_center + eye_offset_x
    ry = head_y - eye_y_offset
    draw.line([(rx - eye_size, ry - eye_size), (rx + eye_size, ry + eye_size)], fill=eye_color, width=max(1, size // 48))
    draw.line([(rx - eye_size, ry + eye_size), (rx + eye_size, ry - eye_size)], fill=eye_color, width=max(1, size // 48))

    # Draw body
    body_top = head_y + head_radius
    body_bottom = body_top + size // 4
    draw.line([(center, body_top), (center, body_bottom)], fill=ACCENT_COLOR, width=max(2, size // 32))

    # Draw arms
    arm_length = size // 5
    arm_y = body_top + size // 8
    draw.line([(center - arm_length, arm_y), (center + arm_length, arm_y)], fill=ACCENT_COLOR, width=max(2, size // 40))

    # Draw legs
    leg_length = size // 5
    leg_spread = size // 7
    draw.line([(center, body_bottom), (center - leg_spread, body_bottom + leg_length)], fill=ACCENT_COLOR, width=max(2, size // 40))
    draw.line([(center, body_bottom), (center + leg_spread, body_bottom + leg_length)], fill=ACCENT_COLOR, width=max(2, size // 40))

    # Draw gallows base at the bottom
    base_y = size - size // 10
    draw.rectangle(
        [size // 6, base_y, size - size // 6, size],
        fill=(72, 43, 29)
    )

    # Draw vertical pole
    pole_x = center - size // 3
    draw.rectangle(
        [pole_x - max(2, size // 40), size // 8,
         pole_x + max(2, size // 40), base_y],
        fill=(72, 43, 29)
    )

    # Draw horizontal beam
    draw.rectangle(
        [pole_x, size // 8,
         center, size // 8 + max(3, size // 30)],
        fill=(72, 43, 29)
    )

    img.save(output_path, 'PNG')
    print(f"  Created {size}x{size} -> {output_path}")

if __name__ == '__main__':
    icons_dir = os.path.join(os.path.dirname(__file__), 'icons')
    os.makedirs(icons_dir, exist_ok=True)

    print("Generating Enforcado 3D icons...")
    for size in SIZES:
        output_path = os.path.join(icons_dir, f'icon-{size}x{size}.png')
        create_icon(size, output_path)
    print("Done!")

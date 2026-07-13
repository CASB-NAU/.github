#!/usr/bin/env python3
"""Build the Style B animated GitHub profile hero from a source video."""

from __future__ import annotations

import argparse
from pathlib import Path

import av
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps


FONT_LATIN = "/System/Library/Fonts/SFNS.ttf"
FONT_MONO = "/System/Library/Fonts/SFNSMono.ttf"
FONT_CJK = "/System/Library/Fonts/Hiragino Sans GB.ttc"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


def fit_video_frame(frame: Image.Image, size: tuple[int, int]) -> Image.Image:
    """Crop a 16:9 source into the wider GitHub hero without stretching."""
    return ImageOps.fit(
        frame.convert("RGB"),
        size,
        method=Image.Resampling.LANCZOS,
        centering=(0.58, 0.50),
    )


def glass_panel(
    base: Image.Image,
    box: tuple[int, int, int, int],
    *,
    radius: int,
    fill: tuple[int, int, int, int],
    outline: tuple[int, int, int, int],
    width: int = 2,
) -> Image.Image:
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)
    return Image.alpha_composite(base.convert("RGBA"), layer)


def add_left_vignette(image: Image.Image) -> Image.Image:
    width, height = image.size
    x = np.linspace(0.0, 1.0, width, dtype=np.float32)
    alpha = np.interp(x, [0.0, 0.42, 0.72, 1.0], [238, 214, 92, 28]).astype(np.uint8)
    overlay = np.empty((height, width, 4), dtype=np.uint8)
    overlay[..., 0] = 3
    overlay[..., 1] = 12
    overlay[..., 2] = 34
    overlay[..., 3] = alpha[None, :]
    return Image.alpha_composite(image.convert("RGBA"), Image.fromarray(overlay, "RGBA"))


def framed_logo(logo: Image.Image, size: int) -> Image.Image:
    """Place a transparent institutional emblem on a restrained glass halo."""
    source = logo.convert("RGBA")
    alpha_box = source.getchannel("A").getbbox()
    if alpha_box:
        source = source.crop(alpha_box)
    source.thumbnail((size - 18, size - 18), Image.Resampling.LANCZOS)

    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(result)
    draw.ellipse(
        (1, 1, size - 2, size - 2),
        fill=(4, 20, 47, 174),
        outline=(77, 211, 216, 142),
        width=2,
    )
    x = (size - source.width) // 2
    y = (size - source.height) // 2
    result.alpha_composite(source, (x, y))
    return result


def draw_chip(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, label: str) -> None:
    draw.rounded_rectangle(
        (x, y, x + w, y + 44),
        radius=14,
        fill=(11, 40, 72, 192),
        outline=(87, 196, 209, 155),
        width=1,
    )
    draw.ellipse((x + 15, y + 16, x + 27, y + 28), fill=(71, 226, 185, 255))
    draw.text((x + 37, y + 12), label, font=font(FONT_MONO, 16), fill=(224, 249, 246, 255))


def compose_frame(video_frame: Image.Image, logo: Image.Image, index: int, total: int) -> Image.Image:
    canvas = add_left_vignette(video_frame)

    # A restrained data grid keeps the scientific feel without fighting the footage.
    grid = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(grid)
    for x in range(0, canvas.width, 80):
        gd.line((x, 0, x, canvas.height), fill=(58, 190, 201, 16), width=1)
    for y in range(0, canvas.height, 80):
        gd.line((0, y, canvas.width, y), fill=(58, 190, 201, 14), width=1)
    canvas = Image.alpha_composite(canvas, grid)

    canvas = glass_panel(
        canvas,
        (48, 42, 930, 556),
        radius=30,
        fill=(5, 25, 54, 158),
        outline=(81, 212, 216, 125),
        width=2,
    )

    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(
        (1228, 36, 1552, 78),
        radius=16,
        fill=(8, 30, 57, 150),
        outline=(81, 212, 216, 100),
        width=1,
    )
    draw.ellipse((1250, 51, 1262, 63), fill=(71, 226, 185, 255))
    draw.text(
        (1274, 48),
        "LIVE CELLULAR SYSTEM  //  24 FPS",
        font=font(FONT_MONO, 14),
        fill=(203, 240, 241, 235),
    )

    # Subtle animated scan line on the exposed video area.
    scan_y = 110 + int((canvas.height - 180) * (index / max(total - 1, 1)))
    draw.line((955, scan_y, 1570, scan_y), fill=(58, 231, 205, 68), width=2)

    canvas.alpha_composite(framed_logo(logo, 146), (70, 62))

    x = 240
    title_y = 72
    latin_bold = font(FONT_LATIN, 78)
    draw.text((x, title_y), "CASB", font=latin_bold, fill=(245, 252, 255, 255))
    casb_w = int(draw.textlength("CASB", font=latin_bold))
    draw.text((x + casb_w + 8, title_y), "-NAU", font=latin_bold, fill=(67, 225, 181, 255))

    draw.text((82, 218), "农业合成生物学中心", font=font(FONT_CJK, 30), fill=(236, 250, 250, 255))
    draw.text(
        (82, 264),
        "Center of Agricultural Synthetic Biology",
        font=font(FONT_LATIN, 27),
        fill=(218, 237, 245, 255),
    )
    draw.text(
        (82, 306),
        "Computable models of living cells for agriculture",
        font=font(FONT_LATIN, 22),
        fill=(154, 202, 216, 255),
    )

    draw.line((82, 358, 886, 358), fill=(76, 202, 203, 128), width=1)
    draw.text((82, 378), "RESEARCH AXES", font=font(FONT_MONO, 15), fill=(91, 231, 205, 255))

    labels = ["WHOLE-CELL", "AI CELL", "DIGITAL TWIN", "DBTL"]
    widths = [188, 164, 196, 128]
    chip_x = 82
    for label, chip_w in zip(labels, widths):
        draw_chip(draw, chip_x, 414, chip_w, label)
        chip_x += chip_w + 14

    draw.text(
        (82, 500),
        "MODEL  •  PREDICT  •  DESIGN  •  VALIDATE",
        font=font(FONT_MONO, 16),
        fill=(164, 215, 223, 230),
    )

    draw.line((50, 575, 1550, 575), fill=(64, 222, 197, 110), width=1)
    draw.text((1414, 548), "CASB//NAU", font=font(FONT_MONO, 14), fill=(184, 228, 232, 220))
    return canvas.convert("RGB")


def decode_frames(
    input_path: Path,
    logo_path: Path,
    *,
    size: tuple[int, int],
    start: float,
    duration: float,
    fps: int,
) -> list[Image.Image]:
    container = av.open(str(input_path))
    stream = container.streams.video[0]
    container.seek(int(start / float(stream.time_base)), stream=stream)
    logo = Image.open(logo_path)
    targets = [start + i / fps for i in range(round(duration * fps))]
    frames: list[Image.Image] = []
    next_target = 0

    for frame in container.decode(stream):
        if frame.time is None:
            continue
        while next_target < len(targets) and frame.time >= targets[next_target]:
            video_frame = fit_video_frame(frame.to_image(), size)
            frames.append(compose_frame(video_frame, logo, next_target, len(targets)))
            next_target += 1
        if next_target >= len(targets):
            break

    container.close()
    if len(frames) != len(targets):
        raise RuntimeError(f"Expected {len(targets)} frames, decoded {len(frames)}")
    return frames


def make_palette(frames: list[Image.Image], colors: int) -> Image.Image:
    sample_count = min(12, len(frames))
    sample_indexes = np.linspace(0, len(frames) - 1, sample_count, dtype=int)
    thumbs = []
    for index in sample_indexes:
        thumb = frames[index].resize((400, 150), Image.Resampling.BILINEAR)
        thumbs.append(thumb)
    montage = Image.new("RGB", (400, 150 * sample_count))
    for i, thumb in enumerate(thumbs):
        montage.paste(thumb, (0, i * 150))
    return montage.quantize(colors=colors, method=Image.Quantize.MAXCOVERAGE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--logo", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--poster", required=True, type=Path)
    parser.add_argument("--width", type=int, default=1600)
    parser.add_argument("--height", type=int, default=600)
    parser.add_argument("--start", type=float, default=3.0)
    parser.add_argument("--duration", type=float, default=7.0)
    parser.add_argument("--fps", type=int, default=10)
    parser.add_argument("--colors", type=int, default=96)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.poster.parent.mkdir(parents=True, exist_ok=True)

    frames = decode_frames(
        args.input,
        args.logo,
        size=(args.width, args.height),
        start=args.start,
        duration=args.duration,
        fps=args.fps,
    )
    frames[0].save(args.poster, optimize=True)

    palette = make_palette(frames, args.colors)
    indexed = [
        frame.quantize(palette=palette, dither=Image.Dither.FLOYDSTEINBERG)
        for frame in frames
    ]
    indexed[0].save(
        args.output,
        save_all=True,
        append_images=indexed[1:],
        loop=0,
        duration=round(1000 / args.fps),
        disposal=2,
        optimize=True,
    )

    print(f"frames={len(indexed)}")
    print(f"gif_bytes={args.output.stat().st_size}")
    print(f"poster_bytes={args.poster.stat().st_size}")


if __name__ == "__main__":
    main()

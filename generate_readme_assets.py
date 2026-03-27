#!/usr/bin/env python3
"""Generate README visual assets using Gemini Imagen API.

Uses google-genai SDK with imagen-4.0-generate-001 model.
Outputs cached PNGs into assets/ — skips generation if file already exists.
Free-tier rate limit: 35s sleep between calls.

Run from repo root: python generate_readme_assets.py
"""

from __future__ import annotations

import os
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent
ASSETS = REPO / "assets"

API_KEY = ""

# ── Asset specifications ────────────────────────────────────────────
ASSETS_SPECS = [
    {
        "output": ASSETS / "origin_hero.png",
        "aspect_ratio": "16:9",
        "prompt": (
            "Abstract futuristic scientific research headquarters visualization "
            "on dark navy-to-deep-purple gradient background. A central luminous "
            "nexus radiating spectral energy lines outward to six glowing orbital "
            "nodes arranged in a hexagonal constellation pattern. Each node pulses "
            "with different colored light: electric blue (optimization), emerald "
            "green (drug discovery), violet (genomics), amber (voice), cyan "
            "(molecular proof), golden (commerce). Thin spectral connection lines "
            "between all nodes suggesting unified physics foundation. Subtle "
            "Hamiltonian flow field lines and statistical mechanics particle "
            "distributions in the background. Mathematical symbols and eigenvalue "
            "spectra faintly visible as watermarks. Clean scientific visualization, "
            "cinematic lighting, no text, wide panoramic, dark background, "
            "publication quality."
        ),
    },
    {
        "output": ASSETS / "origin_logo_icon.png",
        "aspect_ratio": "1:1",
        "prompt": (
            "Minimalist geometric logo icon on dark background. A stylized "
            "spectral prism or crystal at center emitting six thin spectral "
            "rays in different colors (blue, green, purple, amber, cyan, gold) "
            "fanning outward symmetrically. The prism suggests physics-based "
            "computation splitting unified theory into applications. Enclosed "
            "in a subtle circular border. Clean vector-style edges, subtle inner "
            "glow, centered, modern tech organization logo aesthetic. No text, "
            "no letters, simple iconic shape."
        ),
    },
    {
        "output": ASSETS / "origin_social_preview.png",
        "aspect_ratio": "16:9",
        "prompt": (
            "Professional scientific research organization banner. Dark "
            "navy-purple gradient background. Abstract glowing spectral nexus "
            "at center with six orbital nodes connected by thin energy lines. "
            "Hamiltonian flow fields and eigenvalue spectra as subtle background "
            "patterns. Particle distributions suggesting statistical mechanics. "
            "Scientific data visualization aesthetic, modern, clean, no text, "
            "dark theme, publication quality."
        ),
    },
]


def generate_assets():
    """Generate all README visual assets using Gemini Imagen API."""
    api_key = os.environ.get("GOOGLE_API_KEY", API_KEY)

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("WARNING: google-genai not installed. Generating placeholders.")
        print("  Install with: pip install google-genai")
        _generate_placeholders()
        return

    client = genai.Client(api_key=api_key)
    generated_count = 0

    for spec in ASSETS_SPECS:
        output = spec["output"]
        output.parent.mkdir(parents=True, exist_ok=True)

        if output.exists() and output.stat().st_size > 0:
            print(f"  Cached: {output.relative_to(REPO)}")
            continue

        if generated_count > 0:
            print("  Rate limit: waiting 35s...")
            time.sleep(35)

        print(f"  Generating: {output.relative_to(REPO)}...")
        try:
            response = client.models.generate_images(
                model="imagen-4.0-generate-001",
                prompt=spec["prompt"],
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    aspect_ratio=spec["aspect_ratio"],
                    output_mime_type="image/png",
                ),
            )
            if response.generated_images:
                img = response.generated_images[0]
                img.image.save(str(output))
                print(f"    Saved: {output.name} ({output.stat().st_size:,} bytes)")
                generated_count += 1
            else:
                print(f"    WARNING: No image generated for {output.name}")
                _make_placeholder(output, spec["prompt"])
        except Exception as e:
            print(f"    ERROR: {e}")
            _make_placeholder(output, spec["prompt"])


def _generate_placeholders():
    """Generate placeholder images when API is unavailable."""
    for spec in ASSETS_SPECS:
        output = spec["output"]
        if output.exists() and output.stat().st_size > 0:
            print(f"  Cached: {output.relative_to(REPO)}")
            continue
        _make_placeholder(output, spec["prompt"])


def _make_placeholder(output: Path, prompt: str):
    """Create a simple placeholder PNG with the prompt text."""
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        from PIL import Image, ImageDraw, ImageFont

        img = Image.new("RGB", (1280, 720), color=(10, 15, 25))
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", 16)
            title_font = ImageFont.truetype("arial.ttf", 24)
        except OSError:
            font = ImageFont.load_default()
            title_font = font

        draw.text((40, 30), "[PLACEHOLDER — Gemini Imagen]", fill=(140, 140, 180), font=title_font)
        words = prompt.split()
        lines, line = [], ""
        for w in words:
            if len(line + w) > 80:
                lines.append(line)
                line = w + " "
            else:
                line += w + " "
        if line:
            lines.append(line)
        for i, ln in enumerate(lines[:20]):
            draw.text((40, 80 + i * 24), ln.strip(), fill=(100, 100, 140), font=font)
        img.save(str(output))
        print(f"  Placeholder: {output.relative_to(REPO)}")
    except ImportError:
        import struct, zlib

        def _png_chunk(chunk_type, data):
            c = chunk_type + data
            return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c) & 0xFFFFFFFF)

        width, height = 320, 180
        raw = b"".join(b"\x00" + b"\x0a\x0f\x19" * width for _ in range(height))
        png = b"\x89PNG\r\n\x1a\n"
        png += _png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        png += _png_chunk(b"IDAT", zlib.compress(raw))
        png += _png_chunk(b"IEND", b"")
        output.write_bytes(png)
        print(f"  Minimal placeholder: {output.relative_to(REPO)}")


def main():
    print("=" * 60)
    print("OriginNeuralAI: Generating README Visual Assets")
    print("=" * 60)
    generate_assets()
    total = sum(1 for s in ASSETS_SPECS if s["output"].exists())
    print(f"\n  Total asset files: {total}/{len(ASSETS_SPECS)}")
    print("Done!")


if __name__ == "__main__":
    main()

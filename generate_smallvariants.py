#!/usr/bin/python3

import os
from PIL import Image

path = os.path.dirname(os.path.realpath(__file__)) + "/"
resources = ["res/drawable-nodpi"]
TARGET_SIZE = (600, 600)

def clean(wallpapers_path):
    if not os.path.exists(wallpapers_path):
        return
    wallpapers = os.listdir(wallpapers_path)
    for wallpaper in wallpapers:
        if wallpaper.endswith("_small.png"):
            os.remove(os.path.join(wallpapers_path, wallpaper))


def generate_smallvariants(resource):
    wallpapers_path = os.path.join(path, resource)
    if not os.path.exists(wallpapers_path):
        return

    clean(wallpapers_path)
    wallpapers = os.listdir(wallpapers_path)
    valid_extensions = (".png", ".jpg", ".jpeg", ".webp")

    for wallpaper in wallpapers:
        if not wallpaper.lower().endswith(valid_extensions) or wallpaper.endswith("_small.png"):
            continue

        base_name = os.path.splitext(wallpaper)[0]
        wallpaper_small = base_name + "_small.png"

        input_path = os.path.join(wallpapers_path, wallpaper)
        output_path = os.path.join(wallpapers_path, wallpaper_small)

        try:
            with Image.open(input_path) as img:
                img_small = img.copy()
                img_small.thumbnail(TARGET_SIZE, Image.Resampling.LANCZOS)
                img_small.save(output_path, "PNG", optimize=True)
        except Exception:
            pass


if __name__ == "__main__":
    for resource in resources:
        generate_smallvariants(resource)
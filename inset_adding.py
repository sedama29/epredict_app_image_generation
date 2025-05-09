import os
from PIL import Image, ImageDraw

# Config
folder_path = r"C:\wamp64\www\map_enterococcus_2\test_4"
corner_size = (65, 65)
corner_position = 'bottom-right'

def get_parent_map_name(child_map_name):
    """
    Get parent map based on filename. For L2 maps, always return map_L1.png.
    """
    parts = child_map_name.replace('.png', '').split('-')
    level = int(parts[0][-1])
    if level <= 1:
        return None
    if level == 2:
        return "map_L1.png"
    parent_level = f"L{level - 1}"
    parent_parts = parts[1:-1]
    if not parent_parts:
        return f"map_{parent_level}.png"
    return f"map_{parent_level}-{'-'.join(parent_parts)}.png"

def get_corner_coordinates(base_size, inset_size, position='bottom-right'):
    bx, by = base_size
    ix, iy = inset_size
    if position == 'bottom-right':
        return (bx - ix, by - iy)
    elif position == 'top-left':
        return (0, 0)
    elif position == 'top-right':
        return (bx - ix, 0)
    elif position == 'bottom-left':
        return (0, by - iy)
    return (bx - ix, by - iy)

# Process all images in the folder
for filename in os.listdir(folder_path):
    if not filename.startswith("map_L") or not filename.endswith(".png"):
        continue

    filepath = os.path.join(folder_path, filename)
    parent_name = get_parent_map_name(filename)

    if not parent_name:
        continue  # Skip L1
    parent_path = os.path.join(folder_path, parent_name)

    if not os.path.exists(parent_path):
        print(f"❌ Parent map not found for {filename}: {parent_name}")
        continue

    try:
        base_img = Image.open(filepath).convert("RGBA")
        inset_img = Image.open(parent_path).convert("RGBA").resize(corner_size)

        # Draw soft semi-transparent brown border
        draw = ImageDraw.Draw(inset_img)
        brown_rgba = (160, 82, 45, 136)  # #A0522D88
        draw.rectangle([0, 0, inset_img.width - 1, inset_img.height - 1], outline=brown_rgba)

        # Paste inset into child image
        paste_position = get_corner_coordinates(base_img.size, inset_img.size, corner_position)
        base_img.paste(inset_img, paste_position, inset_img)

        base_img.save(filepath)
        print(f"✅ Updated {filename} with inset from {parent_name}")
    except Exception as e:
        print(f"⚠️ Error processing {filename}: {e}")

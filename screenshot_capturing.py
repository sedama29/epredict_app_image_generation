import time
import keyboard
from PIL import Image, ImageDraw, ImageFont
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Screenshot and cropping config
crop_left = 70
crop_bottom_margin = 20
final_size = (350, 350)

# Set Chrome window size
window_width = 425
window_height = 430

# Set Chrome options
options = Options()
options.headless = False
options.add_argument(f"--window-size={window_width},{window_height}")

# Launch browser
driver = webdriver.Chrome(options=options)
driver.get("http://localhost/map_enterococcus_2/index_2.html")

print("Focus the browser and drag the map as needed.")
print("Press Ctrl+Shift+S to take a screenshot.")
print("Press Ctrl+Shift+Q to quit.")

count = 0

try:
    while True:
        if keyboard.is_pressed('ctrl+shift+s'):
            level = input("Enter level/part (e.g. L1, L2-P3): ").strip()
            raw_filename = f"map_screenshot_raw_{count:02d}.png"
            final_filename = f"map_{level}.png"

            # Take screenshot
            driver.save_screenshot(raw_filename)

            with Image.open(raw_filename) as img:
                width, height = img.size

                # Crop: left and bottom
                cropped = img.crop((
                    crop_left,
                    0,
                    width,
                    height - crop_bottom_margin
                ))

                # Resize to 350x350
                resized_img = cropped.resize(final_size, Image.Resampling.LANCZOS)

                # Draw text and line
                draw = ImageDraw.Draw(resized_img)
                try:
                    font = ImageFont.truetype("arialbd.ttf", 20)  # Bold font
                except IOError:
                    font = ImageFont.load_default()
                    print("⚠️ Bold font not found, using default.")

                text = "Texas Coast"
                x_text = 10
                y_text = 10

                # Draw text
                draw.text((x_text, y_text), text, font=font, fill="black")

                # Draw line below text with no side padding
                text_height = font.getbbox(text)[3] - font.getbbox(text)[1]
                line_y = y_text + text_height + 5
                draw.line((0, line_y, final_size[0], line_y), fill="black", width=2)

                # Save and preview
                resized_img.save(final_filename)
                resized_img.show()

            print(f"✅ Screenshot saved as {final_filename}")

            keep = input("Keep this screenshot? (y/n): ").strip().lower()
            if keep != 'y':
                os.remove(final_filename)
                print("❌ Screenshot deleted.")
            else:
                count += 1

            os.remove(raw_filename)
            time.sleep(1)

        if keyboard.is_pressed('ctrl+shift+q'):
            print("👋 Quitting...")
            break

except KeyboardInterrupt:
    print("🛑 Stopped by user.")

finally:
    driver.quit()

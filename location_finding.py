import cv2
import os

# Images to annotat5
# image_names = [f"map_L5-P3-P1-P2-P{i}.png" for i in range(1, 7)]
image_names = [f"map_L4-P3-P3-P1.png"]

image_folder = "C:/projects/epredict/assets/map_images"
output_file = "bounding_boxes_output.txt"

font = cv2.FONT_HERSHEY_SIMPLEX

def annotate_image(image_name):
    img_path = os.path.join(image_folder, image_name)
    img = cv2.imread(img_path)
    if img is None:
        print(f"⚠️ Image not found: {img_path}")
        return

    clone = img.copy()
    click_buffer = []
    coords = []
    box_counter = 1

    def click_event(event, x, y, flags, param):
        nonlocal click_buffer, box_counter, img

        if event == cv2.EVENT_LBUTTONDOWN:
            click_buffer.append((x, y))
            print(f"Clicked ({x}, {y})")

            # Draw a small dot
            cv2.circle(img, (x, y), 3, (0, 255, 0), -1)
            cv2.imshow("Image", img)

            # Once 4 points are collected
            if len(click_buffer) == 4:
                label = f"{image_name.replace('.png','')}_POINT{box_counter}"
                coords.append((label, click_buffer.copy()))
                print(f"✅ {label} recorded: {click_buffer}")

                # Draw polygon
                pts = click_buffer + [click_buffer[0]]
                for i in range(4):
                    cv2.line(img, pts[i], pts[i+1], (255, 0, 0), 1)
                cv2.putText(img, f"POINT{box_counter}", pts[0], font, 0.5, (255, 0, 255), 1)

                click_buffer.clear()
                box_counter += 1
                cv2.imshow("Image", img)

    print(f"🖱 Annotating {image_name} — Click 4 corners per box. Press any key when done.")
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save results
    with open(output_file, 'a') as f:
        for label, points in coords:
            flat = [str(coord) for pt in points for coord in pt]
            f.write(f"{label}," + ",".join(flat) + "\n")
    print(f"💾 Saved {len(coords)} boxes for {image_name}\n")

# === MAIN LOOP ===
for image_name in image_names:
    annotate_image(image_name)

print(f"✅ All done. Saved results to {output_file}")

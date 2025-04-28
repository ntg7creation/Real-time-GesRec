import cv2
import os

# === USER INPUTS ===
video_path = input("Enter path to your video (.mp4): ").strip()
subject_name = input("Enter subject name (e.g., Subject02): ").strip()
group_name = input("Enter group name (e.g., Group01): ").strip()

# === OUTPUT PATH ===
root_output_path = os.path.join("results", "videos", subject_name, group_name, "rgb")
os.makedirs(root_output_path, exist_ok=True)

# === EXTRACT FRAMES ===
cap = cv2.VideoCapture(video_path)
frame_idx = 0

if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}")
    exit(1)

print(f"Saving frames to: {root_output_path}")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_filename = os.path.join(root_output_path, f"rgb_{frame_idx:05d}.jpg")
    cv2.imwrite(frame_filename, frame)
    frame_idx += 1

cap.release()

print(f"Done! Extracted {frame_idx} frames.")

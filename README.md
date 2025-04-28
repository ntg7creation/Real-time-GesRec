# Real-time Gesture Recognition

This repository is based on [Real-time-GesRec](https://github.com/ahmetgunduz/Real-time-GesRec) with modifications for easier setup and custom usage.

It includes:
- Real-time gesture detection and classification
- Video splicer utility for frame extraction
- Updated scripts and instructions for streamlined usage

---

## 📦 Setup Instructions

**Requirements**:
- Python 3.7
- PyTorch 1.8
- OpenCV (`opencv-python`)

**Installation**:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ntg7creation/Real-time-GesRec.git
   cd Real-time-GesRec
   ```

2. **(Optional) Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   .\venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install torch==1.8.0 torchvision==0.9.0 opencv-python
   ```

4. **Download Pretrained Models**:

Download the pretrained models from the following link:

[Download Pretrained Models](https://drive.google.com/file/d/1rSWnzlOwGXjO_6C7U8eE6V43MlcnN6J_/view)

After downloading, extract the `results` folder into the root of the project directory.

Your structure should look like:
```
Real-time-GesRec/
├── results/
│   ├── egogesture_resnetl_10_Depth_8_9939.pth
│   ├── egogesture_resnext_101_Depth_32_9403.pth
│   └── ...
├── extract_frames.py
├── online_test.py
├── run_online.sh
└── README.md
```

---

## 🎥 Extract Frames from Video

Before running the recognition, **frames must be extracted** from your video.

Use the provided `extract_frames.py` script:

```bash
python extract_frames.py
```

It will ask you to provide:
- Video file path (e.g., `Videos/my_video.mp4`)
- Subject name (e.g., `Subject02`)
- Group name (e.g., `Group01`)

Frames will be saved in:
```
results/videos/{SubjectName}/{GroupName}/rgb/
```

Example:
```
results/videos/Subject02/Group01/rgb/rgb_00000.jpg
```

> ✅ *Use the exact folder naming format (SubjectXX/GroupXX) as expected by the model.*

---

## ⚙️ Running the Gesture Recognition System

After extracting frames, run the detection/classification system.

### 1. Update Paths (If Needed)

Edit the `run_online.sh` script to adjust paths if necessary:

```bash
--root_path "./"
--video_path "results/videos"
--annotation_path "annotation_EgoGesture/egogestureall.json"
--resume_path_det "results/egogesture_resnetl_10_Depth_8_9939.pth"
--resume_path_clf "results/egogesture_resnext_101_Depth_32_9403.pth"
```

If your folder structure differs, update these accordingly.

### 2. Run the Script

On **Linux/macOS**:
```bash
bash run_online.sh
```

On **Windows** (with Git Bash or WSL installed):
```bash
bash run_online.sh
```

If unable to run `.sh` files directly on Windows, copy the commands inside `run_online.sh` and execute them manually.

---

## ⚠️ Important Notes

- The current code processes **only Subject02** by default:
  ```python
  subject_list = ['Subject{:02d}'.format(i) for i in [2]]
  ```
  ✉️ *To use other subjects, manually edit `subject_list` in the relevant scripts.*

- Pre-trained models must be placed correctly under the `results/` folder.

- The detection uses **Depth modality**. Make sure your frames and settings match the expected input.

---

## ✨ Future Improvements

- Allow dynamic subject selection instead of hardcoding `Subject02`.
- Auto-detect relative paths in `run_online.sh`.
- Expand to support RGB+Depth fusion.

---

# ✅ Quick Summary Table

| Task                         | Command/Instructions                         |
|-------------------------------|----------------------------------------------|
| Set up environment            | Install Python 3.7 + pip install requirements |
| Extract video frames          | `python extract_frames.py`                  |
| Download pretrained models    | [Download models and extract `results/`](https://drive.google.com/file/d/1rSWnzlOwGXjO_6C7U8eE6V43MlcnN6J_/view) |
| Run real-time gesture test    | `bash run_online.sh`                         |

---

# Acknowledgement

Based on the original work: [Real-time-GesRec](https://github.com/ahmetgunduz/Real-time-GesRec).

---

> Created and maintained by [ntg7creation](https://github.com/ntg7creation)

# Real-time Gesture Recognition (Custom Clean Version)

This is a cleaned and fixed version of the [Real-time-GesRec](https://github.com/ahmetgunduz/Real-time-GesRec) project, adapted for easier setup and running.

✅ Clean loading: Models are loaded **only once**.
✅ No messy prints.
✅ Compatible with CPU evaluation.

---

## Acknowledgment

This project is based on the original work by Ahmet Gunduz: [Real-time-GesRec](https://github.com/ahmetgunduz/Real-time-GesRec).

---

## Requirements

- **Python** 3.7.9
- **PyTorch** 1.8.0
- **Torchvision** 0.8.1
- **Git Bash** (recommended on Windows)


## Installation Instructions

### 1. Install Python 3.7
- Download from: [Python 3.7.9 64-bit installer](https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe)
- During installation:
  - Check "Add Python 3.7 to PATH"
  - Enable `pip` installation


### 2. Set up the Virtual Environment
Open Git Bash inside your project folder.

```bash
py -3.7 -m venv venv37
source venv37/Scripts/activate
```

✅ You should now see `(venv37)` in your prompt.


### 3. Install PyTorch and Torchvision
Inside the activated venv:

```bash
pip install torch==1.8.0 torchvision==0.8.1
```


### 4. Prepare the Model Files
- Download the pretrained models.
- Move and rename the models into the `results/` folder:

| From | To |
|:----|:---|
| `results/shared/egogesture_resnetl_10_Depth_8.pth` | `results/egogesture_resnetl_10_Depth_8_9939.pth` |
| `results/shared/egogesture_resnext_101_Depth_32.pth` | `results/egogesture_resnext_101_Depth_32_9403.pth` |


### 5. Prepare the Test Video
Create this folder structure inside your project:

```
results/videos/Subject02/Scene1/Color/rgb1.avi
```

- Place your test `.avi` video as `rgb1.avi` in the `Color/` folder.


### 6. (Optional) Prepare Labels
If you want real evaluation, you must also have corresponding label CSV files:

```
results/videos/labels-final-revised1/subject02/Group01/Groupg.csv
```

Otherwise, the model will predict but cannot calculate accuracy.


## Running the Project

Activate the venv and run the evaluation:

```bash
source venv37/Scripts/activate
bash run_online.sh
```

✅ Models will load once, then evaluation will start cleanly.


## Important Notes

- If no valid videos are found, accuracy = 0.
- If labels are missing, predictions can run but accuracy will not be computed.
- FutureWarnings about `kaiming_normal` can be ignored.
- **No training is performed**, only real-time evaluation.


---

**This custom setup provides a much cleaner experience for working with Real-time Gesture Recognition.** 🚀


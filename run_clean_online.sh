#!/bin/bash

# Activate the virtual environment (you still need to do it manually or before running this script)
# source venv37/Scripts/activate

# Run the clean version
python clean_online_test.py \
  --root_path "C:/Users/natai/OneDrive/Documents/Repos/Hand_AI/Real-time-GesRec" \
  --video_path "C:/Users/natai/OneDrive/Documents/Repos/Hand_AI/Real-time-GesRec/results/videos" \
  --annotation_path "C:/Users/natai/OneDrive/Documents/Repos/Hand_AI/Real-time-GesRec/annotation_EgoGesture/egogestureall.json" \
  --resume_path_det "results/egogesture_resnetl_10_Depth_8_9939.pth" \
  --resume_path_clf "results/egogesture_resnext_101_Depth_32_9403.pth" \
  --result_path "results" \
  --dataset "egogesture" \
  --sample_duration_det 8 \
  --sample_duration_clf 32 \
  --model_det "resnetl" \
  --model_clf "resnext" \
  --model_depth_det 10 \
  --model_depth_clf 101 \
  --resnet_shortcut_det "A" \
  --resnet_shortcut_clf "B" \
  --batch_size 1 \
  --n_classes_det 2 \
  --n_finetune_classes_det 2 \
  --n_classes_clf 83 \
  --n_finetune_classes_clf 83 \
  --test

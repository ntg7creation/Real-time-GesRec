import torch
import argparse
from opts import parse_opts_online
from models.resnetl import resnetl
from models.resnext import resnext
from spatial_transforms import Compose, Scale, CenterCrop, ToTensor, Normalize
from target_transforms import ClassLabel
from utils import AverageMeter
from make_dataset import make_test_data
from mean import get_mean


def load_models(opt):
    # Load detector
    detector = resnetl(opt.model_depth_det, opt.n_classes_det)
    checkpoint_det = torch.load(opt.resume_path_det, weights_only=False)
    new_state_dict_det = {k[7:] if k.startswith('module.') else k: v for k, v in checkpoint_det['state_dict'].items()}
    detector.load_state_dict(new_state_dict_det)
    detector.eval()

    # Load classifier
    classifier = resnext(opt.model_depth_clf, opt.n_classes_clf, opt.resnext_cardinality_clf, opt.sample_size, opt.sample_duration_clf, shortcut_type=opt.resnet_shortcut_clf)
    checkpoint_clf = torch.load(opt.resume_path_clf, weights_only=False)
    new_state_dict_clf = {k[7:] if k.startswith('module.') else k: v for k, v in checkpoint_clf['state_dict'].items()}
    classifier.load_state_dict(new_state_dict_clf)
    classifier.eval()

    return detector, classifier


def main():
    opt = parse_opts_online()

    # Load models once
    detector, classifier = load_models(opt)

    # Transformations
    transform = Compose([
        Scale(opt.sample_size),
        CenterCrop(opt.sample_size),
        ToTensor(opt.norm_value),
        Normalize(opt.mean, opt.std)
    ])

    # Evaluation start
    print("Start Evaluation")

    # Load test videos
    test_loader = make_test_data(opt, transform)

    with torch.no_grad():
        for i, (inputs, targets) in enumerate(test_loader):
            inputs = inputs.unsqueeze(0)

            outputs_det = detector(inputs)
            outputs_clf = classifier(inputs)

            # Process outputs if needed
            # This is simplified. Your original evaluation logic should continue here.


if __name__ == '__main__':
    main()

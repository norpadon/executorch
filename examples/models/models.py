# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# @file models.py
# Simple models for demonstration purposes.

from dataclasses import dataclass


MODEL_NAME_TO_MODEL = {
    "mul": ("toy_model", "MulModule"),
    "linear": ("toy_model", "LinearModule"),
    "add": ("toy_model", "AddModule"),
    "add_mul": ("toy_model", "AddMulModule"),
    "mv2": ("mobilenet_v2", "MV2Model"),
    "mv3": ("mobilenet_v3", "MV3Model"),
    "vit": ("torchvision_vit", "TorchVisionViTModel"),
    "w2l": ("wav2letter", "Wav2LetterModel"),
    "ic3": ("inception_v3", "InceptionV3Model"),
    "ic4": ("inception_v4", "InceptionV4Model"),
    "resnet18": ("resnet", "ResNet18Model"),
    "resnet50": ("resnet", "ResNet50Model"),
}

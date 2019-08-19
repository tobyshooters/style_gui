# Jupyter GUI for AdaIN Style Transfer

Based on [Naoto's Pytorch implementation](https://github.com/naoto0804/pytorch-AdaIN) of AdaIn.
See his repo for information about testing options and how to train a new model.

## Install
- `git clone https://github.com/tobyshooters/style_gui.git`
- `cd style_gui`
- `bash install.sh`
- `jupyter notebook style_gui.ipynb`

## Requirements
- Inference: Python 3.5+, PyTorch 0.4+, TorchVision, - Pillow
- Test: tqdm, TensorboardX

## Other options
* `--content_size`: New (minimum) size for the content image. Keeping the original size if set to 0.
* `--style_size`: New (minimum) size for the content image. Keeping the original size if set to 0.
* `--alpha`: Adjust the degree of stylization. It should be a value between 0.0 and 1.0 (default).
* `--preserve_color`: Preserve the color of the content image.

## References
- [1]: X. Huang and S. Belongie. "Arbitrary Style Transfer in Real-time with Adaptive Instance Normalization.", in ICCV, 2017.
- [2]: [Original implementation in Torch](https://github.com/xunhuang1995/AdaIN-style)

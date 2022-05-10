# Conditional-GAN-based-Mask-Guided-Portrait-Editing
This is the pytorch implementation of "Conditional GAN based Mask Guided Portrait Editing" as a part of my research project.

## Introduction
This thesis investigates geometry-guided technique using semantic facial mask as a shape guide for high-level facial component editing. The framework built in this research work leverages conditional GANs directed by supplied face masks for learning individual facial feature embeddings and the facial style. The generated images display high diversity, quality and the framework provides very good controllability on the features and the style of the generated images. The framework is capable of generating new faces from a single fixed mask, transfer style form one face to other, edit individual facial components of the image, and copy facial features from one face to another. By changing the feature extracting technique from the facial masks for training, this framework gives more control over the generated image when compared to original research work.

## Citation
Citation for the original research work
```
S. Gu, J. Bao, H. Yang, D. Chen, F. Wen and L. Yuan, “Mask-guided portrait editing with conditional gans,” in Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, 2019, pp. 3436–3445.
```


### Minimum Prerequisite
- Linux.
- Pytorch 0.4.1.
- Nvidia GPU: K40, M40, P100.
- CUDA9.2 or 10.

### Running code
- download pretrained models [here](https://drive.google.com/drive/folders/1TFI2dFzi6VZ9hL6Tin6geowUre8D_tgC?usp=sharing), put it under folder checkpoints/pretrained .
- component editing:
  ./scripts/test_edit.sh
- component transfer:
  ./scripts/test_edit_free_encode.sh 
- change the corresponding component file in results/pretrained/editfree_latest, then run:
  ./scripts/test_edit_free_generate.sh
  get the component transfer results.
- training:
  ./scripts/train.sh

### Description of the files in each directory
####Thesis

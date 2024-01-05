# Table Detection using Detectron2

- [1. Getting Started](#1-getting-started)
	- [1.1. Create a local copy of the code](#11-create-a-local-copy-of-the-code)

- [2. Setting Up the Enviornment](#2-setting-up-the-enviornment)
    - [2.1. Go to the "tableDetection" folder](#21-go-to-the-tabledetection-folder)
    - [2.2. Create a python virtual environment](#22-create-a-python-virtual-environment-to-install-the-dependencies)
    - [2.3. Activate the virtual environment](#23-activate-the-virtual-environment)

- [3. Installing Dependencies](#3-installing-dependencies)
    - [3.1. Install required packages](#31-install-following-packages-prerequisite-for-detectron2)
    - [3.2. Install detectron2](#32-install-detectron2)
    
- [4. Folder Structure](#4-folder-structure)

- [5. Run the Code](#5-run-the-code)

- [6. Result](#6-result)


# 1. Getting Started
## 1.1. Create a local copy of the code
```bash
git clone https://github.com/kvarad6/tableDetection-using-detectron2.git
```

# 2. Setting Up the Enviornment
## 2.1. Go to the "tableDetection" folder
```bash
cd tableDetection-using-detectron2
```

## 2.2. Create a python virtual environment to install the dependencies
```bash
python3 -m venv venv
```

## 2.3. Activate the virtual environment
```bash
source venv/bin/activate
```

# 3. Installing Dependencies
## 3.1. Install following packages (prerequisite for detectron2):
* `layoutparser` - is a Python library designed for document layout analysis. It allows you to extract and understand the structure and content of documents, such as images or scanned pages. It's particularly useful for tasks like detecting and parsing text regions, tables, and other elements in documents. 

* `opencv-python` - is an open-source computer vision library that provides tools for image and video processing. It includes various functions for tasks like image manipulation, object detection, image stitching, and more. It is widely used in computer vision applications and offers efficient and optimized algorithms.

* `torch & torchvision` - torch and torchvision are part of the PyTorch framework, which is a popular deep learning library.

    torch is the core library for tensor computations, and it provides a flexible and dynamic computational graph for building and training neural networks.

    torchvision is an extension of PyTorch specifically designed for computer vision tasks. It includes datasets, models, and utilities for working with images and videos. It simplifies the process of loading and preprocessing image data and integrates with PyTorch for building and training deep learning models.
* `wheel` - is a packaging format that simplifies the distribution and installation of Python packages, particularly those with compiled components.
* `Pillow` - is a powerful image processing library that facilitates a wide range of tasks related to working with images in Python.
```bash
pip install layoutparser opencv-python torch torchvision 
```
```bash
pip install wheel
```
```bash
pip install Pillow==9.5.0
```

## 3.2. Install detectron2:
```bash
pip install 'git+https://github.com/facebookresearch/detectron2.git@v0.4#egg=detectron2'
```

# 4. Folder Structure
* `tableDetection-using-detectron2` - The main code folder which includes a python file (containing code) and sub-folders to store raw and processed images.
* `imgs` - This folder contains the images from which tables need to be detected.
* `resultImgs` - This folders contains the output images which has a bounding boxes around the detected tables.

# 5. Run the Code
```bash
python3 tableDetection.py
```

# 6. Result
![table image]("https://github.com/kvarad6/tableDetection-using-detectron2/blob/main/imgs/table.jpeg")

![result image]("https://github.com/kvarad6/tableDetection-using-detectron2/blob/main/resultImgs/result_table.jpeg")

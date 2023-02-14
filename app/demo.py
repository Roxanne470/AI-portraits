#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import numpy as np
import requests
import tarfile
import torch
# from skimage import transform
# from torch.utils.data import DataLoader
# from dataloader import LoadDataset
# from torchvision import transforms
from torch.autograd import Variable
from PIL import Image
from model import U2NET
from preprocess import normPRED, prepare
from dataloader import download_model_weights


def predict(inp):

    processed_image = prepare(inp)
    input_test = Variable(processed_image)

    d = net(input_test)

    # normalization
    pred = 1.0 - d[:, 0, :, :]
    pred = normPRED(pred)

    predict = pred.squeeze()
    predict_np = predict.cpu().data.numpy()
    img = Image.fromarray(predict_np * 255).convert('RGB')
    del input_test, d, pred, predict, predict_np

    return img



if __name__ == "__main__":

    print("Downloading model weights and initializing the U-squared model...")
    download_model_weights()
    net = U2NET(3, 1)
    net.load_state_dict(torch.load("u2net.pth", map_location='cpu'))
    print("Model is ready!")

    image_files = os.listdir(os.getcwd() + "/test_photos")
    print("Starting the task...")
    i = 0
    for file in image_files:

        result_path = os.getcwd() + "/test_results/" + file
        if not os.path.isfile(result_path) and file[0] != ".":
            print(f"Generating a portrait for {file}...")
            img = Image.open(os.getcwd() + "/test_photos/" + file)
            output = predict(img)
            output.save(result_path)
            print(f"{file} is done!")
            i += 1

    if i == 0:
        print("Eh oh, looks like you didn't put any new image in the test_photos folder. The task is terminated.")
    else:
        print("The task is done! You can check the results in the test_results folder.")



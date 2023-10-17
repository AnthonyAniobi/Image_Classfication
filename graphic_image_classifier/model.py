from sklearn.svm import LinearSVC
import numpy as np
import cv2 as cv
import PIL


class Model:

    def __init__(self) -> None:
        self.model = LinearSVC()

    def train_model(self):
        img_list = np.array([])
        class_list = np.array([])

        # for i in range

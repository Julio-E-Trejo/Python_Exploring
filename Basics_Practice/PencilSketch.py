import cv2
import numpy as np
class PencilSketch:
    def __init__(self, width, height, bg_gray='pencilsketch_bg.jpg'):
        self.width = width
        self.height = height

        # try to open background canvas (if it exists)
        self.canvas = cv2.imread(bg_gray, cv2.CV_8UC1)
        if self.canvas is not None:
            self.canvas = cv2.resize(self.canvas, (self.width, self.height))
    def dodgeV2(image, mask):
        return cv2.divide(image, 255-mask, scale=256)
    def renderV2(self, img_rgb):
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        img_gray_inv = 255 - img_gray
        img_blur = cv2.GaussianBlur(img_gray_inv, (21,21), 0, 0)
        img_blend = self.dodgeV2(img_gray, img_blur)
        if self.canvas is not None:
            img_blend = cv2.multiply(img_blend, self.canvas, scale=1./256)
        return cv2.cvtColor(img_blend, cv2.COLOR_GRAY2RGB)
    def render(img_rgb):
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (21,21), 0, 0)
        img_blend = cv2.divide(img_gray, img_blur, scale=256)
        return img_blend
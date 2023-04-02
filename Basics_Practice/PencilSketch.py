import cv2
import numpy as np
class PencilSketch:
    def __init__(self, width, height, bg_gray):
        self.width = width
        self.height = height

        # try to open background canvas (if it exists)
        img_gray = cv2.cvtColor(bg_gray, cv2.COLOR_RGB2GRAY)
        self.canvas = img_gray
        if self.canvas is not None:
            self.canvas = cv2.resize(self.canvas, (self.width, self.height))

    def dodgeV2(self,image, mask):
        return cv2.divide(image, 255-mask, scale=256)
    
    # gives a sketch-like feel to an image
    def renderV2(self, img_rgb):
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        img_gray_inv = 255 - img_gray
        img_blur = cv2.GaussianBlur(img_gray_inv, (21,21), 0, 0) # gauss-blur with inverted img_gray
        img_blend = cv2.divide(img_gray, 255-img_blur, scale=256) # per-element division with img_gray_inv
        return cv2.cvtColor(img_blend, cv2.COLOR_GRAY2RGB)
    
    # not working; similar to renderV2, but with light blending
    def render(self, img_rgb):
        # similar to renderV2
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY) # gray-scale
        img_blur = cv2.GaussianBlur(img_gray, (21,21), 0, 0) # gauss blur
        img_blend = cv2.divide(img_gray, img_blur, scale=256) # per-element division
        
        # per-element multiplication
        if self.canvas is not None:
            img_blend = cv2.multiply(img_blend, self.canvas, scale=1./256)
        return img_blend
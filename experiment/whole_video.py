from crystal_tracer.visual.draw import draw_contour
import numpy as np
import cv2
from pathlib import Path
from crystal_tracer.img_utils import load_czi_slice, get_czi_shape
import platform

font = cv2.FONT_HERSHEY_PLAIN
color = (255, 255, 255)  # white color
font_scale = 1
position = (2, 2 + int(font_scale * 10))  # position of text, adjust as needed
thickness = 1


def make_video(save_path: Path, czi_path: Path, frame_rate=25., scale=.5):
    tag = 'DIVX' if platform.system() == 'Windows' else 'XVID'
    tot, c, height, width, interval = get_czi_shape(czi_path)
    width = int(scale * width)
    height = int(scale * height)
    writer = cv2.VideoWriter(str(save_path), cv2.VideoWriter_fourcc(*tag), frame_rate, (width, height))
    for i in range(tot):
        img = load_czi_slice(czi_path, 0, i)
        img = cv2.resize(img, (width, height))
        img = ((img / img.max()) * 255).astype(np.uint8)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        writer.write(img)


if __name__ == '__main__':
    save_path = Path('../data/whole.avi')
    czi_path = Path(r"D:\下载\FC1-01-Create Image Subset-04.czi")
    make_video(save_path, czi_path)
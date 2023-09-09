import os
import cv2

base_path = "./data_test"

dirs = os.listdir(base_path)
for dir in dirs:
    sub_paths = os.listdir(os.path.join(base_path, dir))
    for sub in sub_paths:
        files = os.listdir(os.path.join(base_path, dir, sub))
        for f in files:
            if 'depth' in f:
                os.remove(os.path.join(base_path, dir, sub, f))
            if 'seg' in f:
                os.remove(os.path.join(base_path, dir, sub, f))
            if 'rgb' in f:
                img = cv2.imread(os.path.join(base_path, dir, sub, f))
                img = cv2.resize(img, (224, 224))
                cv2.imwrite(os.path.join(base_path, dir, sub, f), img)
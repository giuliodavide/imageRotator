# import the necessary packages
import argparse
import imutils
import cv2
import os


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", required=True,
                help="path which contanins the list of images you want to rotate")
ap.add_argument("-d", "--degree", required=True,
                help="degree of rotation")
args = vars(ap.parse_args())
# load the image from disk
folder = args["folder"]
degree = int(args["degree"])
images = load_images_from_folder(folder)
for i in range(len(images)):
    # rotate the image
    rotated = imutils.rotate(images[i], degree)
    cv2.imwrite(folder + "/" + str(i) + ".jpg", rotated)

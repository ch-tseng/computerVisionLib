import argparse
import cv2
from libCH.descriptor import momentsDescriptor

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

moment = momentsDescriptor()
moment.loadImage(imgPath=args["image"], resize_w=200)
print moment.HuFeatures()

print moment.HuFeatures1(colorSpace="RGB", channelSelect=(1,1,1), blur=11, threshold=(120,140,150), bwInvert=True, debug=True)

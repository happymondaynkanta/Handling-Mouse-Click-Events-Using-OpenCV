# using mouse_event (switch color to other images)
import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]

        new_img = np.zeros((512, 512, 3), np.uint8)
        new_img[:] = [blue, green, red]

        cv2.imshow('color_image', new_img)



img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)


cv2.waitKey(0)
cv2.destroyAllWindows()

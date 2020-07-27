import cv2
import PIL
from PIL import Image
import numpy as np

img_list = []
cv_img_list = []
cv_img_merge_h_list = []
cv_img_merge_h_list_top = []
cv_img_merge_h_list_bottom = []
cv_img_panorama_list = []

cv_img_output_panorama = []

cv_y_zero_list = []
cv_y_two_list = []

panorama = "panorama_"

width = 900
height = 900

for i in range(0, 6):
    img_list.append(panorama + str(i) + ".png.pale")

count = 0
for img in img_list:
    img_cv = cv2.imread(img)

    cv_img_list.append(img_cv)

    count += 1

count = 0
for img in cv_img_list:
    if count <= 3:
        img = cv2.resize(img, (width, height))
        cv_img_merge_h_list.append(img)
    if count == 4:
        img = cv2.resize(img, (width, height))
        image_top = img
    if count == 5:
        img = cv2.resize(img, (width, height))
        image_bottom = img
    count += 1



for i in range(0, 4):
    rotation_matrix=cv2.getRotationMatrix2D((width / 2, height / 2), i * 90, 1)
    image_temp=cv2.warpAffine(image_bottom, rotation_matrix, (width, height))
    
    cv_img_merge_h_list_bottom.append(image_temp)

for i in range(0, 4):
    rotation_matrix=cv2.getRotationMatrix2D((width / 2, height / 2), i * 90, 1)
    image_temp=cv2.warpAffine(image_top, rotation_matrix, (width, height))
    
    cv_img_merge_h_list_top.append(image_temp)


h_stack_top = np.hstack(tuple(cv_img_merge_h_list_top))
h_stack_middle = np.hstack(tuple(cv_img_merge_h_list))
h_stack_bottom = np.hstack(tuple(cv_img_merge_h_list_bottom))

v_stack = np.vstack((h_stack_top, h_stack_middle, h_stack_bottom))
v_stack_blur = cv2.GaussianBlur(v_stack, (5, 5), 5)

for x in range(0, 4):
    for y in range(0, 3):
        image_out = v_stack_blur[y * height:y * height + height, x * width:x * width + width]
        cv_img_panorama_list.append((image_out, x, y))

def rotateAndAvg(lst : list, panoramaNumber : int):
    tempList = []
    count = 0
    for img in lst:
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), count * -90, 1)
        image_temp = cv2.warpAffine(img, rotation_matrix, (width, height))

        tempList.append(image_temp)
        count += 1

    dst = tempList[0]
    for i in range(len(tempList)):
        if i == 0:
            pass
        else:
            alpha = 1.0/(i + 1)
            beta = 1.0 - alpha
            dst = cv2.addWeighted(tempList[i], alpha, dst, beta, 0.0)

    filename = f"{panorama}{panoramaNumber}.png"
    out_dir = "output/"
    cv2.imwrite(out_dir + filename, dst)

for tup in cv_img_panorama_list:
    img = tup[0]
    x = tup[1]
    y = tup[2]
    if y == 0:
        cv_y_zero_list.append(img)
    elif y == 1:
        cv_img_output_panorama.append((img, x))
    elif y == 2:
        cv_y_two_list.append(img)

rotateAndAvg(cv_y_zero_list, 4)
rotateAndAvg(cv_y_two_list, 5)

for tup in cv_img_output_panorama:
    img = tup[0]
    x = tup[1]
    filename = f"{panorama}{x}.png"
    out_dir = "output/"
    cv2.imwrite(out_dir + filename, img)
import datetime
import time

import cv2
from collections import Counter
import rectangle_detecton.video as video
import numpy as np


hsv_min = np.array((0, 54, 5), np.uint8)
hsv_max = np.array((187, 255, 253), np.uint8)
color_red = (0,0,128)


def find_rect(img, max, min):
    hsv = cv2.cvtColor(img,
                       cv2.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр
    _, contours0, _ = cv2.findContours(thresh.copy(), cv2.RETR_TREE,
                                             cv2.CHAIN_APPROX_SIMPLE)

    # перебираем все найденные контуры в цикле
    for cnt in contours0:
        count = 0
        rect = cv2.minAreaRect(cnt)  # пытаемся вписать прямоугольник
        box = cv2.boxPoints(rect)  # поиск четырех вершин прямоугольника
        box = np.int0(box)  # округление координат
        area = int(rect[1][0] * rect[1][1])  # вычисление площади
        if area < max and area > min:
            cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
            return img, box
    return img, box


def find(img):

    # img = img[140:320]
    res = []
    hsv = cv2.cvtColor(img,
                      cv2.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр
    c_, contours0, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # перебираем все найденные контуры в цикле
    for cnt in contours0:
        count = 0
        rect = cv2.minAreaRect(cnt)  # пытаемся вписать прямоугольник
        box = cv2.boxPoints(rect)  # поиск четырех вершин прямоугольника
        box = np.int0(box)  # округление координат
        area = int(rect[1][0] * rect[1][1])  # вычисление площади
        if area < 7000 and area > 4000:
            center = (int(rect[0][0]), int(rect[0][1]))

            N = 100

            cub = []
            cube = img[center[1] - N if center[1] - N > 0 else 0: center[1] + N if center[1] + N < 480 else 480]
            for i in range(cube.shape[0]):
                cub.append(cube[i][center[0] - N if center[0] - N > 0 else 0: center[0] + N if center[0] + N < 640 else 640])
            cub = np.array(cub)
            if cub.size > 0:
                # cub, border = find_rect(cub, 8000, 5000)
                hsv_1 = cv2.cvtColor(cub,
                                     cv2.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
                thresh = cv2.inRange(hsv_1, hsv_min,
                                     hsv_max)  # применяем цветовой фильтр
                _, contours1, _ = cv2.findContours(thresh.copy(),
                                                         cv2.RETR_TREE,
                                                         cv2.CHAIN_APPROX_SIMPLE)
                width_1 = 7
                heigth_1 = 20

                for cnt in contours1:
                    if len(cnt) > 4:
                        ellipse = cv2.fitEllipse(cnt)
                        if width_1 < ellipse[1][0] < heigth_1 and width_1 < ellipse[1][1] < heigth_1:
                            count += 1
                            cv2.ellipse(cub, ellipse, (255, 0, 0), 2)

                #cv2.imshow('cube', cub)

            cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
            cv2.putText(img, count.__str__(), (center[0] + 60, center[1] - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, color_red, 2)
            if 0 < count < 7:
                res.append(count)

    width = 50
    heigth = 100

    for cnt in contours0:
        if len(cnt) > 4:
            ellipse = cv2.fitEllipse(cnt)
            if width < ellipse[1][0] < heigth and width < ellipse[1][1] < heigth:
                cv2.ellipse(img, ellipse, (255, 0, 0), 2)

    return img, res


def detect():
    cap = video.create_capture(0)
    result = []
    for i in range(30):
        flag, img = cap.read()
        try:
            img, count = find(img)

            counter = Counter(count)
            common = counter.most_common(1)
            if len(common) > 0:
                result.append(common[0][0])
        except:
            cap.release()
            raise

    result = Counter(result).most_common(1)
    return result[0][0]


def online_detect():
    cap = video.create_capture(0)

    while True:
        flag, img = cap.read()
        try:
            img, count = find(img)
            cv2.imshow('result', img)
        except:
            cap.release()
            raise

        ch = cv2.waitKey(5)
        if ch == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    print(detect())
    #online_detect()
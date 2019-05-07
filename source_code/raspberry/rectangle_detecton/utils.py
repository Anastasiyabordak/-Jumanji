import sys
from threading import Thread

import numpy as np
import cv2 as cv

hsv_min = np.array((0, 54, 5), np.uint8)
hsv_max = np.array((187, 255, 253), np.uint8)


def find(num):
    fn = f'data/3/1/photo ({num}).jpg'  # имя файла, который будем анализировать
    img = cv.imread(fn)

    hsv = cv.cvtColor(img,
                      cv.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
    thresh = cv.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр
    contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE,
                                              cv.CHAIN_APPROX_SIMPLE)

    # перебираем все найденные контуры в цикле
    count = 0
    for cnt in contours0:
        rect = cv.minAreaRect(cnt)  # пытаемся вписать прямоугольник
        box = cv.boxPoints(rect)  # поиск четырех вершин прямоугольника
        box = np.int0(box)  # округление координат
        area = int(rect[1][0] * rect[1][1])  # вычисление площади
        if area < 400 and area > 120:
            count += 1
            cv.drawContours(img, [box], 0, (255, 0, 0), 2)

    width = 10
    heigth = 30

    for cnt in contours0:
        if len(cnt) > 4:
            ellipse = cv.fitEllipse(cnt)
            if width < ellipse[1][0] < heigth and width < ellipse[1][1] < heigth:
                count += 1
                cv.ellipse(img, ellipse, (0, 0, 255), 2)

    cv.imshow('contours', img)  # вывод обработанного кадра в окно
    print(count)
    cv.waitKey()
    cv.destroyAllWindows()


class MyThread(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        find(self.num)


def create_threads():
    threads = []

    for num in range(9):
        my_thread = MyThread(num + 1)
        my_thread.start()
        threads.append(my_thread)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    find(5)
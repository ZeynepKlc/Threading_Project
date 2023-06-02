import threading
import cv2
import numpy as np
import time

start = time.perf_counter()


class ImageProcessing:
    """
    Görüntü işlemede kullanılan morfolojik işlemler (erozyon,
    genişleme ve tophat) uygulandı ve resim üzerindeki arabalar
    tespit edildi.
    """
    def __init__(self):
        """
        Üzerinde işlem yapacağımız resim dosyası tanımlandı ve thread işlemi
        start metoduyla başladı. Daha sonra join metoduyla threadlerin bitmesi beklendi.
        """

        self.image_path = "resim.jpeg"
        self.img = cv2.imread(self.image_path, 0)

        thread1 = threading.Thread(target=self.apply_morphology, args=())
        thread1.start()
        thread1.join()

        thread2 = threading.Thread(target=self.carTracking, args=())
        thread2.start()

        thread2.join()

    def apply_morphology(self):
        """
        Resim üzerinde erozyon, genişleme ve tophat işlemi
        gerçekleştirildi.
        """

        kernel = np.ones((10, 10), np.uint8)
        self.dilation = cv2.dilate(self.img, kernel, iterations=1)
        self.erosion = cv2.erode(self.img, kernel, iterations=2)
        self.tophat = cv2.morphologyEx(self.img, cv2.MORPH_TOPHAT, kernel)

        cv2.imshow("img_dilation", self.dilation)
        cv2.waitKey(2)
        time.sleep(2)

        cv2.imshow("img_erosion", self.erosion)
        cv2.waitKey(2)
        time.sleep(2)

        cv2.imshow("img_tophat", self.tophat)
        cv2.waitKey(2)
        time.sleep(2)

        print("Process continues. . .")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    def carTracking(self):
        """
        Resim dosyasındaki arabalar tespit edildi.
        """

        self.img = cv2.imread(self.image_path)
        car_classifier = cv2.CascadeClassifier("cars.xml")
        gray_image = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        cars = car_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

        while True:
            for (x, y, w, h) in cars:
                cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow("Car Tracking", self.img)
            cv2.waitKey(2)
            time.sleep(2)

            if cv2.waitKey(0) & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()
        print("Process completed for main!")


image_processor = ImageProcessing()

cv2.waitKey(0)
cv2.destroyAllWindows()

finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} seconds.")
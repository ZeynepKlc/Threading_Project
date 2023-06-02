import main
import threading
import time
import cv2

start = time.perf_counter()

class Thread1:

    """
    main klasöründeki ImageProcessor sınıfındaki metotlar birbirine senkron bir şekilde çalıştırıldı.
    """

    def __init__(self):
        """threding kütüphanesindeki Thread metoduyla sınıf içerisinde bulunan
        metotların thread işlemi başlatıldı ve join metodu ile threadlerin tamamlanması bekleniyor. """

        thread1 = threading.Thread(target=self.test1, args=())
        thread1.start()
        thread1.join()

        thread2 = threading.Thread(target=self.test1_2, args=())
        thread2.start()
        thread2.join()

    def test1(self):

        """
        Morfolojik işlemler uygulanan resimler ekranda belirli sürelerle gösterildi.
        """

        cv2.imshow("Img_dilation_thread1", main.dilation)
        cv2.waitKey(3)
        print("Image dilation_thread1 completed")
        time.sleep(2)

        cv2.imshow("Img_erosion_thread1", main.erosion)
        cv2.waitKey(3)
        print("Image erosion_thread1 completed")
        time.sleep(2)

        cv2.imshow("Img_tophat_thread1", main.tophat)
        cv2.waitKey(3)
        print("Image tophat_thread1 completed")
        time.sleep(3)
        print("Process continues for thread1. . .")

    cv2.destroyAllWindows()

    def test1_2(self):

        """
        Tespiti yapılan arablar kutu içerisine alınarak ekranda gösterildi.
        """

        cv2.imshow("Img_car_thread1", main.img)
        cv2.waitKey(4)
        print("Car image for thread1 completed")
        time.sleep(5)

    cv2.waitKey(1)

    cv2.destroyAllWindows()


main = main.ImageProcessing()
thread_1 = Thread1()


finish = time.perf_counter()
print(f"Thread1 finished in {round(finish - start, 2)} seconds.")

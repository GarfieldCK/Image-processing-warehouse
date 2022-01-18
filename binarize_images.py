import cv2
"""
    Goal : To study the method of thresholding from openCV library

"""


def otsu_imbinarize(images) :

    #1.) Otsu thresholding :

    res, thresh = cv2.threshold(images, 127, 255, cv2.THRESH_BINARY)

    return thresh



def adaptive_binarize(images) :

    #2.) Adaptive thresholding :

    #2.1 ) ADAPTIVE_THRESH_MEAN_C : The threshold value is the mean of the neighbourhood area minus the constant C.
    thresh1 = cv2.adaptiveThreshold(images,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)

    #2.2 ) ADAPTIVE_THRESH_GAUSSIAN_C : The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.
    thresh2 = cv2.adaptiveThreshold(images,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

    return thresh2


if __name__ == "__main__" :
    
    data_dir = "C:/Users/ADMIN/Downloads/Lenna.jpg"

    image = cv2.imread(data_dir)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 1.) Binarize image by using otsu method:
    bwim_1 = otsu_imbinarize(gray)

    # 2.) Binarize by using the process of adaptiveMethod : the algorithms  determines the thresholding for a pixel based on a small region around it
    bwim_2 = adaptive_binarize(gray) 

    # 3.) Truncate binarization :
    cv2.imshow("Windows",bwim_2)
    cv2.waitKey(0)

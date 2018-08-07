from image import getImage as img

from VARS import TIME_STAMP


if __name__ == '__main__':

    ts = TIME_STAMP
    
    path = img.getimage(ts)

    print path

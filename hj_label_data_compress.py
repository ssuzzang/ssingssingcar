
import sys
import os 
import glob
import zipfile

def main():
    """
    3단계에서 슬라이싱 되고 생성된 수많은 이미지 데이터-라벨 파일들을 하나로 압축
    """

    condition =  "./data/*.png"

    png_files = glob.glob(condition)
    print(png_files)

    with zipfile.ZipFile("car_image_angle.zip", 'w') as my_zip:
        for file in png_files:
            my_zip.write(file)
    my_zip.close()

if __name__ =='__main__':
	main()



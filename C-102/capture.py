import cv2
import time
import dropbox
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result = True

    while(result):
        rect, frame=videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time=time.time
        result = False
    return img_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="sl.A9fejo6ey0-sUM7OvrMPVJDM26NaZZkuDzgaCynNa2CpwGxh2nHbFXzlgFLbZgHxUxeasx98dWCIOaNBtXSAWm1mb8e1K9bjGm6EpQBEj-pNdOsdygRjSDY-zO9jqI6Jpdbmemw"
    file=img_name
    file_from=file
    file_to="/test/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("file Uploaded")

def main():
    while(True):
        if((time.time()-start_time) >=300):
            name=take_snapshot()
            upload_file(name)

    

main()
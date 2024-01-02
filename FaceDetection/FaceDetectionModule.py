import cv2
import mediapipe as mp
import time

mpfaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpfaceDetection.FaceDetection(0.75)

while True:
    success, img = cap.read()

    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB) #increases frame rate
    print(results)

    if results.detections:
        for id, detection in enumerate(results.detections): #enumerate because we want id number too
            # print(id,detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)
            # mpDraw.draw_detection(img,detection)#get points
            bboxC = detection.location_data.relative_bounding_box #bounding box from class
            ih,iw,ic = img.shape #get dimensions (image height, image width, image channel)
            bbox = int(bboxC.xmin*iw), int(bboxC.ymin*ih), int(bboxC.width*iw), int(bboxC.height*ih)
            cv2.rectangle(img,bbox,(255,0,255),2)
            cv2.putText(img,f'{int(detection.score[0]*100)}%',(bbox[0],bbox[1]-20),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),2)

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0

    while True:
        success, img = cap.read()

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img,f'FPS: {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()
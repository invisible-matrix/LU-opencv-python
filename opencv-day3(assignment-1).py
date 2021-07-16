import cv2

cam = cv2.VideoCapture(0)
image = cv2.imread('E:\photos/iron.jpg')
image1 = cv2.imread('E:\photos/background.jpg')
image2 = cv2.imread('E:\photos/avg.jpg')
image3 = cv2.imread('E:\photos/falls.jpg')
image4 = cv2.imread('E:\photos/space.png')
image5 = cv2.imread('E:\photos/tiger.jpg')



k = int(input('choose any one number from 1 to 6: '))

while True:
    flag, frame = cam.read()
    if not flag:
        print('Could not access the camera')
        break
    elif flag:
      if k == 1:
         image = cv2.resize(image, (frame.shape[1], frame.shape[0]))
         blended_frame1 = cv2.addWeighted(frame, 0.7, image, 0.3, gamma = 0.1)
         cv2.imshow('Blended Frame 1', blended_frame1)
      elif k == 2:
           image1 = cv2.resize(image1, (frame.shape[1], frame.shape[0]))
           blended_frame2 = cv2.addWeighted(frame, 0.7, image1, 0.3, gamma = 0.1)
           cv2.imshow('Blended Frame 2', blended_frame2)
      elif k == 3:
          image2 = cv2.resize(image2, (frame.shape[1], frame.shape[0]))
          blended_frame3 = cv2.addWeighted(frame, 0.7, image2, 0.3, gamma = 0.1)
          cv2.imshow('Blended Frame 3', blended_frame3)
      elif k == 4:
          image3 = cv2.resize(image3, (frame.shape[1], frame.shape[0]))
          blended_frame4 = cv2.addWeighted(frame, 0.7, image3, 0.3, gamma = 0.1)
          cv2.imshow('Blended Frame 4', blended_frame4)
      elif k == 5:
         image4 = cv2.resize(image4, (frame.shape[1], frame.shape[0]))
         blended_frame5 = cv2.addWeighted(frame, 0.7, image4, 0.3, gamma = 0.1)
         cv2.imshow('Blended Frame 5', blended_frame5)
      elif k == 6:
         image5 = cv2.resize(image5, (frame.shape[1], frame.shape[0]))
         blended_frame6 = cv2.addWeighted(frame, 0.7, image5, 0.3, gamma = 0.1)
         cv2.imshow('Blended Frame 6', blended_frame6)
   
    m = cv2.waitKey(1)
    if m == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()
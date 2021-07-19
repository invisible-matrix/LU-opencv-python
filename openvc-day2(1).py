import cv2
import numpy as np
canvas = np.zeros((500,500,3),np.uint8)
cv2.line(canvas,(0,0),(511,511),(0,0,200),3)
cv2.rectangle(canvas,(0,0),(300,300),(0,255,0),9)
cv2.putText(canvas,"over 9000",(200,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,225))
cv2.imshow("canvas",canvas)
cv2.waitKey(0)
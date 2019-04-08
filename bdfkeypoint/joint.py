import cv2
import os
class Joint(object):
    
    __circle_list = []
    
    def __init__(self,dic):    
        self.dic = dic
    
    def draw_line(self,img):
        #nose ---> neck
        cv2.line(img, (int(self.dic['nose']['x']),int(self.dic['nose']['y'])),
                 (int(self.dic['neck']['x']),int(self.dic['neck']['y'])), (0,255,0), 2)
        #neck --> left_shoulder
        cv2.line(img, (int(self.dic['neck']['x']),int(self.dic['neck']['y'])),
                 (int(self.dic['left_shoulder']['x']),int(self.dic['left_shoulder']['y'])), (0,255,0), 2)        
        #neck --> right_shoulder
        cv2.line(img, (int(self.dic['neck']['x']),int(self.dic['neck']['y'])),
                 (int(self.dic['right_shoulder']['x']),int(self.dic['right_shoulder']['y'])), (0,255,0), 2)        
        #left_shoulder --> left_elbow
        cv2.line(img, (int(self.dic['left_shoulder']['x']),int(self.dic['left_shoulder']['y'])),
                 (int(self.dic['left_elbow']['x']),int(self.dic['left_elbow']['y'])), (0,255,0), 2)         
        #left_elbow --> left_wrist
        cv2.line(img, (int(self.dic['left_elbow']['x']),int(self.dic['left_elbow']['y'])),
                 (int(self.dic['left_wrist']['x']),int(self.dic['left_wrist']['y'])), (0,255,0), 2)         
        #right_shoulder --> right_elbow
        cv2.line(img, (int(self.dic['right_shoulder']['x']),int(self.dic['right_shoulder']['y'])),
                 (int(self.dic['right_elbow']['x']),int(self.dic['right_elbow']['y'])), (0,255,0), 2)          
        #right_elbow --> right_wrist
        cv2.line(img, (int(self.dic['right_elbow']['x']),int(self.dic['right_elbow']['y'])),
                 (int(self.dic['right_wrist']['x']),int(self.dic['right_wrist']['y'])), (0,255,0), 2)         
        #neck --> left_hip
        cv2.line(img, (int(self.dic['neck']['x']),int(self.dic['neck']['y'])),
                 (int(self.dic['left_hip']['x']),int(self.dic['left_hip']['y'])), (0,255,0), 2)         
        #neck --> right_hip
        cv2.line(img, (int(self.dic['neck']['x']),int(self.dic['neck']['y'])),
                 (int(self.dic['right_hip']['x']),int(self.dic['right_hip']['y'])), (0,255,0), 2)       
        #left_hip --> left_knee
        cv2.line(img, (int(self.dic['left_hip']['x']),int(self.dic['left_hip']['y'])),
                 (int(self.dic['left_knee']['x']),int(self.dic['left_knee']['y'])), (0,255,0), 2)        
        #right_hip --> right_knee
        cv2.line(img, (int(self.dic['right_hip']['x']),int(self.dic['right_hip']['y'])),
                 (int(self.dic['right_knee']['x']),int(self.dic['right_knee']['y'])), (0,255,0), 2)        
        #left_knee --> left_ankle
        cv2.line(img, (int(self.dic['left_knee']['x']),int(self.dic['left_knee']['y'])),
                 (int(self.dic['left_ankle']['x']),int(self.dic['left_ankle']['y'])), (0,255,0), 2)        
        #right_knee --> right_ankle
        cv2.line(img, (int(self.dic['right_knee']['x']),int(self.dic['right_knee']['y'])),
                 (int(self.dic['right_ankle']['x']),int(self.dic['right_ankle']['y'])), (0,255,0), 2)
        
    def xunhun(self,img):
        im1 = cv2.imread(img,cv2.IMREAD_COLOR)
        #im2 = cv2.resize(im1, (1040,768), interpolation=cv2.INTER_CUBIC)
        
        for i in self.dic:
            cv2.circle(im1,(int(self.dic[i]['x']),int(self.dic[i]['y'])),5,(0,255,0),-1)
               
        self.draw_line(im1)
        cv2.imshow('image',im1)
        cv2.waitKey(0)


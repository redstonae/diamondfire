#special thanks to stack overflow for the enitre code here <3

import cv2
import os

#EDIT HERE!!!!!!
input_path = r"C:/your_video_path_here"
output_patch = r"C:/your_frames_path_here"
videos_fps = 30 #change this to macth the number of frames per second in your video
pictures_per_second = 1 #1 is recomended, it can go lower (such as 0.5), but should never be higher than 2
#DON'T EDIT ANYTHING BELOW

tpf = videos_fps/pictures_per_second
pathOut = output_patch
count = 0
counter = 1
num = 1
listing = os.listdir(input_path)
for vid in listing:
    vid = input_path+vid
    cap = cv2.VideoCapture(vid)
    count = 0
    counter += 1
    success = True
    while success:
        success,image = cap.read()
        print('read a new frame:',success)
        if count%tpf == 0 :
             cv2.imwrite(pathOut + '%d.png'%num,image)
             num+=1
        count+=1
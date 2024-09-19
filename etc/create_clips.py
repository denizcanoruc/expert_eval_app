import boto3
import json
import cv2
from botocore.exceptions import ClientError
import gzip
import json
import io
import pandas as pd
import os
import shutil

"""
client = boto3.client(
    's3',
    aws_access_key_id = 'AKIAQ66ZZ7D4Z2FZR44S',
    aws_secret_access_key = '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',
    region_name = 'eu-central-1'
)


cb_research_bucket = client.list_objects_v2(Bucket='clubbrugge-research-wyscout', Prefix="video/competition-198/season-187389")

tot = 0
for object in cb_research_bucket['Contents']:
    if object["Key"].endswith('mp4'):
        print(object["Key"])




for (dirpath, dirnames, filenames) in os.walk("/Users/denizcanoruc/Desktop/shot-clips-example"):
        temp = filenames


try:
    df = pd.read_csv('/Users/denizcanoruc/Desktop/shot_clips/clip_frames.csv', index_col=None)
except FileNotFoundError: 
    df = pd.DataFrame(columns=['match','shot','frame'])


    
path_vid = os.path.join("/Users/denizcanoruc/Desktop/shot-clips-example")
path_clip = os.path.join("/Users/denizcanoruc/Desktop/shot_clips")
for file in temp:
    if(file.endswith(".mp4")):
            if(df['shot'].eq(file.replace(".mp4",""))).any():
                continue
            file_path = os.path.join(path_vid,file)
            print(file_path)
            video = cv2.VideoCapture(file_path)
            video.set(cv2.CAP_PROP_POS_FRAMES, 130)
            while video.isOpened():
                ret, frame = video.read()
                next_frame = video.get(cv2.CAP_PROP_POS_FRAMES)
                current_frame = next_frame - 1
                previous_frame = current_frame - 1
                #if previous_frame >= 0:
                #    video.set(cv2.CAP_PROP_POS_FRAMES, previous_frame)
                # Display each frame
                cv2.imshow("video", frame)
                # show one frame at a time
                key = cv2.waitKey(0)
                while key not in [ord('q'), ord('k'), ord('j'), ord('e')]:
                    key = cv2.waitKey(0)
                # Quit when 'q' is pressed
                if key == ord('k'):
                    continue
                elif key == ord('j'):
                    video.set(cv2.CAP_PROP_POS_FRAMES, previous_frame)
                elif key == ord('q'):
                    new_row = pd.DataFrame.from_dict([{'match' : file[5:13] , 'shot' : file.replace(".mp4",""), 'frame' : current_frame}], orient='columns')
                    df = pd.concat([df, new_row])
                    cv2.imwrite(os.path.join(path_clip,file.replace(".mp4",".jpg")), frame)
                    df.to_csv('/Users/denizcanoruc/Desktop/shot_clips/clip_frames.csv', index = False)
                    break
                elif key == ord('e'):
                    break   





# this loop is for loading video files from older file hiararchy.
for dir in temp:
    path_vid = os.path.join("/Users/denizcanoruc/Desktop/video_data/competition-198/season-187389", dir)
    path_clip = os.path.join("/Users/denizcanoruc/Desktop/clips/competition-198/season-187389", dir)
    for file in os.listdir(path_vid):
        if((df['match'].eq(dir)).any() and (df['shot'].eq(file.replace(".mp4",""))).any()):
            continue
        file_path = os.path.join(path_vid,file)
        if(file.endswith(".json")):
            shutil.copy(file_path, path_clip)
            continue
        elif(file.endswith(".mp4")):
            video = cv2.VideoCapture(file_path)
            video.set(cv2.CAP_PROP_POS_FRAMES, 310)
            while video.isOpened():         
                ret, frame = video.read()
                next_frame = video.get(cv2.CAP_PROP_POS_FRAMES)
                current_frame = next_frame - 1
                previous_frame = current_frame - 1
                #if previous_frame >= 0:
                #    video.set(cv2.CAP_PROP_POS_FRAMES, previous_frame)
                # Display each frame
                cv2.imshow("video", frame)
                # show one frame at a time
                key = cv2.waitKey(0)
                while key not in [ord('q'), ord('k'), ord('j'), ord('e')]:
                    key = cv2.waitKey(0)
                # Quit when 'q' is pressed
                if key == ord('k'):
                    continue
                elif key == ord('j'):
                    video.set(cv2.CAP_PROP_POS_FRAMES, previous_frame)
                elif key == ord('q'):
                    new_row = pd.DataFrame.from_dict([{'match' : dir , 'shot' : file.replace(".mp4",""), 'frame' : current_frame}], orient='columns')
                    df = pd.concat([df, new_row])
                    cv2.imwrite(os.path.join(path_clip,file.replace(".mp4",".jpg")), frame)
                    df.to_csv('/Users/denizcanoruc/Desktop/clips/clip_frames.csv', index = False)
                    break
                elif key == ord('e'):
                    break

"""
        

def trim(file, end):
    cap = cv2.VideoCapture(file)

    ret, frame = cap.read()
    h, w, _ = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*"h264")
    writer = cv2.VideoWriter(file.replace("shot-clips-example","shot_clips"), fourcc, 25.0, (w, h))

    f = 0
    while ret and f <= end:
        f += 1
        if end - 70 <= f <= end+1:
            writer.write(frame)
        ret, frame = cap.read()

    writer.release()
    cap.release()
    return

print(cv2.getBuildInformation())
df = pd.read_csv('/Users/denizcanoruc/Desktop/shot_clips/clip_frames.csv', index_col=None)
for index, row in df.iterrows():
    dir = os.path.join("/Users/denizcanoruc/Desktop/shot-clips-example",row["shot"])
    #dir = os.path.join(dir,row["shot"])
    dir += ".mp4"
    print(index)
    if os.path.exists(dir.replace("shot-clips-example", "shot_clips")):
        continue
    try:
        trim(dir,float(row["frame"]))
    except AttributeError:
        print(dir)
        continue
        


        



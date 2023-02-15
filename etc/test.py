import boto3
import json
import cv2
from botocore.exceptions import ClientError
import gzip
import json
import io
import pandas as pd









client = boto3.client(
    's3',
    aws_access_key_id = 'AKIAQ66ZZ7D4Z2FZR44S',
    aws_secret_access_key = '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',
    region_name = 'eu-central-1'
)

"""
cb_research_bucket = client.list_objects_v2(Bucket='clubbrugge-research-wyscout', Prefix="data/competition-198/season-187389")

matches_list = []

for object in cb_research_bucket['Contents']:
    if object["Key"].endswith('events-v3.json.gz'):
        matches_list.append(object["Key"])
    
meta_data = [] 

for match in matches_list:
    s3_object = client.get_object(Bucket="clubbrugge-research-wyscout", Key=match)['Body']
    content = s3_object.read()
    with gzip.GzipFile(fileobj=io.BytesIO(content), mode='rb') as fh:
        yourJson = json.load(fh)
    events_df = pd.DataFrame.from_dict(yourJson["events"])
    for index, row in events_df[~events_df["shot"].isnull()].iterrows():
        if(row["shot"]["isGoal"] == True):
            meta_data.append({'matchId': row["matchId"], "videoTimestamp" : row["videoTimestamp"], 
                "postShotXg": row["shot"]["postShotXg"],  "xg": row["shot"]["xg"], "videoPath": None})

meta_data_df = pd.DataFrame(meta_data)
print(meta_data_df)
meta_data_df.to_csv('out.csv',index=False)





meta_data_df = pd.read_csv('out.csv')
meta_data_df["videoTimestamp"] = meta_data_df["videoTimestamp"].astype('int')
meta_data_df["videoPath"] = meta_data_df["videoPath"].astype('string')


print(meta_data_df.dtypes)

cb_research_bucket = client.list_objects_v2(Bucket='clubbrugge-research-wyscout', Prefix="video/competition-198/season-187389/")

for object in cb_research_bucket['Contents']:
    if object["Key"].endswith('json'):
        s3_object = client.get_object(Bucket="clubbrugge-research-wyscout", Key=object["Key"])["Body"]
        with io.BytesIO(s3_object.read()) as bio:
            yourJson = json.load(bio)
            matchId = int(yourJson["matchId"])
            start = int(yourJson["start"])
            end = int(yourJson["end"])
            if (len(meta_data_df[(meta_data_df["matchId"] == matchId) & (meta_data_df['videoTimestamp'].between(start, end))]) != 1):
                print("WARNING! " + str(len(meta_data_df[(meta_data_df["matchId"] == matchId) & (meta_data_df['videoTimestamp'].between(start, end))])))
                print(matchId)
            meta_data_df.loc[((meta_data_df["matchId"] == matchId) & (meta_data_df['videoTimestamp'].between(start, end))), "videoPath"] = object["Key"].replace("json","mp4")


meta_data_df.to_csv('out_with_path.csv',index=False)

"""

meta_data_df = pd.read_csv('out_with_path.csv')
meta_data_df = meta_data_df[~meta_data_df["videoPath"].isnull()]
meta_data_df.to_csv('out_final.csv',index=False)






'''

# Fetch the list of existing buckets
clientResponse = client.list_buckets()
    
#Print the bucket names one by one
print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')

cb_research_bucket = client.list_objects_v2(Bucket='clubbrugge-research-wyscout', Prefix="video/competition-198/season-187389/")

print(cb_research_bucket["Contents"])

print('Printing objects keys...')
for object in cb_research_bucket['Contents']:
    if object["Key"].endswith('mp4'):
        print(object["Key"])

cb_research_bucket = client.list_objects_v2(Bucket='clubbrugge-research-wyscout', Prefix="data/competition-198/season-187389")

print(cb_research_bucket["Contents"])

print('Printing objects keys...')
for object in cb_research_bucket['Contents']:
    print(object["Key"])






#client.download_file(
#    Bucket = 'clubbrugge-research-wyscout',
#    Key = 'video/competition-198/season-187389/match-5228091/goal-s4228-e4275.mp4',
#    Filename = "./etc/goal-s4228-e4275.mp4"
#    #Key = "video/competition-198/season-187389/match-5228091/goal-s4228-e4275.json"
#)

#response = client.head_object(Bucket = 'clubbrugge-research-wyscout', Key = 'video/competition-198/season-187389/match-5228091/goal-s4228-e4275.mp4')

#print(response)

s3 = boto3.resource('s3')
object = s3.Object('bucket_name','key')

resp = client.get_object(Bucket = 'clubbrugge-research-wyscout', Key = 'video/competition-198/season-187389/match-5228091/goal-s4228-e4275.mp4', Range='bytes=100000-200000')
print(resp)

try:
    url = client.generate_presigned_url('get_object', 
        Params = {'Bucket': 'clubbrugge-research-wyscout', 'Key': "video/competition-198/season-187389/match-5228091/goal-s4228-e4275.mp4"}, 
        ExpiresIn = 600) 
except ClientError as e:
    print(e)

vid = cv2.VideoCapture(url)

video_length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT)) 
print(video_length)

vid.set(1, 350)
ret, frame = vid.read()
cv2.imwrite("./etc/img.jpg", frame)



  
while(False):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

print(url)

'''


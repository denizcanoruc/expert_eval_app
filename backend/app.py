from flask import Flask, request, g
from flask_cors import CORS, cross_origin
import random
import sqlite3
from flask_ngrok import run_with_ngrok
import boto3
import pandas as pd
import cv2




app = Flask(__name__)
#run_with_ngrok(app)
DATABASE = '/Users/denizcanoruc/Desktop/expert_evaluation/test_database.db'
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        cur = get_db().cursor()
        cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (str(username), str(password)))
        users = cur.fetchall()
        close_connection()
        if(users):
            print("YES")
            return "YES"
        else:
            print("NO")
            return "NO"
    else:
        return "Please Login"

    

@app.route('/questions_back',  methods=['POST', 'GET'])
def question():
    if request.method == 'POST':
        con = get_db()
        try:
            q_id = request.json['question_id']
            usr = request.json['username']
            ans = request.json['answer']
            cur = con.cursor()
            cur.execute("INSERT INTO answers (question_id,username,answer) VALUES (?,?,?)", (int(q_id), str(usr), int(ans)))
            con.commit()
            app.logger.info("Record successfully added")
            print("Record successfully added")
        except Exception as e:
            con.rollback()
            app.logger.info("error in insert operation")
            print(e)
        finally:
            close_connection()
            return "Answered"
    else:
        """
        cur = get_db().cursor()
        # TODO: random selection at DB or here?
        cur.execute("SELECT id, url1, tn1, url2, tn2 FROM questions")
        all_questions = cur.fetchall()
        # question = random.choice(all_questions)
        questions = []
        for question in random.sample(all_questions, 10):
            questions.append({
            "question_id" : question[0],
            "url1" : question[1],
            "tn1" : question[2],
            "url2" : question[3],
            "tn2" : question[4]})
        close_connection()
        return questions
        """
        clips_df = pd.read_csv("/Users/denizcanoruc/Desktop/expert_evaluation/frontend/public/shot_clips/clip_frames.csv")
        clips = clips_df.sample(20)["shot"]

        questions = []
        for i in range(10):
            questions.append({
                "question_id" : 2*i,
                "url1" : "./shot_clips/" + clips.iloc[2*i] + ".mp4",
                "tn1" : "./shot_clips/" + clips.iloc[2*i] + ".jpg",
                "url2" : "./shot_clips/" + clips.iloc[2*i+1] + ".mp4",
                "tn2" : "./shot_clips/" + clips.iloc[2*i+1] + ".jpg",})
        
        print("aaaaaa")
        print(questions[0]["url1"])
        return questions






def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def get_clips():
    client = boto3.client(
    's3',
    aws_access_key_id = 'AKIAQ66ZZ7D4Z2FZR44S',
    aws_secret_access_key = 'HX0C+2IqLXgYJHv4Av+gbyYrx0TdFzK7hktXduI+',
    region_name = 'eu-central-1')
    
    meta_data_df = pd.read_csv('../out_final.csv')
    clips_df = meta_data_df.sample(n=20)
    clips_df["url"] = ""

    count = 0
    for index, row in clips_df.iterrows():
        url = client.generate_presigned_url('get_object', 
            Params = {'Bucket': 'clubbrugge-research-wyscout', 'Key': row["videoPath"]}, 
            ExpiresIn = 600)
        clips_df.loc[index,"url"] = url
        vid = cv2.VideoCapture(url)
        #video_length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT)) 
        #print(video_length)
        vid.set(1, 310)
        ret, frame = vid.read()
        video_length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT)) 
        path = "../frontend/src/clips/tn_" + str(count) + ".jpg"
        cv2.imwrite(path, frame)
        count += 1

    return clips_df



@app.teardown_appcontext
def close_connection(exception = None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":

    app.run(debug=True, port=5002)

from .. import celery,app,db
from ..models import Emails
from datetime import datetime 
from flask_mail import Mail, Message
import random 
import requests 


#flask mail init 
mail = Mail(app)


#helper for sending reset emails ===> Not efficient, consider production level batch emails if you use this 
def send_single_email(email, video_link, video_name):
    msg = Message('Daily Coding Video - Coding Video Mailer', sender='exvmm@gmail.com', recipients=[email])
    msg.body = f'Hi {email},\r\n\nHere is your coding video for the day. {video_name} -- {video_link}. \r\n\nGood Luck!'
    with app.app_context():
        mail.send(msg)


def get_random_video_link():
    """
    Step 1: From a provided list of playlists, choose one 
    Step 2: Fetch that from the youtube api and randomly select a video to be emailed. 
    Return tuple of title of video and the id of video 
    """
    playlist = random.choice(app.config['HOST_PLAYLISTS'])

    params = {
        "part":"snippet",
        "playlistId":playlist,
        "maxResults":50,
        "key":app.config['YT_API_KEY']
    }
    resp = requests.get(url="https://www.googleapis.com/youtube/v3/playlistItems",params=params)
    selected_video = random.choice(resp.json()["items"])

    return (selected_video['snippet']['title'],selected_video['snippet']['resourceId']['videoId'])




@celery.task(name="site_async_tasks.send_video_links")
def send_video_links():
    """
    Loop through available emails at the specified time and send emails containing link to the youtube video

    """
    email_list = Emails.query.filter_by(status="active").all() 
    print("Sending newsletters to ", len(email_list), " users")
    random_video = get_random_video_link()
    video_link = f"https://www.youtube.com/watch?v={random_video[1]}"

    for email in email_list:
        #send email to user
        try:
            send_single_email(email.email, video_link, random_video[0])
        except Exception as e:
            print(e)
            


    print("DEBUG- Emails send job finished ")
    return "Success"


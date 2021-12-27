import yagmail
import pandas as pd
import news_feed
import datetime
import time

while True:
    if datetime.datetime.now().hour == 1 and datetime.datetime.now().minute == 29:
        df = pd.read_excel('sample.xlsx')
        today = datetime.datetime.now().strftime('%Y-%m-%d')

        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        email = yagmail.SMTP(user='saadebesin@student.oauife.edu.ng', password='******')

        print('Sending email...')
        for name, email_, interest in zip(df['name'], df['email'], df['interest']):
            newsfeed = news_feed.NewsFeed(language='en', interest=interest)
            email.send(to=f"{email_}",
                       subject=f"Hi, {name.title()}, here is your {interest.title()} news for today",
                       contents=f"{newsfeed.get()}")
        print('Done!!!')
    time.sleep(60)

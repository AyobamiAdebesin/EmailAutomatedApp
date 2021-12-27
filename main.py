# http requests
import requests
# web scraping
from bs4 import BeautifulSoup
# send the email
import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# datetime
import datetime

now = datetime.datetime.now()

# email content placeholder
content = ''

# extracting Hacker News stories
def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt += '<b>HN Top Stories: </b> \n ' + '<br>' + '-' * 50 + '</br>'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i + 1) + ' :: ' + tag.text + "\n" + '<br>') if tag.text != 'More' else '')
    return cnt


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>--------------<br>')
content += ('<br><br> End of Message')

# send the mail
# email authentication
print('Composing email...')

# update your email address
SERVER = 'smtp.gmail.com'  # your smtp server
PORT = 587  # your port  number
FROM = 'saadebesin@student.oauife.edu.ng'
TO = 'eqwoeavklouf@dropmail.me'  # your to email id . This can be a list
PASS = '********'  # your email id password

# Create a text/plain message
msg = MIMEMultipart()

# create a dynamic message header
msg['Subject'] = 'Top News Stories Hacker News [AUTOMATED EMAIL] ' + \
                 str(now.day) + '-' + str(now.month) + ' ' + str(now.year)
msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText(content, 'html'))

print('Initiating server...')
#server = smtplib.SMTP(SERVER, PORT)
server = smtplib.SMTP_SSL(SERVER, 465)
server.set_debuglevel(1)  # for seeing error message 1, and 0 otherwise
server.ehlo()
#server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()

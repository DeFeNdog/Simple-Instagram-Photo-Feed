import os
import requests
from flask import Flask, render_template, Response, request, redirect, url_for, session


app = Flask(__name__, template_folder="templates")
app.access_token = os.environ['ACCESS_TOKEN']


@app.route('/')
def index():
    return render_template('index.jinja2')


def get_media(account_id):
    endpoint = 'https://graph.facebook.com/v3.2'
    payload = {
        'access_token': app.access_token,
        'fields': 'id,media_type,media_url,timestamp,permalink,caption'
    }
    resp = requests.get('{}/{}/media'.format(endpoint, account_id),
                        params=payload)
    media = resp.json()
    return media['data']


@app.route('/media')
def media():
    media = False
    account_id = ''  # Your Account ID
    if account_id:
        media = get_media(account_id)

    return render_template('feed.jinja2', media=media)


if __name__ == "__main__":
    app.run()

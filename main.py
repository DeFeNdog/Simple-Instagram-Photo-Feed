import os
import requests
from flask import Flask, render_template, Response, request, redirect, url_for, session

# import pprint
# pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)
app.access_token = os.environ['ACCESS_TOKEN']


@app.route('/')
def index():
    return render_template('index.jinja2')


# def get_app_access_token():
#     endpoint = 'https://graph.facebook.com/oauth/access_token'
#     payload = {
#         'client_id': app.app_id,
#         'client_secret': app.app_secret,
#         'grant_type': 'client_credentials'
#     }
#     r = requests.get(endpoint, params=payload)
#     r = r.json()
#     return r['access_token']


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
    account_id = '17841400463092183'  # Polachecks
    if account_id:
        media = get_media(account_id)

    return render_template('feed.jinja2', media=media)


if __name__ == "__main__":
    app.run()

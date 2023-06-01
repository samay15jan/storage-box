import os, requests, json
from flask import Flask, render_template, request
import pickle
import random
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 5120 * 5120

SCOPES = ['https://www.googleapis.com/auth/drive']

TOKEN_FILE = 'token.pickle'

def authenticate():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
    return creds

folder_links = 'folder_id.txt'

def random_line(folder_links):
    with open(folder_links, 'r') as file:
        lines = file.read().splitlines()
        if lines:
            random_folder_id = random.choice(lines)
            return random_folder_id

def upload_file(file_path, folder_id):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    media = MediaFileUpload(file_path)
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [folder_id]
    }
    data = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    file_id = data['id']
    service.permissions().create(
        fileId=file_id,
        body={'role': 'reader', 'type': 'anyone'}
    ).execute()
    link = f"https://drive.google.com/file/d/{file_id}/view?usp=sharing"
    return link

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.files.get("data")
        folder_id = random_line(folder_links)
        if data:
            file_path = os.path.join("/tmp", data.filename)
            data.save(file_path)
            link = upload_file(file_path, folder_id)
            os.remove(file_path)  # Remove the temporary file
            url = "https://api.apilayer.com/short_url/hash"
            payload = link.encode("utf-8")
            headers= {
                "apikey": "your api key"
            }
            response = requests.request("POST", url, headers=headers, data = payload)
            result = response.text
            r = json.loads(result)
            short_url = r['short_url']
            return render_template("output.html", short_url=short_url)
        else:
            return "No file selected."
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

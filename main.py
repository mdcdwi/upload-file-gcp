from flask import Flask, request
import os, upload, json

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def main():
    try:
        GOOGLE_STORAGE_CREDENTIAL = os.environ.get("GOOGLE_STORAGE_CREDENTIAL")
        GOOGLE_STORAGE_NAME = os.environ.get("GOOGLE_STORAGE_NAME")
        try:
            request_data = request.get_json()
            file = request_data['file']
            filename = request_data['filename']
            upload.upload(file, filename, GOOGLE_STORAGE_NAME, GOOGLE_STORAGE_CREDENTIAL)
            return json.dumps({'Status': 'Success', 'data': 'https://storage.googleapis.com/'+ GOOGLE_STORAGE_NAME +'/'+filename}), 200, {'ContentType':'application/json'}
        except (Exception) as e:
            return json.dumps({'status': 'Failed to upload', 'message': str(e)}), 400, {'ContentType':'application/json'}
    except (Exception) as e:
        return json.dumps({'Status': 'Failed to load env', 'message': str(e)}), 400, {'ContentType':'application/json'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
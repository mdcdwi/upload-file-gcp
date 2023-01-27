from flask import Flask, request
import os, upload, json

def main():
    try:
        GOOGLE_STORAGE_CREDENTIAL = os.environ.get("GOOGLE_STORAGE_CREDENTIAL")
        GOOGLE_STORAGE_NAME = os.environ.get("GOOGLE_STORAGE_NAME")
    except (Exception) as e:
        return json.dumps({'Status': 'Failed to load env', 'message': str(e)}, status=400)
    try:
        request_data = request.get_json()
        file = request_data['file']
        filename = request_data['filename']
        upload.upload(file, filename, GOOGLE_STORAGE_NAME)
    except (Exception) as e:
        return json.dumps({'status': 'Failed to upload', 'message': str(e)}, status=400)

if __name__ == "__main__":
    main()
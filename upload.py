from google.cloud import storage
import base64, io

def upload(file_base64, filename, bucket_name):
    file = io.BytesIO(base64.b64decode(file_base64))
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(filename)

    blob.upload_from_filename("./{0}".format(file))
    print("file", filename, "is uploaded")

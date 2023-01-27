from google.cloud import storage
import base64, io

def upload(file_base64, filename, bucket_name, creds):
    file = open("{0}".format(filename), "wb")
    file.write(base64.b64decode(file_base64))
    file.close()

    storage_client = storage.Client(credentials=creds)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(filename)

    blob.upload_from_filename("./{0}".format(filename))
    print("file", filename, "is uploaded")

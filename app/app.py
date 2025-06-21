from flask import Flask, request, render_template, redirect
from minio import Minio
import os

app = Flask(__name__)

MINIO_HOST = os.getenv("MINIO_HOST", "minio:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "minioadmin")

client = Minio(
    MINIO_HOST,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

BUCKET = "images"
if not client.bucket_exists(BUCKET):
    client.make_bucket(BUCKET)

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            client.put_object(
                BUCKET, file.filename, file.stream, length=-1, part_size=10*1024*1024
            )
            return redirect("/")
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

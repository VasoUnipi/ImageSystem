# Εισαγωγή απαραίτητων βιβλιοθηκών: Flask για το web app, Minio για τη σύνδεση με το object storage, os για περιβαλλοντικές μεταβλητές
from flask import Flask, request, render_template
from minio import Minio
import os

# Δημιουργία Flask εφαρμογής
app = Flask(__name__)


# Ανάγνωση μεταβλητών περιβάλλοντος για σύνδεση με το MinIO
MINIO_HOST = os.getenv("MINIO_HOST", "minio:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "minioadmin")

# Δημιουργία MinIO client αντικειμένου για διασύνδεση με τον server
client = Minio(
    MINIO_HOST,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)
# Δηλώνεται το όνομα του bucket όπου θα αποθηκεύονται οι εικόνες
BUCKET = "images"
# Αν δεν υπάρχει ήδη το bucket στο MinIO, δημιουργείται αυτόματα
if not client.bucket_exists(BUCKET):
    client.make_bucket(BUCKET)
# Ορίζεται η ρίζα ("/") της εφαρμογής – δέχεται GET και POST
@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"] # Ανάκτηση αρχείου από τη φόρμα
        if file:
            filename = file.filename # Ανάκτηση του ονόματος του αρχείου
             # Αποθήκευση του αρχείου στο MinIO bucket
            client.put_object( 
                BUCKET, filename, file.stream, length=-1, part_size=10*1024*1024
            )
            # Επιστροφή της σελίδας με μήνυμα επιτυχίας
            return render_template("upload.html", success=True, filename=filename)
     # Αν είναι GET ή δεν έγινε upload, απλώς εμφανίζεται η φόρμα
    return render_template("upload.html")

# Εκκίνηση της εφαρμογής Flask στο host 0.0.0.0 και port 5000 (για να είναι προσβάσιμη από Docker)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

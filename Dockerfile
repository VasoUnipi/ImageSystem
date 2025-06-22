# Βασική εικόνα: Επίσημη Python 3.10 έκδοση με ελαφρύ αποτύπωμα
FROM python:3.10-slim
# Ορισμός του working directory μέσα στο container 
WORKDIR /app
# Αντιγραφή του αρχείου requirements.txt από τον φάκελο app του host στο root του container
COPY app/requirements.txt .
# Αναβάθμιση του pip και εγκατάσταση των εξαρτήσεων από το requirements.txt χωρίς cache
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
# Αντιγραφή όλου του περιεχομένου του φακέλου app/ από τον host στον φάκελο /app του container
COPY app/ .
# Εντολή εκκίνησης της εφαρμογής Flask όταν ξεκινά το container
CMD ["python", "app.py"]
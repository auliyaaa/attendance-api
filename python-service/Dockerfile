# Gunakan base image Python
FROM python:3.11

# Set work directory di dalam container
WORKDIR /app

# Salin semua file dari direktori lokal ke dalam container
COPY . /app

# Install dependencies dari requirements.txt (jika ada)
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan Flask di port 5000
CMD ["python", "app.py"]

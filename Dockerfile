FROM python:3.9

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Expose ports
EXPOSE 8000
EXPOSE 8501

# Copy the application code
COPY . .

# Run the application
CMD ["uvicorn", "manage:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

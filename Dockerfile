# 1. THE BASE: 
FROM python:3.9-slim

# 2. THE SETUP: 
WORKDIR /app

# 3. THE FILES: 
COPY . .

# 4. THE LIBRARIES: 
RUN pip install --no-cache-dir -r requirements.txt

# 5. THE COMMAND: 
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]

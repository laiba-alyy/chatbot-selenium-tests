FROM python:3.11-slim

# Install Chrome + dependencies for headless mode
RUN apt-get update && apt-get install -y \
    wget curl unzip xvfb \
    libglib2.0-0 libnss3 libgconf-2-4 \
    libfontconfig1 libxi6 libatk1.0-0 libatk-bridge2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN CHROME_VERSION=$(curl -sS https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json | grep -oP '"version"\s*:\s*"\K[^"]+' | head -1) && \
    wget -q https://storage.googleapis.com/chrome-for-testing-public/$CHROME_VERSION/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    mv chromedriver-linux64/chromedriver /usr/local/bin/ && \
    rm -rf chromedriver-linux64.zip chromedriver-linux64

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create reports directory
RUN mkdir -p test-reports

# Run pytest with JUnit XML output
CMD ["python3", "-m", "pytest", "test_chatbot.py", "-v", "--tb=short", "--junitxml=test-reports/results.xml"]
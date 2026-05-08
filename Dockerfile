FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    jq \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get update \
    && apt-get install -y /tmp/chrome.deb \
    && rm /tmp/chrome.deb \
    && rm -rf /var/lib/apt/lists/*

# Install matching ChromeDriver
RUN CHROME_VERSION=$(google-chrome --version | awk '{print $3}') \
    && CHROME_MAJOR=$(echo $CHROME_VERSION | cut -d'.' -f1) \
    && echo "Chrome Version: $CHROME_VERSION, Major: $CHROME_MAJOR" \
    && DRIVER_URL=$(curl -s "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json" | jq -r ".channels.Stable.downloads.chromedriver[] | select(.platform==\"linux64\") | .url") \
    && echo "ChromeDriver URL: $DRIVER_URL" \
    && wget -q -O /tmp/chromedriver.zip "$DRIVER_URL" \
    && unzip /tmp/chromedriver.zip -d /tmp/ \
    && mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver \
    && rm -rf /tmp/chromedriver.zip /tmp/chromedriver-linux64

# Verify installations
RUN google-chrome --version && chromedriver --version

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run tests and generate JUnit XML report for Jenkins
CMD ["python", "-m", "pytest", "test_chatbot.py", "-v", "--tb=short", "--junitxml=test-results.xml"]
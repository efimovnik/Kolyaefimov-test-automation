FROM python:3.9-slim

# Install only Playwright dependencies
RUN apt-get update && apt-get install -y \
    libnss3 libx11-xcb1 libxcomposite1 libxcursor1 libxdamage1 libxi6 libxtst6 libnss3 libxrandr2 \
    fonts-liberation libasound2 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdbus-1-3 libdrm2 libgbm1 \
    libglib2.0-0 libnspr4 libpango-1.0-0 libx11-6 libx11-xcb1 libxcb1 libxdamage1 libxrandr2 libxshmfence1 \
    xdg-utils wget ca-certificates unzip fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install playwright && playwright install chromium --with-deps && rm -rf /var/lib/apt/lists/* 


CMD ["python", "-m", "pytest", "--alluredir", "allure-results", "./tests/step_defs/test_main_page_bdd.py", "-n", "6"]

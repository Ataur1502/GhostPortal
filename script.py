import random
from datetime import datetime, timedelta

NUM_REQUESTS = 1000
OUTPUT_FILE = "access.log"

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/137.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) Firefox/128.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) Safari/605.1.15",
    "curl/8.5.0",
]

PATHS = [
    "/",
    "/login",
    "/logout",
    "/dashboard",
    "/profile",
    "/download/Employee_Handbook.pdf",
    "/favicon.ico",
    "/robots.txt",
    "/static/css/bootstrap.min.css",
    "/static/css/style.css",
    "/static/js/app.js",
    "/static/js/bootstrap.bundle.min.js",
    "/static/img/logo.png",
    "/static/img/profile.png",
]

STATUS_CODES = [200, 200, 200, 200, 302, 304, 404]

start = datetime(2026, 6, 30, 9, 0, 0)

special_line = (
    '10.10.10.42 - - [30/Jun/2026:12:34:56 +0530] '
    '"GET /dev/backup/flag-4d9b2e HTTP/1.1" 200 41 "-" "curl/8.5.0"'
)

lines = []

for i in range(NUM_REQUESTS):
    dt = start + timedelta(seconds=i * random.randint(2, 8))

    ip = ".".join(str(random.randint(1, 254)) for _ in range(4))

    path = random.choice(PATHS)

    status = random.choice(STATUS_CODES)

    size = random.randint(200, 50000)

    ua = random.choice(USER_AGENTS)

    line = (
        f'{ip} - - '
        f'[{dt.strftime("%d/%b/%Y:%H:%M:%S +0530")}] '
        f'"GET {path} HTTP/1.1" '
        f'{status} {size} '
        f'"-" '
        f'"{ua}"'
    )

    lines.append(line)

# Insert the hidden clue somewhere random
lines.insert(random.randint(200, 800), special_line)

with open(OUTPUT_FILE, "w") as f:
    for line in lines:
        f.write(line + "\n")

print(f"Generated {OUTPUT_FILE} with {len(lines)} entries.")
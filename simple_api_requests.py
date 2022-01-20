import requests
import time

# CONSTANTLY CHECKING THE REQUESTS
while True:
    req = requests.get("https://kalob.io")
    print(req.status_code)
    if req.status_code != 200:
        # EMAIL ME OR TEXT ME
        pass
    time.sleep(3)      # SECONDS


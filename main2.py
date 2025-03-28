import sys
import time
from datetime import datetime

seconds = int(sys.argv[1])

for second in range(seconds):
    print(datetime.now().time())
    time.sleep(1)

print("End.")

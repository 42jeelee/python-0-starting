from datetime import datetime

standard = datetime(1970, 1, 1)
now = datetime.now()

diff_seconds = (now - standard).total_seconds()

print(f"Seconds since January 1, 1970: {diff_seconds:,} or {diff_seconds:.2e} in scientific notation")
print(now.strftime("%b %d %Y"))
from datetime import datetime

now = datetime.now()
seconds = now.timestamp()

formatted_seconds = "{:,.4f}".format(seconds)
scientific_notation = "{:.2e}".format(seconds)
print(f"Seconds since January 1, 1970: {formatted_seconds} or {scientific_notation} in scientific notation")
print(now.strftime("%b %d %Y"))

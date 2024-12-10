from time import time, gmtime, strftime

timestamp = time()

print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")
print(strftime("%b %d %Y", gmtime()))
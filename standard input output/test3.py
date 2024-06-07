import time
import os


# --------------------여기서부턴 '\n'-------------------


os.system("cls")
print("False")
time.sleep(1)
os.system("cls")

print("aaaaaaaaaaaaaaaaaaa", end="\n", flush=False)

time.sleep(2)

print("ZZZZ")

time.sleep(2)

# 흠....

os.system("cls")
print("True")
time.sleep(1)
os.system("cls")


print("aaaaaaaaaaaaaaaaaaa", end="\n", flush=True)

time.sleep(2)

print("ZZZZ")


# --------------------여기서부턴 '\r'-------------------


os.system("cls")
print("False")
time.sleep(1)
os.system("cls")

print("aaaaaaaaaaaaaaaaaaa", end="\r", flush=False)

time.sleep(2)

print("ZZZZ")

time.sleep(2)

# 흠....

os.system("cls")
print("True")
time.sleep(1)
os.system("cls")


print("aaaaaaaaaaaaaaaaaaa", end="\r", flush=True)

time.sleep(2)

print("ZZZZ")

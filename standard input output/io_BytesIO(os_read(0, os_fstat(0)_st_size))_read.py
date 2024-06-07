import os, io

input2 = io.BytesIO(os.read(0, os.fstat(0).st_size)).read()

print(input2)

print("\n----------------------------------\n")

print("input2.decode() : ", input2.decode())

print("\n----------------------------------\n")

print("os.write(1, input2) : ", end="", flush=True)  # flush 쓴 이유 readme에 나와있음
os.write(1, input2)

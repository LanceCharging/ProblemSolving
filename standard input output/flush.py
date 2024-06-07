import time

for i in range(10):
    print(i, end="  ")
    time.sleep(1)

# 결국 화면에 무언가 출력되는 건 print가 실행된 후가 아닌, 버퍼가 비워질 때인 것. 기본적으로는 end = '\n'이기에 print가 실행될 때 버퍼가 비워지는 조건 중 하나인 '개행'이 함께 일어나서 둘이 거의 동치였음.

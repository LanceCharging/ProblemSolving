import time

import os

list_123 = ["aaaaaa", "bbb", "cccccc"]

for i in range(3):
    # d = (i + 10).encode() ! 불가능 ! .encode는 정수형에서 불가능

    """
    int.to_bytes() 메서드
    이 메서드는 정수를 지정된 길이의 바이트 배열로 변환합니다. 이때 바이트 순서(endianness)를 지정할 수 있습니다. 파라미터는 다음과 같습니다:

    length: 결과 바이트 배열의 길이.
    byteorder: 바이트 순서. 'big' 또는 'little'로 지정합니다.
    signed: 정수를 부호 있는 형식으로 해석할지 여부 (True 또는 False).

    """

    print(i + 1, end="\r", flush=False)

    time.sleep(2)

    d = (list_123[i]).encode()
    os.write(1, d)

    time.sleep(5)

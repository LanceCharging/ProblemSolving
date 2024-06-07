import os

input_data = os.read(0, os.fstat(0).st_size)  # 파일 디스크립터 0에서 모든 입력 읽기

print(input_data.decode())


# os.read -> 파일 디스크립터에서 직접적으로 정보 읽기
# input을 하던 뭘 하던 어차피 '읽어들인 정보'는 '바이너리화' 되어서 파일 디스크립터에 들어간다!

# 파일 디스크립터 0, 1, 2는 각각 이렇게 매핑된다
# 0: 표준 입력(stdin)
# 1: 표준 출력(stdout)
# 2: 표준 에러(stderr)

"""
- 파일 디스크립터 : 
유닉스 계열의 시스템에서 프로세스(process)가 파일(file)을 다룰 때 사용하는 개념으로, 프로세스에서 특정 파일에 접근할 때 사용하는 추상적인 값이다. 파일 디스크럽터는 일반적으로 0이 아닌 정수값을 갖는다. 

흔히 유닉스 시스템에서 모든 것을 파일이라고 한다. 일반적인 정규파일부터 디렉토리, 소켓, 파이프, 블록 디바이스, 케릭터 디바이스 등 모든 객체들을 파일로 관리한다. 유닉스 시스템에서 프로세스가 이 파일들을 접근할 때 파일 디스크립터라는 개념일 이용한다. 프로세스가 실행 중에 파일을 Open하면 커널은 해당 프로세스의 파일 디스크립터 숫자 중 사용하지 않는 가장 작은 값을 할당해준다. 그 다음 프로세스가 열려있는 파일에 시스템 콜을 이용해서 접근할 때, 파일 디스크립터(FD)값을 이용해서 파일을 지칭할 수 있다.

프로그램이 프로세스로 메모리에서 실행될 때, 기본적으로 할당되는 파일디스크립터는 표준입력(Standard Input), 표준 출력(Standard Output), 표준에러(Standard Error)이며 이들에게 각각 0, 1, 2라는 정수가 할당된다.
"""

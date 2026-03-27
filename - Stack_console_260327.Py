# 스택의 최대 용량을 5로 설정 
MAX_SIZE = 5

# 스택으로 사용할 빈 파이썬 리스트 생성 
stack = []

# 1. 스택이 비어있는지 확인하는 함수
def isEmpty():
    # 리스트의 길이가 0이면 True, 아니면 False 반환
    return len(stack) == 0

# 2. 스택이 가득 찼는지 확인하는 함수
def isFull():
    # 리스트의 길이가 최대 용량(5) 이상이면 True 반환
    return len(stack) >= MAX_SIZE

# 3. 스택에 데이터를 추가하는 함수 [cite: 4]
def push(data):
    if isFull():
        # 스택이 가득 찼을 경우의 예외 처리 [cite: 44]
        print("> Stack이 차 있어서 더 이상 추가할 수 없습니다.")
    else:
        # 가득 차지 않았다면 리스트의 맨 끝에 데이터 추가
        stack.append(data)
    # 현재 스택의 상태를 출력 [cite: 8]
    print(f"> 현재 스택 상태 {stack}")

# 4. 스택에서 데이터를 꺼내는 함수 [cite: 5]
def pop():
    if isEmpty():
        # 스택이 비어있을 경우의 예외 처리 [cite: 38]
        print("> Stack이 비어 있습니다.")
    else:
        # 리스트의 맨 끝(가장 최근) 데이터를 꺼내고 변수에 저장
        data = stack.pop()
        print(f"> 가져온 데이터 : {data}") # [cite: 24]
    # 데이터를 꺼낸 후의 스택 상태 출력 [cite: 25]
    print(f"> 현재 스택 상태 {stack}")

# 5. 스택의 가장 위(최근) 데이터를 확인만 하는 함수 [cite: 9]
def peek():
    if isEmpty():
        # 스택이 비어있을 경우의 예외 처리
        print("> Stack이 비어 있습니다.")
    else:
        # pop()과 달리 데이터 삭제 없이 인덱스 [-1]로 가장 위 데이터만 확인
        data = stack[-1]
        print(f"> 최상단 데이터 : {data}")
    # 상태 출력
    print(f"> 현재 스택 상태 {stack}")

# 전체 프로그램 실행을 제어하는 메인 함수
def main():
    print("[정수형 스택 연산 실습 (용량 5)]") # 
    
    while True:
        # 메뉴 출력 [cite: 12, 13, 14, 15]
        print("1.Push")
        print("2.Pop")
        print("3.Peek")
        print("0.Exit")
        
        # 사용자로부터 메뉴 입력받기 [cite: 16]
        menu = input("> 메뉴 선택: ")
        
        if menu == '1':
            # 데이터를 정수형으로 입력받아 push 함수에 전달 [cite: 17]
            data = int(input("> 데이터 입력 : "))
            push(data)
            
        elif menu == '2':
            # pop 함수 호출 [cite: 30]
            pop()
            
        elif menu == '3':
            # peek 함수 호출
            peek()
            
        elif menu == '0':
            # 프로그램 종료 메시지 출력 후 while 루프 탈출 [cite: 47, 48]
            print("[정수형 스택 연산 실습 종료]")
            break
            
        else:
            print("> 잘못된 입력입니다. 0~3 사이의 숫자를 입력해주세요.")

# 파이썬 스크립트가 직접 실행될 때 main() 함수를 호출
if __name__ == "__main__":
    main()
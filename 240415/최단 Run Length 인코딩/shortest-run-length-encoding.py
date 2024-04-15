# 변수 선언 및 입력:
A = input()


def run_length_encoding(target):
    # 이 함수는 input 문자열을 Run-Length-Encoding한 결과를 반환합니다.
    encoded = ""

    # 입력의 첫번째 값을 읽고 초기화합니다.
    curr_char = target[0]
    num_char = 1
    for target_char in target[1:]:
        if target_char == curr_char:
            num_char += 1
        else:
            # 지금까지 세어온 curr_char와 num_char를 기록합니다.
            encoded += curr_char
            encoded += str(num_char)
    
            # curr_char와 num_char를 현재 값으로 초기화합니다.
            curr_char = target_char
            num_char = 1
        
    # 마지막 덩어리에 해당하는 curr_char와 num_char를 기록합니다.
    encoded += curr_char
    encoded += str(num_char)
    return encoded


min_length = len(run_length_encoding(A)) # 초기값은 shift안했을 때의 값
n = len(A)
num_shift = n - 1 # 0부터 length - 1

while num_shift:
    # 문자열 A를 오른쪽으로 1번 shift합니다.
    A = A[-1] + A[:-1]
    
    length = len(run_length_encoding(A))
    if min_length > length:
        min_length = length
    
    num_shift -= 1
    
# 출력
print(min_length)
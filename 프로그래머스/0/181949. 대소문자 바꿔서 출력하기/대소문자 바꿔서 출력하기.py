str = input().strip()

if 1 <= len(str) <= 20:
    print(str.swapcase())
else:
    print("해당 문자열은 1~20자여야 합니다.")
    
# 제한 사항 체크하는 것이 맞는지 검토 필요

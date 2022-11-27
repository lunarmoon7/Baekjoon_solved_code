import sys

def input(type=str): # 입력 함수 재정의
    return type(sys.stdin.readline())
def input_s(type=str):
    return type(sys.stdin.readline()).strip()

n = input(int)
words = [input_s() for _ in range(n)]
    
dic = dict()
answer = 0

for word in words:
    for i in range(len(word)):
        num = 10 ** (len(word) - i - 1)
        if word[i] in dic:
            dic[word[i]] += num    
        else:
            dic[word[i]] = num

dic = sorted(dic.values(), reverse=True) # dictionary turn into list
num = 0
for val in dic: 
    if val > 0:
        answer += val * (9 - num)
        num += 1
        
print(answer)
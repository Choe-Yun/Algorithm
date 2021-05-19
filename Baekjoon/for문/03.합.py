### 문제

# n이 주어졌을 때, 1 부터 n까지 합을 구하는 프로그램을 작성하시오


### 입력

# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.


### 출력

# 1부터 n까지 합을 출력한다.


##### code

count = 0
num = int(input())

for i in range(num+1):
    count = count + i
print(count)
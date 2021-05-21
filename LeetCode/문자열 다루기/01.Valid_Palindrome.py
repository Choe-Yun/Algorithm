### 문제

# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# 주어진 문자열이 팰린드롬인지 확인하고 대소문자를 구분하지 않는다

### Example 1

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.





##### code

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():  # pop()함수는 인덱스를 지정할 수 있으므로 0번째 인덱스를 지정하면 맨 앞의 값을 가져옴
                return False

        return True


# 20~23번 라인은 isalnum()는 영문자, 숫자 여부를 판별하는 함수. 이를 이용해 해당하는 문자만 추가
# 대소문자를 구분하지 않으므로 lower()로 소문자로 변환.




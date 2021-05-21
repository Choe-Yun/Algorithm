### 문제

# Write a function that reverses a string. The input string is given as an array of characters s.
# 문자열을 뒤집는 함수를 작성해라. 인풋값은 배열이다

### Example 1

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]





###### code

from typing import List

# 투 포인터를 이용한 스왑 방식
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1



# 파이싼의 reverse() 함수를 이용한 방식
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
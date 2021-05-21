### 문제

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


### Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]




##### code

import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())




# anagrams = collections.defaultdict(list)
# 만약 존재하지 않는 키를 삽입하려 할 경우 keyError가 발생하므로, 에러가 나지않도록 defaultdict()로 선언하여
# 매번 키 존재 여부를 체크하지 않고 비교 구문을 생략해 간결하게 구성한다

# anagrams[''.join(sorted(word))].append(word)
# sorted()는 문자열로 잘 정렬하며 결과를 리스트 형태로 리턴하는데 이를 다시 키로 사용하기 위해 join()으로 합쳐 이 값을 키로 하는 딕셔너리로 구성
# 애너그램끼리는 같은 키를 같게 되고 따라서 여기에 append()하는 형태가 된다. 이 형식은 해시테이블 형식이다
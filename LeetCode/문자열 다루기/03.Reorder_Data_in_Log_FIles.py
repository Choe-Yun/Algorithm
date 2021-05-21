### 문제

# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.
#
# There are two types of logs:
#
# - Letter-logs: All words (except the identifier) consist of lowercase English letters.
# - Digit-logs: All words (except the identifier) consist of digits.
# - Reorder these logs so that:
#
# 1. The letter-logs come before all digit-logs.
# 2. The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# 3. The digit-logs maintain their relative ordering.
# Return the final order of the logs.


### Example

# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".





###### code

class Solution:
		def reorderLogFiles(self, logs: List[str]) -> List[str]:
				letters = []
				digits = []

				for log in logs:
						if log.split()[1].isdigit():
								digits.append(log)
						else:
								letters.append(log)

				letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
				return letters + digits


# letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
# 식별자를 제외한 문자열 [1:]을 키로 하여 정렬함. 동일한 경우 후순위로 식별자 [0]를 지정해 정렬되도독, 람다 표현식으로 정렬
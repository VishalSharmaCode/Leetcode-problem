from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        n = len(s)

        if n < total_len:
            return []

        need = Counter(words)
        result = []

        # Try each possible offset (0..word_len-1)
        for i in range(word_len):
            left = i
            seen = Counter()
            count = 0

            # Step by word_len each time
            for j in range(i, n - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in need:
                    seen[word] += 1
                    count += 1

                    # Too many occurrences → shrink window
                    while seen[word] > need[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # If we matched all words
                    if count == word_count:
                        result.append(left)
                else:
                    # reset window
                    seen.clear()
                    count = 0
                    left = j + word_len

        return result
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0

        for w in words:
            # Check if adding this word exceeds maxWidth
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # Distribute spaces
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += " "
                res.append("".join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)

        # Last line (left-justified)
        res.append(" ".join(cur).ljust(maxWidth))
        return res
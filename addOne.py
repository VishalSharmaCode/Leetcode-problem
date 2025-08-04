def plusOne(digits):
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    # If all digits were 9 (e.g., [9,9,9]), result is [1,0,0,0]
    return [1] + digits
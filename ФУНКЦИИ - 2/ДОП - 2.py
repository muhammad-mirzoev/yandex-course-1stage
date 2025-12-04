def palindrome(s):
    cleaned_s = ''.join(s.lower().split())

    if cleaned_s == cleaned_s[::-1]:
        return "Палиндром"
    else:
        return "Не палиндром"
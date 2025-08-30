def longest_palindromic_substring(s):
    def is_palindrome(sub):
        return sub == sub[::-1]
    
    longest = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if is_palindrome(substring):
                if len(substring) > len(longest):
                    longest = substring
    return longest

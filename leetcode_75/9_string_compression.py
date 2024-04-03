"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
"""

class Solution:
    def compress(self, chars) -> int:
        i, len_output, len_input = 0, 0, len(chars)
        while i < len_input:
            faster_j = i + 1
            while faster_j < len_input and chars[faster_j] == chars[i]:     ### KEEP PROGRESSING IF DUPLICATES.
                faster_j += 1
            
            chars[len_output] = chars[i]    ##### THIS CAN BRING BACK A CHAR TO FIT INTO THE OUTPUT NUM.
            len_output += 1
            
            if faster_j - i > 1:        ##### LOGIC - ADD NUMBER TO ARRAY?
                cnt = str(faster_j - i)
                for c in cnt:           ##### HERE ADD THE COUNT TO THE ARRAY.
                    chars[len_output] = c
                    len_output += 1
                
            i = faster_j            ##### CATCHUP.
        print(f"revised chars = {chars}")
        return len_output
        
soln = Solution()
assert  soln.compress(chars = ["a","a","b","b","c","c","c"]) == 6 
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

assert  soln.compress(chars = ["a"]) == 1
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.

assert  soln.compress(chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]) == 4
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

assert  soln.compress(chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b", "c"]) == 5
# Output: Return 5, and the first 5 characters of the input array should be: ["a","b","1","2","c"].



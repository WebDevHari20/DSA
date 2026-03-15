class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index_map = {}
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            if s[right] in char_index_map:
                if char_index_map[s[right]] >= left:
                    left = char_index_map[s[right]] + 1
            
            char_index_map[s[right]] = right
            
            current_window_len = right - left + 1
            if current_window_len > max_length:
                max_length = current_window_len
                
        return max_length
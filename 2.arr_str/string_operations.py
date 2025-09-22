from typing import Dict, List

# ---------- Test Helper ----------
_total = 0
_passed = 0
def CHECK(msg: str, cond: bool) -> None:
    global _total, _passed
    _total += 1
    if cond:
        _passed += 1
    print(f"[{'PASS' if cond else 'FAIL'}]: {msg}")

# =====================================================
# 1) BASICS
# =====================================================
# Problem: Reverse the given string
# Input:  s (str) - input string
# Output: str     - reversed string
# Complexity: O(n) time, O(n) space
def reverse_string(s: str) -> str:
    # s[::-1] also works
    return s[-1:-len(s)-1:-1]

# Problem: Reverse the given string
# Input:  s (str) - input string
# Output: str     - reversed string
# Complexity: O(n^2) time (string concatenation), O(n) space
def reverse_string2(s: str) -> str:
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

# ASCII Cheat Sheet (Digits + Letters)
# -----------------------------------
# Digits (0–9):      '0' = 48  (0x30)   ...   '9' = 57  (0x39)
# Uppercase (A–Z):   'A' = 65  (0x41)   ...   'Z' = 90  (0x5A)
# Lowercase (a–z):   'a' = 97  (0x61)   ...   'z' = 122 (0x7A)
#
# Binary difference (bit trick):
# 'A' = 65  = 0b0100_0001
# 'a' = 97  = 0b0110_0001
#                 ^
#              0x20 bit → lowercase
#
# Trick:
# - To lowercase: ch | 0x20
# - To uppercase: ch & ~0x20

# Problem: Convert all uppercase letters in a string to lowercase (without using str.lower()).
# Input:  s (str) - input string
# Output: str     - lowercase string
# Complexity: O(n) time, O(n) space

def lower_case(s: str) -> str:
    result = ""
    for ch in s:
        ch = ord(ch)                            # get ASCII code
        if (ch >= ord("A")) and (ch <= ord("Z")):
            ch |= 0x20                          # set 6th bit → convert to lowercase
        result += chr(ch)                       # append converted character
    return result

# Problem: Convert all lowercase letters in a string to uppercase (without using str.upper()).
# Input:  s (str) - input string
# Output: str     - uppercase string
# Complexity: O(n) time, O(n) space
#
# ASCII bit trick:
# 'a' = 97 (0x61) → 0b0110_0001
# 'A' = 65 (0x41) → 0b0100_0001
# Flip off 0x20 bit (bit 5):
#   ch & ~0x20 → uppercase

def upper_case(s: str) -> str:
    result = ""
    for ch in s:
        ch = ord(ch)
        if (ch >= ord("a")) and (ch <= ord("z")):
            ch &= ~0x20
        result += chr(ch)
    return result

# Problem: Check if a string is a palindrome using two-pointer technique
# Input:  s (str)          - input string
#         ignore_case (bool) - whether to ignore case when checking
# Output: bool             - True if palindrome, else False
# Complexity: O(n) time, O(1) extra space
#
# Approach:
# - Start with two pointers: i at start, j at end
# - Compare characters moving inward
# - Stop if mismatch found
# - If ignore_case=True, first convert to lowercase

def is_palindrome_two_pointer(s: str, ignore_case: bool = False) -> bool:
    i = 0
    j = len(s) - 1

    if ignore_case:
        s = lower_case(s)

    while i < j:
        if s[i] != s[j]:
            break
        i += 1
        j -= 1
    
    return False if (i < j) else True

# Problem: Normalize a string by:
#          - Keeping only alphanumeric characters
#          - Converting letters to lowercase
# Input:   s (str) - input string
# Output:  str     - normalized lowercase alphanumeric string
# Complexity: O(n) time, O(n) space
#
# Examples:
#   "Hello, World! 123"         → "helloworld123"
#   "PYTHON3.9"                 → "python39"
#   "A man, a plan, a canal!"   → "amanaplanacanal"
#   "Room #42B"                 → "room42b"
#   "!!!@@@###"                 → ""
#
# Approach:
# - 'a'–'z' → keep
# - '0'–'9' → keep
# - 'A'–'Z' → lowercase via OR 0x20
# - else    → skip

def normalize_alnum_lower(s: str) -> str:
    result = ""
    for ch in s:
        ch = ord(ch)
        if (ch >= ord("a") and ch <= ord("z")) or \
           (ch >= ord("0") and ch <= ord("9")):
            result += chr(ch)
        elif (ch >= ord("A") and ch <= ord("Z")):
            ch |= 0x20                  # make lowercase
            result += chr(ch)
        else:
            pass                        # skip non-alnum
    return result

# Problem: Count frequency of each character in a string
# Input:   s (str) - input string
# Output:  dict[str,int] - mapping of char → frequency
# Complexity: O(n) time, O(k) space (k = unique chars)
#
# Examples:
#   "hello"    → {'h':1, 'e':1, 'l':2, 'o':1}
#   "aabbccc"  → {'a':2, 'b':2, 'c':3}
#   ""         → {}
#
# Approach #1:
# - Iterate through string
# - Use dict.get(ch,0)+1 to update count

from typing import Dict

def char_frequency(s: str) -> Dict[str,int]:
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# Approach #2:
# - Iterate through string
# - If char already seen, increment count
# - Else initialize to 1
def char_frequency2(s:str) -> Dict[str,int]:
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch,0)+1
    return freq

# Problem: Find the first non-repeating character in a string
# Input:   s (str) - input string
# Output:  str or None - first char with frequency 1 (None if none exist)
# Complexity: O(n) time, O(k) space (k = unique chars)
#
# Examples:
#   "leetcode"    → 'l'
#   "aabbccde"    → 'd'
#   "aabbcc"      → None
#
# Approach (two-pass):
# 1. Count frequency of each character
# 2. Scan string again in order, return first char with freq == 1

def first_non_repeating_char(s: str) -> str:
    freq = char_frequency(s)        # Pass 1: count
    for ch in s:                    # Pass 2: scan in order
        if freq[ch] == 1:
            return ch
    return None

# ---------- Sub Runner ----------
def _tests_basics():
    CHECK("reverse_string", reverse_string("Ashfaq") == "qafhsA")
    CHECK("reverse_string2", reverse_string2("Ashfaq") == "qafhsA")
    CHECK("is_palindrome_two_pointer", is_palindrome_two_pointer("Ashfaq",False) == False)
    CHECK("is_palindrome_two_pointer", is_palindrome_two_pointer("AbCCbA",False) == True)
    CHECK("is_palindrome_two_pointer", is_palindrome_two_pointer("AbCbA",False) == True)
    CHECK("is_palindrome_two_pointer", is_palindrome_two_pointer("AbcCbA",True) == True)
    CHECK("is_palindrome_two_pointer", normalize_alnum_lower("A man, a plan, a canal: Panama") == "amanaplanacanalpanama")
    CHECK("is_palindrome_two_pointer:normalize_alnum_lower", is_palindrome_two_pointer(normalize_alnum_lower("A man, a plan, a canal: Panama")) == True)
    CHECK("char_frequency", char_frequency("abcc") == {'a':1,'b':1,'c':2})
    CHECK("char_frequency2", char_frequency2("abcc") == {'a':1,'b':1,'c':2})
    CHECK("first_non_repeating_char", first_non_repeating_char("aaabbcddd") == 'c')
    CHECK("first_non_repeating_char", first_non_repeating_char("aaabbccddd") == None)

# =====================================================
# 1) ANAGRAMS
# =====================================================
# Problem: Check if two strings are anagrams
# Input:   s (str), t (str) - input strings
# Output:  bool - True if anagrams, else False
# Complexity: O(n) time, O(k) space (k = unique chars)
#
# Examples:
#   "listen", "silent"   → True
#   "anagram", "nagaram" → True
#   "rat", "car"         → False

# Version 1: Frequency dictionary compare
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return char_frequency(s) == char_frequency(t)

# Version 2: Optimized one-pass counter. Works for any character set.
# Approach:
# - Use a single dictionary
# - Increment counts for s
# - Decrement counts for t
# - If all counts return to 0 → anagram
def is_anagram_one_pass(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    freq = {}
    for ch1, ch2 in zip(s, t):
        freq[ch1] = freq.get(ch1, 0) + 1
        freq[ch2] = freq.get(ch2, 0) - 1
    
    # all values must be 0
    return all(v == 0 for v in freq.values())

# Version 3: Optimized one-pass counter with fixed-size array
# Approach:
# - Use fixed-size array of length 26
# - Increment counts for chars in s
# - Decrement counts for chars in t
# - If all counts return to 0 → anagram
# Complexity: O(n) time, O(1) space (26 letters only)
def is_anagram2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    base = ord('a')
    cnt = [0]*26

    for ch in s: cnt[ord(ch)-base] += 1 
    for ch in t: cnt[ord(ch)-base] -= 1

    return all(c==0 for c in cnt)

# Problem: Group strings that are anagrams of each other.
# Input:   l (List[str]) - list of strings
# Output:  List[List[str]] - groups of anagrams
#
# Examples:
#   ["eat","tea","tan","ate","nat","bat"]
#     → [["eat","tea","ate"], ["tan","nat"], ["bat"]]

# ------------------------------------------------------
# Version 1: Pairwise check with visited
# Complexity: O(n^2 * m) time, O(n) space
#   n = number of strings, m = avg length per string
# Approach:
# - Maintain visited[] to track used strings
# - For each unvisited string:
#     - Start a new group
#     - Compare with all later strings using is_anagram
#     - Mark matches as visited and add them to group
# - Append group to result and continue

from typing import List

def group_anagrams(l: List[str]) -> List[List[str]]:
    result: List[List[str]] = []
    visited = [False] * len(l)

    for i in range(len(l)):
        if visited[i]:
            continue
        group = [l[i]]
        for j in range(i + 1, len(l)):
            if not visited[j] and is_anagram(l[i], l[j]):
                group.append(l[j])
                visited[j] = True
        result.append(group)
    return result

# ------------------------------------------------------
# Version 2: Hashing with sorted key
# Complexity: O(n * m log m) time, O(n * m) space
# Approach:
# - For each string, sort its characters to form a key
# - Use dictionary: key → list of words
# - Strings with the same sorted key are grouped together
# - Return dictionary values as the result

def group_anagrams_sorted(l: List[str]) -> List[List[str]]:
    buckets = {}
    for s in l:
        key = ''.join(sorted(s))
        if key not in buckets:
            buckets[key] = []
        buckets[key].append(s)
    return list(buckets.values())

# ---------- Sub Runner ----------
def _tests_anagrams():
    CHECK("is_anagram", is_anagram("listen", "silent"))
    CHECK("is_anagram2", is_anagram2("listen", "silent"))
    CHECK("is_anagram2", is_anagram_one_pass("listen", "silent"))
    grouped = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    grouped = frozenset (map(frozenset,grouped))
    expected = [['tan','nat'],['bat'],['eat','ate','tea']]
    expected = frozenset(map(frozenset, expected))
    CHECK("group_anagrams", expected == grouped)
    grouped = group_anagrams_sorted(["eat","tea","tan","ate","nat","bat"])
    grouped = frozenset (map(frozenset,grouped))
    CHECK("group_anagrams", expected == grouped)

# =====================================================
# 3) SLIDING WINDOW
# =====================================================
# Problem: Find the length of the longest substring without repeating characters
# Input:   s (str) - input string
# Output:  (int, str) - length of longest substring, and the substring itself
# Complexity: O(n) time, O(k) space (k = unique chars in window)
#
# Examples:
#   "abcabcbb"   → (3, "abc")
#   "bbbbb"      → (1, "b")
#   "pwwkew"     → (3, "wke")
#   ""           → (0, "")
#
# Approach:
# - Use sliding window with two pointers (l and r)
# - Maintain a dict last[ch] = last seen index of char
# - If repeat found, move l to last[ch] + 1
# - Track best length and substring

def length_of_longest_substring_no_repeat(s: str):
    l = 0
    best = 0
    last = {}
    
    for r, ch in enumerate(s):
        if ch in last and last[ch] >= l:   # FIX: ensure l moves forward
            l = last[ch] + 1
        last[ch] = r

        best = max(r-l+1,best)

    return best

def length_of_longest_substring_no_repeat_bf(s: str):
    maxl = 0
    for i,ch in enumerate(s):
        cur_s = ch
        for next_ch in s[i+1:]:
            if next_ch in cur_s:
                break
            else:
                cur_s += next_ch
        maxl = max(len(cur_s),maxl)
    return maxl

# Problem: Generate all permutations of a string.
# Input:   s (str) - input string
# Output:  List[str] - list of all permutations (order not guaranteed)
# Complexity: 
#   Time  ≈ O(n * n!)   (permutation count is n!; building strings adds a factor of n)
#   Space ≈ O(n * n!)   (to store all permutations)
#
# Examples:
#   "ab"   → ["ab", "ba"]
#   "abc"  → ["abc", "bac", "bca", "acb", "cab", "cba"]
#
# Approach (iterative insertion):
# - Start with [""].
# - For each character ch in s:
#     - Insert ch into every position of every word built so far.
# - The list grows from 1 → n! items.

from typing import List

def find_permutations(s: str) -> List[str]:
    word_list = ['']
    for ch in s:
        new_word_list = []
        for word in word_list:
            for pos in range(len(word) + 1):
                new_word_list.append(word[:pos] + ch + word[pos:])
        word_list = new_word_list
    return word_list

def _tests_sliding_window():
    s = "pwkwkakdfewjourkadf"
    best = length_of_longest_substring_no_repeat(s)
    CHECK ("length_of_longest_substring_no_repeat", best == 10)
    s = "pwkwkakdfewjourkadf"
    best = length_of_longest_substring_no_repeat_bf(s)
    CHECK ("length_of_longest_substring_no_repeat_bf", best == 10)
    #print (find_permutations("abcd"))

# =====================================================
# 4) PATTERN MATCHING
# =====================================================
# Naive substring search: find the first occurrence of needle in haystack.
# Approach:
#  • Slide a window of length n = len(needle) across haystack.
#  • At each position i, compare haystack[i : i+n] with needle.
#  • If a match is found, return starting index i.
#  • If no match is found after scanning, return -1.
# Edge case: empty needle → return 0 by convention (like Python str.find()).
# Example:
#   haystack = "hello", needle = "ll" → return 2
#   haystack = "aaaaa", needle = "bba" → return -1
# Complexity: O((h-n+1)·n) = O(h·n) in worst case (h = len(haystack)).
def find_substring_naive(haystack: str, needle: str) -> int:
    n = len(needle)
    h = len(haystack)

    if n == 0:
        return 0
    
    for i in range(h + 1 - n):
        if haystack[i:i+n] == needle:
            return i
    return -1

# Check if string ss is a subsequence of string s.
# Approach:
#  • Use two pointers i (for s) and j (for ss).
#  • Walk through s:
#       - If chars match, move both i and j.
#       - Otherwise, move only i.
#  • If j reaches len(ss), all chars of ss were found in order inside s.
# Example:
#   s = "abcde", ss = "ace" → True  (a, c, e found in order)
#   s = "abcde", ss = "aec" → False (order not preserved)
# Complexity: O(len(s)), O(1) space.
def _find_word_within_a_string(s: str, ss: str) -> bool:
    ls = len(s)
    lss = len(ss)

    i = j = 0
    while i < ls and j < lss:
        if s[i] == ss[j]:
            j += 1
        i += 1
    return j == lss

# Count how many words in lss are subsequences of string s.
# Approach:
#  • For each word ss in list lss, check if it is a subsequence of s
#    using _find_word_within_a_string.
#  • Increment count if True.
# Example:
#   s = "abcde", lss = ["a","bb","acd","ace"]
#   Subsequences: "a", "acd", "ace" → total = 3
# Complexity: O(m·n), where m = len(lss), n = len(s).
def find_words_within_a_string(s: str, lss: List[str]) -> int:
    occ = 0
    for ss in lss:
        occ += _find_word_within_a_string(s, ss)
    return occ

# ---------- Sub Runner ----------
def _tests_pattern_matching():
    CHECK("find_substring_naive", find_substring_naive("hello", "ll") == 2)
    # --- Tests for single subsequence ---
    CHECK("empty ss is subsequence", _find_word_within_a_string("abc", "") == True)
    CHECK("non-empty ss in empty s", _find_word_within_a_string("", "a") == False)
    CHECK("basic subsequence", _find_word_within_a_string("abxxymxxyz", "xxyz") == True)
    CHECK("wrong order", _find_word_within_a_string("abxxymxxyz", "xyzx") == False)
    CHECK("exact match", _find_word_within_a_string("hello", "hello") == True)
    CHECK("not present", _find_word_within_a_string("hello", "world") == False)

    # --- Tests for multiple subsequences ---
    CHECK("2 matches", find_words_within_a_string("abxxymxxyz", ["xxyz", "xyz", "abc"]) == 2)
    CHECK("all match", find_words_within_a_string("hello", ["he", "lo", "hlo"]) == 3)
    CHECK("none match", find_words_within_a_string("data", ["xyz", "qq", "ttt"]) == 0)

#----------------------------------------------------------
# 424. Longest Repeating Character Replacement
#----------------------------------------------------------
"""
Problem: Given a string s consisting of uppercase English letters and an integer k,
return the length of the longest substring that can be obtained by replacing at most
k characters so that all characters in the substring are the same.

Input: str s (A-Z only), int k (k >= 0)
Output: int (max length)

Examples:
  s="ABAB", k=2         -> 4        (replace two 'A'->'B' or two 'B'->'A')
  s="AABABBA", k=1      -> 4        ("AABA" or "ABBA")
  s="AAAA", k=2         -> 4        (already uniform)
  s="ABCDE", k=1        -> 2        (any pair with one change)
  s="", k=3             -> 0

Edge cases to watch:
- Empty string → 0
- k = 0 (no replacements allowed)
- All same letters (already optimal)
- Many distinct letters with small k
- Very long strings (performance)

Pattern: Sliding Window + frequency count + track max_freq in window
"""

from typing import List, Dict

def longest_replacement_bf(s: str, k: int) -> int:
    """
    Brute force: Try all substrings s[i:j+1]. For each, count the frequency
    of letters and check if (window_len - max_freq) <= k. Track the best length.
    T: O(n^2 * Σ) where Σ ≤ 26 (build/count per window)
    S: O(Σ) for frequency map
    """
    n = len(s)
    best = 0

    A = ord('A')
    for i in range(n):
        freq = [0]*26
        max_freq = 0
        for j in range(i,n):
            idx = ord(s[j]) - A
            freq[idx] += 1
            max_freq = max(max_freq, freq[idx])
            window_len = j - i + 1
            if (window_len - max_freq) <= k:
                best = max(window_len, best)
    return best

def longest_replacement_bf1(s: str, k: int) -> int:
    l = len(s)
    A = ord('A')
    best = 0
    for i in range(l):
        freq = [0]*26
        max_freq = 0
        for j in range(i,l):
            freq[ord(s[j])-A] += 1
            max_freq = max(max(freq),max_freq)
            if j-i+1 - max_freq<= k:
                best = max(j-i+1,best)
    return best

def longest_replacement_op(s: str, k: int) -> int:
    """
    Optimal: Sliding window with a frequency map of chars in the window.
    Maintain max_freq = highest count of any single letter in the window.
    If (window_len - max_freq) > k, shrink from the left.
    Answer is max window length seen.
    T: O(n) amortized, S: O(Σ) with Σ ≤ 26
    """
    best = 0
    l = 0
    n = len(s)
    freq = [0]*26
    A = ord('A')
    for r in range(n):
        freq[ord(s[r])-A] += 1
        if ((r-l+1) - max(freq)) > k:
            freq[ord(s[l])-A] -= 1
            l += 1
        best = max(r-l+1,best)

    return best

"""
------------------------------------------------------------
Complexity Comparison
------------------------------------------------------------
Version                    | Time          | Space | Notes
---------------------------|---------------|-------|------------------------------
longest_replacement_bf     | O(n^2 * 26)   | O(26) | Check all windows via counts
longest_replacement_op     | O(n)          | O(26) | SW + freq + track max_freq
------------------------------------------------------------
"""

# Assumes a CHECK helper exists:
# def CHECK(msg: str, cond: bool): print("PASS" if cond else "FAIL", "-", msg)

def _demo_longest_repeating_character_replacement():
    #---------------- longest_replacement_bf -----------------
    CHECK("BF basic ABAB,k=2 -> 4", longest_replacement_bf("ABAB", 2) == 4)
    CHECK("BF AABABBA,k=1 -> 4",   longest_replacement_bf("AABABBA", 1) == 4)
    CHECK("BF AAAA,k=2 -> 4",      longest_replacement_bf("AAAA", 2) == 4)
    CHECK("BF ABCDE,k=1 -> 2",     longest_replacement_bf("ABCDE", 1) == 2)
    CHECK("BF empty,k=3 -> 0",     longest_replacement_bf("", 3) == 0)
    CHECK("BF k=0 strict",         longest_replacement_bf("ABBA", 0) == 2)  # "AA" or "BB"

    CHECK("BF basic ABAB,k=2 -> 4", longest_replacement_bf1("ABAB", 2) == 4)
    CHECK("BF AABABBA,k=1 -> 4",   longest_replacement_bf1("AABABBA", 1) == 4)
    CHECK("BF AAAA,k=2 -> 4",      longest_replacement_bf1("AAAA", 2) == 4)
    CHECK("BF ABCDE,k=1 -> 2",     longest_replacement_bf1("ABCDE", 1) == 2)
    CHECK("BF empty,k=3 -> 0",     longest_replacement_bf1("", 3) == 0)
    CHECK("BF k=0 strict",         longest_replacement_bf1("ABBA", 0) == 2)  # "AA" or "BB"

    #---------------- longest_replacement_op -----------------
    CHECK("OP basic ABAB,k=2 -> 4", longest_replacement_op("ABAB", 2) == 4)
    CHECK("OP AABABBA,k=1 -> 4",    longest_replacement_op("AABABBA", 1) == 4)
    CHECK("OP AAAA,k=2 -> 4",       longest_replacement_op("AAAA", 2) == 4)
    CHECK("OP ABCDE,k=1 -> 2",      longest_replacement_op("ABCDE", 1) == 2)
    CHECK("OP empty,k=3 -> 0",      longest_replacement_op("", 3) == 0)
    CHECK("OP k=0 strict",          longest_replacement_op("ABBA", 0) == 2)

# ---------- Runner ----------
def run_all_checks():
    _tests_basics()
    _tests_anagrams()
    _tests_sliding_window()
    _tests_pattern_matching()
    _demo_longest_repeating_character_replacement()
    print(f"TOTAL: {_passed}/{_total} passed")

# ---------- Main ----------
if __name__ == "__main__":
    run_all_checks()

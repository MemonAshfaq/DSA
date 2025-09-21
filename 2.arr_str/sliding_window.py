from typing import Dict, List

_passed = 0
_total = 0
def CHECK(msg: str, cond: bool):
    global _total
    global _passed

    _total += 1
    if cond: _passed += 1

    print ("[{}] {}".format("PASS" if cond else "FAIL", msg))

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

    #---------------- longest_replacement_op -----------------
    CHECK("OP basic ABAB,k=2 -> 4", longest_replacement_op("ABAB", 2) == 4)
    CHECK("OP AABABBA,k=1 -> 4",    longest_replacement_op("AABABBA", 1) == 4)
    CHECK("OP AAAA,k=2 -> 4",       longest_replacement_op("AAAA", 2) == 4)
    CHECK("OP ABCDE,k=1 -> 2",      longest_replacement_op("ABCDE", 1) == 2)
    CHECK("OP empty,k=3 -> 0",      longest_replacement_op("", 3) == 0)
    CHECK("OP k=0 strict",          longest_replacement_op("ABBA", 0) == 2)

#----------------------------------------------------------
# 76. Minimum Window Substring
#----------------------------------------------------------
"""
Problem: Given strings s and t, return the minimum window substring of s
that contains all the characters of t (including multiplicities). If no
such window exists, return "".

Input: str s, str t
Output: str

Examples:
  s="ADOBECODEBANC", t="ABC" -> "BANC"
  s="a", t="a"               -> "a"
  s="a", t="aa"              -> ""

Edge cases to watch:
- t longer than s → ""
- Either s or t empty
- Repeated characters in t (e.g., t="AABC")
- Multiple valid windows; must return the shortest
- Case sensitivity matters ("a" ≠ "A")

Pattern: Sliding Window with need/have counts; expand then contract when valid
"""
def min_window_bf(s: str, t: str) -> str:
    """
    Brute force: Enumerate all substrings of s and check if each covers t using
    frequency counts. Track and return the shortest valid window.

    T: O(n^3) in the naive form (O(n^2) substrings * O(n) check),
       can be improved to O(n^2 * Σ) with counting-based checks.
    S: O(Σ) for frequency maps (Σ = character set size)
    """
    ns = len(s)
    nt = len(t)
    if ns < nt:
        return ""
    l = 0
    vt = [0]*nt
    found = False
    r = 0
    done = False
    best = float('inf')

    for i in range(ns):
        loop = True
        for k in range(nt):
            if loop:
                if s[i] == t[k]:
                    vt[k] = 1
                    if found == False:
                        found = True
                        l = i
                    else:
                        r = i
                    if all(vt):
                        best = min(best, r-l+1)
                        vt = [0]*nt
                        found = False
                    loop = False
    print (s[l:r+1])
    return s[l:r+1]
    

def min_window_op(s: str, t: str) -> str:
    """
    Optimal: Sliding window with two hash maps:
      - need[c] = required count of char c from t
      - have[c] = current count of c in the window
    Expand right pointer r to include characters; once all required counts are met,
    move left pointer l to shrink the window while keeping it valid. Track best.

    T: O(n + Σ) ~ O(n) — each index visited at most twice (expand/contract)
    S: O(Σ) for the need/have maps (bounded by unique chars in t)
    """
    # TODO: implement
    return ""

"""
------------------------------------------------------------
Complexity Comparison
------------------------------------------------------------
Version         | Time         | Space | Notes
----------------|--------------|-------|-------------------------------
min_window_bf   | O(n^3)       | O(Σ)  | Check every substring
min_window_op   | O(n + Σ)≈O(n)| O(Σ)  | Expand→contract sliding window
------------------------------------------------------------
"""

#---------------------------
# Self-Tests (demo)
#---------------------------
def _demo_min_window_substring():
    #---------------- bf -----------------
    CHECK("BF basic", min_window_bf("ADOBECODEBANC", "ABC") == "BANC")
    CHECK("BF exact", min_window_bf("a", "a") == "a")
    CHECK("BF impossible", min_window_bf("a", "aa") == "")
    CHECK("BF repeats", min_window_bf("AAABBC", "AABC") in {"AABB", "AABBC"})  # shortest valid windows
#
    #---------------- op -----------------
    #CHECK("OP basic", min_window_op("ADOBECODEBANC", "ABC") == "BANC")
    #CHECK("OP exact", min_window_op("a", "a") == "a")
    #CHECK("OP impossible", min_window_op("a", "aa") == "")
    #CHECK("OP repeats", min_window_op("AAABBC", "AABC") in {"AABB", "AABBC"})

# -------------- Runner -------------------
def demo_lc_sliding_window():
    print ("=========== _tests_sliding_window ==============")
    _demo_longest_repeating_character_replacement()
    _demo_min_window_substring()

# -------------- Main -------------------
if __name__ == "__main__":
    demo_lc_sliding_window()
    print ("============================================")
    print ("Result: {}/{} passed".format(_passed, _total))
    print ("============================================")

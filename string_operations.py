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
def reverse_string(s: str) -> str:
    return s[-1:-len(s)-1:-1]

def reverse_string2(s: str) -> str:
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

def lower_case (s: str) -> str:
    result = ""
    for ch in s:
        ch = ord(ch)
        if (ch >= ord("A")) and (ch <= ord("Z")):
            ch |= 0x20
        result += chr(ch)
    return result

def upper_case (s: str) -> str:
    result = ""
    for ch in s:
        ch = ord(ch)
        if (ch >= ord("a")) and (ch <= ord("z")):
            ch &= ~0x20
        result += chr(ch)
    return result

def is_palindrome_two_pointer (s: str, ignore_case: bool = False) -> bool:
    i = 0
    j = len(s) - 1

    if ignore_case:
        s = lower_case(s)

    while (i < j):
        if (s[i] != s[j]):
            break
        i += 1
        j -= 1
    
    return False if (i < j) else True

def normalize_alnum_lower(s: str) -> str:
    result = ""
    for ch in s:
        ch = ord(ch)
        if (ch >= ord("a") and ch <= ord("z")) or \
            (ch >= ord("0") and ch <= ord("9")):
            result += (chr(ch))
        elif (ch >= ord("A") and ch <= ord("Z")):
            ch |= 0x20
            result += (chr(ch))
        else:
            pass
    return result

def char_frequency(s:str) -> Dict[str,int]:
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch,0) + 1
    return freq

def char_frequency2(s:str) -> Dict[str,int]:
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

def first_non_repeating_char(s:str) -> str:
    freq = char_frequency(s)
    for k,v in freq.items():
        if v == 1:
            return k
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
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return char_frequency(s) == char_frequency(t)

def is_anagram2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    base = ord('a')
    cnt = [0]*26

    for ch in s: cnt[ord(ch)-base] += 1 
    for ch in s: cnt[ord(ch)-base] -= 1

    return all(c==0 for c in cnt)

def group_anagrams(l: List):
    result = []
    visted = [False]*len(l)

    for i in range(len(l)):
        if visted[i]:
            continue
        group = [l[i]]
        for j in range(i+1,len(l)):
            if not visted[j] and is_anagram(l[i],l[j]):
                group.append(l[j])
                visted[j] = True
        result.append(group)
    return result

# ---------- Sub Runner ----------
def _tests_anagrams():
    CHECK("is_anagram", is_anagram("listen", "silent"))
    CHECK("is_anagram2", is_anagram2("listen", "silent"))
    grouped = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    grouped = frozenset (map(frozenset,grouped))
    expected = [['tan','nat'],['bat'],['eat','ate','tea']]
    expected = frozenset(map(frozenset, expected))
    CHECK("group_anagrams", expected == grouped)

# =====================================================
# 3) SLIDING WINDOW
# =====================================================
def length_of_longest_substring_no_repeat(s):
    l = 0
    best = 0
    last = {}
    window = ""
    longest = ""
    for r, ch in enumerate(s):
        if ch in window:
            l = last[ch] + 1
        window = s[l:r+1]
        last[ch] = r

        if len(window) > best:
            best = len(window)
            longest = window
        
    return best,longest

def find_permutations1(s:str) -> List[str]:
    word_list = ['']
    for ch in s:
        new_word_list = []
        for word in word_list:
            for pos in range(len(word)+1):
                new_word_list.append(word[:pos] + ch + word[pos:])
        word_list = new_word_list
    return word_list

def _tests_sliding_window():
    s = "pwkwkakdfewjourkadf"
    best, longest = length_of_longest_substring_no_repeat(s)
    CHECK ("length_of_longest_substring_no_repeat", best == 10 and longest == "akdfewjour")
    print (find_permutations1("abcd"))

# =====================================================
# 4) PATTERN MATCHING
# =====================================================
def find_substring_naive(haystack: str, needle: str) -> int:
    n = len(needle)
    h = len(haystack)

    if n == 0:
        return 0
    
    for i in range(h+1-n):
        if haystack[i:i+n] == needle:
            return i
            break
    return -1

def _find_word_within_a_string(s:str,ss:str) -> bool:
    ls = len(s)
    lss = len(ss)

    i = j = 0

    while (i < ls and j < lss):
        if s[i] == ss[j]:
            j += 1
        i += 1
    return (j == lss)

def find_words_within_a_string(s:str,lss:List[str]) -> int:
    occ = 0
    for ss in lss:
        occ += _find_word_within_a_string(s,ss)
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

# ---------- Runner ----------
def run_all_checks():
    _tests_basics()
    _tests_anagrams()
    _tests_sliding_window()
    _tests_pattern_matching()
    print(f"TOTAL: {_passed}/{_total} passed")

# ---------- Main ----------
if __name__ == "__main__":
    run_all_checks()


# Python translation of the C bit operations demo
# Notes:
# - We emulate 32-bit unsigned behavior with u32() masking where needed.
# - Functions return new values (no pointers); where C used &reg, we return the updated value.

# ============================
# Bit Manipulation – Interview Notes (Python-style comments)
# ============================

# Core identities
# ---------------
# a ^ a = 0
# a ^ 0 = a
# a & a = a
# a | a = a
# a & ~a = 0
# a | ~a = all_ones
# (a & b) | (a & ~b) = a
# a + b using bits: sum = a ^ b, carry = (a & b) << 1, repeat until carry == 0

# Safe shifts (concept)
# ---------------------
# Left/right shifting by >= word size yields 0 (by convention in many "safe" helpers).
# In Python use masks to emulate 32-bit: x & 0xFFFFFFFF before/after shifts if needed.

# Bit set/clear/toggle/test
# -------------------------
# set   bit k:  x |  (1 << k)
# clear bit k:  x & ~(1 << k)
# flip  bit k:  x ^  (1 << k)
# test  bit k: (x >> k) & 1   or  (x & (1 << k)) != 0

# Power of two check
# ------------------
# x != 0 and (x & (x - 1)) == 0

# Popcount (Kernighan)
# --------------------
# count = 0
# while x: x &= (x - 1); count += 1
# Complexity: O(# of set bits), ≤ 32 for 32-bit ints.

# Reverse bits (byte)
# -------------------
# Methods:
# 1) bit-by-bit swap: res |= ((n >> i) & 1) << (7 - i)
# 2) masks: swap nibbles/pairs/singles:
#    n = ((n & 0xF0) >> 4) | ((n & 0x0F) << 4)
#    n = ((n & 0xCC) >> 2) | ((n & 0x33) << 2)
#    n = ((n & 0xAA) >> 1) | ((n & 0x55) << 1)
# 3) table lookup rev_table[256]; for 32-bit do 4 byte lookups

# Rightmost set bit (LSB 1)
# -------------------------
# mask = n & -n              # isolates the lowest set bit
# index (0-based):
#   loop: while (n & 1) == 0: n >>= 1; i++
#   or for mask: index = mask.bit_length() - 1

# Leftmost set bit (MSB 1)
# ------------------------
# index = n.bit_length() - 1   # for n > 0

# Add without '+'
# ---------------
# while b != 0:
#   sum = a ^ b
#   carry = (a & b) << 1
#   a, b = sum, carry
# return a
# (For Python 32-bit simulation, mask with 0xFFFFFFFF and sign-fix at the end.)

# Subtract without '-'
# --------------------
# a - b == a + two_complement(b)
# two_complement(b) == (~b + 1) under a fixed width (mask to 32-bit).
# Then reuse the add-with-carry loop.

# Mapping unsigned 32-bit to signed in Python
# -------------------------------------------
# x &= 0xFFFFFFFF
# if x >= 0x80000000: x -= 1 << 32   # e.g., 0xFFFFFFFE -> -2

# ‘Add 2^k’ vs ‘Set bit k’
# ------------------------
# add 2^k: n + (1 << k)
# set bit: n | (1 << k)        # NOT the same if bit k already 1

# Swap
# ----
# Python: a, b = b, a
# C: tmp = a; a = b; b = tmp;   # XOR swap exists but is less readable.

# Single Number problems (canonical)
# ----------------------------------
# I: one appears once, others appear twice
#    XOR all → result
# II: one appears once, others appear thrice
#    For each bit b: cnt_b = sum((x >> b) & 1); result_b = cnt_b % 3
#    Reconstruct; fix sign if needed.
# III: two appear once, others appear twice
#    xor_all = a ^ b
#    mask = xor_all & -xor_all
#    XOR numbers in two buckets split by mask → yields a and b

# Generalizing by frequency r
# ---------------------------
# If duplicates appear r times:
# - r even (2,4,...): XOR-based bucket split works (pairs cancel).
# - r odd  (3,5,...): per-bit counts % r. To get TWO uniques:
#     1) global residues per bit; pick a bit with residue == 1 (uniques differ there)
#     2) split by that bit; rebuild each unique via per-bit % r in its bucket

# Hamming distance
# ----------------
# Between two ints: popcount(x ^ y)
# Total Hamming distance over array:
#   For each bit b: ones = count of numbers with bit b = 1
#                   zeros = n - ones
#                   add ones * zeros to total
# Complexity: O(32 * n)

# Complexity quick notes
# ----------------------
# Single Number I (XOR):      O(n) time, O(1) space
# Single Number II (mod 3):   O(32 * n) ~ O(n), O(1) space
# Single Number III (r=2):    O(n), O(1)
# Total Hamming Distance:     O(32 * n), O(1)
# Brute-force total Hamming:  O(n^2), O(1)

# Signed/negative handling in Python
# ----------------------------------
# Always force 32-bit view when needed: x = x & 0xFFFFFFFF
# After reconstruction, if x >= 1<<31: x -= 1<<32

# Common pitfalls
# ---------------
# - Using list.count() → O(n) hidden cost; loops nesting → O(n^2)
# - Forgetting sign fix for 32-bit when using Python ints
# - Confusing “set bit” (|) with “add power-of-two” (+)
# - Shifting by >= word size or negative shift → define/guard behavior
# - Relying on XOR split when duplicates appear an odd number of times (won’t work)

# Tiny worked examples
# --------------------
# Single Number I: [4,1,2,1,2] -> 4
# Single Number II: [2,2,3,2] -> 3 (per-bit %3)
# Single Number III: [1,2,1,3,2,5] -> (3,5)
# Rightmost set bit: n=12 (1100b) → n & -n = 0100b (4), index=2
# Total Hamming Distance: [4,14,2] -> 6 via per-bit ones*zeros

# Interview tips
# --------------
# - State the property first (e.g., “pairs cancel under XOR”, “per-bit modulo r”).
# - Give time/space upfront.
# - Mention Python impl but note C translation (loops, masks, fixed-width).
# - Validate with a tiny example and edge cases (0, negatives, duplicates).


# ============================
# Subtraction using Two's Complement (8-bit examples)
# ============================

# Example 1: 49 - 5
# -----------------
# Step 1: Write in 8-bit binary
#   49 = 00110001
#    5 = 00000101
#
# Step 2: Compute two’s complement of 5
#   invert(00000101) = 11111010
#   add 1 → 11111011   (this is -5 in 8-bit)
#
# Step 3: Add 49 and -5
#   00110001
# + 11111011
# -----------
# 1 00101100   (9th carry discarded)
# Result = 00101100 = 44
#
# 49 - 5 = 44

# Example 2: 5 - 49
# -----------------
# Step 1: Write in 8-bit binary
#    5 = 00000101
#   49 = 00110001
#
# Step 2: Compute two’s complement of 49
#   invert(00110001) = 11001110
#   add 1 → 11001111   (this is -49 in 8-bit)
#
# Step 3: Add 5 and -49
#   00000101
# + 11001111
# -----------
#   11010100
#
# Step 4: Interpret 11010100 as negative
#   invert(11010100) = 00101011
#   add 1 → 00101100 = 44
# So value = -44
#
# 5 - 49 = -44 (in 8-bit, result stored as 11010100)

def u32(x):
    return x & 0xFFFFFFFF

def safe_shift_left(var, shift):
    return 0 if shift >= 32 else u32(var << shift)

def safe_shift_right(var, shift):
    return 0 if shift >= 32 else (var >> shift)  # Python >> on non-negative is logical

def print_binary(ubit32):
    bits = ''.join('1' if (ubit32 & (1 << i)) else '0' for i in range(31, -1, -1))
    # Add spaces every 8 bits for readability
    grouped = ' '.join(bits[i:i+8] for i in range(0, 32, 8))
    print(grouped)

def set_bit(var, bit):
    return var if bit >= 32 else u32(var | (1 << bit))

def clear_bit(var, bit):
    return var if bit >= 32 else u32(var & ~(1 << bit))

def toggle_bit(var, bit):
    return var if bit >= 32 else u32(var ^ (1 << bit))

def is_bit_set(var, bit):
    return 0 if bit >= 32 else (1 if (var & (1 << bit)) != 0 else 0)

# [7:4] = mode, [3:0] = speed
MODE_MASK  = 0xF
MODE_SHIFT = 4
SPEED_MASK = 0xF
SPEED_SHIFT = 0

def set_mode_speed_shift(reg, mode, speed):
    reg = u32(reg & ~(MODE_MASK << MODE_SHIFT))
    reg = u32(reg | ((mode & MODE_MASK) << MODE_SHIFT))
    reg = u32(reg & ~(SPEED_MASK << SPEED_SHIFT))
    reg = u32(reg | ((speed & SPEED_MASK) << SPEED_SHIFT))
    return reg

def set_mode_speed_fields(reg, mode, speed):
    # Emulate the bitfield layout: speed [3:0], mode [7:4]
    value = ((speed & SPEED_MASK) << 0) | ((mode & MODE_MASK) << 4)
    return u32(value)

def is_only_one_bit_set(var):
    return 1 if (var != 0 and (var & (var - 1)) == 0) else 0

def count_set_bits(var):
    var = u32(var)
    count = 0
    while var:
        var &= (var - 1)
        count += 1
    return count

def reverse_bits_8(n):
    # Safe, straightforward bit-by-bit reverse
    n &= 0xFF
    result = 0
    for i in range(8):
        result |= ((n >> i) & 1) << (7 - i)
    return result & 0xFF

def reverse_bits_32(n):
    n = u32(n)
    result = 0
    for i in range(32):
        result |= ((n >> i) & 1) << (31 - i)
    return u32(result)

def reverse_bits_32(n):
    n = u32(n)
    n = (n&0xFFFF0000) >> 16 | (n&0x0000FFFF) << 16
    n = (n&0xFF00FF00) >> 8 | (n&0x00FF00FF) << 8
    n = (n&0xF0F0F0F0) >> 4 | (n&0x0F0F0F0F) << 4
    n = (n&0xCCCCCCCC) >> 2 | (n&0x33333333) << 2
    n = (n&0xAAAAAAAA) >> 1 | (n&0x55555555) << 1
    n = u32(n)
    return n    

def reverse_bits2(n):
    n &= 0xFF
    n = ((n & 0xF0) >> 4) | ((n & 0x0F) << 4)
    n = ((n & 0xCC) >> 2) | ((n & 0x33) << 2)
    n = ((n & 0xAA) >> 1) | ((n & 0x55) << 1)
    return n & 0xFF

def reverse_bits3(n):
    n &= 0xFF
    n = ((n >> 1) & 0x55) | ((n & 0x55) << 1)
    n = ((n >> 2) & 0x33) | ((n & 0x33) << 2)
    n = ((n >> 4) & 0x0F) | ((n & 0x0F) << 4)
    return n & 0xFF

def find_right_most_set_bit(n):
    n &= 0xFF
    for i in range(8):
        if (n >> i) & 1:
            return i
    return -1

def find_left_most_set_bit(n):
    n &= 0xFF
    for i in range(7, -1, -1):
        if n & (1 << i):
            return i
    return -1

def swap_xor(a, b):
    # In Python, just return swapped; XOR swap shown for parity with C logic
    a ^= b
    b ^= a
    a ^= b
    return a, b

# Build rev_table programmatically (byte-wise reverse)
rev_table = [reverse_bits_8(i) for i in range(256)]

def rev_with_table(n):
    n = u32(n)
    result = 0
    for i in range(4):
        byte = (n >> (8 * i)) & 0xFF
        result |= rev_table[byte] << (8 * (3 - i))
    return u32(result)

_total = 0
_passed = 0

def CHECK(msg, cond):
    global _total
    global _passed
    _total += 1
    if cond: _passed += 1
    print(f"[{'PASS' if cond else 'FAIL'}]: {msg}")

def SUMMARIZE():
    global _total
    global _passed
    print ("--------------------------------------------")
    print ("PASS:  {}".format(_passed))
    print ("TOTAL: {}".format(_total))
    print ("--------------------------------------------")

# Find unique number in the given array
def single_number(a):
    uniq_set = set(a)

    for i in uniq_set:
        if (a.count(i) == 1):
            return i

# Find single number in given array using where every other number appears
# even number of times. XOR all elements - result is the single number 
def single_number_xor(a):
    res = 0
    for i in range(0, len(a)):
        res ^= a[i]
    return res

# Find the unique element in an array where every other element appears r times.
# Approach:
#  • For each bit position (0–31), count how many numbers have that bit set.
#  • Since duplicates appear r times, their contributions cancel under (count % r).
#  • The leftover bits reconstruct the unique number.
# Complexity: O(32·n) time, O(1) extra space.
def single_number_sum(a, r):
    result = 0
    for i in range(32):
        cnt = 0
        for n in a:
            cnt += (n >> i) & 1
        if cnt % r:
            result |= (1 << i)
    return result

# Find the two unique elements in an array where every other element appears exactly twice.
# Approach:
#  • XOR all numbers → result = num1 ^ num2 (pairs cancel).
#  • In this xor, bits set to 1 are where num1 and num2 differ.
#  • We only need one such differing bit to tell them apart.
#       - Use mask = xor & -xor to isolate the lowest set bit.
#       - That bit is 0 in one unique number and 1 in the other.
#  • Partition numbers by this bit, XOR within each group → each group’s result is one unique number.
# Example: a = [2, 3, 2, 5]
#          xor = 6 (110), mask = 2 (010)
#          Group1 (bit=0): {2,2,5} → 5
#          Group2 (bit=1): {3} → 3
#          Result = (3,5)
# Complexity: O(n) time, O(1) space.
def two_single_num(a):
    xor = 0
    for n in a:
        xor ^= n
    mask = xor & -xor

    g1 = 0
    g2 = 0
    for n in a:
        if n & mask:
            g1 ^= n
        else:
            g2 ^= n
    return (g1, g2)

# Add two integers using bitwise operations (no + or -).
# Approach:
#  • Loop through each of the 32 bits.
#  • For bit i:
#       - Extract ai = bit of a, bi = bit of b.
#       - Sum bit = ai ^ bi ^ carry (XOR = addition without carry).
#       - Carry = (ai & bi) | (ai & carry) | (bi & carry) (majority function).
#  • Place sum bit in result at position i, update carry for next bit.
# Example:
#   a = 5 (0101), b = 3 (0011)
#   bit0: sum=0, carry=1
#   bit1: sum=1, carry=1
#   bit2: sum=0, carry=1
#   bit3: sum=1, carry=0
#   result = 1000 (8) → correct
# Complexity: O(32) time, O(1) space.
def bit_sum(a, b):
    carry = 0
    result = 0
    for i in range(32):
        ai = (a >> i) & 1
        bi = (b >> i) & 1
        s = (carry ^ ai ^ bi) & 1
        carry = (ai & bi) | (ai & carry) | (bi & carry)
        result |= (s << i)
    return result

# Compute Hamming Distance between two integers a and b.
# Definition: Number of bit positions where a and b differ.
# Approach:
#  • XOR the two numbers → bits set in result indicate positions where they differ.
#  • Count set bits in this XOR result → that’s the Hamming distance.
# Example:
#   a = 5 (0101), b = 9 (1001)
#   a ^ b = 1100 → two set bits → distance = 2
# Complexity: O(32) time if using bit-count loop, O(1) with built-in popcount.
def hamming_distance(a, b):
    diff = a ^ b
    return count_set_bits(diff)

# Compute the two’s complement of an integer a (assuming 32-bit).
# Approach:
#  • Two’s complement = invert all bits (~a) + 1.
#  • u32(a) ensures masking into 32-bit unsigned space.
# Example:
#   a = 5  → binary 000...0101
#   ~a     → binary 111...1010
#   ~a + 1 → binary 111...1011 = -5 (in 32-bit signed form)
# Complexity: O(1).
def two_complement(a):
    return (~(u32(a)) + 1)

# Convert a lowercase character to uppercase using bit manipulation.
# Approach:
#  • ASCII 'a'–'z' differ from 'A'–'Z' only by bit 5 (0x20).
#  • Clearing this bit (~0x20) converts lowercase → uppercase.
#  • If the char is already uppercase (or non-alpha), it stays unchanged.
# Example:
#   'a' (0110 0001) & ~0x20 = 'A' (0100 0001)
# Complexity: O(1).
def upper_case(ch):
    ch = ord(ch)
    if ch >= ord("a") and ch <= ord("z"):
        ch &= ~0x20
    return chr(ch)

# Compute total Hamming Distance for all pairs in array a (brute force).
# Approach:
#  • For every unique pair (i, j), compute hamming_distance(a[i], a[j]).
#  • Accumulate the sum over all pairs.
# Example:
#   a = [4, 14, 2]
#   Pairs: (4,14)=2, (4,2)=2, (14,2)=2 → total = 6
# Complexity:
#  • O(n^2 * k), where n = len(a), k = number of bits (≤32).
#  • Inefficient for large n, but correct.
def hamming_distance_brute_force(a):
    total = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            total += hamming_distance(a[i], a[j])
    return total

# Compute total Hamming Distance for all pairs in array a (optimized).
# Approach:
#  • For each bit position (0–31):
#       - Count how many numbers have a 1 at this bit (ones).
#       - Count how many have a 0 at this bit (zeros).
#       - Each differing pair contributes 1 to Hamming distance → ones * zeros.
#  • Sum contributions across all 32 bits.
# Example:
#   a = [4, 14, 2]
#   Bit0: ones=0, zeros=3 → 0
#   Bit1: ones=2, zeros=1 → 2
#   Bit2: ones=2, zeros=1 → 2
#   Bit3: ones=1, zeros=2 → 2
#   Total = 6
# Complexity: O(n·k), where n = len(a), k = 32 (bit width).
# Much faster than brute force O(n^2·k).
def hamming_distance_bitops(a):
    total = 0
    for i in range(32):
        ones = 0
        zeros = 0
        for n in a:
            ones += ((n >> i) & 1) == 1
            zeros += ((n >> i) & 1) == 0
        total += ones * zeros
    return total

def demoBits():
    a = 0x5A5A5A5A
    b = 0xA5A5A5A5

    AND = u32(a & b)
    OR  = u32(a | b)
    XOR = u32(a ^ b)
    NOT = u32(~a)
    SHL = safe_shift_left(a, 4)
    SHR = safe_shift_right(a, 4)
    SHL0 = safe_shift_left(a, 32)
    SHR0 = safe_shift_right(a, 32)
    SET = set_bit(a, 0)
    CLR = clear_bit(a, 1)
    TGL = toggle_bit(a, 2)
    IS_SET = is_bit_set(a, 1)
    reg1 = 0
    reg1 = set_mode_speed_shift(reg1, 0xA, 0x5) # mode=0xA, speed=0x5
    reg2 = 0
    reg2 = set_mode_speed_fields(reg2, 0x5, 0xA) # (mode=0xA, speed=0x5) -> fields mapping
    IS_POW2 = is_only_one_bit_set(0x00010000)
    ISNT_POW2 = is_only_one_bit_set(0x00050000)
    COUNT = count_set_bits(0x5A5A5A5A)
    REV = reverse_bits_8(0xAA)
    REV32 = reverse_bits_32(0xAAAAAAAA)
    REV2 = reverse_bits2(0xAA)
    REV3 = reverse_bits3(0xAA)
    RMOST = find_right_most_set_bit(0x80)
    RMOST0 = find_right_most_set_bit(0x00)
    LMOST = find_left_most_set_bit(0x01)
    LMOST0 = find_left_most_set_bit(0x00)
    swap_a = 0xAAAAAAAA
    swap_b = 0xBBBBBBBB
    swap_a, swap_b = swap_xor(swap_a, swap_b)
    a = [4,14,2]
    dist_bf = hamming_distance_brute_force(a)
    dist_bo = hamming_distance_bitops(a)

    a = [1,2,1,3,2,3,4]
    single = single_number(a)
    single_xor = single_number_xor(a)
    a = [1,2,3,1,2,9,1,2,3,3]
    single_sum3 = single_number_sum(a,3)
    a = [1,2,1,2,3,7,4,4,3,5,5]
    single_sum2 = single_number_sum(a,2)

    print (two_single_num([1,2,3,4,5,1,2,3]))
    
    sum = bit_sum(55,88)
    dist = hamming_distance(0x55,0xAA)
    comp2 = two_complement(55)
    ch = upper_case("p")

    CHECK("AND", AND == 0x00000000)
    CHECK("OR",  OR  == 0xFFFFFFFF)
    CHECK("XOR", XOR == 0xFFFFFFFF)
    CHECK("NOT", NOT == 0xA5A5A5A5)
    CHECK("SHL", SHL == 0xA5A5A5A0)
    CHECK("SHR", SHR == 0x05A5A5A5)
    CHECK("SHL0", SHL0 == 0x00000000)
    CHECK("SHR0", SHR0 == 0x00000000)
    CHECK("SET", SET == 0x5A5A5A5B)
    CHECK("CLR", CLR == 0x5A5A5A58)
    CHECK("TGL", TGL == 0x5A5A5A5E)
    CHECK("IS_SET", IS_SET == 1)
    CHECK("REG1", reg1 == 0x000000A5)
    CHECK("REG2", reg2 == 0x0000005A)
    CHECK("IS_POW2", IS_POW2 == 1)
    CHECK("ISNT_POW2", ISNT_POW2 == 0)
    CHECK("COUNT", COUNT == 16)
    CHECK("REV", REV == 0x55)
    CHECK("REV32", REV32 == 0x55555555)
    CHECK("REV2", REV2 == 0x55)
    CHECK("REV3", REV3 == 0x55)
    CHECK("RMOST", RMOST == 7)
    CHECK("RMOST0", RMOST0 == -1)
    CHECK("LMOST", LMOST == 0)
    CHECK("LMOST0", LMOST0 == -1)
    CHECK("SWAPA", swap_a == 0xBBBBBBBB)
    CHECK("SWAPB", swap_b == 0xAAAAAAAA)
    CHECK("REVTAB32", reverse_bits_32(0x12345678) == rev_with_table(0x12345678))
    CHECK("SINGLE", single == 4)
    CHECK("SINXOR", single_xor == 4)
    CHECK("SINSUM3", single_sum3 == 9)
    CHECK("SINSUM2", single_sum2 == 7)
    CHECK("SUM", sum == 55+88)
    CHECK("DISTANCE", dist == 8)
    CHECK("TWOCOMP", comp2 == -55)
    CHECK("UPCASE", ch == "P")
    CHECK("DISTBF", dist_bf == 6)
    CHECK("DISTBO", dist_bo == 6)
    CHECK("all zeros",          reverse_bits_32(0x00000000) == 0x00000000)
    CHECK("all ones",           reverse_bits_32(0xFFFFFFFF) == 0xFFFFFFFF)
    CHECK("lsb -> msb",         reverse_bits_32(0x00000001) == 0x80000000)
    CHECK("msb -> lsb",         reverse_bits_32(0x80000000) == 0x00000001)
    CHECK("alt 1010...",        reverse_bits_32(0xAAAAAAAA) == 0x55555555)
    CHECK("alt 0101...",        reverse_bits_32(0x55555555) == 0xAAAAAAAA)
    CHECK("byte pal 0x00FF00FF",reverse_bits_32(0x00FF00FF) == 0xFF00FF00)
    CHECK("nibble swap demo",   reverse_bits_32(0x12345678) == 0x1E6A2C48)

if __name__ == "__main__":
    demoBits()
    SUMMARIZE()
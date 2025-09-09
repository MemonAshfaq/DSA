from typing import List

def valid_parentheses_bf(s:str) -> bool:
    done = False
    while not done:
        new_s = s.replace("[]","").replace("{}","").replace("()","")
        if new_s == s:
            done = True
        s = new_s
    return len(s) == 0

def valid_parentheses_op(s:str) -> bool:
    match = {
        ']' : '[',
        '}' : '{',
        ')' : '('
    }
    stack = []

    for ch in s:
        if ch in "{[(":
            stack.append(ch)
        else:
            expected = stack.pop()
            if match[ch] != expected:
                return False
    return True

_total = 0
_passed = 0

def CHECK(msg:str, cond:bool):
    print ("[{}] {}".format("PASS" if cond else "FAIL",msg))
    global _passed
    global _total
    if cond:
        _passed += 1
    _total += 1

def _demo_stack():
    #---------------- bf -----------------
    CHECK("BF ()", valid_parentheses_bf("()") == True)
    CHECK("BF ()[]{}", valid_parentheses_bf("()[]{}") == True)
    CHECK("BF (]", valid_parentheses_bf("(]") == False)
    CHECK("BF ([)]", valid_parentheses_bf("([)]") == False)
    CHECK("BF {[]}", valid_parentheses_bf("{[]}") == True)
    CHECK("BF empty", valid_parentheses_bf("") == True)
    #---------------- op -----------------
    CHECK("OP ()", valid_parentheses_op("()") == True)
    CHECK("OP ()[]{}", valid_parentheses_op("()[]{}") == True)
    CHECK("OP (]", valid_parentheses_op("(]") == False)
    CHECK("OP ([)]", valid_parentheses_op("([)]") == False)
    CHECK("OP {[]}", valid_parentheses_op("{[]}") == True)
    CHECK("OP empty", valid_parentheses_op("") == True)

class Stack:
    def __init__(self):
        self.min = []
        self.stack = []
        self.min_so_far = float ('inf')

    def push(self, val:int):
        self.min_so_far = min (val, self.min_so_far)
        self.stack.append(val)
        self.min.append(self.min_so_far)

    def pop(self):
        val = self.stack.pop()
        self.min.pop()
        if len(self.min) != 0:
            self.min_so_far = self.min[-1]
        return val

    def top(self):
        val = self.stack[-1]
        return val
    
    def getmin(self):
        return self.min[-1]

def _demo_min_stack():
    #---------------- basic -----------------
    st = Stack()
    st.push(5)
    st.push(3)
    st.push(7)
    st.push(2)

    CHECK("Top is 2", st.top() == 2)
    CHECK("Min is 2", st.getmin() == 2)

    st.pop()   # removes 2
    CHECK("Top is 7", st.top() == 7)
    CHECK("Min is 3", st.getmin() == 3)

    st.pop()   # removes 7
    CHECK("Top is 3", st.top() == 3)
    CHECK("Min is 3", st.getmin() == 3)

    st.pop()   # removes 3
    CHECK("Top is 5", st.top() == 5)
    CHECK("Min is 5", st.getmin() == 5)

    st.pop()   # removes 5
    CHECK("Empty stack?", len(st.stack) == 0 and len(st.min) == 0)

    #---------------- edge: negatives -----------------
    st2 = Stack()
    for x in [0, -2, -3, 4, -1]:
        st2.push(x)

    CHECK("Min with negatives", st2.getmin() == -3)
    st2.pop()   # remove -1
    CHECK("Min after popping -1", st2.getmin() == -3)
    st2.pop()   # remove 4
    CHECK("Min still -3", st2.getmin() == -3)
    st2.pop()   # remove -3
    CHECK("Min updated to -2", st2.getmin() == -2)

    #---------------- edge: increasing order -----------------
    st3 = Stack()
    for x in [1, 2, 3, 4, 5]:
        st3.push(x)
    CHECK("Min increasing", st3.getmin() == 1)

    #---------------- edge: decreasing order -----------------
    st4 = Stack()
    for x in [5, 4, 3, 2, 1]:
        st4.push(x)
    CHECK("Min decreasing", st4.getmin() == 1)
    st4.pop()
    CHECK("Min after pop 1", st4.getmin() == 2)

def evaluate_rpl(tokens: List[str]):
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a,b = stack.pop(), stack.pop()
            stack.append(b-a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a,b = stack.pop(), stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(c))

    return stack[0]

def _demo_evaluate_rpl():
    # Example 1: ["2","1","+","3","*"] → (2+1)*3 = 9
    CHECK("Basic addition + multiply",
          evaluate_rpl(["2","1","+","3","*"]) == 9)

    # Example 2: ["4","13","5","/","+"] → 4 + (13/5) = 6
    CHECK("Division + addition",
          evaluate_rpl(["4","13","5","/","+"]) == 6)

    # Example 3: ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # This is from LeetCode — evaluates to 22
    CHECK("Complex expression",
          evaluate_rpl(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22)

    # Edge: subtraction order matters
    CHECK("Subtraction 3-4",
          evaluate_rpl(["3","4","-"]) == -1)

    # Edge: division truncates toward zero
    CHECK("Division -7/3 → -2",
          evaluate_rpl(["-7","3","/"]) == -2)
    

def decode_string_bf(s:str) -> str:
    count = 0
    repeat = ""
    output = ""
    for ch in s:
        if '0' <= ch <= '9':
            count = count*10 + int(ch)
        elif ch == '[':
            repeat = ""
        elif ch == ']':
            output += (repeat*count)
            count = 0
        else:
            repeat += ch

    return output

def decode_str_op(s:str) -> str:
    stack = []

    for ch in s:
        if ch != ']':
            stack.append(ch)
        else:
            substr = ""
            while stack[-1] != '[':
                k = stack.pop()
                substr = k + substr
            stack.pop()

            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(substr* int(k))
    return "".join(stack)


def _demo_decode_str_op():
    # basics
    CHECK("basic 3[a]",                 decode_str_op("3[a]") == "aaa")
    CHECK("concat blocks",              decode_str_op("2[ab]3[cd]ef") == "abcabccdcdcdef")
    CHECK("multi-digit 12[a]",          decode_str_op("12[a]") == "aaaaaaaaaaaa")
    CHECK("zero times 0[x]",            decode_str_op("0[x]") == "")
    # nesting
    CHECK("nested 3[a2[c]]",            decode_str_op("3[a2[c]]") == "accaccacc")
    CHECK("deep nest 2[a3[b2[c]]]",     decode_str_op("2[a3[b2[c]]]") == "abccbccbccabccbccbcc")
    # prefixes/suffixes
    CHECK("prefix/suffix xy2[z]w",      decode_str_op("xy2[z]w") == "xyzzw")
    CHECK("prefix + nested",            decode_str_op("p3[q2[r]]s") == "prrqrrqrrs")
    # mixed letters inside
    CHECK("letters inside 2[aXb]",      decode_str_op("2[aXb]") == "aXbaXb")
    # large repeat (sanity only, not printing)
    CHECK("large repeat 50[a] len==50", len(decode_str_op("50[a]")) == 50)


#[2,4]
#[2,1,3,4]

def next_greater_element_bf(nums1:List[int], nums2:List[int]) -> List[int]:
    nums = [-1] * len(nums1)
    for i,n in enumerate(nums1):
        found = False
        for j,m in enumerate(nums2):
            if n == m:
                found = True
            if found and m > n and nums[i] == -1:
                nums[i] = m
    return nums

def next_greater_element_op(nums1:List[int], nums2:List[int]) -> List[int]:
    nums = [-1] * len(nums1)
    stack = []

    idx_dict = {n:i for i,n in enumerate(nums1)}

    for m in nums2:
        while stack and m > stack[-1]:
            n = stack.pop()
            nums[idx_dict[n]] = m
        if m in idx_dict:
            stack.append(m)
    return nums

def _demo_next_greater_element():
    #---------------- bf -----------------
    CHECK("BF ex1",
          next_greater_element_bf([4,1,2], [1,3,4,2]) == [-1,3,-1])
    CHECK("BF ex2",
          next_greater_element_bf([2,4], [1,2,3,4]) == [3,-1])
    CHECK("BF single",
          next_greater_element_bf([1], [1]) == [-1])
    CHECK("BF inc",
          next_greater_element_bf([1,2], [1,2,3]) == [2,3])
    #---------------- bf -----------------
    CHECK("BF ex1",
          next_greater_element_op([4,1,2], [1,3,4,2]) == [-1,3,-1])
    CHECK("BF ex2",
          next_greater_element_op([2,4], [1,2,3,4]) == [3,-1])
    CHECK("BF single",
          next_greater_element_op([1], [1]) == [-1])
    CHECK("BF inc",
          next_greater_element_op([1,2], [1,2,3]) == [2,3])


def _print_summary():
    global _total
    global _passed
    print ("-------------------------------------------")
    print ("Total: {}, Passed: {}".format(_total, _passed))
    print ("-------------------------------------------")
    
if __name__ == "__main__":
    _demo_stack()
    _demo_min_stack()
    _demo_evaluate_rpl()
    _demo_decode_str_op()
    _demo_next_greater_element()
    _print_summary()

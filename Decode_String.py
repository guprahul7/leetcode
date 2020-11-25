
s0 = "100[leetcode]"
s5 = "sd2[f2[e]g]i" #--> expected: "sdfeegfeegi"
s1 = "3[a]2[bc]"
s2 = "3[a2[c]]"
s3 = "2[abc]3[cd]ef"
s4 = "abc3[cd]xyz"

def decode_string(s):
    numbers = {'0','1','2','3','4','5','6','7','8','9'}
    stack = []
    
    for i in range(len(s)):
        if s[i] == '[':
            stack.append(i)
        
    while stack:
        print('current_s = ', s)
        current_open_index = stack.pop()

        multiplier_index_end = current_open_index
        multiplier_index_start = current_open_index-1
        
        #print('multiplier_start= ', multiplier_index_start, '\t', 'multiplier_end = ', multiplier_index_end)

        while s[multiplier_index_start] in numbers:
            multiplier_index_start -= 1

        multiplier_index_start += 1

        multiplier = int(s[multiplier_index_start : multiplier_index_end])
        i = current_open_index + 1
        
        sub_s = ''
        while ( (i <= len(s)-1) and (s[i] != ']') ):
            sub_s = sub_s + s[i]
            i += 1

        print('sub_s = ', sub_s)
        mult_s = multiplier * sub_s
        print('mult_s = ',mult_s)
        
        if i+1 <= len(s) - 1:
            s = s[:multiplier_index_start] + mult_s + s[i+1:]
        else:
            s = s[:multiplier_index_start] + mult_s
        
        print('---------------')\

    return s

print(decode_string(s5), '\n===========\n')

# print(decode_string(s1), '\n===========\n')
# print(decode_string(s2), '\n===========\n')
# print(decode_string(s3), '\n===========\n')
# print(decode_string(s4), '\n===========\n')
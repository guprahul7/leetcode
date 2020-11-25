
s = 'race!c@ar...'

while start < end:
    inc_start = True
    dec_end = True
    if s[start] != isAlpha:
        start += 1
        inc_start = False
    elif s[end] != isAlpha:
        s[end] -= 1
        dec_end = False
    else:
        if s[start] != s[end]:
            return False

    if inc_start:
        start += 1
    if dec_end:
        end -= 1
        
return True
    
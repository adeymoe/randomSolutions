def shortcut(s):
    for i in ["a","e","i","o","u"]:
        if i in s:
            s = s.replace(i,"")

    return(s)

def hex_to_dec(s):
    s = int(s, 16)
    return s





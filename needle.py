haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

def find_needle(haystack):
    haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
    for item in range(len(haystack)):
        if item == "needle":
            print(f"found the needle at position {haystack[item]}")

find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"])
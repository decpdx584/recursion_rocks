# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

ss = input("Type any string: ")

def reverse(ss): 
    if len(ss) == 0: 
        return ss 
    else: 
        return reverse(ss[1:]) + ss[0]
print(reverse(ss))


# print(reverse("")) 
# => ""
# print(reverse("a")) 
# => "a"
# print(reverse("ab")) 
# => "ba"
# print(reverse("computer")) 
# => "retupmoc"
# print(reverse(reverse("computer"))) 
# => "computer"
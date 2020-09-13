'''
Verifies both demorgan theorems:
not(A and B) == (not A)  or (not B)
not(A  or B) == ((not A) and (not B))

Look carefully!  They're not the same.
Also, notice the extra parentheses in the second one.

Why are those parentheses needed?
'''

# There are 4 True/False combinations for the first theorem,
# and 4 more for the second theorem, so you should have eight
# versions of these 3 lines of code :

#First Theorem
A = True
B = True
print ("not(", A, "and", B, ")", "==",
       "(not", A, ") or (not", B, "):",
       not(A and B)==(not A) or (not B) )
A = True
B = False
print ("not(", A, "and", B, ")", "==",
       "(not", A, ") or (not", B, "):",
       not(A and B)==(not A) or (not B) )
A = False
B = True
print ("not(", A, "and", B, ")", "==",
       "(not", A, ") or (not", B, "):",
       not(A and B)==(not A) or (not B) )
A = False
B = False
print ("not(", A, "and", B, ")", "==",
       "(not", A, ") or (not", B, "):",
       not(A and B)==(not A) or (not B) )
#Second Theorem
A = True
B = True
print ("not(", A, "and", B, ")", "==",
       "(not", A, ") or (not", B, "):",
       not(A or B)==((not A) and (not B)))
A = True
B = False
print ("not(", A, "and", B, ")", "==",
       "(not", A, ") or (not", B, "):",
       not(A or B)==((not A) and (not B)))
A = False
B = True
print ("not(", A, "and", B, ")", "==",
       "(not", A, ") or (not", B, "):",
       not(A or B)==((not A) and (not B)))
A = False
B = False
print ("not(", A, "and", B, ")", "==",
       "(not", A, ") or (not", B, "):",
       not(A or B)==((not A) and (not B)))

#RS

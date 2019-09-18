#One list comprehensions
S = [x**2 for x in range(10)]
print(S)
M = [x for x in S if x % 2 == 0]
print(M)

M.reverse() 
print(M)


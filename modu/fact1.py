def fact(n):
    facto = 1;
    for i in range(1,n+1):
        facto = facto*i
    return facto

print(fact(10))
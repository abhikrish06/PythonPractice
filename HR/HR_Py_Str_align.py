thickness = 3 #This must be an odd number
c = 'H'
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Mat size must be N*M. (N is an odd natural number, M and 3 is N times .)
N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2):
    print(("-"*((M-3*i)//2))+ (".|."*i) + ("-"*((M-3*i)//2)))
print("-"*((M-7)//2)+ "WELCOME" + "-"*((M-7)//2))
for i in range(N-2,-1,-2):
    print(("-"*((M-3*i)//2))+ (".|."*i) + ("-"*((M-3*i)//2)))


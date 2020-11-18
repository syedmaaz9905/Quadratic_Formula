#Quadratic Formula

print("------------------ QUADRATIC FORMULA ------------------")
A=int(input("Put The Value Of A = "))
B=int(input("Put The Value Of B = "))
C=int(input("Put The Value Of C = "))
d=(B**2-4*A*C)
X1=(-B+d)/2*A
print("\nFor Positive Value")
print("Quadratic Formula = (-B+(B^2-4*A*C)*0.5)/2*A ")
print('X1 =',X1)
print("\nFor Negative Value")
print("Quadratic Formula = (-B-(B^2-4*A*C)*0.5)/2*A ")
X2=(-B-d)/2*A
print('X2 =',X2)

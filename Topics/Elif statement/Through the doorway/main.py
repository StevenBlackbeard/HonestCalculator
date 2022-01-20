A = int(input())
B = int(input())
C = int(input())
X = int(input())
Y = int(input())
doorway = X * Y
package = min(A * B, B * C, A * C)
if doorway >= package:
    print("The box can be carried")
else:
    print("The box cannot be carried")

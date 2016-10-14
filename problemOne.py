import math
x1 = int(raw_input("Take the first co-ordinate: "))
y1 = int(raw_input("Take the second co-ordinate: "))
x2 = int(raw_input("Take the third co-ordinate: "))
y2 = int(raw_input("Take the four co-ordinate: "))

c = x2 - x1
ans1 = c * c

d = y2 - y1
ans2 = d * d

e = math.sqrt(ans1+ans2)

print "Distance between 2D co-ordinate: %d" %e

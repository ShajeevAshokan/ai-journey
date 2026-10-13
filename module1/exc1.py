class A:
       def __init__(self):
           self.x = 1
       def inc(self):
           self.x += 1
a = A()
b = A()
a.inc()
print(a.x, b.x)
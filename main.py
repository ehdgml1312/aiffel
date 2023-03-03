import sys

class Set():
    def __init__(self):
        self.list = [0]*20
    def add(self,x):
        if self.list[x] == 0:
            self.list[x] = 1
    def remove(self,x):
        if self.list[x] == 1:
            self.list[x] = 0
    def check(self,x):
        if self.list[x] == 1:
            print(1)
        else:
            print(0)
    def toggle(self,x):
        if self.list[x] == 0:
            self.list[x] = 1
        else:
            self.list[x] = 0
    def all(self):
        self.list = [1]*20
    def empty(self):
        self.list = [0]*20

n = int(input())
set = Set()
for _ in range(n):
    order = sys.stdin.readline().split()
    if len(order) == 1:
        getattr(set,order[0])()
    else:
        getattr(set,order[0])(int(order[1])-1)

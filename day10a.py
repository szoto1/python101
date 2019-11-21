class A():
    def daj(self):
        print("Mam A")

class BA(A):
    def daj(self):
        print("Mam BA")

class B(BA):
    pass

class C(A):

    def daj(self):
        print("Mam C")

class D(B,C):
    pass

d = D()
d.daj()
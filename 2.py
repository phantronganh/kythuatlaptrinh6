class hinhchunhat(object):
    def __init__(self,d,r):
        self.dai = d
        self.rong = r
    def dien_tich(self):
        return self.dai*self.rong
d=int(input("nhap chieu dai: "))
r=int(input("nhap chieu rong: "))

c=hinhchunhat(d,r)
print(c.dien_tich()) 

    



class Permutation:
    def __init__(self):
        pass

    def fac(self,n):
        n=n-1
        return n

    def permu_NR(self,nr):
        nr=nr+1
        nrli=[]
        while not nr==0:
            # print(nr)
            nr=self.fac(nr)
            nrli.append(nr)
        return nrli

    def forLoop_NR(self,li):
        temp=1
        for i in li:
            if li[i]==0:
                pass
            else:
                # print(li[i])
                temp*=li[i]
                # print("temp: ",temp)
        return temp

    def test(self,n):
        print(n)

    def npr(self,n,r):
        n_N=self.permu_NR(n)
        print(n_N)
        real_N=self.forLoop_NR(n_N)
        
        r_R=self.permu_NR(r)
        new_li_n=[x for x in range(0,((n-r)+1))]
        real_R=self.forLoop_NR(new_li_n)
        
        nPr=(real_N/real_R)
        print(int(nPr))
        return int(nPr)



    





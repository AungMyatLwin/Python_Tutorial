

class Permutation:
    #constructor (self is equal to this.)
    def __init__(self):
        pass

    # factorial function
    def fac(self,n):
        n=n-1
        return n

    def permu_NR(self,nr):
        nr=nr+1
        nrli=[]
        while not nr==0:
            #recursive function 
            nr=self.fac(nr)
            nrli.append(nr)
        return nrli

    # temp = temp*li
    #total sum of list values
    #unpack and multiply the result

    def forLoop_NR(self,li):
        temp=1
        for i in li:
            if li[i]==0:
                pass
            else:
                temp*=li[i]
        return temp

    def npr(self,n,r):
        n_N=self.permu_NR(n)
        
        real_N=self.forLoop_NR(n_N)
        
        #new_li is new list based on n-r+1 == (10-4)+1
        new_li_n=[x for x in range(0,((n-r)+1))]
        real_R=self.forLoop_NR(new_li_n)
        
        nPr=(real_N/real_R)
        print(int(nPr))
        return int(nPr)



    





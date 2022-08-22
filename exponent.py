class ExponentClass:
    def __init__(self):
        pass
    def expo(self,number,exponent):
        pows=1
        for _ in range(exponent):
            pows*=number
        print(pows)
        return pows


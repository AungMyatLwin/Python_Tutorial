
empty_list=[]
def second_max(li:list):
    for x in li:
        if x not in empty_list:
            empty_list.append(x)
    t=sorted(empty_list,reverse=True)
    return t[1]



if __name__ == '__main__':
    n = int(input())
    if n<=10 and n>=2:
        
        arr = list(map(int, input().split()))
        if len(arr)>= -100 and len(arr)<=100:
            max2=second_max(arr)
            print(max2)
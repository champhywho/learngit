def createCounter():
    ans=[0]
    def counter():
        ans[0]+=1
        print(ans)
        return ans[0]
    print(ans)
    return counter
A=createCounter()
print(A())
print(A())
print(A())

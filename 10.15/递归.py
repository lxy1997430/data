import time
def fbi(n):
    if n<=1:#n=1和0是出口
        return n
    else:
        return fbi(n-1)+fbi(n-2)

start = time.time()
print(fbi(40))
end = time.time()
dur = end - start
print(dur)

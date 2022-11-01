import time
try:
    a = input("Familiyangizni kiriting: ")

    def f():
        for x in range(20):
            time.sleep(0.2)
            print(a)
            
except:
    print("Xatolik bor")
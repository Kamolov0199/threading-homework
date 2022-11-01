import time

try:
    a = input("Otangizni ismini kiriting: ")

    def otch():
        for x in range(20):
            time.sleep(0.2)
            print(a)
            
except:
    print("Xatolik bor")
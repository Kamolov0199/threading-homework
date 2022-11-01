import time

try:
    a = int(input("""Jinsingizni tanlang:
1-ayol;
2-erkak: """))

    def fayl():
        if a == 1:
            for x in range(20):
                time.sleep(0.2)
                print("qizi")
        elif a == 2:
            for x in range(20):
                time.sleep(0.2)
                print("o'g'li")
        else:
            print("Xato kirityapsiz")

except ValueError:
    print("Siz string kirityapsiz")
except:
    print("Xatolik bor")
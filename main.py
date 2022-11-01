import threading
from surname import *
from name import *
from fname import *
from fayl import *

t1 = threading.Thread(target=f)
t2 = threading.Thread(target=name)
t3 = threading.Thread(target=otch)
t4 = threading.Thread(target=fayl)

t1.start()
t2.start()
t3.start()
t4.start()
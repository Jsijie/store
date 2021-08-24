from threading import  Thread
import time


class makeshow(Thread):
    chushi=""
    guke=""
    num = 0
    num1 = 3000

    def run(self) -> None:
        while True:
            if self.num<500:
                self.num+=1
                print(self.chushi,"制作了1个面包，剩余",self.num,"个面包")
            else:
                time.sleep(2)

            if self.num1<=0:
                break
            else:
                if self.num>0:
                    self.num1-=3
                    print(self.guke,"购买了1个面包，剩余余额",self.num1)
                else:
                    time.sleep(2)

p1=makeshow()
p2=makeshow()
p3=makeshow()
p4=makeshow()
p1.chushi="厨师1"
p2.chushi="厨师2"
p3.chushi="厨师3"
p1.guke="顾客1"
p2.guke="顾客2"
p3.guke="顾客3"
p4.guke="顾客4"


p1.start()
p2.start()
p3.start()
p4.start()











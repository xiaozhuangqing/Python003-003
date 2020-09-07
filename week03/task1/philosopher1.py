
''''
哲学家进餐问题
参考 https://github.com/strongwucc/Python003-003/blob/master/week03/dining_philosophers.py
改进：发现上述方法运行几次之后，会出现死锁情况，我加了一个判断，防止死锁
实现如下：
    规定每次左侧叉子最多不能超过4把拿起，否则就容易死锁
    定义了一个队列，记录左侧叉子拿起放下的情况，拿起入队，放下出队，保证队列长度不能大于4，可以等于

'''


import threading
import time
import queue

# 定义一个吃饭顺序队列，记录所有的动作
results = queue.Queue() 
# 定义一个队列，记录左侧叉子被拿起的情况
num_locked = queue.Queue()

class DiningPhilosophers(threading.Thread):
    def __init__(self,philosopher,eat_num,left_fork,right_fork):
        super().__init__()
        self.philosopher = philosopher
        self.eat_num = eat_num
        self.left_fork = left_fork
        self.right_fork = right_fork


# philosopher 哲学家的编号。
# eat_num   吃饭次数
# pickLeftFork 和 pickRightFork 表示拿起左边或右边的叉子。
# eat 表示吃面。
# putLeftFork 和 putRightFork 表示放下左边或右边的叉子。
    # 模拟竞争吃饭,重写run方法
    def run(self):
        while self.eat_num > 0:
            #竞争左边叉子
            if self.left_fork.acquire(timeout=0.1):
                # continue
                self.pickLeftFork()
                # 竞争右边的叉子
                if self.right_fork.acquire(timeout=0.1):
                    self.pickRightFork()
                    # 吃饭
                    self.eat()
                    # 完成一次吃饭
                    self.eat_num-=1
                    # 放下左叉
                    self.putLeftFork()
                    # 放下右叉子
                    self.putRightFork()
                else:
                    self.left_fork.release()
                    # continue

    # 拿起左边的叉子
    def pickLeftFork(self):
        print(f'{self.philosopher} 拿起左叉 ')
        results.put([self.philosopher, 1,1])

    # 拿起右边的叉子
    def pickRightFork(self):
        print(f'{self.philosopher} 拿起左叉 ')
        results.put([self.philosopher, 2,1])

    # 吃面
    def eat(self):
        print(f'{self.philosopher} 吃饭')
        results.put([self.philosopher, 0,3])

    # 放下左边的叉子
    def putLeftFork(self):
        print(f'{self.philosopher} 放下左边的叉子 ')
        results.put([self.philosopher,2,2])
        self.left_fork.release()

    # 放下右边的叉子
    def putRightFork(self):
        print(f'{self.philosopher} 放下右边的叉子 ')
        results.put([self.philosopher, 2,2])
        self.right_fork.release()


if __name__ =="__main__":

    eat_num =2

    # 创建五把叉子锁
    fork_lock = {}
    for i in range (5):
        fork_lock[i] = threading.Lock()

    # 创建5个哲学家，分配相应的叉子
    philosophers = {}
    for i in range(5):
        if i== 0:
            philosophers[i] = DiningPhilosophers(i,eat_num,fork_lock[4],fork_lock[i])
        else:
            philosophers[i] = DiningPhilosophers(i,eat_num,fork_lock[i-1],fork_lock[i])

    for i in range(5):
        philosophers[i].start()

    for i in range(5):
        philosophers[i].join()
    print(results.qsize())
    value = []
    while 1:
        if results.empty():
            break
        else:
            value.append(results.get())
    
    print (value)


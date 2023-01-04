class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class BrowserHistory(object):

    def __init__(self, homepage):
        init_node = Node(homepage)
        self.head = init_node
        self.tail = init_node
        self.ptr = 1

    def visit(self, url):
        new_node = Node(url)
        current = self.tail

        if current.next is None:
            current.next = new_node

    
        else:
            temp = current  # naver.com
            current = current.next  # discord.com
            new_node.next = current
            temp.next = new_node

        self.tail = new_node
        self.ptr += 1

        return None

    def back(self, steps):
        # self.tail 정보와 steps 계산해야
        current = self.head

        # 들어가기 전에 검사
        if self.ptr - 1 < steps:
            self.ptr = 1
            self.tail = self.head
            return self.head.value

        for _ in range(self.ptr-steps-1):
            current = current.next

        self.tail = current
        self.ptr = self.ptr - steps

        return self.tail.value

    def forward(self, steps):
        current = self.tail

        # 들어가기 전에 검사
        temp = self.tail
        cnt = 0

        while(temp.next):
            temp = temp.next
            cnt += 1

        if steps > cnt:
            return self.tail.value

        for _ in range(steps):
            current = current.next

        self.tail = current
        self.ptr = self.ptr + steps

        return self.tail.value
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

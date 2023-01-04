class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):  # O(n)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while(current.next):  # head부터 시작해야함! 마지막(=li의 마지막)까지 탐색해야함!
                current = current.next
            current.next = new_node

    def get(self, idx):  # O(n)
        current = self.head  # Node(1)
        for _ in range(idx):
            current = current.next
        return current.value
        # return Node(idx + 1).value  # 아니 이거 간단한데 ㅋㅋ ㅠㅠ 좀 야매인가? Node 클래스가 있어야하니까 그런듯

    def insert(self, idx, value):
        new_node = Node(value)

        current = self.head
        for _ in range(idx - 1):
            current = current.next
        temp = current  # 노드 벌써 끊어버리면 안 된다!

        # temp.value = 2
        # temp.next = 0x4A2F5(9)

        # new_node.value = 9
        # new_node.next = 0x4AF47(3)

        current = current.next
        new_node.next = current
        temp.next = new_node

        # current.value = 3
        # current.next = 0x4AF67 (4)

        # 디스코드에 공유하래용

    def remove(self, idx):
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        temp = current  # 항상 저장하는게 핵심

        # temp.value = 2
        # temp.next = 0x4A2F5(9)

        current = current.next
        temp.next = current.next

        # current.value = 9
        # current.next = 0x4AF47(3)

    def print_all(self, idx = 0):
        print("=============== Print node ===============")
        current = self.head
        while(current):
            print("(" + str(current.value) + "," + str(current.next) + ")")
            current = current.next
        print("===========================================")
        print()

    def insert_back(self, value):
        new_node = Node(value)

        print("new_node.value = ", end='')
        print(new_node.value)
        print("new_node = ", end='')
        print(new_node)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
            # self.tail.next = new_node
            # self.tail = self.tail.next
            # 이거 안 돌아감

        # self.head = Node(1)
        # self.tail = Node(1)
        # new_node = Node(6)
        # 마지막 노드의 next 에 새로 만든 노드 넣어 주면 될텐데

        # insert_back 이랑 append 랑은 전혀 다른 함수
        # append 함수 쓰고 insert_back 은 절대 못 쓰나?



li = LinkedList()
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.append(5)
li.print_all()

li.insert(2, 9)
li.print_all()

li.remove(2)
li.print_all()

ll = LinkedList()
ll.insert_back(1)
ll.insert_back(2)
ll.insert_back(3)
ll.insert_back(4)
ll.insert_back(5)
ll.insert_back(6)
ll.insert_back(7)
ll.print_all()

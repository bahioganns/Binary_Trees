import heapq
import random


class Node(object):
    __slots__ = ("left", "right", "data", "priority")

    def __init__(self, data, priority):
        self.left, self.right = None, None
        self.data, self.priority = data, priority


class Tree(object):
    def __init__(self):
        self.root = None

    def split(self, node, data):
        if node is None:
            return None, None

        if data < node.data:
            left, node.left = self.split(node.left, data)
            right = node
            return left, right

        node.right, right = self.split(node.right, data)
        left = node
        return left, right

    def merge(self, left, right):
        if left is None:
            return right
        elif right is None:
            return left
        elif left.priority > right.priority:
            left.right = self.merge(left.right, right)
            return left

        right.left = self.merge(left, right.left)
        return right

    def find(self, data):
        return self.__find(self.root, data)

    def __find(self, node, data):
        if node is None:
            return None
        if node.data == data:
            return node
        elif data < node.data:
            return self.__find(node.left, data)

        return self.__find(node.right, data)

    def add(self, data):
        node = Node(data, random.randint(1, 2 ** 64))

        if self.root is None:
            self.root = node
            return

        left, right = self.split(self.root, data)
        self.root = self.merge(left, node)
        self.root = self.merge(self.root, right)


def tree_single_task(filein, fileout):
    fin = open(filein)
    fout = open(fileout)

    tree = Tree()

    tree_size = int(fin.readline())

    for i in range(tree_size):
        val = int(fin.readline())
        line = fout.readline()
        if tree.find(val) is None:
            if line != "-\n" and line != "-":
                print("task on file ", filein, " Failed")
                return False

            tree.add(val)
        else:
            if line != "+\n" and line != "+":
                print("task on file ", filein, " Failed")
                return False

    fin.close()
    fout.close()

    print("task on file ", filein, " Succeed")


def tree_tasks():
    print("contain tree tasks results: ")
    tree_single_task("tree_sources/1.in", "tree_sources/1.contains.out")
    tree_single_task("tree_sources/2.in", "tree_sources/2.contains.out")
    tree_single_task("tree_sources/3.in", "tree_sources/3.contains.out")
    tree_single_task("tree_sources/4.in", "tree_sources/4.contains.out")
    tree_single_task("tree_sources/5.in", "tree_sources/5.contains.out")
    tree_single_task("tree_sources/6.in", "tree_sources/6.contains.out")
    tree_single_task("tree_sources/7.in", "tree_sources/7.contains.out")


def next_value(root, node):
    if node.right is not None:
        current = node.right
        while current is not None:
            if current.left is None:
                break
            current = current.left
        return current

    succ = None
    while root:
        if root.data < node.data:
            root = root.right
        elif root.data > node.data:
            succ = root
            root = root.left
        else:
            break

    return succ


def heap_single_task(filein, fileout):
    heap = []
    fin = open(filein)
    fout = open(fileout)
    heap_size = int(fin.readline())

    for i in range(heap_size):
        line = fin.readline()

        if line == "GET\n":
            num = heapq.heappop(heap)
            if -num != int(fout.readline()):
                print("task on file ", filein, " Failed")
                return False
        else:
            if line != "GET":
                num = -1 * int(line)
                heapq.heappush(heap, num)
            else:
                num = heapq.heappop(heap)

                if -num != int(fout.readline()):
                    print("task on file ", filein, " Failed")
                    return False

    fin.close()

    print("task on file ", filein, " Succeed")
    return True


def heap_tasks():
    print("heap tasks results: ")
    heap_single_task("heap_sources/1.in", "heap_sources/1.out")
    heap_single_task("heap_sources/2.in", "heap_sources/2.out")
    heap_single_task("heap_sources/3.in", "heap_sources/3.out")
    heap_single_task("heap_sources/4.in", "heap_sources/4.out")


def tree_after_task(filein, fileout):
    tree = Tree()
    fin = open(filein)
    fout = open(fileout)

    n = int(fin.readline())

    for i in range(n):
        val = int(fin.readline())
        result = fout.readline()

        node = tree.find(val)

        was_in_tree = "+"
        if node is None:
            was_in_tree = "-"
            tree.add(val)
            node = tree.find(val)

        min_after = next_value(tree.root, node)
        if min_after is None:
            min_after = "-"
        else:
            min_after = min_after.data

        if result != f"{was_in_tree} {min_after}\n":
            print("task on file ", filein, " Failed")
            return False

    print("task on file ", filein, " Succeed")
    return True


def tree_after_tasks():
    print("Tree after tasks: ")
    tree_after_task("tree_sources/1.in", "tree_sources/1.min-after.out")
    tree_after_task("tree_sources/2.in", "tree_sources/2.min-after.out")
    tree_after_task("tree_sources/3.in", "tree_sources/3.min-after.out")
    tree_after_task("tree_sources/4.in", "tree_sources/4.min-after.out")
    tree_after_task("tree_sources/5.in", "tree_sources/5.min-after.out")
    tree_after_task("tree_sources/6.in", "tree_sources/6.min-after.out")
    tree_after_task("tree_sources/7.in", "tree_sources/7.min-after.out")



if __name__ == '__main__':
    heap_tasks()
    tree_tasks()
    tree_after_tasks()

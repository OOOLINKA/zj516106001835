# encoding=utf-8

from random import randint
import copy

def graph_size():
    """
    生成 6-10 的随机数
    :return: int
    """
    return randint(6, 10)

def make_complete_graph(num_nodes):
    """
    生成有向图
    :param num_nodes 节点数
    :return dict
    """
    _graph = dict()
    for i in range(num_nodes):
        nodes = []
        for j in range(0, num_nodes):
            if i != j and randint(0, 4) == 1:  # 20%概率 随机设置相连的点
                nodes.append(j)
        if not nodes:  # 保证至少有一个点与其相连
            while True:
                rn = randint(0, num_nodes)
                if rn != i:
                    nodes.append(rn)
                    break
        _graph[i] = nodes
    return _graph


def Initial_node(path, x):  #寻找起始节点
    if len(path) == 0:
        return False
    if path[0] == x:
        return True
    return False


def Check_node(path, x):  #check路径中未再次出现起始节点并封装
    p = copy.deepcopy(path)  #把path的值赋给P
    if len(p) > 0:
        p.pop(0)
    while len(p) > 0:
        if p[0] == x:
            return True
        p.pop(0)
    return False


def Compare(path1, path2): #依次比较，看是否是其他路径的子路径。
    len1 = len(path1)
    len2 = len(path2)
    if len1 > len2:
        return False
    i = 0
    j = 0
    while i < len1 and j < len2:
        if path1[i] == path2[j]:
            i += 1
            j += 1
        else:
            j = j - i + 1
            i = 0
    if i >= len1:
        return True
    return False


def DFS(path, key):
    value = a[key]
    for t in value:
        while not Check_node(path, t):
            path.append(t)      #构造下次递归的父路径
            simple_path.append(copy.deepcopy(path))#向simple_path这个列表里面添加元素
            print(path)
            if not Initial_node(path, t):
                DFS(copy.deepcopy(path), t)
        path.pop()


def get_simple_path():
    """
    simple path
    """
    for key in a.keys():   #循环遍历a中的所有键(点)
        path = []
        path.append(key)
        simple_path.append(copy.deepcopy(path))
        print(path)
        DFS(copy.deepcopy(path), key)
        path.pop() #弹栈

def get_prime_path():
    """
    prime path
    """
    for path1 in simple_path:
        flag = False
        for path2 in simple_path:
            if path1 != path2:
                if Compare(path1, path2):
                    flag = True
                    break
        if flag is False:
            prime_path.append(copy.deepcopy(path1))


if __name__ == '__main__':
    size = graph_size()
    a = make_complete_graph(size)  # 随机生成有向图
    print(a)
    simple_path = []
    prime_path = []
    get_simple_path()  # 打印 simple path
    print("simple_path:%d" % (len(simple_path)))
    get_prime_path()
    print(prime_path)  # 打印 prime path
    print("prime_path:%d" % (len(prime_path)))

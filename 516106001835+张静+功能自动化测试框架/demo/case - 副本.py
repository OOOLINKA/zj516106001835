# encoding=utf-8
import copy
import os
import datetime


class PrimePath:
    def __init__(self):
        #字典
        self.graph = dict()
        #列表
        self.simplePath = []
        #列表
        self.primePath =[]

    #初始化
    def Init(self, fileName):
        path = os.path.dirname(__file__)
        filePath = path + "/" + fileName
        print filePath
        with open(filePath, 'r') as fr:
            i = 0
            for line in fr:
                if line[-1] == '\n':
                    line = line[:-1]
                if line.strip() != "": 
                    line = line.strip().replace(' ','')
                    if line != '-1':
                        data = map(int, line.split(','))
                        self.graph[i] = data
                    else:
                        self.graph[i] = []
                    i += 1
       
        return

    #判断初始节点
    def IsHead(self,path, x):
        if len(path) == 0:
            return False
        if path[0] == x:
            return True
        return False

    #判断路径中是否还有初始节点
    def Repetitive(self,path, x):
        p = copy.deepcopy(path)
        if len(p) > 0:
            p.pop(0)
        while len(p) > 0:
            if p[0] == x:
                return True
            p.pop(0)
        return False

    #深度遍历找出所有简单路径
    def DFS(self,path, key):
        value = self.graph[key]
        for t in value:
            while self.Repetitive(path,t) == False:
                path.append(t)
                self.simplePath.append(copy.deepcopy(path))
                # print path
                if self.IsHead(path,t) == False:
                    self.DFS(copy.deepcopy(path),t)
            while path[-1] != key:
                path.pop()
        path.pop()
        return

    #向simplePath变量中添加简单路径
    def GetSimplePath(self):
        # print 'hahah'
        for key in self.graph.keys():     
            path = []
            path.append(key)
            self.simplePath.append(copy.deepcopy(path))
            # print path
            self.DFS(copy.deepcopy(path),key)
            path.pop()       
        return

    #判断是否是其他路径的子路径
    def IsSub(self, path1, path2):
        len1 = len(path1)
        len2 = len(path2)
        if len1 > len2:
            return False
        i=0
        j=0
        while (i<len1 and j<len2):
            if path1[i] == path2[j]:
                i+=1
                j+=1
            else:
                j = j - i + 1
                i = 0
        if i >= len1:
            return True
        return False

    def GetPrimePath(self):
       
        self.primePath = copy.deepcopy(self.simplePath)
        i = 0
        while(i != len(self.primePath)):
            for j in range(0, len(self.primePath)):
                flag = False
                if i == j:
                    pass
                else:
                    if self.IsSub(self.primePath[i], self.primePath[j]) == True:
                        del(self.primePath[i])
                        flag = True
                        break
            if flag == False:
                i += 1
    def GetResult(self):
        self.Init('\case16.txt')
        self.GetSimplePath()
        print self.simplePath
        print("simplePath-size:%d"%(len(self.simplePath)))
        self.GetPrimePath()
        self.primePath = sorted(self.primePath, key=lambda a: (len(a), a))
        print self.primePath
        print("primePath-size:%d"%(len(self.primePath)))
        return self.primePath

if __name__ == "__main__":
    ob = PrimePath()
    print(ob.GetResult())







#
# Weighted Union Find Algorithm
#
# -*- coding: utf-8 -*-

class UnionFindWeighted:
    tree = []
    weight = []

    def __init__(self, N):
        for i in range(0, N):
            self.tree.insert(i,i)
            self.weight.insert(i,0)

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def root(self, node):
        while(node != self.tree[node]):
            parent = self.tree[node]
            #Path Compression
            self.tree[node] = self.tree[parent]
            node = self.tree[node]
        return node

    def union(self, p, q):
        qroot = self.root(q)
        proot = self.root(p)
        if self.weight[qroot] > self.weight[proot]:
            self.tree[proot] = qroot
            self.weight[qroot] += 1
        else:
            self.tree[qroot] = proot
            self.weight[proot] += 1

    def showTree(self):
        print self.tree


uf = UnionFindWeighted(10)
print "Initial Tree"
uf.showTree()
uf.union(4,3)
uf.union(3,8)
uf.union(6,5)
uf.union(9,4)
uf.union(2,1)
uf.union(5,0)
uf.union(7,2)
uf.union(6,1)
uf.union(7,3)
print "Final Tree"
uf.showTree()

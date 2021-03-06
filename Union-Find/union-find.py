#
# Union Find Algorithm
#
# -*- coding: utf-8 -*-

class UnionFind:
    tree = []

    def __init__(self, N):
        for i in range(0, N):
            self.tree.insert(i,i)

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def root(self, node):
        while(node != self.tree[node]):
            node = self.tree[node]
        return node

    def union(self, p, q):
        qroot = self.root(q)
        proot = self.root(p)
        self.tree[proot] = qroot

    def showTree(self):
        print self.tree


uf = UnionFind(10)
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


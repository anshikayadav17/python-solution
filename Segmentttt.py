class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, node * 2, start, mid)
            self.build(arr, node * 2 + 1, mid + 1, end)
            self.tree[node] = (
                self.tree[node * 2] +
                self.tree[node * 2 + 1]
            )

arr = [1, 2, 3, 4, 5]
st = SegmentTree(arr)
print(st.tree[:15])

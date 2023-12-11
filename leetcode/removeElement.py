class Solution:
    def removeElement(self, n: List[int], val: int) -> int:
        index = 0
        for i in range(len(n)):
            if n[i] != val:
                n[index] = n[i]
                index += 1
        return index
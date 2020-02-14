class Heap():
    def __init__(self,data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    # 대상 노드를 올려도 되는지 마는지 체크하는 함수(크기의 비교를 통해서 알아본다.)
    # 올려줘야 하는 경우를 생각한다.(1. root_node가 아닌경우, 2. 부모노드가 더 작은 경우)
    def Move_Up(self, inserted_idx):
        # 1.
        if inserted_idx <= 1:
            return False
        # 2.
        parent_idx = inserted_idx // 2
        if self.heap_array[parent_idx] < self.heap_array[inserted_idx]:
            return True
        else:
            return False

    # 1. Insert
    def Insert(self,data):
        # 1.1 아무것도 존재하지 않을 경우
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        # 1.2 존재하며, swap이 필요할 경우
        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1

        while self.Move_Up(inserted_idx):               # 올려야 되는게 참(True)이면 옮겨준다.
            parent_idx = inserted_idx // 2
            self.heap_array[parent_idx],self.heap_array[inserted_idx] = self.heap_array[inserted_idx],self.heap_array[parent_idx]
            inserted_idx = parent_idx

        return True

    # 2.Delete
    def Pop(self):
        if len(self.heap_array) <= 1:
            return False

        # 2.1 가장 먼저 마지막 노드를 root node로 들고온다.
        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        # 2.2 root node에 존재하는 녀석을 올바른 자리에 넣자.
        while True:
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # 2.2.1 옮기는 노드의 자식들이 둘다 존재하지 않을 경우(사실 왼쪽만 범위를 넘어가면 없는것이나 마찬가지)
            if len(self.heap_array) <= left_child_popped_idx:
                return False

            # 2.2.2 옮기는 노드의 자식들이 오른쪽만 존재하지 않는경우 -> 크기를 비교하고 왼쪽의 것과 바꿔준다.
            elif right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[left_child_popped_idx] >= self.heap_array[popped_idx]:
                    self.heap_array[left_child_popped_idx],self.heap_array[popped_idx] = self.heap_array[popped_idx],self.heap_array[left_child_popped_idx]
                    popped_idx = left_child_popped_idx

                else:
                    return False

            # 2.2.3 읾기는 노드의 자식들이 모두 존재하는 경우 -> 노드끼리 비교한다. -> 큰것과 popped_node를 바꿔준다.
            else:
                if self.heap_array[left_child_popped_idx] >= self.heap_array[right_child_popped_idx]:
                    if self.heap_array[left_child_popped_idx] >= self.heap_array[popped_idx]:
                        self.heap_array[left_child_popped_idx],self.heap_array[popped_idx] = self.heap_array[popped_idx],self.heap_array[left_child_popped_idx]
                    else:
                        return False

                else:
                    if self.heap_array[right_child_popped_idx] >= self.heap_array[popped_idx]:
                        self.heap_array[right_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[right_child_popped_idx]
                    else:
                        return False

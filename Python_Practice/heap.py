class Heap:
    # 힙은 list형태로 생성되기 때문에 Heap class가 호출되면 곧바로 List가 하나 추가된다.
    def __init__(self,data):
        self.heap_array = list()
        self.heap_array.append(None)
        # 가장 먼저 들어가는 data로 root설정
        self.heap_array.append(data)

    # 힙에 정보를 넣는 정의
    def insert(self,data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        self.heap_array.append(data)
        return True
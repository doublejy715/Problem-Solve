'''
힙은 기본적으로 list형식 구성이다.

기능으로는 1.init 2.insert 3.move up 4.delete 5. move_down

부모노드를 찾기 위해서는 자식노드의 % 2 를 통해 부모노드를 찾을 수 있다.
'''

class Heap:
    #1. init(생성 및 첫 데이터 지정)
    def __init__(self,data):
        self.heap_array = list() # 시작하자마자 리스트를 하나 만들어 준다.
        self.heap_array.append(None)
        self.heep_array.append(data)

    #3. move up(위로 올려야 하는지에 대한 점검을 하기 위한 구조이다.)
    def move_up(self,inserted_idx):
        #3.1 만약 넣는 곳이 1의 위치(정렬할 필요가 없을경우)
        if inserted_idx <= 1:
            return False

        #3.2 아니고 정렬해야 되는 경우
        if self.heap_array[inserted_idx] >= self.heap_array[inserted_idx/2]: # 부모노드보다 자식노드가 더 큰 값일 경우
            return True
        else:
            return False

    #2. insert
    def insert(self,data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
        # 삽입 할 떄 기본적으로 append를 통해서 넣기만 하면 된다. 어떻게 하면 항상 큰 숫자가 위로 나오게 넣을 수 있을까?
        # 순서는 일단 추가하고 다시 정리하는 것을 원칙으로 한다.
        self.heap_array.append(data)    # 먼저 데이터를 넣어준다. (넣어주는 위치는 가장 왼쪽 위치)
        insert_idx = len(self.heap_array) - 1

        # move_up 정의를 이용해서 자식 노드를 다시 올려야 하는지에 대한 여부를 결정지을 수 있다.
        # 만약 move_up의 결과가 True이면, 해당 내용을 반복하도록 한다.
        while self.move_up(self,insert_idx):
            parent_idx = insert_idx /2
            # 이것이 실제 교환하는 코드줄이다.
            self.heap_array[insert_idx],self.heap_array[parent_idx]=self.heap_array[parent_idx],self.heap_array[insert_idx]
            # 다시 부모의 노드를 넣는 노드로 지정해줘서 반복하게 한다.
            insert_idx = parent_idx

    # 5. move down(다시 정렬하기 위한 점검 구조)
    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        #5.1 자식들 중에서 왼쪽 자식도 존재하지 않는경우
        if len(self.heap_array) < left_child_popped_idx: # 길이를 측정해서 여부를 확인한다 append로 길이를 추가하기 때문에 값의 유무로 확인 불가능
            return False
        #5.2 왼쪽 자식은 있으나 오른쪽 자식이 없는 경우
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[right_child_popped_idx] > self.heap_array[popped_idx]:
                self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx],self.heap_array[popped_idx]
                popped_idx = left_child_popped_idx
                return True
            else:
                return False
        #5.3 자식들이 둘 다 존재할 때
        else:
            # 큰 숫자가 위로 올라가야 하기 때문에 왼쪽, 오른쪽의 숫자, popped_idx 를 비교 하고 큰 것을 바꿔준다.
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx],self.heap_array[left_child_popped_idx]=self.heap_array[left_child_popped_idx],self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
                    return True
                elif self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                    self.heap_array[popped_idx],self.heap_array[right_child_popped_idx]=self.heap_array[right_child_popped_idx],self.heap_array[popped_idx]
                    popped_idx = right_child_popped_idx
                    return True

    #4. delete(힙은 기본적으로 빠져나올 수 있는 구멍은 list의 첫뻔쨰 요소만 뺴내기가 가능하다.)
    def delete(self):
        #4.1 가장 위에 있는 것을 리턴한다.
        returned_data = self.heap_array[1]
        #4.2 가장 마지막의 것을 맨 앞으로 당겨온다.
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1
        #4.3 다시 정렬을 시도해야 한다.(move_down)
        while self.move_down(self,popped_idx):          # 다시 정렬을 시도할 때 자식의 여부에 따라서 정렬해 줘야한다.

        


# Implement the function RemoveMin for the min priority queue class.
# For a minimum priority queue, write the function for removing the minimum element present. Remove and return the minimum element.
# Note : main function is given for your reference which we are using internally to test the code.

class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority
        
class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
        
    def __percolateDown(self):
        i = 0
        parentIndex = i
        childIndex1 = 2*i+1
        childIndex2 = 2*i+2
        while childIndex1 <= self.getSize()-1:
            minIndex = parentIndex
            if self.pq[minIndex].priority > self.pq[childIndex1].priority:
                minIndex  = childIndex1
            if childIndex2<self.getSize() and self.pq[minIndex].priority > self.pq[childIndex2].priority:
                minIndex = childIndex2
            if minIndex == parentIndex:
                break
            self.pq[minIndex],self.pq[parentIndex] = self.pq[parentIndex],self.pq[minIndex]
            parentIndex = minIndex
            childIndex1 = 2*parentIndex+1
            childIndex2 = 2*parentIndex+2
        
        
        
    def insert(self,ele,priority):
        pqNode = PriorityQueueNode(ele,priority)
        self.pq.append(pqNode)
        self.__percolateUp()
        
    def removeMin(self):
        n = self.getSize()
        if n==0:
            return None
        ans = self.pq[0].ele
        self.pq[0] = self.pq[n-1]
        self.pq.pop()
        self.__percolateDown()
        return ans
        
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1
        
    
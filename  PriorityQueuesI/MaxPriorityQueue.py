# Implement the class for Max Priority Queue which includes following functions -
# 1. getSize -
# Return the size of priority queue i.e. number of elements present in the priority queue.
# 2. isEmpty -
# Check if priority queue is empty or not. Return true or false accordingly.
# 3. insert -
# Given an element, insert that element in the priority queue at the correct position.
# 4. getMax -
# Return the maximum element present in the priority queue without deleting. Return -Infinity if priority queue is empty.
# 5. removeMax -
# Delete and return the maximum element present in the priority queue. Return -Infinity if priority queue is empty.
# Note : main function is given for your reference which we are using internally to test the class.

class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.value = ele
        self.priority = priority
  
class PriorityQueue:
    def __init__(self):
        self.pq = []
        
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)
    
    def getMax(self):
        if self.isEmpty() == True:
            return float('inf')
        return self.pq[0].value
    
    def __percolateup(self):
        n = len(self.pq)
        childIndex = n-1
        parentIndex = (childIndex-1)//2
        while childIndex>0:
            if self.pq[childIndex].priority > self.pq[parentIndex].priority:
                self.pq[childIndex],self.pq[parentIndex] = self.pq[parentIndex],self.pq[childIndex]
                childIndex = parentIndex
                parentIndex = (childIndex-1)//2
            else:
                break
                
    def insert(self,ele,priority):
        node = PriorityQueueNode(ele,priority)
        self.pq.append(node)
        self.__percolateup()
        return
        
    def __percolateDown(self):
        parentIndex = 0
        leftchildIndex = 2*parentIndex +1
        rightchildIndex = 2*parentIndex+2
        while leftchildIndex<self.getSize():
            maxIndex = parentIndex
            if self.pq[parentIndex].priority < self.pq[leftchildIndex].priority:
                maxIndex = leftchildIndex
            if rightchildIndex <= self.getSize()-1 and self.pq[maxIndex].priority < self.pq[rightchildIndex].priority:
                maxIndex = rightchildIndex
            if maxIndex == parentIndex:
                break
            self.pq[maxIndex],self.pq[parentIndex] = self.pq[parentIndex],self.pq[maxIndex]
            parentIndex = maxIndex
            leftchildIndex = 2*parentIndex+1
            rightchildIndex = 2*parentIndex +2
        return 
        
    
        
    def removeMax(self):
        ans = self.pq[0].value
        self.pq[0],self.pq[self.getSize()-1] = self.pq[self.getSize()-1],self.pq[0]
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
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
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

front = 0
rear = 0
top = -1
stack = []
queue = []

# testCases = [
#     "5 ",
#     "ARRIVE 101",
#     "PICK ",
#     "DELIVER 101",
#     "ARRIVE 102",
#     "PICK "
# ]

# testCases = [
#     "6",
#     "ARRIVE 101",
#     "ARRIVE 102",
#     "PICK",
#     "PICK",
#     "DELIVER 101",
#     "DELIVER 102"
# ]


# testCases = [
#     "6",
#     "ARRIVE 10",
#     "PICK",
#     "DELIVER 99",
#     "ARRIVE 20",
#     "PICK",
#     "DELIVER 20"
# ]

# testCases = [
#     "10",
#     "ARRIVE 10",
#     "ARRIVE 20",
#     "ARRIVE 30",
#     "PICK",
#     "PICK",
#     "DELIVER 20",
#     "DELIVER 10",
#     "ARRIVE 40",
#     "PICK",
#     "DELIVER 30"
# ]

testCases = [
    "10",
    "ARRIVE 101",
    "ARRIVE 102",
    "ARRIVE 103",
    "PICK",
    "PICK",
    "DELIVER 101",
    "PICK",
    "DELIVER 102",
    "DELIVER 103",
    "ARRIVE 104",
    "PICK",
    "ARRIVE 105",
    "ARRIVE 106",
    "PICK",
    "PICK",
    "DELIVER 105",
    "ARRIVE 107",
    "DELIVER 107",
    "PICK",
    "DELIVER 105",
    "DELIVER 106"
]

n = testCases[0]

success = 0
temporal_removal = 0
failed = 0

def binarySearch(stack, key, low, high):
    if high >= low:
        mid = (high + low) // 2
        if stack[mid] == key:
            return mid
        elif stack[mid] > key:
            return  binarySearch(stack, key, low, mid - 1)
        else:
            return binarySearch(stack, key, mid + 1, high)
    else:
        return -1

def removeElement(idx, stack):
    global top
    for i in range(idx,top):   
        stack[i] = stack[i+1]
    top -=1


for i in range(1,len(testCases)):
   
    if "ARRIVE" in testCases[i]:
        [command, id] = testCases[i].split()
        queue.append(id)
        rear +=1
    elif "PICK" in testCases[i]:
        stack.append(queue[front])
        front +=1
        top +=1

    elif "DELIVER" in testCases[i]:
        [command, id] = testCases[i].split()
        if stack[top] == id:
            stack.pop()
            top -=1
            success +=1
        else:
            idx = binarySearch(stack, id, 0, top)
            if idx != -1:
                removeElement(idx, stack)
                temporal_removal += 1
                success +=1
            else:
                failed +=1

print(success ,"", temporal_removal, "", failed)
import random

maxLimit = random.randint(10, 30)
sampleList = [random.randint(1, 99) for _ in range(maxLimit)]
seachFor = int(input('Enter a number to search : '))

sampleList.sort()
start = 0
middle = 0
end = len(sampleList)
steps = 0
found = False

while start <= end:
    middle = (start + end) // 2
    steps += 1

    if (seachFor == sampleList[middle]):
        found = True
        break

    if (seachFor > sampleList[middle]):
        start = middle + 1

    if (seachFor < sampleList[middle]):
        end = middle - 1

print()
if found:
    print(f'Found the number at {middle} postion in {steps} steps.')
    print(sampleList)
else:
    print('Number not present!')
    print(sampleList)

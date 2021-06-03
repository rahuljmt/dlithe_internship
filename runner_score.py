#program for runner score
n = int(input('enter number of scores : '))
arr = map(int, input('enter scores: ').split())
arr = list(set(list(arr)))
ar = len(arr)
arr = sorted(arr)
print(arr[ar-2])
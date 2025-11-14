inputs = list(map(int, input().split()))
for i in range(len(inputs)):
    hun = inputs[i]%10 * 100
    ten = inputs[i]//10%10 * 10
    one = inputs[i]//100 * 1
    inputs[i] = hun + ten + one
print(max(inputs))
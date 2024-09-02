
lengths = [30, 55, 11]

costPerCut = 1

salePrice = 10 

totalCuts = 0

upto = min(lengths)

totalProfit = 0

for i in range(1,upto+1):

    totalUniformRods = 0

    for j in lengths:

        totalUniformRods += j//i

        if j%i ==0 and j/i > 1:

            totalCuts = totalUniformRods - 1

        else:

            totalCuts = totalUniformRods

    tempProfit = (totalUniformRods * i * salePrice)- (totalCuts * costPerCut)

    if tempProfit>totalProfit:

        totalProfit = tempProfit

print(totalProfit)
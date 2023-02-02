import math
oldRegimeIncomeTaxSlabs = [[0, 2.5], [5, 2.5], [20, 5], [30, math.inf]]
newRegimeIncomeTaxSlabs = [[0, 3], [5, 3], [10, 3], [15, 3], [20, 3],[30,  math.inf]]
standard_ded = 50000
#nps = 0
def taxCalculation(totalSalary, regime, totalExemption):
    if regime == 'old':
        regimeSlabs = oldRegimeIncomeTaxSlabs
    else:
        regimeSlabs = newRegimeIncomeTaxSlabs
        totalExemption = 0
    taxableIncome = totalSalary - totalExemption
    tax = 0
    index = 0
    taxableIncomeAux = taxableIncome
    while(index < len(regimeSlabs) and taxableIncomeAux > 0):
        if taxableIncomeAux >= regimeSlabs[index][1] * 100000:
            tax = tax + regimeSlabs[index][1] * 100000 * regimeSlabs[index][0] * 0.01
        else:
            tax = tax + taxableIncomeAux * \
                           regimeSlabs[index][0] * 0.01
        taxableIncomeAux = taxableIncomeAux - regimeSlabs[index][1] * 100000
        index += 1
    return tax

income_min = 800000
income_max = 2500000
exemption_min = 0
exemption_max = 500000
income_temp = income_min
exemption_temp = 0
x = 0
income_exempt = {}
while income_temp < income_max:
    exemption_temp = 0
    newTax = taxCalculation(income_temp, 'new', standard_ded)
    while exemption_temp < exemption_max and exemption_temp < income_temp:
        exemption_temp += 5000
        oldTax = taxCalculation(income_temp, 'old', (exemption_temp + standard_ded))
        print(income_temp, (exemption_temp + standard_ded), newTax, oldTax)
        if(oldTax <= newTax):
            if income_temp not in income_exempt:
                income_exempt[income_temp] = (exemption_temp + standard_ded)
    income_temp += 100000

print(income_exempt)
for key, value in income_exempt.items():
    print(key, value)

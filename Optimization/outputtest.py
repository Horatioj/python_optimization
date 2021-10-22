income = eval(input("please enter your salary:   $"))

while income > 0:

    block20k = 20000
    block20k = 20000
    block40k = 40000
    block80k = 80000
    block120k = 120000

    level1 = 144000
    level2 = level1 + block20k
    level3 = level2 + block20k
    level4 = level3 + block40k
    level5 = level4 + block80k
    level6 = level5 + block120k

    if income > level6:
        tax = block20k * 0.07 + block20k * 0.08 + block40k * 0.09 + block80k * 0.1 + block120k * 0.11 + (
                    income - level6) * 0.12
    elif income > level5:
        tax = block20k * 0.07 + block20k * 0.08 + block40k * 0.09 + block80k * 0.10 + (income - level5) * 0.11
    elif income > level4:
        tax = block20k * 0.07 + block20k * 0.08 + block40k * 0.09 + (income - level4) * 0.10
    elif income > level3:
        tax = block20k * 0.07 + block20k * 0.08 + (income - level3) * 0.09
    elif income > level2:
        tax = block20k * 0.07 + (income - level2) * 0.08
    elif income > level1:
        tax = (income - level1) * 0.07
    else:
        tax = 0
    print("your income：{0:,.2f} need to pay the tax {1:,.2f}".format(income, tax))

    income = eval(input("please enter your salary:   $"))

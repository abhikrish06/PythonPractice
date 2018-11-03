# print(round(2.375, 2))
# print(round(2.475, 2))
# print(round(2.575, 2))
# print(round(2.675, 2))
# print(round(2.775, 2))
# print()
#
# print(format(2.675, '.2f'))
# print(format(2.775, '.2f'))

#from decimal import Decimal, ROUND_HALF_UP
# import decimal
#
# val1 = 2.375
# val2 = 2.475
# val3 = 2.575
# val4 = 2.675
# val5 = 2.775
# val6 = 2.875
# val7 = 2.975
# # print(Decimal(val1.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
# print(decimal.Decimal('2.375').quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP))
# print(decimal.Decimal('2.475').quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP))
# print(decimal.Decimal('2.575').quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP))
# print()
# print(decimal.Decimal('2.675').quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP))
# print(decimal.Decimal('2.3447').quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP))
# print()
# print(decimal.Decimal(val5).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP))
# print(decimal.Decimal(val6).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP))
# print(decimal.Decimal(val7).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP))
# print()
# print(decimal.Decimal(100 / 10).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP))
#
# print(10/2)


arr = [True, True, True, True]
print(arr)
arr[0] = False

print(arr)
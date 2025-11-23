months = ['jan','feb','mar','apr','may','jun']

months.append('jul')
print(months)

months.remove('jan')
print(months)

months.pop()
print(months)
  
for m in months:
     print(f"{m} ,2025")
     
full_name = 'James Francis M. Tiongco'

namee = list(full_name)

namee.reverse()
print(namee)
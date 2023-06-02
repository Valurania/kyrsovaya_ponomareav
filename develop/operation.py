import json
import functoins as func

with open("../operations.json", encoding="utf-8") as f:
    operations_data = json.load(f)

operations_data_new = func.operatoin_data_filer(operations_data)
operations_data_new.sort(key=lambda x: x['date'], reverse=True)

count_record = 0
for i in operations_data_new:
    if i['state'] == 'EXECUTED':
        print(func.operations_output(i))
        count_record += 1
        if count_record == 5:
            break
    print()

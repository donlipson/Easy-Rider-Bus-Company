import json
import re
from collections import Counter

json_file = input()

stations = json.loads(json_file)

error_dict = {
    "stop_name": 0,
    "stop_type": 0,
    "a_time": 0}
bus_dict = {}

for item in stations:
    bus_id_dict = None
    for key, value in item.items():

        if key == "bus_id":
            if type(value) != int:
                error_dict[key] += 1
            elif str(value) not in bus_dict:
                bus_dict[str(value)] = {'stop_type': [], 'stop_name': []}
            bus_id_dict = value
        elif key == "stop_id":
            if type(value) != int:
                error_dict[key] += 1
            # elif value not in bus_dict[str(bus_id_dict)]:
            # bus_dict[str(bus_id_dict)].append(value)
        elif key == "stop_name":
            if type(value) != str or len(value) == 0:
                error_dict[key] += 1
            elif bool(re.match(r"[A-Z]{1}.*(Avenue|Street|Road|Boulevard)$", value)) is False:
                error_dict[key] += 1
            else:
                bus_dict[str(bus_id_dict)][key].append(value)
        elif key == "next_stop":
            if type(value) != int:
                error_dict[key] += 1
        elif key == "stop_type":
            if type(value) != str or len(value) > 1:
                error_dict[key] += 1
            elif bool(re.match(r"[SOF]|$", value)) is False:
                error_dict[key] += 1
            else:
                bus_dict[str(bus_id_dict)][key].append(value)
        elif key == "a_time":
            if type(value) != str or len(value) == 0 or len(value) > 5:
                error_dict[key] += 1
            elif bool(re.match(r"[0-2][0-9]:[0-5][0-9]$", value)) is False:
                error_dict[key] += 1

# count_errors = sum(int(value) for value in error_dict.values())

# print('Format validation:', count_errors, 'errors')
# for key, value in error_dict.items():
# if value > 0:
# print(key, ': ', value)

# print('Line names and number of stops:')


start_stop = []
transfer = []
finish_stop = []
for key1, value1 in bus_dict.items():
    for key2, value2 in value1.items():
        if key2 == 'stop_type':
            if 'S' not in value2:
                print('There is no start or end stop for the line:', key1)
                break
            elif 'F' not in value2:
                print('There is no start or end stop for the line:', key1)
                break

    for stop_type, stop_name in zip(value1['stop_type'], value1['stop_name']):
        if stop_type == 'S':
            if stop_name not in start_stop:
                start_stop.append(stop_name)
        elif stop_type == "F":  # or stop_type == ''
            if stop_name not in finish_stop:
                finish_stop.append(stop_name)
        # elif stop_type == 'O'  or stop_type == '':
        # if stop_name not in transfer:
        transfer.append(stop_name)

transfer = Counter(transfer)
transfer_count = []
for key_t, value_t in transfer.items():
    if value_t >= 2:
        transfer_count.append(key_t)

print('Start stops: {} {}'.format(len(start_stop), sorted(start_stop)))
print('Transfer stops: {} {}'.format(len(transfer_count), sorted(transfer_count)))
print('Finish stops: {} {}'.format(len(finish_stop), sorted(finish_stop)))

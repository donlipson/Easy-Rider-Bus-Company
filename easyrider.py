import json
import re

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
                bus_dict[str(value)] = []
            bus_id_dict = value
        elif key == "stop_id":
            if type(value) != int:
                error_dict[key] += 1
            elif value not in bus_dict[str(bus_id_dict)]:
               bus_dict[str(bus_id_dict)].append(value)
        elif key == "stop_name":
            if type(value) != str or len(value) == 0:
                error_dict[key] += 1
            elif bool(re.match(r"[A-Z]{1}.*(Avenue|Street|Road|Boulevard)$", value)) is False:
                error_dict[key] += 1
        elif key == "next_stop":
            if type(value) != int:
                error_dict[key] += 1
        elif key == "stop_type":
            if type(value) != str or len(value) > 1:
                error_dict[key] += 1
            elif bool(re.match(r"[SOF]|$", value)) is False:
                error_dict[key] += 1
        elif key == "a_time":
            if type(value) != str or len(value) == 0 or len(value) > 5:
                error_dict[key] += 1
            elif bool(re.match(r"[0-2][0-9]:[0-5][0-9]$", value)) is False:
                error_dict[key] += 1

#count_errors = sum(int(value) for value in error_dict.values())

#print('Format validation:', count_errors, 'errors')
#for key, value in error_dict.items():
    #if value > 0:
        #print(key, ': ', value)

print('Line names and number of stops:')
for key, value in bus_dict.items():
    print("bus_id: {}, stops: {}".format(key,len(value)))

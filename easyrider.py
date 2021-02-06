import json

json_file = input()

stations = json.loads(json_file)
error_dict = {"bus_id": 0,
              "stop_id": 0,
              "stop_name": 0,
              "next_stop": 0,
              "stop_type": 0,
              "a_time": 0}

for item in stations:
    for key, value in item.items():
        if key == "bus_id":
            if type(value) != int:
                error_dict[key] += 1
        elif key == "stop_id":
            if type(value) != int:
                error_dict[key] += 1
        elif key == "stop_name":
            if type(value) != str or len(value) == 0:
                error_dict[key] += 1
        elif key == "next_stop":
            if type(value) != int:
                error_dict[key] += 1
        elif key == "stop_type":
            if type(value) != str or len(value) > 1:
                error_dict[key] += 1
        elif key == "a_time":
            if type(value) != str or len(value) == 0:
                error_dict[key] += 1

count_errors = sum(int(value) for value in error_dict.values())

print('Type and required field validation:', count_errors)
for key, value in error_dict.items():
    print(key, ': ', value)

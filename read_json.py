import json
f_w = open('temp1.txt', 'w')
for line in open('data\data_2017-04-24.json'):
    data = json.loads(line)
    f_w.write(data['time'] + data['state'] + ' ' + data['name'] + '\n')
f_w.close()

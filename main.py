import json


def write_json(datause, filename):
    with open(filename, 'w') as f:
        json.dump(datause, f, indent=4)


#for item in data['iot_stats']:
 #   print(item['destination_services']['connection_count'])
def creat_new_json(data,filename):
    count=0
    numcount=0
    for item in data['iot_stats']:
        numcount+=1
        num=len(item['destination_services'])
        for use in range(num):
            count=0
            servicename=item['destination_services'][use].get('service_name')
            for i in range(num):
                if(item['destination_services'][i].get('service_name')==servicename):
                    count+=item['destination_services'][i].get('connection_count')
        if(count>10):
            print(f'{servicename} {count}')
            datause = {
                "_id": item['device'].get('ID'),
                "Type": item['device'].get('type'),
                "Brand": item['device'].get('brand'),
                "toInternetPolicy": {
                    "rules": [
                        {
                            "_id": data['gw_hash_id'],
                            "name": data['smp-domain'],
                            "description": data['gw_identifier'],
                            "destination": [
                                {
                                    "type": "DOMAIN",
                                    "value": data['smp-domain']
                                }
                            ],
                            "services": [
                                {
                                    "type": "SERVICE",
                                    "value": servicename
                                }
                            ]
                        }
                    ]
                }
            }
            print(numcount)
            write_json(datause, f'{"new_json"} {filename}{numcount}')


        #print(item['destination_services'][i].get('connection_count'))






 # for item in data():
 #   if int(data['iot_stats']['connection_count']) > 10:
  #      print(data['iot_stats']['device'])

with open("furst.json", "r") as f:
    data = json.load(f)
    creat_new_json(data, "furst")
with open("FAM-SouthHarrow-Njk4MmM5MGEyZWJjOTZmNjMxMzVlYzc1YmUwMjIyMDc=.json", "r") as f:
    data1= json.load(f)
    creat_new_json(data1,"FAM-SouthHarrow-Njk4MmM5MGEyZWJjOTZmNjMxMzVlYzc1YmUwMjIyMDc=")
with open("HAK-Workinton-ODIwZDk2OTYwYTUwNmRmY2I2NGQxNWQ0NDA2NTNmOTk=.json", "r") as f:
    data2 = json.load(f)
    creat_new_json(data2, "HAK-Workinton-ODIwZDk2OTYwYTUwNmRmY2I2NGQxNWQ0NDA2NTNmOTk=")
with open("SMW-Immingham-MDA0MzBlZWUzYmZiZGJkYjYzYWNmMjE5ZTU0NmM2ZGY=.json", "r") as f:
    data3 = json.load(f)
    creat_new_json(data3, "SMW-Immingham-MDA0MzBlZWUzYmZiZGJkYjYzYWNmMjE5ZTU0NmM2ZGY=")
with open("SpecialSecGateway-Mzc4MjIxMDE4MjgwYmVmZjEyYTU3MzEzN2I3ZmE2NDY=.json", "r") as f:
    data4 = json.load(f)
    creat_new_json(data4, "SpecialSecGateway-Mzc4MjIxMDE4MjgwYmVmZjEyYTU3MzEzN2I3ZmE2NDY=")
with open("Zjg5MmJmODFlN2Q3NjIwNmIwZjI2ZDczNGZiYjIwOGQ=.json", "r") as f:
    data5 = json.load(f)
    creat_new_json(data5, "Zjg5MmJmODFlN2Q3NjIwNmIwZjI2ZDczNGZiYjIwOGQ=")
with open("ZTYwNzIwMDAzNDNlOGIxZmFiNDcyYzY2NzM4ZWU4YzA=.json", "r") as f:
    data6 = json.load(f)
    creat_new_json(data6, "ZTYwNzIwMDAzNDNlOGIxZmFiNDcyYzY2NzM4ZWU4YzA=")

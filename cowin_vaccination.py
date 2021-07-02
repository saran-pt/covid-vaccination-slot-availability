from urllib.request import urlopen
import json


print('Type the pincode : ', end='')
pincode = int(input())
print('Type the Date (dd-mm-yyyy): ', end='')
date = input()
print('\n', "-"*50)


print("Start Searching for COVID vaccine solts...!")
print("-"*50, '\n')

url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}"
clienturl = urlopen(url)

json_data = json.loads(clienturl.read())
# print(json.dumps(json_data, indent=4))
for i in range(len(json_data["sessions"])):

    center = json_data["sessions"][i]["center_id"]
    hospital = json_data["sessions"][i]["name"]
    location = json_data["sessions"][i]["address"]
    area = json_data["sessions"][i]["block_name"]
    price = json_data["sessions"][i]["fee"]
    does1 = json_data["sessions"][i]["available_capacity_dose1"]
    does2 = json_data["sessions"][i]["available_capacity_dose2"]
    vaccine = json_data["sessions"][i]["vaccine"]
    slots = json_data["sessions"][i]["slots"]

    print(f'Center ID : {center}')
    print(f'Name of the Hospital : {hospital}')
    print(f'Address : {location}')
    print(f'Name of the Block : {area}')
    print(f'Price of the Vaccine : {price}')
    print(f'Availability of First does : {does1}')
    print(f'Availability of Second does : {does2}')
    print(f'Vaccine Type : {vaccine}')
    print(f'Slots : {slots}', '\n\n')


# coverts byte string into json value
# data = (clienturl.read()).decode('UTF-8')


print("The Search is Finished !")
clienturl.close()
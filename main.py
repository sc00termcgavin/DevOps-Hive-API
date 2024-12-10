import requests
from fastapi import FastAPI
from datetime import datetime, timezone


app = FastAPI()


# Version Endpoint
@app.get("/version")
async def get_version():
    version = version = "v0.0.1"
    return {"version": version}


# format: https://api.opensensemap.org/boxes/:senseBoxId?format=:format

# Temperature Endpoint
@app.get("/temperature")
def get_temp():
    url1= 'https://api.opensensemap.org/boxes/6351780cc18329001ba8d4a3?format=json'
    url2= 'https://api.opensensemap.org/boxes/63ac947f1aaa3a001b8a34bd?format=json'
    url3= 'https://api.opensensemap.org/boxes/62abdbfbb91502001b7c05a8?format=json'
    
    # get request to fetch data from the API
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)

    now = datetime.now(timezone.utc)

    #print(response.status_code)
    #print(response.json())

    # 1
    # access sensors array, 2nd index, 3rd object 
    temp1 = float(response1.json()['sensors'][2]['lastMeasurement']['value'])
    time1 = response1.json()['sensors'][2]['lastMeasurement']['createdAt']

    # Parse the createdAt timestamp from the API response
    timestamp1 = datetime.fromisoformat(time1.replace("Z", "+00:00"))
    # Calculate the difference between the current time and the createdAt time
    time_difference1 = now - timestamp1
    # Check if the data is older than 1 hour (3600 seconds)
    if time_difference1.total_seconds() > 3600:  
        print("The data is older than 1 hour.")
    else:
        print(time1,"Data is within the last hour.")

    print(temp1)

    # 2

    temp2 = float(response2.json()['sensors'][0]['lastMeasurement']['value'])
    time2 = response2.json()['sensors'][0]['lastMeasurement']['createdAt']

    timestamp2 = datetime.fromisoformat(time1.replace("Z", "+00:00"))
    time_difference2 = now - timestamp2
    if time_difference2.total_seconds() > 3600:  
        print("The data is older than 1 hour.")
    else:
        print(time2,"Data is within the last hour.")

    print(temp2)

    # 3
    temp3 = float(response3.json()['sensors'][2]['lastMeasurement']['value'])
    time3 = response3.json()['sensors'][2]['lastMeasurement']['createdAt']

    timestamp3 = datetime.fromisoformat(time1.replace("Z", "+00:00"))
    time_difference3 = now - timestamp3
    if time_difference3.total_seconds() > 3600:  
        print("The data is older than 1 hour.")
    else:
        print(time3,"Data is within the last hour.")

    print(temp3)


    print("------")
    temp_total = round((float(temp1) + float(temp2) + float(temp3) ) / 3, 2)

    print(temp_total)
    return(temp_total)


# Run the function
if __name__ == '__main__':
    get_temp()
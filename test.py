import requests

URL         = "http://127.0.0.1:5000/"

# How to get API
response    = requests.get(URL + "RestFull")

# How to get API (Storing in Memory)
response    = requests.put(URL + "RestFull/person2")

# How to post API
response    = requests.post(URL + "RestFull/Bot/Get")

# How to put API (Request Argument Parse)
# response    = requests.put(URL + "RestFull/1", {"like":100})

# How to put and get API (Sending status code)
# response    = requests.put(URL + "RestFull/1", {"like":100, "name":"phirakbot", "view":1000000})

response    = requests.get(URL + "RestFull/1")

# How to put, delete and get API
data = [
        {"like":700, "name":"Learn python", "view":4000000},
        {"like":60, "name":"Learn C#", "view":500000},
        {"like":420, "name":"Learn Rest Full API", "view":2900000}
]

for row in range(len(data)):
    # print(data[row], "Data roe")
    response    = requests.put(URL + "RestFull/" + str(row), data[row])
    print(response.json())
input()
response    = requests.delete(URL + "RestFull/0")
print("response delete", response)
input()
response    = requests.get(URL + "RestFull/2")
print("response get", response.json())
import requests
import asyncio
import json

def get_json(response):
    # cериализация
    return json.loads(response.text)
def sinc()->None:
    response = get_json(requests.get('http://127.0.0.1:5000/api1'))
    print(response)  # json
    response = requests.post('http://127.0.0.1:5000/api1')
    print(response.text)  # only get
    response = get_json(requests.post('http://127.0.0.1:5000/api2'))
    print(response)  # json
    response = requests.get('http://127.0.0.1:5000/api2')
    print(response.text)  # only post

async def taskGet()->None:
    while True:
        api1 = get_json(requests.get('http://127.0.0.1:5000/api1'))
        await asyncio.sleep(2)
        print(api1)

async def taskPost()->None:
    while True:
        api2 = get_json(requests.post('http://127.0.0.1:5000/api2', data={'request':'hello from cycle2'}))
        await asyncio.sleep(3)
        print(api2)
        
async def main()->None:
    get = asyncio.create_task(taskGet())
    post = asyncio.create_task(taskPost())
    await get
    await post

if __name__ == '__main__':
    sinc()
    asyncio.run(main())
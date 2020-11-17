import requests
import pyglet
request = requests.get('https://cs1-41v4.vkuseraudio.net/p3/d709c7bcea061a.mp3?extra=QxgIdd5SLh0KJLiZgerrDduLkStl7hZ6MlXanCaOMYek-eRfHYf1u9o_u8O3bmaUuekCj7K6Dr69AGD7vkHlyhqMq98AJiIvc7gvyIZSixxITj1pWS0y5oGimEttkMcLuuwNkLij_oHfNsM')
with open('foo.mp3', 'wb') as file:
    file.write(request.content)
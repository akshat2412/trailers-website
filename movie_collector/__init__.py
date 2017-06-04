import json
import requests

api_key="768929d95c69e980195111082927dda2"

url="https://api.themoviedb.org/3/discover/movie?api_key=<<api_key>>&language=en-US&sort_by=vote_count.desc&include_adult=false&include_video=true&page=1"
video_url="http://api.themoviedb.org/3/movie/{id}/videos?api_key=###"
starting_poster_url="http://image.tmdb.org/t/p/w500"
youtube_url="https://www.youtube.com/watch?v="

url=url.replace("<<api_key>>",api_key)
video_url=video_url.replace("###",api_key)

connection=requests.get(url)
data=connection.json()
# print(json.dumps(data, indent=4))
json_list=list()
for i in range(1,3):
    new_url=url[:-1]
    if new_url.endswith("="):
        new_url=new_url+str(i)
    else:
        new_url=new_url[:-1]
        new_url=new_url+str(i)
    connection = requests.get(new_url)
    data = connection.json()
    json_list.append(data)


poster_list=list()
name_list=list()
url_list=list()
def return_info():
    global name_list
    for data in json_list:
        for name in data['results']:
            name_list.append(name['title'])

    global poster_list
    for data in json_list:
        for name in data['results']:
            poster_list.append(starting_poster_url+name['poster_path'])

    global url_list
    for data in json_list:
        for name in data['results']:
            id=str(name['id'])
            new_video_url = video_url.replace("{id}", id)
            connection2 = requests.get(new_video_url)
            data2 = connection2.json()
            try:
                trailer_url=youtube_url+data2['results'][0]['key']
            except:
                index=len(url_list)-1
                del poster_list[index]
                del name_list[index]
                continue
            trailer_url=trailer_url.replace("watch?v=","embed/")
            url_list.append(trailer_url)

    return name_list,poster_list,url_list

# return_url_data()
import json , requests , rstr
import time

headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjY0NTQ5ZjRiMDc3MWFhYzA5MzdmMjE2ZDIxZWVkODdkNjQ4MjFhZjJlYTZhZGU5NTliYzBlYTc2MTY2MzZiNTAyYmU0OTE2YTU5NDc4NGVlIn0.eyJhdWQiOiIxODIyMjQ5MzguZWVkZTdmMTk1N2FhYTA2ZDQwMzY1NjE1NjMxOTMyMzZkNDU3NWQ3YzA5MDM2NTUwOGZjZTE5NzU2YzI0ZDAzOSIsImp0aSI6IjY0NTQ5ZjRiMDc3MWFhYzA5MzdmMjE2ZDIxZWVkODdkNjQ4MjFhZjJlYTZhZGU5NTliYzBlYTc2MTY2MzZiNTAyYmU0OTE2YTU5NDc4NGVlIiwiaWF0IjoxNTMwNTk4Mjk1LCJuYmYiOjE1MzA1OTgyOTUsImV4cCI6MTU0NjE1MDI5NSwic3ViIjoiNzg4NjU1NDgwNjgzODkyNzM2Iiwic2NvcGVzIjpbInJlYWQiXX0.FUo0Gr-8-KmI0JEHuKIWPdw80kHb8Lb6awIc910IJQQoolVKYlTYjq4zkx0DMQrD1uCDk2OMVYWpi6jtRrde1qMEx47JjOtXhrBwkRowU80Rio_fIJpWprCO3Hirf49-PGPQOAUp9SrOwZk-CrEdrAkEA4fl41x8JBpC4mYbGlNfUb525f69CFS1p2WBvPWBBcznHqU-qkS0CuSYiY2XylPkqgjAjzyqMrnpQ2C8MLi94QBve0FvS43Gw-MLwkdsjSAEXw7_4e4YCY67UAbyUGmfVcC9NKzjyQ25aL-AwJrJ5MQbbdl76HmY5qG594EjWvKQ0ZS7oOFoJ2_wBNOOIg"}

r=requests.get('https://apiv2.twitcasting.tv/internships/2018/games?level=3',headers=headers)

print(r.text)

data = r.json()

print(data['id'])

post_url = 'https://apiv2.twitcasting.tv/internships/2018/games/' + data['id']

headers2 = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjY0NTQ5ZjRiMDc3MWFhYzA5MzdmMjE2ZDIxZWVkODdkNjQ4MjFhZjJlYTZhZGU5NTliYzBlYTc2MTY2MzZiNTAyYmU0OTE2YTU5NDc4NGVlIn0.eyJhdWQiOiIxODIyMjQ5MzguZWVkZTdmMTk1N2FhYTA2ZDQwMzY1NjE1NjMxOTMyMzZkNDU3NWQ3YzA5MDM2NTUwOGZjZTE5NzU2YzI0ZDAzOSIsImp0aSI6IjY0NTQ5ZjRiMDc3MWFhYzA5MzdmMjE2ZDIxZWVkODdkNjQ4MjFhZjJlYTZhZGU5NTliYzBlYTc2MTY2MzZiNTAyYmU0OTE2YTU5NDc4NGVlIiwiaWF0IjoxNTMwNTk4Mjk1LCJuYmYiOjE1MzA1OTgyOTUsImV4cCI6MTU0NjE1MDI5NSwic3ViIjoiNzg4NjU1NDgwNjgzODkyNzM2Iiwic2NvcGVzIjpbInJlYWQiXX0.FUo0Gr-8-KmI0JEHuKIWPdw80kHb8Lb6awIc910IJQQoolVKYlTYjq4zkx0DMQrD1uCDk2OMVYWpi6jtRrde1qMEx47JjOtXhrBwkRowU80Rio_fIJpWprCO3Hirf49-PGPQOAUp9SrOwZk-CrEdrAkEA4fl41x8JBpC4mYbGlNfUb525f69CFS1p2WBvPWBBcznHqU-qkS0CuSYiY2XylPkqgjAjzyqMrnpQ2C8MLi94QBve0FvS43Gw-MLwkdsjSAEXw7_4e4YCY67UAbyUGmfVcC9NKzjyQ25aL-AwJrJ5MQbbdl76HmY5qG594EjWvKQ0ZS7oOFoJ2_wBNOOIg", 'Content-Type': 'application/json'}

status = False
start = time.time()
while status==False:
    random_num = rstr.xeger(r'[0-9]{3}')
    payload = {'answer': random_num}
    elpased_time = time.time() - start
    print(elpased_time)
    r2 = requests.post(post_url, data = json.dumps(payload), headers=headers2)
    print(r2.json())
    if (int(elpased_time) == 20) or (r2.status_code == 404):
        status = True




import requests
import json

import os
import subprocess
playlist = []
data_hash_strt = 'act=reload_audio&al=1&ids='
data_hash = ''
data_id = 'access_hash=&act=load_section&al=1&claim=0&offset=30&owner_id=138308279&playlist_id=-1&type=playlist'
headers_id = {'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '100',
            'Cookie': 'remixlang=0; remixstid=0_a4ebb2ebb6b918adc5; remixscreen_depth=24; remixseenads=1; remixflash=30.0.0; remixab=1; remixdt=18000; remixrefkey=9b7405eb5ffff4d992; remixgp=a2825e6fc0837296340bee8f460125b5; remixsid=fe4f8bb6e5c8bbaccc04fd844bae56107cd2e8a65df455787490f; tmr_detect=1%7C1533036055460; remixcurr_audio=138308279_456239033',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'}
datasd = 'act=reload_audio&al=1&ids=138308279_456239086%2C138308279_456239033%2C138308279_442869086%2C138308279_396007684%2C138308279_456239048%2C138308279_456239086'
headers =  {'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '100',
            'Cookie': 'remixlang=0; remixstid=0_a4ebb2ebb6b918adc5; remixscreen_depth=24; remixseenads=1; remixflash=30.0.0; remixab=1; remixdt=18000; remixsid=dfea9666fc595629b0c0879decc1c133ea56c93f6ad68c8b48c38; remixrefkey=9b7405eb5ffff4d992; remixgp=a2825e6fc0837296340bee8f460125b5; tmr_detect=1%7C1532972554193; remixcurr_audio=138308279_456239147',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'}


# r = requests.post(url="https://vk.com/al_audio.php", data=json.dumps(payload),headers=headers)
id_response = requests.post(url="https://vk.com/al_audio.php", data=data_id,headers=headers_id)

# print(r.text)


enter_id = id_response.text.find('<!json>')
out_id = id_response.text.find('<!><div class="audio_pl')
json_text_id = id_response.text[enter_id+7:out_id]
# print(json_text)
parsed_line_id = json.loads(json_text_id)

for track in parsed_line_id['list']:
	playlist.append([track[3],track[4],track[15]['content_id']])
data_hash = data_hash_strt + playlist[0][2] + '%2C' + playlist[1][2] + '%2C' + playlist[2][2] + '%2C' + playlist[3][2] + '%2C' + playlist[4][2]
hash_response = requests.post(url="https://vk.com/al_audio.php", data=data_hash, headers=headers_id)
# print(hash_response.text)

enter_hash = hash_response.text.find('<!json>')
out_hash = hash_response.text.find('<!><!bool><!>')
json_text_hash = hash_response.text[enter_hash+7:out_hash]
parsed_line_hash = json.loads(json_text_hash)
for i in range(len(parsed_line_hash)):
	playlist[i].append(parsed_line_hash[i][2])
for i in range(5):
	print(playlist[i])
cmd = 'node audio.js ' + playlist[0][3]
print(cmd)
# returned_unmaskurl = os.system('audio.js ' + playlist[0][3])
returned_value = subprocess.call(cmd, shell=True)
print(returned_value)
print(data_hash) 
print(playlist[0][2])
print(enter_id)
print(out_id)

import requests
import collections, heapq
from bs4 import BeautifulSoup
import json
import time

def parsePlayNum(s):
  num = ""
  for c in s:
    if c.isdigit():
      num += c
  if c == '万':
    return int(num)*10000
  return int(num)



base_url = "https://www.ixigua.com/"

# get the vlog channel
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
cookie = 'xiguavideopcwebid=6745658905164350980; xiguavideopcwebid.sig=BoTIfV77vpAH0Qx5MdljpaPXdFY; _ga=GA1.2.198142826.1570596115; s_v_web_id=52be566e989bdc2ef20ea328d4264a38; _gid=GA1.2.686722596.1571015678; RT="z=1&dm=ixigua.com&si=o2dht0alimn&ss=k1pvhjtc&sl=1&tt=0&obo=1&ld=cp7e&r=0ebe4929e3b0c4f3626c2f79422e203f&ul=cp7n"'
response = requests.get(base_url+"channel/vlog/", headers={'user-agent': userAgent, 'cookie': cookie})
response.encoding = 'utf-8'

# get the json data
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())
json_data = soup.find("script",type='application/json').contents
#print(json_data)

# get base video list
videoQueue = collections.deque()
videoPq = []
videoPlayInfo = dict()

for data in json_data:
  ChannelFeedV2 = json.loads(data)["ChannelFeedV2"]
  for each in ChannelFeedV2:
    for videoData in each["channelFeedData"]:
      #print(videoData)
      vId= videoData["videoId"]
      if vId not in videoPlayInfo:
        videoPlayInfo[vId] = [videoData["videoTitle"], parsePlayNum(videoData["playNum"])]
        videoQueue.append(vId)

#print(videoQueue)
total_video_to_parse = 100
top_list_length = 10
while len(videoQueue)>0 and total_video_to_parse>0:
  vId= videoQueue.popleft()
  print(f'videoId: {vId}, title: {videoPlayInfo[vId][0]}')
  if len(videoPq)<top_list_length:
    heapq.heappush(videoPq, [videoPlayInfo[vId][1], vId])
  else:
    if videoPlayInfo[vId][1]>videoPq[0][0]:
      heapq.heappop(videoPq)
      heapq.heappush(videoPq, [videoPlayInfo[vId][1], vId])
  time.sleep(2)
  response = requests.get(base_url+"i"+vId, headers={'user-agent': userAgent, 'cookie': cookie})
  response.encoding = 'utf-8'
  soup = BeautifulSoup(response.text, "html.parser")
  #print(soup.prettify())
  for data in json_data:
    ChannelFeedV2 = json.loads(data)["ChannelFeedV2"]
    for each in ChannelFeedV2:
      for videoData in each["channelFeedData"]:
        #print(videoData)
        vId= videoData["videoId"]
        if vId not in videoPlayInfo:
          videoPlayInfo[vId] = [videoData["videoTitle"], parsePlayNum(videoData["playNum"])]
          videoQueue.append(vId)

  total_video_to_parse -= 1

print("result:")
rank = []
while len(videoPq)>0:
  rank.append(heapq.heappop(videoPq))
for each in reversed(rank):
  print(f'title: {videoPlayInfo[each[1]][0]}, playNum: {videoPlayInfo[each[1]][1]}')
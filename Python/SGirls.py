# Step 1 : install relevant packages
!pip install bs4
!pip install folium
import requests
from bs4 import BeautifulSoup
import folium

# Step 2: Get from Open data site
url = 'http://openapi.kepco.co.kr/service/EvInfoServiceV2/getEvSearchList'
params ={'serviceKey' : 'pzu8M6kHuMVoSmGMVoV8OFf4f7A0X1SgPoIf2PYEyM/z1+Yk5jEpkEmIE7yEkPlkyTO54QqOpnFdKQOucl5DvA==', 'pageNo' : '1', 'numOfRows' : '300', 'addr' : '제주' }
response = requests.get(url, params=params)
print(response.content)

# Step 3 : Parse the downloaded content
wsoup = BeautifulSoup(response.text, 'html.parser')
res = wsoup.find_all('item')
print(res)

# Step 4 : Filters only what we need
coor, mark =[], []
for n in res:
	t1 = n.select_one('cpstat')
	t2 = n.select_one('lat')
	t3 = n.select_one('longi')
#	print(t1.get_text(), t2.get_text(), t3.get_text())
	coor.append([float(t2.get_text()), float(t3.get_text())])
	mark.append(int(t1.get_text()))
print(coor)
print(mark)

# Step 5 : Calculate the boundary
mx1, mx2 = coor[0][0], coor[0][0]
my1, my2 = coor[0][1], coor[0][1]
for i in range(1, len(coor)):
	mx1 = min([mx1, coor[i][0]])
	mx2 = max([mx1, coor[i][0]])
	my1 = min([my1, coor[i][1]])
	my2 = max([my1, coor[i][1]])
mxc, myc = (mx1+mx2) / 2, (my1+my2)/2
print(mxc, myc)

# Step 6 : Plot on the map
m = folium.Map([mxc, myc], zoom_start=10)
for i in range(len(coor)):
    folium.Marker(coor[i], tooltip = mark[i]).add_to(m)
m

# Step 7 : Plot with different colors
m = folium.Map([mxc, myc], zoom_start=10)
for i in range(len(coor)):
	if (mark[i] == 1):
    		folium.Marker(coor[i], icon=folium.Icon(color = 'red'), tooltip = mark[i]).add_to(m)
	elif (mark[i] == 2):
    		folium.Marker(coor[i], icon=folium.Icon(color = 'darkgreen'),  tooltip = mark[i]).add_to(m)
	else:
    		folium.Marker(coor[i], icon=folium.Icon(color = 'grey'),  tooltip = mark[i]).add_to(m)
m

# Step 8 : Plot on different types
# Change only Step 4

coor, mark =[], []
for n in res:
	t1 = n.select_one('chargetp')
	t2 = n.select_one('lat')
	t3 = n.select_one('longi')
#	print(t1.get_text(), t2.get_text(), t3.get_text())
	coor.append([float(t2.get_text()), float(t3.get_text())])
	mark.append(int(t1.get_text()))
print(coor)
print(mark)

# 

list_id_name_page = []
import requests, threading
import os, sys
from time import sleep
from datetime import datetime
os.system('title TOOL BUFF MENBER GROUP BẰNG PAGE PRO5')
try:
	import requests,pystyle
except:
	Write.Print ("Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải \n",Colors.blue_to_red,interval=0.0001)
    os.system('pip install requests && pip install bs4 && pip install pystyle')
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    Write.Print('────────────────────────────────────────────────────────────\n',Colors.blue_to_red,interval=0.0001)
def idelay(o):
    while(o>0):
        o=o-1
        Write.Print(f"[FRIVE][.....""]""["+str(o)+"]",Colors.blue_to_red,interval=0.0001,end='\r')
        sleep(1/6)
        Write.Print(f"[FRIVE][X....""]""["+str(o)+"]",Colors.blue_to_red,interval=0.0001,end='\r')
        sleep(1/6)
        Write.Print(f"[FRIVE][XX...""]""["+str(o)+"]",Colors.blue_to_red,interval=0.0001,end='\r')
        sleep(1/6)
        Write.Print(f"[FRIVE][XXX..""]""["+str(o)+"]",Colors.blue_to_red,interval=0.0001,end='\r')
        sleep(1/6)
        Write.Print(f"[FRIVE][XXXX.""]""["+str(o)+"]",Colors.blue_to_red,interval=0.0001,end='\r')
        sleep(1/6)
        Write.Print(f"[FRIVE][XXXXX""]""["+str(o)+"]",Colors.blue_to_red,interval=0.0001,end='\r')
        sleep(1/6)
def rungr(x):
    time = datetime.now().strftime("%H:%M:%S")
    dem +=1
    uid_page = list_id_name_page[x].split('|')[0]
    name_page = list_id_name_page[x].split('|')[1]
    list1 = (f'i_user={uid_page};')
    cookie9 = (f'{cookie}{list1}')
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/groups/'+str(id_gr)+'',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'viewport-width': '1221',
        'x-fb-friendly-name': 'GroupCometJoinForumMutation',
        'x-fb-lsd': '1CWQYotunk8BXwcjavghDO',
        'cookie': cookie9,
    }

    data = {
        'av': uid_page,
        '__user': uid_page,
        '__a': '1',
        '__dyn': '7AzHxqU5a5Q1ryaxG4VuC0BVU98nwgU765QdwSwMwNw9G2Saxa1NwJwpUe8hw6vwb-q7oc81xoswMwto88422y11xmfz83WwgEcHzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzEaE5e7oqBwJK2W5olwUwlu5pUfE2FBx_y8lz83VBwJCwLyES0Io88cA0z8c84qifxe3u362-2B0oobo8o',
        '__csr': 'gT3c9Tf4Ph3lndq9E8btWdIy8B6OFTAFqZuBpWIDkDYLF8HWhaKiB9qhqHB-yAFpRXyqWV4dWpaBiHZ7J9d4G5V8GmV9u9CgGK4oKVu4agtG5quFoy9zkeBGucHAmbGnKnyonykmErBg84ubyU6e4FGxa10zpo42axi1AwNzp8C13wIz98a8O6U9UiG2-48bU3fCK19wPwpoOdwKwsrwCw-wk85q1swu84C4E1gE0aJE09kE031nw2780oow8q0S8ANO06fg0F-05mE0m4y3Q0cnwtyw0r1oW0A81oE1981VE0-K0L82xw',
        '__req': 's',
        '__hs': '19323.HYP:comet_pkg.2.1.0.2.1',
        'dpr': '1',
        '__ccg': 'EXCELLENT',
        '__rev': '1006638605',
        '__s': 'g46m30:o2pr1z:3yzc8j',
        '__hsi': '7170501783158722778',
        '__comet_req': '15',
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'lsd': '1CWQYotunk8BXwcjavghDO',
        '__aaid': '497084035286445',
        '__spin_r': '1006638605',
        '__spin_b': 'trunk',
        '__spin_t': '1669512545',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
        'variables': '{"feedType":"DISCUSSION","groupID":"'+str(id_gr)+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1669512546874,734244,2361831622,","group_id":"'+str(id_gr)+'","group_share_tracking_params":{"app_id":"2220391788200892","exp_id":"null","is_from_share":false},"actor_id":"'+uid_page+'","client_mutation_id":"1"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":1,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":true}',
        'server_timestamps': 'true',
        'doc_id': '5608919199222447',
        'fb_api_analytics_tags': '["qpl_active_flow_ids=431626709"]',
    }

    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).text
    Write.Print(f'{dem} | {time} | SUCCESS | {uid_page} | {name_page} | {id_gr} | \n',Colors.blue_to_red,interval=0.0001)
    #print('['+str(x+1)+'] | '+str(time)+' | Success | '+str(uid_page)+' | '+str(name_page)+' | '+str(id_gr)+' ')


# =================[ START TOOL ]===========================
clear()
cookie = Write.Input('Nhập Cookie: ',Colors.blue_to_red,interval=0.0001)
headers = {
        'authority': 'mbasic.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://mbasic.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://mbasic.facebook.com/',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie,
}
    
try:
    Write.Print("Đang Check Live Cookie...",Colors.blue_to_red,interval=0.0001, end="\r")
    find_data = requests.get("https://mbasic.facebook.com/", headers=headers).text
    fb_dtsg = find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
except:
    Write.Print('KHÔNG GET ĐƯỢC THÔNG TIN - KIỂM TRA COOKIE\n',Colors.blue_to_red,interval=0.0001)
    exit()
headers_getid = {
    'cookie': cookie, 
}
data = {
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
    'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
    'doc_id': '5300338636681652'
}
getidpro5 = requests.post('https://www.facebook.com/api/graphql/', headers = headers_getid, data = data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']

for i in getidpro5:
    uid_page = i['profile']['id']
    name_page = i['profile']['name']
    gomlist = f'{uid_page}|{name_page}'
    list_id_name_page.append(gomlist)
clear()
Write.Print(f'Đã Tìm Thấy '+str(len(list_id_name_page))+' Page\n',Colors.blue_to_red,interval=0.0001)
thanh()
linkgr = input('Vui Lòng Nhập Link Group: ')
get_id_gr = requests.post('https://id.traodoisub.com/api.php',data={"link":linkgr,}).json()
if 'success' in get_id_gr:
    id_gr = get_id_gr["id"]
else:
    exit('Link Group Sai')
thanh()
Write.Print(f'Success Uid Group: {id_gr}'Write.Input)
thanh()
soluongrungr = int(Write.Input('Số Lượng Menber: ',Colors.blue_to_red,interval=0.0001))
thanh()
delay = int(Write.Input('Nhập Delay: ',Colors.blue_to_red,interval=0.0001))
thanh()
for x in range(soluongrungr):
    threading.Thread(target=rungr,args=(x, )).start()
    ndp_delay(delay)

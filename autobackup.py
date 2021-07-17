import requests
import datetime
import json
#module
from module import vultr

#Api key 목록
g_api_vultr = "4RM2WS6WEJTO6V52CZPKNFXBXIOKBXZ7CMBA"

#백업할 서버 목록
g_list_ipv4 = ['216.155.135.234']
g_list_ipv6 = []
g_list_label = []

#version
VERSION = "1.0.0.1"

def autodelete(apikey,expired):
    #현재시각
    date_now = datetime.datetime.now()
    #오래된 스냅샷 삭제
    js_array = vultr.snapshots_list(apikey)
    if js_array != False:
        for idx in js_array:
            date_created = idx['date_created']
            date_created = date_created[:len(date_created)-6]
            date_created = datetime.datetime.strptime(date_created,'%Y-%m-%dT%H:%M:%S')
            if (date_now-date_created).days >= expired and idx['description'].find('backup_') == 0:
                vultr.snapshots_delete(apikey,idx['id'])
    return

def autobackup(apikey,list_ipv4,list_ipv6,list_label):
    servers = []
    js_array = vultr.instances_list(apikey)
    if js_array != False:
        #백업해야할 기기 찾아서 배열로 추가
        for idx in js_array:
            #ipv4 확인
            try:
                list_ipv4.index(idx['main_ip'])
                servers.append(idx['id'])
            except:
                pass
            #ipv6 확인
            try:
                list_ipv6.index(idx['v6_main_ip'])
                servers.append(idx['id'])
            except:
                pass
            #ipv4 확인
            try:
                list_label.index(idx['label'])
                servers.append(idx['id'])
            except:
                pass
        #중복된 instance 제거
        servers = set(servers)
        servers = list(servers)
    else:
        return False
    #백업시작
    for idx in servers:
        #스냅샷 Label 생성
        js_server = vultr.instances_get(apikey,idx)
        if js_server != False:
            snapshot = datetime.datetime.now().strftime('%y%m%d')
            if js_server['label'] != '':
                snapshot = 'backup_'+js_server['label']+'_'+snapshot
            elif js_server['main_ip'] != '':
                snapshot = 'backup_'+js_server['main_ip']+'_'+snapshot
            elif js_server['v6_main_ip'] != '':
                snapshot = 'backup_'+js_server['v6_main_ip']+'_'+snapshot
            #스냅샷 생성
            vultr.snapshots_create(apikey,idx,snapshot)
    return True

autobackup(g_api_vultr,g_list_ipv4,g_list_ipv6,g_list_label)
autodelete(g_api_vultr,2)

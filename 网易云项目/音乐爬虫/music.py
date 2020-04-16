import requests 
from lxml import etree

def get_data():
    url = "https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=邓紫棋"
    headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36",
            "referer": "https://y.qq.com/portal/search.html",
            "cookie": "pgv_pvid=1768631471; pgv_pvi=3107664896; ts_uid=5285307810; RK=AyIYmysdPV; ptcz=12d4633d0c1b428b0c1f513b3567358c28ce8c9da492aeaf4dd95e3b00f90855; tvfe_boss_uuid=bebe37a4dac6b3c4; LW_uid=r1v59738V4D619Y9y762a6U1E6; eas_sid=s1r547p8G4N6P9k9U7g4Q7z6x9; LW_sid=Z1H5s7N8s4e7O0j0I0a5w2J4g1; sd_userid=30191582207652222; sd_cookie_crttime=1582207652222; o_cookie=1244353765; psrf_qqaccess_token=546E87BD4A477E7C6F558B5D7B9823BA; psrf_qqunionid=0094468E2E371AC76F8DECB4E12A7DE0; psrf_qqrefresh_token=1EF240B259D5FEACC2BFF29CE8B65EF0; psrf_qqopenid=3D15B83DCC2D2A06D029B9887A343338; ptui_loginuin=1244353765; ts_refer=www.google.com/; uin=1244353765; pgv_info=ssid=s6956764103; pgv_si=s8061334528; userAction=1; yq_playschange=0; yq_playdata=; player_exist=1; qqmusic_fromtag=66; yq_index=2; yqq_stat=0; yplayer_open=0; _qpsvr_localtk=0.11812390964884956; psrf_access_token_expiresAt=1594808428; qm_keyst=Q_H_L_2mMCOw50e4aRH8UQQHRmPq8GlFbys7Xa98ADA0HLIAdnNwDjDT-m5V_tGasR7W8; qqmusic_key=Q_H_L_2mMCOw50e4aRH8UQQHRmPq8GlFbys7Xa98ADA0HLIAdnNwDjDT-m5V_tGasR7W8; psrf_musickey_createtime=1587032428; ts_last=y.qq.com/portal/search.html"
        }
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'
    response = response.content
    html = etree.HTML(response)
    result = etree.tostring(html, encoding='utf-8')
    print(result.decode('utf-8'))


if __name__ == '__main__':
    get_data()

import json
import requests
from bs4 import BeautifulSoup

data = {
    "username": "",    # 学号
    "password": ""     # UIS 密码
}

login_url = "https://uis.fudan.edu.cn/authserver/login?service=https%3A%2F%2Fzlapp.fudan.edu.cn%2Fa_fudanzlapp%2Fapi%2Fsso%2Findex%3Fredirect%3Dhttps%253A%252F%252Fzlapp.fudan.edu.cn%252Fsite%252Fncov%252FfudanDaily%253Ffrom%253Dhistory%26from%3Dwap"
get_info_url = "https://zlapp.fudan.edu.cn/ncov/wap/fudan/get-info"
save_url = "https://zlapp.fudan.edu.cn/ncov/wap/fudan/save"

s = requests.Session()

response = s.get(login_url)

content = response.text

soup = BeautifulSoup(content, "lxml")

inputs = soup.find_all("input")

for i in inputs[2::]:
    data[i.get("name")] = i.get("value")

response = s.post(login_url, data=data)

response = s.get(get_info_url)

old_pafd_data = json.loads(response.text)

response = s.post(save_url, data=old_pafd_data["d"]["info"])

print(response.text)

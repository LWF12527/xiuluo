
import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"141.0.7390.123\"",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"141.0.7390.123\", \"Not?A_Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"141.0.7390.123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"15.0.0\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
cookies = {
    "privacy_2": "0",
    "privacy_3": "0",
    "privacy_4": "0",
    "privacy_verify": "1",
    "cf_clearance": "9OspfTJUwgBfX0ppwWljCvG4zhJBbYE6285VV8FZM6c-1762478537-1.2.1.1-biYo2Gen.10fZPTG222gkgikXyOEyKZEfgAGREcdleMYs6ampFTPaxehFV2jr9rIJmtAl3PPtyMSSOZquZs7XCTkac9wJ.khepFv0T4cD90zQJncpftnOipAcTUJDUQ9Gf2yqHZLfSxcE71Hb27ZQMygmIDHv3PLA8_PpPDLwd7ZBVgkAzQPa2GREwkxl5SE8v4PVRNu60QVuo21Wd84temPDiOG0recBRHD4PtC9Do",
    "EW4SITE": "ccl554rjlv88trqcd2ktlg9nsc",
    "SITEXSRF141": "qhp7n3buuccx8r8b248ptt32rj1wd6zj"
}
url = "https://archyvas.lrp.lt/adamkus/sarasas15ee.html?nuo=1&kat=4&search="
response = requests.get(url, headers=headers,cookies=cookies)

print(response.text)
print(response)
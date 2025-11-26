import requests

url = "https://npro.maoyan.com/api/ncinema/box/cinema/follow.json"
params = {'type': '0', 'beginDate': '20251126', 'isSplit': '0', 'cityId': '0', 'filterJson': '{}', 'utm_term': '8.12.0', 'utm_source': 'xiaomi', 'utm_medium': 'android',
          'utm_content': '2021BCA31F590CF', 'movieBundleVersion': '8012001', 'utm_campaign': 'AmovieproBmovieproCD-1', 'pushToken': 'dpsh8407478445097dc81c45d126a8e8f98eatpu',
          'uuid': '0000000000000280CD8E870034B1C935885792E216204A176403058303035387', 'deviceId': '2021BCA31F590CF', 'riskLevel': '71', 'optimusCode': '10', 'language': 'zh', 'channelId': '40004'}
headers = {
    "Accept-Encoding": "gzip",
    "Connection": "Keep-Alive",
    "Content-Type": "application/json",
    "Host": "npro.maoyan.com",
    # "M-SHARK-TRACEID": "5310000000000000280CD8E870034B1C935885792E216204A176403058303035387223b06176412045877943a0e8",
    "clientType": "myPro",
    "mtgsig": "{\"a0\":\"3.0\",\"a1\":\"0a03b816-c295-46cc-ad01-f2a3704ce24f\",\"a3\":25,\"a4\":1764120458,\"a5\":\"hzWtS+EYKYNepVu84fd+gsbqegmxXOYvdTXHNGybcWNPKcRNFpm/10cwQncIIM+3i7mNY//wW3JakF/AVx6WuLYXHfNMute8xNl7JU1KLqv7KGoyoLaKXNfeaKIimQ0AAcnwhawSlcTTRR/1xZ6tmS63P7xd39NSu+INDFOXp3RTRb8HgPLoza02wXO56M/VTph2bzd4BTxPjDt6vA+r9crrvYP8D4gC/ZRpOWICyZe8irYCsurK1HlUfXK4eqL0FQFeDB6KHQHcXWl/2uSLlU7WI8HdoS/7UwVW+I+FJ8n4zhJd2A4TcyGJVx/RvApoZ12mWtpnfyY48r1YA0tFn5TbL2MdQgrVF00yACed7nNVPNHUb5hDRWyr/lp2iYqPcRj9GCCH5ing5llQQzOZ0qtC\",\"a6\":0,\"a7\":\"8HvQbR9Vh5e0muGqudzLTmN3/2flOFFJCIKIFip8zC4q4c+aLh9z7fbuz5rqeykLYlWgbqI9kygl74RqZ/INUDod+hdkx+EG40/yf81YtA8=\",\"a8\":\"0e1d7dd3b1b8c9f62dae11157942f554edd5f7d8dd70d8e7b2d837a9\",\"a9\":\"a8bf22d0WR3rPS5p3aAIrf/vlpopgqbMEJdmDg4ZOQelajy4wxBzWD6wFE34ERc4HDxLqkAUTfdccaFBBimuDi/Hj0E5notwyHauoGor+m11PqZuMFeBZ2h9t4IBMbTcjWbRXsz8Hhkz1C4VWSdyijSWDiK36oo8h+dKygXuinBg8fjcn+zCej4VeYVL4hQjL2FJpa61foKNY97feyF9l4c//IpVezDlpmWlKcFSCPUsKE7qCQLQGqJ3SoEbLQhCX/B25CowEhzwWLF5AtH/I9qk4Q3XE0CcrqK6dKDURyP0QbVmdLwnPPIQwwMiTMM4g1eec9PBAXtvJAaCbhbovH/gaAMhKjSLMoUpeA1evGRbtPR4bGqOGOoWMY7jXL2vXzWZW1a1RUJ2Jq4ArjT9zbfLS29ed7HrFZ+9UG9ZetdD9vaVvLiyIGHw9Z1ybWxiFG2WZ5mzxfUXgd9vQZCABRjaAGqvwFDR2sRpeqt5SkB7Xugm6cOulZiPTJbI8SeIwKcvndz/P4e/vz4i8+2iINPfA83EeXIl+f9rnfs+pJHadPvxw7uDUlSesteSRheyCapMOIMyWLUDKRdbk7dwO3hTktN0bAy4weewqlwvqV9yB+XpmzIuy2XnzYqnmhzEwwQ4NYLkXaHuqwk4UvBA8HCANiFGGy4h36UF8gthLgYKNHvLtI3tg2SgKuTlPRwqmyh6eVeJyDu0AiO/di5Kqmc7vxTFJAm9OMBovVCz41izPWws625OmIJCPQEhwPPX417BPRrYyCLRCMQMvC9QDkmVPDnC9Zu2jnjK8MmnsBS7YUrr688QnyoscaCaYSu32bTaRAViiUL8V0CgNDLZfeOE35HgpOqfMqkclnsuOzOZbJycql1RIVtVw7t4RQnQyTZVcXY46z5u8A2br7RMP+lVRRQR/aS8X1Ec6jcbExLh4/0sMrnC6qA5Js3BrnZb0TcqtyA6NC1L3ly5sO/KEmXkDD8LA06FICiXyh3XIiQQowkMCn8=\",\"a10\":\"6,96,1.1.1\",\"x0\":1,\"a2\":\"9e3681211431522b3cf3ee433723a726\"}",
    # "retrofit_exec_time": "1764120458776",
    "token": "b_maoyan_eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3NjQwNjM5NDMsIm5iZiI6MTc2NDA2Mzk0MywiZXhwIjoxNzc5NjE1OTQzLCJkZXZpY2VUeXBlIjoxLCJzYWx0IjoicUplTWFvIiwiaXNUZXN0IjpmYWxzZSwidXNlcklkIjo3Njc5OTkwMDIsInV1aWQiOiIwMDAwMDAwMDAwMDAwMjgwQ0Q4RTg3MDAzNEIxQzkzNTg4NTc5MkUyMTYyMDRBMTc2NDAzMDU4MzAzMDM1Mzg3IiwidmVyc2lvbiI6IjEuNyIsImNoYW5uZWxJZCI6NDAwMDR9.838UGydSwAyppxUxKMrBoVlkLaJiqKqyp4WePomCiNQ",
    "user-agent": "Dalvik/2.1.0 (Linux; U; Android 9; 2311DRK48C Build/PQ3A.190605.09261140)",
    "userid": "767999002",
    "yodaReady": "native",
    "yodaVersion": "1.18.0.272"
}
response = requests.get(
    url=url,
    params=params,
    headers=headers
)

print(f"状态码: {response.status_code}")
print("响应内容:")
print(response.text)

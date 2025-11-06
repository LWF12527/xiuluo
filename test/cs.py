import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.carhartt.com/en-eu/",
    "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
cookies = {
    "C4Country": "HK",
    "AKCountry": "HK",
    "AKA_CONTINENT": "AS",
    "AKA_A2": "A",
    "PIM-SESSION-ID": "vYfalJytKxpPz6j7",
    "ak_bmsc": "73A85A34D2BF42B9D6731681971F18D1~000000000000000000000000000000~YAAQKNgjFwNQwTaaAQAAyR6yVx0puOLn/Inv+hro5ZaeyT+HWumnGh1iB1S/dN5/ASvLcl8bByG4NXbLC6+Uiyqol2KsHUpIoZIx0UgD2uhevO2G+MEwa4E0oUsIwkHo1NojZTlknX8a+2RLgy1pAkRuuY6lGjThANm6rLeBV1i5aOWjn9cvjZeZ9IhoXtLCufO+Hm21w83K18YhtTpOzCeknpbE1WC0eOEGlvo/ahP/yPPcq50PIEcXLS1LsH8pFHOyDxkEXsOlfaRfEmDSrzwwL6auQuu1jtmtfO5/XCsuu0CrRq2xpfwwRJLOhRAMVYwzbGAiybc46hk+b2++Ubwt+bRONroU7zpEWcDRv9iWiA/ZzaV62EblINdlx6JuxJui7jzTEEMMbbu4TxVertPgaGpHw0ydkvfoUHrKOxqhVVVfAJAK4Lmp51Li76AAmF4boGNGf9EzU4GxGk2mKQ==",
    "oct8ne-first-enter": "true",
    "gig_bootstrap_4_G1z-gWiPDtmtIqrPmk36CA": "accounts-cdc-emea_ver4",
    "ROUTE": ".jsapps-68c499c9d5-bzsbf",
    "bm_sz": "7E0CB41413203360BEB316F54EE17D7D~YAAQKNgjFytXwTaaAQAAWUqyVx3370uUHi3vVQErTXsDNJJqUsdjrW7WHkY7QwJ0bPH3yNyFUe5hJWm5srMTN2/iSlW/uFf7L+WRZxrqX2DhHOApzm9uXSokzZJxgOBlK4JwYY8cs2Pt77ckll7jEHw809PeZ+igD+9mgLKwBV0emOoAL9YGVqyDCcjfQc7W6HuvwSCdTKuWUQa/m7C3NqZP7+Y5VET5o36I/5FfCo2LdwFr8tHZ8kmGpM+YoL858+SosnmwvZ/ThMxQgCypfSolPQR4u/s+9b2ila9M+OBjEgueE+PxTJGOgqPG//BlagizZJTUvXsUjGt/4sxDfHbNWzpP5GADZ7JzIkdPvoMsNSe7Rp4KRMTuWigaC5sp+WNq7BRW0eykS1sAv32oLznqqqjjKi0+QvybPA==~3490611~3487800",
    "_abck": "6672F3578A80CCAB623DAE8ADC55D138~0~YAAQKNgjF0RXwTaaAQAA90qyVw53nH9da/64XD/qs24yaOrpAsjjmJ+7EqXBL2m5WZCt0IrMH9knDfP9uPcVW+4osaE77DG3ce/NUk2oUutXZ+g5Uua5V3tEbhgltUNH0Y/PkXE0zj30r7PwDU5s4bT/6UME5AaG2yz1CRYOyZ1EB6nSHp9YsHYiTWgffUmQwxareGJ3Y4+x12RTg5eKGEtuvescT6UQgLupV55XU4f8NP3sGl6DLQiZvAqsznN+J7S3XWg6uXJ2+cY/0H2QPid/4WvfbtmH8RQaNubQUuTEBCMfr4UMMaZ7rL4e78zn6rvrelYS9eb7ilgihGloIQc3RyIsFtqvCObs1XnFAd1hZx8JZXXRHp9MEX797StN/uFdfSJh3/DhdjaHXiEvgWhxGMoMGHtrryoHtyK6LdHftiu0p/fqritpL/63GHijVEXOS1p5Ays84SR5O0YUMQQWL2UBoh5o9ivvOuCE7PMc6QnYcWTQ0PN3Awh087E8NF9eaztGcks/Ld2uscwM8rZn1KLhAq5xCgGlKKUmShfp76Pfc4pqpLzqau85dpFWxKMKPHRCs1lGggbRD7G1d6+u+GAZ9qlK5hmn3tedgzIbjHVP30twQb+lq0tFpflEodSrmQ==~-1~-1~1762411482~AAQAAAAE%2f%2f%2f%2f%2f+JWj86SrsfPuKU6f4Ci4LkeZ3Y8mf+AkJOiHZyNd18go6Yl3l+WMzpEGIjTl+UlKQLtCpmeU738T%2f5zqFYMzsfsnSckVrJxM3F8~-1",
    "AKA_ORIGIN": "EU",
    "bm_sv": "5BCC147D50F1D5EC3A5DFCB9E2042B4D~YAAQKNgjFzBbwTaaAQAAu2iyVx1aiTCQeWXIRZJ7gr5mdEj591AhdLKoxTwWcCU8MKjdoL2eTxooFISTDv0PMVZxi/BVEK/194GLZIFWmAN8yirC1HV/9pnrGSZKCZpotD1NAqYewmIEdQC8U30QfAuoMVIJqMINwUIIHyEjRm6YqNP4NUVxjzDUk4n1W5o/4bBq2GKE0AZJ8i3uTVBcn5LWGYWEbu2sTvD6cdhZs/dPCI1pzo4Gif7+CHJ+eiyi0cpd~1"
}
i=0
while True:
    i+=1
    url = "https://www.carhartt.com/en-eu/p/j140-loose-fit-firm-duck-insulated-flannel-lined-active-jac/106673"
    response = requests.get(url, headers=headers)
    print(response.text)
    print(response,i)
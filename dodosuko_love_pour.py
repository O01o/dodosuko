import random

print("楽しんご")

dodosuko_list = []
dodosuko_str = ''
dodosuko_str_all = ''

dodosukonverter = {
    1: 'ドド',
    2: 'スコ',
}

while True:
    dodosuko = random.randint(1,2)
    dodosuko_list.append(dodosuko)
    if len(dodosuko_list) >= 4: 
        dodosuko_list_tmp = dodosuko_list[-4:]
        for dodosuko in dodosuko_list_tmp:
            dodosuko_str += dodosukonverter[dodosuko]
        print(dodosuko_str)
        if dodosuko_str == 'ドドスコスコスコ':
            for dodosuko in dodosuko_list:
                dodosuko_str_all += dodosukonverter[dodosuko]
            break
        else: dodosuko_str = ''

print(dodosuko_str_all+'ラブ注入♡')
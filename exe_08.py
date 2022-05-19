dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
res = {}

def handle_dict(ret, dic):
    for i in dic:
        ret[i] = dic[i]

handle_dict(res, dic1)
handle_dict(res, dic2)
handle_dict(res, dic3)

print(res)
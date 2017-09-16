def extract(filename):
    dic_u = {}
    dic_i = {}
    with open(filename) as f:
        for each in f:
            es = each.strip().split()
            u = int(es[0])
            i = int(es[4])
            if dic_u.__contains__(u):
                dic_u[u].append(each)
            else:
                dic_u[u] = [each]
            if dic_i.__contains__(i):
                dic_i[i].append(each)
            else:
                dic_i[u] = [each]
    return dic_u, dic_i
    
# 字典按照value排序
def sort_dict(dic, reverse=True, sort = None):
    if sort:
       return sorted(dic.items(), key=sort, reverse = reverse) 
    else:
       return sorted(dic.items(), key=lambda d:d[1], reverse = reverse)

def kenuoladuo(filename):
    with open(filename) as rf:
        dic = {}
        with open('klnd-'+filename, 'w') as wf:
            for each in rf:
                es = each.strip().split('\t')
                u = int(es[0])
                la = float(es[2])
                lo = float(es[3])
                if la < 41 and la > 37 and lo > -109 and lo < -102:
                    if dic.__contains__(u):
                        dic[u].append(each)
                    else:
                        dic[u] = [each]
            uc = 0
            locations = set()
            for k,v in dic.items():
                if len(v) > 5:
                    for e in v:
                        es = e.strip().split('\t')
                        locations.add(int(es[4]))
                        wf.write(e)
                    uc += 1
            print (uc)
            print (len(locations))


def split_train_test(filename, rate):
    from datetime import datetime
    dic = {}
    with open(filename) as f:
        for e in f:
            es = e.strip().split()
            u = es[0]
            i = es[4]
            t = datetime.strptime(es[1],'%Y-%m-%dT%H:%M:%SZ' ).timestamp()
            if dic.__contains__(u):
                dic[u].append((e, t, i))
            else:
                dic[u] = [(e, t, i)]
        for k, v in dic.items():
            dic[k] = sorted(v, key=lambda d:d[1], reverse=True)
    with open('train' + filename, 'w') as trf:
        with open('test' + filename, 'w') as tef:
            for k,v in dic.items():
                l = len(v)
                test_num = max(int(rate*l), 0)
                train_num = l - test_num
                test_set = {e[2] for e in v[:test_num]}
                for i in range(test_num):
                    tef.write(v[i][0])
                for i in range(test_num, l):
                    if test_set.__contains__(v[i][2]):
                        continue
                    trf.write(v[i][0])

def keluonado_egde(check_in_file, edge_file):
    uset = set()
    with open(check_in_file) as f:
        for e in f:
            es = e.split('\t')
            uset.add(int(es[0]))
    print(len(uset))
    with open(edge_file) as f:
        with open('klnd'+edge_file, 'w')as wf:
            for e in f:
                es = e.strip().split('\t')
                if uset.__contains__(int(es[0])) and uset.__contains__(int(es[1])):
                    wf.write(e)

if __name__ == '__main__':
    # split_train_test('klnd-Gowalla_totalCheckins.txt', 0.2)
    # keluonado_egde('klnd-Gowalla_totalCheckins.txt', 'Gowalla_edges.txt')
    # from datetime import datetime
    # import time
    # print(time.localtime(1295820682))
    kenuoladuo('Gowalla_totalCheckins.txt')
    split_train_test('klnd-Gowalla_totalCheckins.txt', 0.2)
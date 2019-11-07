import json
file_name = 'data/testjson.json'

with open(file_name) as j_object:
    data_w = json.load(j_object)
    print(data_w)

while

   ''
        for n in range(1, 25):
            max_cunt = min(a, b, c)
            ans_list = []
            # print(max_cunt)
            ia = 0
            ib = 0
            ic = 0
            iaa = 1
            ibb = 1
            icc = 1
            count = 0
            ans = 0;
            while count < (n-1):
                if (ia+1) * a < max_cunt:
                    ia += 1
                    count += 1
                    if (ia*a) in ans_list:
                        count -= 1
                    else:
                        ans_list.append(ia*a)
                 #   print(ia*a)
                    continue
                if (ib+1) * b < max_cunt:
                    ib += 1
                    count += 1
                    ans = ib*b
                #    print(ib*b)
                    continue
                if (ic+1) * c < max_cunt:
                    ic += 1
                    count += 1
                    ans = ic*c
                #    print(ic*c)
                    continue
                iaa = max(iaa, ia)
                ibb = max(ibb, ib)
                icc = max(icc, ic)
                max_cunt = min((iaa+1)*a, (ibb+1)*b, (ibb+1)*c)
                if max_cunt == ((iaa+1)*a):
                    iaa += 1
                elif max_cunt == ((ibb+1)*b):
                    ib += 1
                elif max_cunt == ((icc+1)*c):
                    icc += 1
            print(ans)
          #  print('updata ')
          #  print(max_cunt,iaa,ibb,icc)
          '''

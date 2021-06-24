# -*- coding: utf-8 -*- 
import csv

### input format 
### sku,count,width,height,depth,p.vol
data_src = csv.reader(open('ungs_meli_dims_ordered_w_vol.csv', encoding="latin9"), delimiter=",")
OUT = 'distribution.csv'
###


with open(OUT, 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow((
            'count', 'prod_vol'))
        _flag = True
        _prod_vol = 0
        _count = 0

        for row_data in data_src:
            prod_vol = int(row_data[5])
            count = int(row_data[1])

            if _prod_vol == 0 or prod_vol == _prod_vol:
                _count = _count + count
            else:
                writer.writerow((_count, _prod_vol))
                print("count: " + str(_count) + ", prod_vol: " + str(_prod_vol))
                _count = count
            _prod_vol = prod_vol
        writer.writerow((_count, _prod_vol))
        print("count: " + str(_count) + ", prod_vol: " + str(_prod_vol))




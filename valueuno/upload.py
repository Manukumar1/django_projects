import csv
import datetime
from .models import NextDay

class insertData():
    def funData(self):
        data = []
        with open('N50 Cluster Private - Sheet1.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                data.append(row)

        for i in data[1:]:
            format_str = '%d/%m/%y'
            datetime_obj = datetime.datetime.strptime(i[0], format_str)
            dt = datetime_obj.date()
            if i[11] == '':
                i[11] = '0'
            if i[2] == '':
                break
            op_v = float(i[4])
            hg_v = float(i[5])
            lw_v = float(i[6])
            cl_v = float(i[7])
            oc_v = float(i[8])
            oh_v = float(i[9])
            ol_v = float(i[10])
            co_v = float(i[11])
            dt = NextDay(date=dt, day=i[1], simple_cluster=i[2], detailed_cluster=i[3],
                         open_value=op_v, high_value=hg_v, low_value=lw_v, close_value=cl_v, oc_d_value=oc_v,
                         oh_d_value=oh_v, ol_d_value=ol_v, co_d1_value=co_v)
            dt.save()
        return True

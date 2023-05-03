import datetime
import re

if __name__ == '__main__':
    start = datetime.date(1920, 1, 1)
    end = datetime.date(2020, 1, 1)

    sd_code = []
    with open('sd.txt', 'r', encoding='UTF-8') as sd_file:
        for line in sd_file.readlines():
            line.strip()
            line = re.sub('[\u4e00-\u9fa5]','',line)
            sd_code.append(line.strip())

    prefix_list = []
    while start < end:
        start += datetime.timedelta(days=1)
        for i in sd_code:
            prefix = '{}{}'.format(i, start.strftime('%Y%m%d'))
            prefix_list.append(prefix)

    with open('prefix.txt', 'w') as prefix_file:
        for i in prefix_list:
            prefix_file.write('{}\n'.format(i))
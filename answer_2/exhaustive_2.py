import datetime
import re
from tqdm import tqdm

if __name__ == '__main__':
    start = datetime.date(1920, 1, 1)
    end = datetime.date(2020, 1, 1)

    sd_code = []
    with open('D:\\PyCharmWorkSpace\\Hash_IDCard\\answer_2\\sd.txt', 'r', encoding='UTF-8') as sd_file: #绝对路径
        for line in tqdm(sd_file.readlines(),desc='处理sd.txt',ncols=100):
            line.strip()
            line = re.sub('[\u4e00-\u9fa5]','',line)
            sd_code.append(line.strip())

    prefix_list = []
    while start < end:
        start += datetime.timedelta(days=1)
        for i in sd_code:
            prefix = '{}{}'.format(i, start.strftime('%Y%m%d'))
            prefix_list.append(prefix)

    with open('answer_2\\prefix.txt', 'w') as prefix_file:
        for i in tqdm(prefix_list,desc='生成',ncols=100):
            prefix_file.write('{}\n'.format(i))
import datetime
import hashlib

TARGET_HASH = "b056184ef62fa3048b349d5a7f4551a977e291b4a8effb78a4665314afca1374" #哈希值
AREA_CODE_FILE = "D:\\PyCharmWorkSpace\\Hash_IDCard\\answer_1\\aeraCode.txt" #绝对路径 注意使用转义字符\\

class DateGenerator:
    """日期生成器, 给出区间, 生成之间的所有日期"""

    def __init__(
        self, start_date: datetime.date, end_date: datetime.date, steps: int = 1
    ):
        self.start_date = start_date
        self.end_date = end_date
        self.steps = steps

        self.current_date = start_date

    @property
    def date(self):
        while self.current_date <= self.end_date:
            yield self.current_date
            self.current_date = self.current_date + datetime.timedelta(days=self.steps)


class AreaCode:
    """从文件中获取所有行政区代码"""

    def __init__(self, area_code_file_path: str):
        self.file_path = area_code_file_path

    @property
    def code(self):
        with open(self.file_path,encoding='UTF-8') as file:
            for data in file.readlines():
                yield data[0:6]

class IdacrdGenerator:
    """身份证号码生成器"""

    def __init__(self, area_code: str, date: datetime.date, gender: int = None):
        self.area_code = area_code
        self.birth_code = "{:0>4d}{:0>2d}{:0>2d}".format(
            date.year, date.month, date.day
        )

        self.gender = gender

    @property
    def _front_0_13_copulas(self):
        factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5]
        items = [int(item) for item in f"{self.area_code}{self.birth_code}"]
        return sum([a * b for a, b in zip(factors, items)])

    @property
    def index_code(self):
        all_index_code = range(1000)
        if self.gender == 0:
            all_index_code = all_index_code[::2]
        elif self.gender == 1:
            all_index_code = all_index_code[1::2]

        for index in all_index_code:
            yield "{:0>3d}".format(index)

    def check_code(self, index_code: str):
        codes = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
        factors = [8, 4, 2]
        items = [int(item) for item in index_code]
        copulas = self._front_0_13_copulas + sum(
            [a * b for a, b in zip(factors, items)]
        )
        return codes[copulas % 11]

    @property
    def idcard(self):
        for index_code in self.index_code:
            yield f"{self.area_code}{self.birth_code}{index_code}{self.check_code(index_code)}"

def idcard_sha3_256(idcard: str):
    hash_object = hashlib.sha3_256()
    #hash_object = sha3.keccak_256()
    hash_object.update(idcard.encode("utf-8"))
    return hash_object.hexdigest()


if __name__ == "__main__":
    status = 0

    start_date = datetime.date(1978, 1, 1)
    end_date = datetime.date(2005, 12, 31)

    date_generator = DateGenerator(start_date=start_date, end_date=end_date)
    for date in date_generator.date:
        if status:
            break
        for area_code in AreaCode(area_code_file_path=AREA_CODE_FILE).code:
            if status:
                break
            for idcard in IdacrdGenerator(area_code, date, gender=1).idcard:
                hash_value = idcard_sha3_256(idcard)
                if hash_value == TARGET_HASH:
                    print(idcard, hash_value, "Bingo!!!")
                    status = 1
                    break
                else:
                    print(idcard, hash_value, "Incorrect")
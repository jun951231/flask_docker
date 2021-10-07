from icecream import ic

class OneToTenSum(object):

    def one_to_ten_sum_1(self):
        # 예시 1
        sum = 0
        for i in range(1, 11):
            sum += i
        return sum


    def one_to_ten_sum_2(self):
        # 예시 2
        val = sum(i for i in range(1, 11))
        return val


    def one_to_ten_sum_3(self):
        # 예시 3
        val = sum(range(1, 11))
        return val


if __name__ == '__main__':
    a = OneToTenSum()
    ic(a.one_to_ten_sum_1())
    ic(a.one_to_ten_sum_2())
    ic(a.one_to_ten_sum_3())
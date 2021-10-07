import csv
import matplotlib.pyplot as plt


class ChangedTemperaturesOnMyBirthday(object):
    data: []
    highest_temperatures: [] = list()
    minimum_temperatures: [] = list()

    def preprocessing(self):
        self.read_data()
        self.save_data_to_list()
        self.visualize_data()
        self.extract_date_data()

    def read_data(self) -> object:
        data = csv.reader(open('./data/seoul.csv', encoding='utf-8'))
        next(data)
        self.data = data
        return data

    def show_highest_temperature(self):
        return [i[-1] for i in self.data]

    def save_highest_temperature(self):
        '''
        self.highest_temperatures = []
        self.minimum_temperatures = []
        [self.highest_temperatures.append(i[-1]) for i in self.read_data()]
        [self.minimum_temperatures.append(i[-2]) for i in self.read_data()]
        # print(self.highest_temperatures)
        # print(self.minimum_temperatures)
        '''
        [self.highest_temperatures.append(float(i[-1])) for i in self.data if i[-1] != '']
        print(f'총 개수 : {len(self.highest_temperatures)}개')

    def visualize_data(self):
        plt.plot(self.highest_temperatures, 'lightpink')
        plt.plot(figsize=(20, 2))
        plt.show()

    def highest_temperatures_my_birthday(self):
        high = []
        low = []
        for i in self.data:
            if i[-1] != '' and i[-2] != '':
                if 1983 <= int(i[0].split('-')[0]):
                    if i[0].split('-')[1] == '03' and i[0].split('-')[2] == '05':
                        high.append(float(i[-1]))
                        low.append(float(i[-2]))
        plt.rc('font', family='Malgun Gothic')
        plt.rcParams['axes.unicode_minus'] = False
        plt.title('내 생일의 기온 변화 그래프')
        plt.plot(high, 'pink', label='high')
        plt.plot(low, 'skyblue', label='low')
        plt.legend()
        plt.show()


class TemperaturesOnMyBirthdayTest(object):
    data: [] = list()
    ls: [] = list()

    def read_data(self):
        data = csv.reader(open('./data/seoul.csv', encoding='utf-8'))
        next(data)
        self.data = data

    def save_data_to_list(self):
        return [self.ls.append(i) for i in self.data if i[-1] != '']

    def visualize_data(self):
        plt.plot()
        plt.show()

    def extracting_date(self):
        high = []
        low = []
        for i in self.ls:
            if 1983 <= int(i[0].split('-')[0]):
                if i[-1] != '' and i[-2] != '':
                    if i[0].split('-')[-1] == '03' and i[0].split('-')[-2] == '05':
                        high.append(float(i[-1]))
                        low.append(float(i[-2]))
        plt.rc('font', family='Malgun Gothic')
        plt.rcParams['axes.unicode_minus'] = False
        plt.title('내 생일의 기후 변화')
        plt.plot(high, 'r', label='High')
        plt.plot(low, 'g', label='Low')
        plt.legend()
        plt.show()
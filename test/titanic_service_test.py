import unittest
import os
from titanic.model.titanic_service import TitanicService


class TitanicServiceTest(object):

    mock = TitanicService()

    def new_model(self):
        # self.mock.new_model('train.csv')
        print(os.getcwd())

    def count_survived_dead(self, ):
        return []

    def creat_train(self):
        return None

    def creat_lable(self):
        return None

    def drop_feature(self, *feature):
        return None

    def embarked_nominal(self):
        return None

    def fare_ordnal(self):
        return None

    def title_nominal(self):
        return None

    def gender_norminal(self):
        return None

    def age_ordinal(self):
        return None

    def create_k_fold(self):
        return None

    def accuracy_by_classfier(self):
        return None


if __name__ == '__main__':
    unittest.main()
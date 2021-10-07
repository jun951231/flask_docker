from book_modu.basic_hist.models import BasicHist

if __name__ == '__main__':
    a = BasicHist()
    a.show_hist_about(a.highest_temperature('01'), '01')
import time

def get_fulltime():
    l_time = list(time.gmtime())
    num_month = l_time[1]
    num_day = l_time[2]
    if num_month < 10:
        str_month = "0{}".format(num_month)
    else:
        str_month = "{}".format(num_month)

    if num_day = < 10:
        str_day = "0{}".format(num_day)
    else:
        str_day = "{}".format(num_day)

    str_ymd = "{}{}{}".format(l_time[0], str_month, str_day)

    str_rest = ""
    for i in [3, 4, 5]:
        if l_time[i] < 10:
            str_rest += "0{}".format(l_time[i])
        else:
            str_rest += "{}".format(l_time[i])

    return [str_ymd, str_rest]

class TimeManager:
    def __init__(self):
        self.starts = {}
        self.stats = {}
    
    def start(self, name, print_msg = False):
        if name in self.starts.keys() and print_msg:
            print("{} exists, overwriting time".format(name))
        self.starts[name] = time.time()

    def check(self, name, renew = True, print_msg = False):
        if name not in self.starts.keys():
            print("!! {} not started !!".format(name))
            return -1

        if name not in self.stats.keys():
            self.stats[name] = list()

        res_check = time.time() - self.starts[name]
        self.stats[name].append(res_check)

        return res_check



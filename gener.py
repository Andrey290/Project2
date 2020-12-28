class Map():
    def __init__(self):
        self.string_lenth = 20
        self.width_of_map = 9
        self.old_map = ["11111111111111111111",
                        "10000000000000000001",
                        "10000000000000000001",
                        "10000000000000000001",
                        "10000000000000000001",
                        "10000000000000000001",
                        "10000000000000000001",
                        "10000000000000000001",
                        "10000000000000000001"]
        self.actual_map = ["10000000000000000001",
                           "10000000000000000001",
                           "10000000000000000001",
                           "10000000000000000001",
                           "10000000000000000001",
                           "10000000000000000001",
                           "10000000000000000001",
                           "10000000000000000001",
                           "10000000000000000001"]
        self.new_map = ["10000000000000000001",
                        "10000000000000000001",
                        "10000000000000000001",
                        "10000000000000000001",
                        "10000000000000000001",
                        "10000000000000000001",
                        "10000000000000000001",
                        "10000000000000000001",
                        "10000000000000000001"]
        self.whole_map = self.old_map + self.actual_map + self.new_map
        self.gener_map = self.gener_foo()

    def summ(self):
        s = 0
        for elem in self.whole_map:
            s += int(sum([int(x) for x in elem]))
        return s


    def gener_foo(self):
        super_map = self.new_map
        sum_of_maps = self.summ()
        field = []
        for j in range(self.width_of_map):
            string = []
            num_of_this_string = 0
            for i in range(self.string_lenth):
                if i in [0, self.string_lenth]:
                    string.append("1")
                    num_of_this_string += 1
                else:
                    if super_map[-1][i - 1] + super_map[-2][i - 1] + super_map[-3][i - 1] == "000" and \
                            super_map[-1][i] == "1":
                        string[i - 1] = "0"
                        num_of_this_string += 0
                        if not sum_of_maps + num_of_this_string % len(string) and i - 2 > 0:
                            string[i - 2] = "0"
                            num_of_this_string += 0
                            string[i] = "0"
                            num_of_this_string += 0
                        elif not sum_of_maps + num_of_this_string % 2:
                            if i - 2 > 0:
                                string[i - 2] = "0"
                                num_of_this_string += 0
                            else:
                                string[i] = "0"
                                num_of_this_string += 0
                        else:
                            string[i] = "0"
                    if super_map[-1][i - 1] + super_map[-1][i] + super_map[-1][i + 1] == "000":
                        string[i - 1] = "0"
                        num_of_this_string += 0
                        string.append("1")
                        num_of_this_string += 1
                        string.append("0")
                        num_of_this_string += 0
                    else:
                        string.append(1)
                        num_of_this_string += 1
            super_map.append("".join(string))

map = Map()
for elem in map.gener_map:
    print(elem)
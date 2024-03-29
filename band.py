class Band:
    def __init__(self, generation_number, minimum, maximum, *duplex):
        self.generation_number = generation_number
        self.minimum = minimum
        self.maximum = maximum
        self.duplex = duplex

    def is_in_range(self, value):
        return self.minimum <= value <= self.maximum

    def covers(self, value):
        return self.generation_number == value

    def in_mode(self, value):
        return self.duplex == value


# バンドのインスタンスを作成
bands = [
    # LTE bands
    Band("B1", 2110, 2170, "FDD"),
    Band("B2", 1930, 1990, "FDD"),
    Band("B3", 1805, 1880, "FDD"),
    Band("B4", 2110, 2155, "FDD"),
    Band("B5", 869, 894, "FDD"),
    Band("B7", 2620, 2690, "FDD"),
    Band("B8", 925, 960, "FDD"),
    Band("B11", 1475.9, 1495.9, "FDD"),
    Band("B12", 729, 746, "FDD"),
    Band("B13", 746, 756, "FDD"),
    Band("B14", 758, 768, "FDD"),  # 2024/3/14追加
    Band("B17", 734, 746, "FDD"),
    Band("B18", 860, 875, "FDD"),
    Band("B19", 875, 890, "FDD"),
    Band("B20", 791, 821, "FDD"),
    Band("B21", 791, 821, "FDD"),
    Band("B26", 859, 894, "FDD"),
    Band("B28", 758, 803, "FDD"),
    Band("B29", 717, 728, "FDD"),
    Band("B30", 2350, 2360, "FDD"),
    Band("B38", 2570, 2620, "TDD"),
    Band("B39", 1880, 1920, "TDD"),
    Band("B40", 2300, 2400, "TDD"),
    Band("B41", 2496, 2690, "TDD"),
    Band("B41K", 2515, 2675, "TDD"),  # 2024/3/29追加
    Band("B42", 3400, 3600, "TDD"),
    Band("B42F", 3420, 3600, "TDD"),  # 2024/3/29追加
    Band("B42G", 3410, 3600, "TDD"),  # 2024/3/29追加
    Band("B43", 3600, 3800, "TDD"),  # 2024/3/29追加
    Band("B46", 5150, 5925, "TDD"),
    Band("B66", 2110, 2200, "FDD"),
    Band("B71", 617, 652, "FDD"),
    Band("B77C", 3900, 4100, "FDD"),  # 2024/3/29追加
    Band("B78AA", 3300, 3670, "FDD"),  # 2024/3/29追加
    Band("B78B", 3500, 3600, "FDD"),  # 2024/3/29追加
    Band("B78T", 3410, 3610, "FDD"),  # 2024/3/29追加
    Band("B78W", 3300, 3580, "FDD"),  # 2024/3/29追加
    Band("B78K", 3420, 3800, "FDD"),  # 2024/3/29追加
    Band("B78H", 3542, 3700, "FDD"),  # 2024/3/29追加
    Band("B85", 728, 746, "FDD"),  # 2024/3/14追加
    # 5G bands
    Band("n1", 2110, 2170, "FDD"),
    Band("n2", 1930, 1990, "FDD"),
    Band("n3", 1805, 1880, "FDD"),
    Band("n5", 869, 894, "FDD"),
    Band("n7", 2620, 2690, "FDD"),
    Band("n8", 925, 960, "FDD"),
    Band("n20", 791, 821, "FDD"),
    Band("n28", 758, 803, "FDD"),
    Band("n38", 2570, 2620, "TDD"),
    Band("n40", 2300, 2400, "TDD"),
    Band("n41", 2496, 2690, "TDD"),
    Band("n46", 5150, 5925, "TDD"),
    Band("n66", 2110, 2200, "FDD"),
    Band("n71", 617, 652, "FDD"),
    Band("n77", 3300, 4200, "TDD"),
    Band("n78", 3300, 3800, "TDD"),
    Band("n79", 4400, 5000, "TDD"),
    Band("n257", 26500, 29500, "TDD"),
    Band("n258", 24250, 27500, "TDD"),
    Band("n260", 37000, 40000, "TDD"),
    Band("n261", 27500, 28350, "TDD"),
]

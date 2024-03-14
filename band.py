class Band:
    def __init__(self, generation_number, minimum, maximum):
        self.generation_number = generation_number
        self.minimum = minimum
        self.maximum = maximum

    def is_in_range(self, value):
        return self.minimum <= value <= self.maximum

    def covers(self, value):
        return self.generation_number == value


# バンドのインスタンスを作成
bands = [
    # LTE bands
    Band("B1", 2110, 2170),
    Band("B2", 1930, 1990),
    Band("B3", 1805, 1880),
    Band("B4", 2110, 2155),
    Band("B5", 869, 894),
    Band("B7", 2620, 2690),
    Band("B8", 925, 960),
    Band("B11", 1475.9, 1495.9),
    Band("B12", 729, 746),
    Band("B13", 746, 756),
    Band("B14", 758, 768),  # 2024/3/14追加
    Band("B17", 734, 746),
    Band("B18", 860, 875),
    Band("B19", 875, 890),
    Band("B20", 791, 821),
    Band("B21", 791, 821),
    Band("B26", 859, 894),
    Band("B28", 758, 803),
    Band("B29", 717, 728),
    Band("B30", 2350, 2360),
    Band("B38", 2570, 2620),
    Band("B39", 1880, 1920),
    Band("B40", 2300, 2400),
    Band("B41", 2496, 2690),
    Band("B42", 3400, 3600),
    Band("B46", 5150, 5925),
    Band("B66", 2110, 2200),
    Band("B71", 617, 652),
    Band("B85", 728, 746),  # 2024/3/14追加
    # 5G bands
    Band("n1", 2110, 2170),
    Band("n2", 1930, 1990),
    Band("n3", 1805, 1880),
    Band("n5", 869, 894),
    Band("n7", 2620, 2690),
    Band("n8", 925, 960),
    Band("n20", 791, 821),
    Band("n28", 758, 803),
    Band("n38", 2570, 2620),
    Band("n40", 2300, 2400),
    Band("n41", 2496, 2690),
    Band("n46", 5150, 5925),
    Band("n66", 2110, 2200),
    Band("n71", 617, 652),
    Band("n77", 3300, 4200),
    Band("n78", 3300, 3800),
    Band("n79", 4400, 5000),
    Band("n257", 26500, 29500),
    Band("n258", 24250, 27500),
    Band("n260", 37000, 40000),
    Band("n261", 27500, 28350),
]

class Band:
    def __init__(self, name, minimum, maximum, *duplex):
        self.name = name
        self.minimum = minimum
        self.maximum = maximum
        self.duplex = duplex

    def is_in_range(self, value):
        return self.minimum <= value <= self.maximum

    def covers(self, value):
        return self.name == value

    def in_mode(self, value):
        return self.duplex == value

    def span_is(self):
        return self.maximum - self.minimum


# バンドのインスタンスを作成
bands = [
    # LTE or sub bands
    Band("B1", 2110, 2170, "FDD"),
    Band("B1A", 2110, 2130, "FDD"),  # 2024/4/4追加
    Band("B1B", 2110, 2165, "FDD"),  # 2024/4/4追加
    Band("B1C", 2150, 2170, "FDD"),  # 2024/4/4追加
    Band("B2", 1930, 1990, "FDD"),
    Band("B3", 1805, 1880, "FDD"),
    Band("B3A", 1830, 1880, "FDD"),  # 2024/4/4追加
    Band("B3B", 1805, 1860, "FDD"),  # 2024/4/4追加
    Band("B3C", 1839.9, 1879.9, "FDD"),  # 2024/4/4追加
    Band("B3D", 1810, 1870, "FDD"),  # 2024/4/4追加
    Band("B3E", 1805, 1830, "FDD"),  # 2024/4/4追加
    Band("B3F", 1805, 1825, "FDD"),  # 2024/4/4追加
    Band("B3G", 1845, 1880, "FDD"),  # 2024/4/4追加
    Band("B3H", 1845, 1860, "FDD"),  # 2024/4/4追加
    Band("B3J", 1805, 1845, "FDD"),  # 2024/4/4追加
    Band("B4", 2110, 2155, "FDD"),
    Band("B5", 869, 894, "FDD"),
    Band("B7", 2620, 2690, "FDD"),
    Band("B7A", 2620, 2680, "FDD"),  # 2024/4/4追加
    Band("B7B", 2640, 2690, "FDD"),  # 2024/4/4追加
    Band("B8", 925, 960, "FDD"),
    Band("B11", 1475.9, 1495.9, "FDD"),
    Band("B12", 729, 746, "FDD"),  # 2024/4/5追加
    Band("B12A", 729, 745, "FDD"),
    Band("B13", 746, 756, "FDD"),
    Band("B14", 758, 768, "FDD"),  # 2024/3/14追加
    Band("B17", 734, 746, "FDD"),
    Band("B18", 860, 875, "FDD"),
    Band("B19", 875, 890, "FDD"),
    Band("B20", 791, 821, "FDD"),
    Band("B21", 1495.9, 1510.9, "FDD"),  # 2024 4/8修正
    Band("B25", 1930, 1995, "FDD"),  # 2024/4/6追加, 4/8修正
    Band("B26", 859, 894, "FDD"),
    Band("B28", 758, 803, "FDD"),
    Band("B28A", 773, 803, "FDD"),  # 2024/4/4追加
    Band("B28B", 758, 788, "FDD"),  # 2024/4/4追加
    Band("B28C", 768, 798, "FDD"),  # 2024/4/4追加
    Band("B28D", 773, 783, "FDD"),  # 2024/4/4追加
    Band("B28E", 761, 791, "FDD"),  # 2024/4/4追加
    Band("B28F", 758, 791, "FDD"),  # 2024/4/4追加
    Band("B28G", 758, 798, "FDD"),  # 2024/4/4追加
    Band("B28H", 758, 788, "FDD"),  # 2024/4/4追加
    Band("B29", 717, 728, "FDD"),
    Band("B30", 2350, 2360, "FDD"),
    Band("B38", 2570, 2620, "TDD"),
    Band("B38A", 2575, 2615, "TDD"),  # 2024/4/4追加
    Band("B38B", 2575, 2595, "TDD"),  # 2024/4/4追加
    Band("B39", 1880, 1920, "TDD"),
    Band("B40", 2300, 2400, "TDD"),
    Band("B41", 2496, 2690, "TDD"),
    Band("B41A", 2496, 2658, "TDD"),  # 2024/4/01追加
    Band("B41B", 2595, 2645, "TDD"),  # 2024/4/01追加
    Band("B41C", 2535, 2655, "TDD"),  # 2024/4/01追加
    Band("B41D", 2535, 2575, "TDD"),  # 2024/4/01追加
    Band("B41E", 2675, 2635, "TDD"),  # 2024/4/01追加
    Band("B41F", 2635, 2675, "TDD"),  # 2024/4/01追加
    Band("B41G", 2535, 2675, "TDD"),  # 2024/4/01追加
    Band("B41H", 2545, 2645, "TDD"),  # 2024/4/01追加
    Band("B41J", 2618, 2690, "TDD"),  # 2024/4/01追加
    Band("B41K", 2515, 2675, "TDD"),  # 2024/4/01追加
    Band("B41L", 2545, 2575, "TDD"),  # 2024/4/01追加
    Band("B41M", 2590, 2690, "TDD"),  # 2024/4/01追加
    Band("B41N", 2496, 2690, "TDD"),  # 2024/4/01追加
    Band("B41Q", 2545, 2595, "TDD"),  # 2024/4/01追加
    Band("B42", 3400, 3600, "TDD"),
    Band("B42A", 3480, 3600, "TDD"),  # 2024/4/01追加
    Band("B42B", 3480, 3650, "TDD"),  # 2024/4/01追加
    Band("B42C", 3560, 3600, "TDD"),  # 2024/4/01追加
    Band("B42D", 3500, 3600, "TDD"),  # 2024/4/01追加
    Band("B42E", 3400, 3500, "TDD"),  # 2024/4/01追加
    Band("B42F", 3420, 3600, "TDD"),  # 2024/4/01追加
    Band("B42G", 3410, 3600, "TDD"),  # 2024/4/01追加
    Band("B42H", 3450, 3600, "TDD"),  # 2024/4/01追加
    Band("B42J", 3400, 3580, "TDD"),  # 2024/4/01追加
    Band("B42K", 3480, 3520, "TDD"),  # 2024/4/01追加
    Band("B42L", 3520, 3560, "TDD"),  # 2024/4/01追加
    Band("B43", 3600, 3800, "TDD"),  # 2024/3/29追加
    Band("B46", 5150, 5925, "TDD"),
    Band("B66", 2110, 2200, "FDD"),
    Band("B66A", 2110, 2180, "FDD"),  # 2024/4/04追加
    Band("B66B", 2110, 2155, "FDD"),  # 2024/4/04追加
    Band("B71", 617, 652, "FDD"),
    Band("B75", 1432, 1517, "FDD"),  # 2024/7/22追加
    Band("B77", 3300, 4200, "TDD"),  # 2024/4/01追加
    Band("B77A", 3900, 4000, "TDD"),  # 2024/4/01追加
    Band("B77B", 3800, 4000, "TDD"),  # 2024/4/01追加
    Band("B77C", 3900, 4100, "TDD"),  # 2024/3/29追加
    Band("B77D", 3700, 3980, "TDD"),  # 2024/4/01追加
    Band("B77E", 3700, 3800, "TDD"),  # 2024/4/01追加
    Band("B77F", 3400, 4000, "TDD"),  # 2024/4/01追加
    Band("B77G", 3450, 3550, "TDD"),  # 2024/4/01追加
    Band("B77H", 3700, 4000, "TDD"),  # 2024/4/01追加
    Band("B77K", 3700, 3900, "TDD"),  # 2024/4/01追加
    Band("B77L", 3500, 4000, "TDD"),  # 2024/4/01追加
    Band("B77M", 3840, 3980, "TDD"),  # 2024/4/01追加
    Band("B77N", 3400, 3600, "TDD"),  # 2024/4/01追加
    Band("B78", 3300, 3800, "TDD"),  # 2024/4/01追加
    Band("B78A", 3300, 3600, "TDD"),  # 2024/4/01追加
    Band("B78AA", 3300, 3670, "TDD"),  # 2024/3/29追加
    Band("B78AB", 3300, 3630, "TDD"),  # 2024/4/01追加
    Band("B78AC", 3480, 3520, "TDD"),  # 2024/4/01追加
    Band("B78AD", 3520, 3560, "TDD"),  # 2024/4/01追加
    Band("B78B", 3500, 3600, "TDD"),  # 2024/3/29追加
    Band("B78C", 3500, 3700, "TDD"),  # 2024/4/01追加
    Band("B78D", 3400, 3600, "TDD"),  # 2024/4/01追加
    Band("B78E", 3400, 3500, "TDD"),  # 2024/4/01追加
    Band("B78F", 3420, 3600, "TDD"),  # 2024/4/01追加
    Band("B78G", 3600, 3800, "TDD"),  # 2024/4/01追加
    Band("B78H", 3542, 3700, "TDD"),  # 2024/3/29追加
    Band("B78J", 3410, 3600, "TDD"),  # 2024/3/29追加
    Band("B78K", 3420, 3800, "TDD"),  # 2024/3/29追加
    Band("B78L", 3500, 3800, "TDD"),  # 2024/4/01追加
    Band("B78M", 3450, 3650, "TDD"),  # 2024/4/01追加
    Band("B78N", 3550, 3700, "TDD"),  # 2024/4/01追加
    Band("B78Q", 3300, 3500, "TDD"),  # 2024/4/01追加
    Band("B78R", 3420, 3650, "TDD"),  # 2024/4/01追加
    Band("B78S", 3700, 3800, "TDD"),  # 2024/4/01追加
    Band("B78T", 3410, 3610, "TDD"),  # 2024/3/29追加
    Band("B78U", 3300, 3650, "TDD"),  # 2024/4/01追加
    Band("B78V", 3410, 3800, "TDD"),  # 2024/4/01追加
    Band("B78W", 3300, 3580, "TDD"),  # 2024/3/29追加
    Band("B78Y", 3300, 3800, "TDD"),  # 2024/3/29追加
    Band("B78Z", 3300, 3620, "TDD"),  # 2024/3/29追加
    Band("B79", 4400, 5000, "TDD"),  # 2024/4/01追加
    Band("B79A", 4800, 5000, "TDD"),  # 2024/4/01追加
    Band("B79B", 4800, 4900, "TDD"),  # 2024/4/01追加
    Band("B79C", 4400, 4900, "TDD"),  # 2024/4/01追加
    Band("B79D", 4700, 5000, "TDD"),  # 2024/4/01追加
    Band("B85", 728, 746, "FDD"),  # 2024/3/14追加
    # 5G bands
    Band("n1", 2110, 2170, "FDD"),
    Band("n2", 1930, 1990, "FDD"),
    Band("n3", 1805, 1880, "FDD"),
    Band("n5", 869, 894, "FDD"),
    Band("n7", 2620, 2690, "FDD"),
    Band("n8", 925, 960, "FDD"),
    Band("n20", 791, 821, "FDD"),
    Band("n24", 1525, 1559, "FDD"),  # 2024/4/08追加
    Band("n25", 1930, 1995, "FDD"),  # 2024/4/08追加
    Band("n26", 859, 894, "FDD"),  # 2024/4/08追加
    Band("n28", 758, 803, "FDD"),  # 2024/4/08追加
    Band("n30", 2350, 2360, "FDD"),  # 2024/4/08追加
    Band("n34", 2010, 2025, "TDD"),  # 2024/4/08追加
    Band("n38", 2570, 2620, "TDD"),
    Band("n40", 2300, 2400, "TDD"),
    Band("n41", 2496, 2690, "TDD"),
    Band("n46", 5150, 5925, "TDD"),
    Band("n66", 2110, 2200, "FDD"),
    Band("n71", 617, 652, "FDD"),
    Band("n77", 3300, 4200, "TDD"),
    Band("n78", 3300, 3800, "TDD"),
    Band("n79", 4400, 5000, "TDD"),
    Band("n96", 5925, 7125, "TDD"),  # 2024/10/7追加
    Band("n102", 5925, 6425, "TDD"),  # 2024/10/7追加
    Band("n104", 6425, 7125, "TDD"),  # 2024/6/25追加
    Band("n257", 26500, 29500, "TDD"),
    Band("n258", 24250, 27500, "TDD"),
    Band("n260", 37000, 40000, "TDD"),
    Band("n261", 27500, 28350, "TDD"),
]

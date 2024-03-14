# Operator のクラス定義
class Operator:
    def __init__(self, name, headquarters, subscribers, *bands):
        self.name = name
        self.headquarters = headquarters
        self.subscribers = subscribers
        self.bands = bands

    def has_bands(self, number):
        return number in self.bands


# オペレーターのインスタンスを作成
operators = [
    Operator(
        "China Mobile", "China", 986, "B1", "B38", "B39", "B40", "B41", "n78", "n79"
    ),
    Operator(
        "Bharti Airtel",
        "India",
        497,
        "B3",
        "B5",
        "B8",
        "B1",
        "B40",
        "n28",
        "n78",
        "n258",
    ),
    Operator("Reliance Jio", "India", 436, "B3", "B5", "B40", "n28", "n78", "n258"),
    Operator("China Telecom", "China", 391, "B1", "B3", "B40", "B41", "n78", "n38"),
    Operator("China Unicom", "China", 928, "B1", "B3", "B41", "n78", "n41"),
    Operator(
        "China Broadcast",
        "China",
        105,
        "B28",
        "n28",
        "n77",
        "n78",
    ),
    Operator(
        "America Movil",
        "Mexico",
        308,
        "B2",
        "B4",
        "B7",
        "B5",
        "B66",
        "B28",
        "n7",
        "n41",
        "n66",
        "n78",
    ),
    Operator("MTN", "South Africa", 289, "B1", "B3", "B40", "n78", "n1", "n3"),
    Operator("Vodafone Group", "UK", 286, "B1", "B7", "B20", "n28", "n42"),
    Operator(
        "Telefonica",
        "Spain",
        278,
        "B3",
        "B7",
        "B20",
        "B38",
        "n28",
        "n20",
        "n8",
        "n3",
        "n1",
        "n38",
        "n7",
        "n78",
        "n257",
        "n258",
    ),
    Operator("Orange", "France", 249, "B1", "B3", "B7", "B20", "B28"),
    Operator("Vodafone Idea", "India", 231, "B3", "B8", "B1", "B40", "B41"),
    Operator(
        "AT&T",
        "United States",
        217,
        "B2",
        "B4",
        "B12",
        "B14",  # 2024/3/14 追加 https://urgentcomm.com/2021/02/22/att-says-firstnet-band-14-buildout-more-than-90-done-adoption-tops-2-million-connections/
        "B17",
        "B29",
        "B30",
        "B66",
        "n2",
        "n5",
        "n77",
        "n258",
        "n260",
        "n261",
    ),  # 確度高い AT&T web+　Wilson amp情報
    Operator("Deutsche Telekom", "Germany", 212, "B1", "B3", "B7", "B20", "B28", "n28"),
    Operator(
        "PT Telekomunikasi",
        "Indonesia",
        176,
        "B3",
        "B5",
        "B8",
        "B40",
        "n40",
        "n1",
        "n3",
        "n40",
    ),
    Operator("Telenor", "Norway", 172, "B7", "B20"),
    Operator("Axiata", "Malaysia", 163, "B1", "B3", "B7", "B40", "B41"),
    Operator("Emirates", "UAE", 159, "B3", "B7", "B20", "B42", "n78"),
    Operator("VEON", "Netherlands", 157, "B1", "B3", "B7", "B20", "B28", "n28"),
    Operator(
        "Verizon",
        "United States",
        143,
        "B13",
        "B2",
        "B4",
        "B66",
        "n77",
        "n2",
        "n5",
        "n66",
        "n77",
        "n260",
        "n261",
    ),
    Operator("Vodacom", "South Africa", 133, "B8", "B3", "B42"),
    Operator("Ooredoo", "Qatar", 121, "B3", "B8", "B1"),
    # T-Mobile may be part of Deutche Telecom, but left as it is
    Operator(
        "T-Mobile",
        "United States",
        121,
        "B2",
        "B12",
        "B71",
        "B5",
        "B4",
        "B66",
        "n71",
        "n41",
        "n258",
        "n260",
        "n261",
    ),
    Operator("Viettel", "Vietnam", 110, "B1", "B3", "B7", "n78", "n257", "n258"),
    Operator("BSNL Mobile", "India", 106, "B3", "B8", "B41"),
    Operator("CK Hutchison", "Hong Kong", 100, "B1", "B8", "B3", "B7", "B40"),
    Operator("MTN Irancell", "Iran", 92, "B1", "B8", "B3", "B7", "B42"),
    Operator(
        "Mobile TeleSystems", "Russia", 84, "B3", "B7", "B20", "B38", "B40", "B46"
    ),
    Operator(
        "NTT Docomo",
        "Japan",
        83,
        "B28",
        "B18",
        "B26",
        "B19",
        "B8",
        "B11",
        "B21",
        "B3",
        "B1",
        "B42",
        "n1",
        "n28",
        "n78",
        "n77",
        "n79",
        "n257",
    ),
    Operator("Globe Telecom", "Philippines", 54, "B28", "B40", "B41"),
    Operator("PLDT", "Philippines", 53, "B5", "B28", "B41"),
    Operator("MegaFon", "Russia", 71, "B3", "B7", "B20", "B38"),
    Operator(
        "KDDI",
        "Japan",
        66,
        "B28",
        "B18",
        "B26",
        "B19",
        "B8",
        "B11",
        "B21",
        "B3",
        "B1",
        "B42",
        "n28",
        "n3",
        "n78",
        "n77",
        "n79",
        "n257",
    ),  # 確度高い KDDI web site
    Operator(
        "Softbank",
        "Japan",
        54,
        "B12",
        "B28",
        "B17",
        "B18",
        "B26",
        "B19",
        "B8",
        "B11",
        "B21",
        "B3",
        "B4",
        "B2",
        "B1",
        "B4",
        "B39",
        "B40",
        "B38",
        "B42",
        "B41",
        "n77",
        "n257",
    ),  # 4G確度高い Softbank web
]

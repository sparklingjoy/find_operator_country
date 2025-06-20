# Operator のクラス定義
class Operator:
    def __init__(self, name, headquarters, oran_status, subscribers, *bands):
        self.name = name
        self.headquarters = headquarters
        self.oran_status = oran_status  # non_member, member_inactive, member_active
        self.subscribers = subscribers
        self.bands = bands

    def has_bands(self, number):
        return number in self.bands


# オペレーターのインスタンスを作成
operators = [
    # Jerry より https://zhuanlan.zhihu.com/p/616370411 teamsにあり
    Operator(
        "China Mobile",
        "China",
        "member_inactive",
        997,
        "B3",  # 2024/06/11 追加
        "B8",  # 2024/06/11 追加
        "B34",
        "B39",
        "B40",
        "B41",
        "n41",  # 2024/06/11 修正 n78を消去
        "n79",
    ),
    Operator(
        "Bharti Airtel",
        "India",
        "member_active",
        390, # udapted 2025/6/12
        "B3",
        "B5",
        "B8",
        "B1",
        "B40",
        # "n28", 2025/5/8 削除
        "n78",
        "n258",
    ),
    Operator(
        "Reliance Jio",
        "India",
        "member_active",
        470, # udapted 2025/6/12 https://www.business-standard.com/industry/news/reliance-jio-leads-mobile-subscriber-additions-in-march-trai-data-125050701676_1.html
        "n3", # 2025/5/8 B3からn3に修正
        "n5", # 2025/5/8 B3からn5に修正
        "B40",
        "n28",
        "n78",
        "n258",
    ),
    Operator(
        "China Telecom",
        "China",
        "member_inactive",
        413,
        "B1",  # 2024/6/11 追加修正
        "B3",
        "B5",
        "B41",
        "n1",  # 2024/6/11 追加修正
        "n77",
        "n78",
    ),
    Operator(
        "China Unicom",
        "China",
        "member_inactive",
        333,
        "B1",  # 2024/6/11 追加修正
        "B3",
        "B5", # 2025/5/8 B8からB5に修正
        "B40",
        "B41",
        "n1",  # 2024/6/11 追加修正
        "n5",  # 2025/5/8 n77からn5に修正
        "n78",
    ),
    Operator(
        "China Broadcast",
        "China",
        "member_inactive",
        105,
        "B28",
        "n28",
        "n77",
        "n79",
    ),
    Operator(
        "America Movil",
        "Mexico",
        "non_member",
        312,
        "B2",
        "B4",
        "B7",
        "B5",
        # "B66", 2025/5/9 削除 peplexity で調査
        "B28",
        "n7",
        # "n41", 2025/5/9 削除 peplexity で調査
        # "n66", 2025/5/9 削除 peplexity で調査
        "n78",
    ),
    Operator(
        "MTN", "South Africa", "non_member", 287, "B1", "B3", "B7", "B20", "B28", "B8", "n78", "n28"
    ), # 2025/5/9 修正 perplexity で調査
    Operator(
        "Vodafone Group",
        "UK",
        "member_active",
        323,
        "B1",
        "B3",
        "B7",
        "B8",
        "B20",
        "B32",
        "B38",
        "n78",
    ),
    Operator(
        "Telefonica",
        "Spain",
        "member_active",
        299,
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
    Operator("Orange", "France", "member_active", 243, "B1", "B3", "B7", "B20", "B28"),
    Operator(
        "Vodafone Idea",
        "India",
        "member_active",
        205, # udapted 2025/6/12
        "B3",
        "B8",
        "B1",
        "B40",
        "B41",
        "n78",
        "n258",
    ),  # https://www.lightreading.com/open-ran/vodafone-idea-launches-open-ran-pilot-in-india-with-mavenir 2024/3/14 added
    Operator(
        "AT&T",
        "United States",
        "member_active",
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
    Operator(
        "Deutsche Telekom",
        "Germany",
        "member_active",
        256,
        "B1",
        "B3",
        "B7",
        "B20",
        "B28",
        "n28",
    ),
    Operator(
        "PT Telekomunikasi",
        "Indonesia",
        "non_member",
        159,
        "B3",
        "B5",
        "B8",
        "B40",
        "n40",
        "n1",
        "n3",
        "n40",
    ),
    Operator("Telenor", "Norway", "non_member", 93, "B7", "B20"),
    Operator("Axiata", "Malaysia", "non_member", 163, "B1", "B3", "B7", "B40", "B41"),
    Operator("Emirates", "UAE", "non_member", 159, "B3", "B7", "B20", "B42", "n78"),
    Operator(
        "VEON", "Netherlands", "non_member", 157, "B1", "B3", "B7", "B20", "B28", "n28"
    ),
    Operator(
        "Verizon",
        "United States",
        "member_active",
        143,
        "B13",
        "B2",
        "B4",
        "B66",
        "n2",
        "n5",
        "n66",
        "n77",
        "n260",
        "n261",
    ),  # duplicated n77 was removed 2024/3/25
    Operator("Vodacom", "South Africa", "non_member", 155, "B8", "B3", "B42"),
    Operator("Ooredoo", "Qatar", "non_member", 121, "B3", "B8", "B1"),
    # T-Mobile may be part of Deutche Telecom, but left as it is
    Operator(
        "T-Mobile",
        "United States",
        "member_active",
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
    Operator(
        "Viettel", "Vietnam", "non_member", 110, "B1", "B3", "B7", "B28", "B29", "n28", "n78", "n257", "n258"
    ), # 2025/5/27 added B28, B29, n28  B2-B2′ block (713–723 MHz and 768–778 MHz) https://www.rcrwireless.com/20250523/5g/viettel-700-mhz-5g
    Operator("BSNL Mobile", "India", "non_member", 89.6, "B3", "B8", "B41"), # updated 2025/6/12
    Operator(
        "CK Hutchison", "Hong Kong", "non_member", 120, "B1", "B8", "B3", "B7", "B40"
    ),
    Operator("MTN Irancell", "Iran", "non_member", 92, "B1", "B8", "B3", "B7", "B42"),
    Operator(
        "Mobile TeleSystems",
        "Russia",
        "non_member",
        84,
        "B3",
        "B7",
        "B20",
        "B38",
        "B40",
        "B46",
    ),
    Operator(
        "NTT Docomo",
        "Japan",
        "member_active",
        91, #updated 2025/6/12
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
    Operator(
        "Rakuten Mobile",
        "Japan",
        "member_active",
        8.6, #updated 2025/6/12
        "B3",
        "B18",
        "B28",
        "n3",
        "n77",
        "n257",
    ),
    Operator("Globe Telecom", "Philippines", "non_member", 54, "B28", "B40", "B41"),
    Operator("PLDT", "Philippines", "non_member", 53, "B5", "B28", "B41"),
    Operator("MegaFon", "Russia", "non_member", 71, "B3", "B7", "B20", "B38"),
    Operator(
        "KDDI",
        "Japan",
        "member_active",
        70, #updated 2025/6/12
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
        "member_active",
        55, #updated 2025/6/12
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
        "B39",
        "B40",
        "B38",
        "B42",
        "B41",
        "n77",
        "n257",
    ),  # 4G確度高い Softbank web
    Operator(
        "SK telecom",
        "Korea",
        "member_active",
        30,
        "B1",
        "B3",
        "B5",
        "B7",
        "n78",
        "n257",
    ),  # telecomのtは小文字を使っているので要注意 大文字だと拾わない
    Operator(
        "Chunghwa Telecom",
        "Taiwan",
        "member_active",
        13,
        "B1",
        "B3",
        "B7",
        "n1",
        "n78",
        "n257",
    ),  #
]

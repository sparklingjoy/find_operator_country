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
        "n28", # 2025/07/30 https://www.frequencycheck.com/carriers
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
        "B3", # 2025/7/30 追加 https://www.frequencycheck.com/carriers
        "B5", # 2025/7/30 追加 https://www.frequencycheck.com/carriers
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
        "B40", # 2025/7/30 B41からB40に修正 
        "n1",  # 2024/6/11 追加修正
        "n5",  # 2025/7/30 追加 https://www.frequencycheck.com/carriers
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
        "B8", # 2025/7/30 追加 https://www.frequencycheck.com/carriers
        "B40",
        "n1",  # 2024/6/11 追加修正
        "n8",  # 2025/7/30 n5からn8に修正 https://www.frequencycheck.com/carriers
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
        "Telcel", # 2025/7/30 America MovilをTelcelに変更
        "Mexico",
        "non_member",
        312,
        "B4",
        "B66", # 2025/5/9 削除 → 2025/7/30 復帰 https://www.frequencycheck.com/carriers
        "n5", 
    ),
    Operator(
        "MTN", "South Africa", "non_member", 287, "B3", "n78",
    ), # 2025/7/30 削除  https://www.frequencycheck.com/carriers
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
        "n1", # 2025/7/30 追加  https://www.frequencycheck.com/carriers
        "n8", # 2025/7/30 追加  https://www.frequencycheck.com/carriers
        "n78",
    ),
    Operator(
        "Movistar", # 2025/7/30 Telefonicaから変更  https://www.frequencycheck.com/carriers 
        "Spain",
        "member_active",
        299,
        "B1",
        "B3",
        "B7",
        "B8",
        "B28",
        "B20",
        "n28",
        "n3",
        "n1",
        "n78",
        "n258",
    ),
    Operator("Orange", "France", "member_active", 243, "B1", "B3", "B7", "B20", "B28", "n1","n78",),
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
        "B5",
        "B12",
        "B14",  # 2024/3/14 追加 https://urgentcomm.com/2021/02/22/att-says-firstnet-band-14-buildout-more-than-90-done-adoption-tops-2-million-connections/
        "B17",
        "B29",
        "B30",
        "B46",
        "B48",
        "B66",
        "n2",
        "n5",
        "n66", 
        "n77",
        "n260",
        "n261",
    ),  
    Operator(
        "Deutsche Telekom",
        "Germany",
        "member_active",
        256,
        "B1",
        "B3",
        "B7",
        "B8",
        "B20",
        "B28",
        "B32",
        "n1",
        "n3",
        "n77",
        "n78",
    ),
    Operator(
        "Telecomsel",
        "Indonesia",
        "non_member",
        159,
        "B3",
        "B8",
        "B40",
        "n40",
        "n1",
    ),
    Operator("Telenor", "Norway", "non_member", 93, "B3", "B7", "B20"),
    Operator("Celcomdigi", "Malaysia", "non_member", 163, "B1", "B3", "B7", "n26", "n28", "n78"),
    Operator("du", "UAE", "non_member", 159, "B3", "B1", "B8", "B20", "B28", "n78"),
    Operator(
        "KPN", "Netherlands", "non_member", 157, "B3", "B7", "B20", "B38", "n1", "n78", "n28"
    ),
    Operator(
        "Verizon",
        "United States",
        "member_active",
        143,
        "B13",
        "B2",
        "B4",
        "B5",
        "B46",
        "B48",
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
        "Viettel", "Vietnam", "non_member", 110, "B3", ), 
    Operator("BSNL Mobile", "India", "non_member", 89.6, "B3", "B5", "B28", "B1", "B41", "n28", "n78", "n258"), # updated 2025/7/30
    Operator(
        "CMHK", "Hong Kong", "non_member", 120,  "B3", "B7", "B40", "n1", "n78", "n79"
    ),
    Operator("MTN Irancell", "Iran", "non_member", 92, "B3", "B7", "B42", "n78"),
    Operator(
        "Mobile TeleSystems",
        "Russia",
        "non_member",
        84,
        "B3",
        "B7",
        "B8",
        "B20",
        "B34",
        "B38",
        "n7",
        "n79",
        "n258",
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
    Operator("Globe Telecom", "Philippines", "non_member", 54, "B28", "B3", "B7", "B41", "n41", "n78"),
    Operator("Smart", "Philippines", "non_member", 53, "B1", "B3", "B5", "B28", "B40", "B41", "n28", "n41", "n78"),
    Operator("MegaFon", "Russia", "non_member", 71, "B1", "B3", "B7", "B8", "B34", "B41", "n1", "n7", "n257", "n258"),
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
        "B8",
        "n1",
        "n78",
    ),  
]

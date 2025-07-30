# 国のクラス、オペレーターを紐づける
class Country:
    def __init__(
        self, name, *operators
    ):  # オペレーターは可変数長因数で複数を受け付ける
        self.name = name
        self.operators = operators

    def has_operators(
        self, player
    ):  # 複数のオペレーターの中に、playerが合致すれば、playerを返す
        # print("in loop")
        return player in self.operators


# 国のインスタンスを作成
countries = [
    Country(
        "China", "China Mobile", "China Telecom", "China Unicom", "China Broadcast"
    ),
    Country("Hong Kong", "CMHK", "China Mobile", "China Unicom"),
    Country("India", "Bharti Airtel", "Reliance Jio", "Vodafone Idea", "BSNL Mobile"),
    Country("Pakistan", "China Mobile", "Telenor", "du", "KPN"),
    Country("Macau", "China Telecom", "CMHK"),
    Country("Japan", "NTT Docomo", "KDDI", "Softbank","Rakuten Mobile"),
    Country("United States", "AT&T", "Verizon", "T-Mobile"),
    Country(
        "Canada",
        "AT&T",
    ),
    # Airtel India
    Country("Chad", "Bharti Airtel", "du"),
    Country("Bangladesh", "Bharti Airtel", "Telenor", "Celcomdigi", "KPN"),
    Country("Congo", "Bharti Airtel", "Orange", "Vodacom"),
    Country("Gabon", "Bharti Airtel", "du"),
    Country("Guernsey", "Bharti Airtel"),
    Country("Jersey", "Bharti Airtel"),
    Country("Kenya", "Bharti Airtel", "Vodacom"),
    Country("Madagascar", "Bharti Airtel", "Orange"),
    Country("Malawi", "Bharti Airtel"),
    Country("Niger", "Bharti Airtel", "Orange", "du"),
    Country("Nigeria", "Bharti Airtel", "MTN"),
    Country("Congo", "Bharti Airtel", "MTN"),
    Country("Kenya", "Bharti Airtel", "Orange"),
    Country("Rwanda", "Bharti Airtel", "MTN"),
    Country("Seychelles", "Bharti Airtel"),
    Country("Sri Lanka", "Bharti Airtel", "Celcomdigi", "CMHK"),
    Country("Tanzania", "Bharti Airtel", "Vodafone Group", "Vodacom", "Viettel"),
    Country("Uganda", "Bharti Airtel", "MTN"),
    Country("Zambia", "Bharti Airtel", "MTN"),
    # Telcel Mexico
    Country("Argentina", "Telcel", "Movistar"),
    Country("Austria", "Telcel", "Deutsche Telekom", "CMHK"),
    Country("Belarus", "Telcel", "Mobile Telesystems"),
    Country("Brazil", "Telcel", "Vodafone Group", "Movistar"),
    Country("Bulgaria", "Telcel"),
    Country("Chile", "Telcel", "Movistar"),
    Country("Columbia", "Telcel", "Movistar"),
    Country("Costa", "Telcel"),
    Country("Croatia", "Telcel", "Deutsche Telekom"),
    Country("Dominican Republic", "Telcel", "Orange"),
    Country("Ecuador", "Telcel", "Movistar"),
    Country("El Salvador", "Telcel"),
    Country("Guatemala", "Telcel"),
    Country("Honduras", "Telcel"),
    Country("Liechtenstein", "Telcel"),
    Country("Mexico", "Telcel", "Movistar", "AT&T"),
    Country("Nicaragua", "Telcel"),
    Country("North Macedonia", "Telcel", "Deutsche Telekom"),
    Country("Panama", "Telcel"),
    Country("Paraguay", "Telcel"),
    Country("Peru", "Telcel", "Movistar", "Viettel"),
    Country("Puerto Rico", "Telcel", "Deutsche Telekom", "Verizon"),
    Country("Serbia", "Telcel"),
    Country("Slovenia", "Telcel"),
    Country("Uruguay", "Telcel", "Movistar"),
    # MTN South Africa
    Country("Afghanistan", "MTN", "du"),
    Country("Benin", "MTN", "du"),
    Country("Botswana", "MTN", "Orange"),
    Country("Cameroon", "MTN", "Orange", "Viettel"),
    Country("Eswatini", "MTN"),
    Country("Ghana", "MTN"),
    Country("Guinea", "MTN", "Orange"),
    Country("Guinea Bissau", "MTN", "Orange"),
    Country("Iran", "MTN"),
    Country("Ivory Coast", "MTN", "Orange", "du"),
    Country("Liberia", "MTN"),
    Country("South Africa", "MTN", "Vodafone Group", "Vodacom"),
    Country("South Sdan", "MTN"),
    Country("Sudan", "MTN", "Movistar"),
    Country("Syria", "MTN"),
    Country("Yemen", "MTN"),
    # Vodafone UK
    Country("Albania", "Vodafone Group"),
    Country("Australia", "Vodafone Group"),
    Country("Cyprus", "Vodafone Group"),
    Country("Czech Republic", "Vodafone Group", "Deutsche Telekom"),
    Country("Egypt", "Vodafone Group", "Orange", "du"),
    Country("Fiji", "Vodafone Group"),
    Country("Germany", "Vodafone Group", "Movistar", "Deutsche Telekom"),
    Country("Greece", "Vodafone Group", "Deutsche Telekom"),
    Country("Hungary", "Vodafone Group", "Deutsche Telekom"),
    Country("Iceland", "Vodafone Group"),
    Country("Ireland", "Vodafone Group", "CMHK"),
    Country("Italy", "Vodafone Group", "CMHK"),
    Country("Iraq", "Vodafone Group", "Orange", "Ooredoo"),
    Country("Jordan", "Vodafone Group", "Orange"),
    Country("Netherlands", "Vodafone Group"),
    Country("New Zealand", "Vodafone Group"),
    Country("Northan Cyprus", "Vodafone Group"),
    Country("Portugal", "Vodafone Group"),
    Country("Qatar", "Vodafone Group", "Ooredoo"),
    Country("Romania", "Vodafone Group", "Orange", "Deutsche Telekom"),
    Country("Spain", "Vodafone Group", "Movistar", "Orange"),
    Country("Turkey", "Vodafone Group"),
    Country("Ukraine", "Vodafone Group", "KPN"),
    Country("United Kingdom", "Vodafone Group", "Movistar", "CMHK"),
    # Movistar Spain
    Country("Venezuela", "Movistar"),
    # Orange France
    Country("Belgium", "Orange"),
    Country("Central African Republic", "Orange", "du"),
    Country("Equatorial Guinea", "Orange"),
    Country("France", "Orange"),
    Country("Luxemboug", "Orange"),
    Country("Mali", "Orange", "du"),
    Country("Moldova", "Orange"),
    Country("Morocco", "Orange", "du"),
    Country("Poland", "Orange", "Deutsche Telekom"),
    Country("Saudi Arabia", "Orange", "du"),
    Country("Senegal", "Orange"),
    Country("Slovakia", "Orange", "Deutsche Telekom"),
    Country("Tunisia", "Orange", "Ooredoo"),
    # Deutsche Telekom Germany
    Country("Bosnia and Herzegovina", "Deutsche Telekom"),
    Country("Montenegro", "Deutsche Telekom"),
    Country("Indonesia", "Telecomsel", "Celcomdigi", "Ooredoo", "CMHK"),
    Country("East Timor", "Telecomsel", "Viettel"),
    # Telenor Norway
    Country("Denmark", "Telenor", "CMHK"),
    Country("Finland", "Telenor"),
    Country("Malaysia", "Telenor", "Celcomdigi"),
    Country("Norway", "Telenor"),
    Country("Sweden", "Telenor", "CMHK"),
    Country("Thailand", "Telenor"),
    Country("Tonga", "Telenor"),
    # Celcomdigi Malaysia
    Country("Cambodia", "Celcomdigi", "Viettel"),
    Country("Nepal", "Celcomdigi"),
    # du UAE
    Country("Burkina Faso", "du"),
    Country("Mauritania", "du"),
    Country("Togo", "du"),
    Country("United Arab du", "du"),
    # KPN Netherland
    Country("Kazakhstan", "KPN"),
    Country("Kyrgyzstan", "KPN"),
    Country("Uzbekistan", "KPN"),
    # Verizon USA
    Country("Virgin Islands", "Verizon"),
    # Vodacom South Africa
    Country("Lesotho", "Vodacom"),
    Country("Mozambique", "Vodacom", "Viettel"),
    Country("Ethiopia", "Vodacom"),
    # Ooredoo Qatar
    Country("Algeria", "Ooredoo"),
    Country("Kuwait", "Ooredoo"),
    Country("Maldive", "Ooredoo"),
    Country("Myanmar", "Ooredoo", "Viettel"),
    Country("Oman", "Ooredoo"),
    # Vittel Vietnam
    Country("Burundi", "Viettel"),
    Country("Haiti", "Viettel"),
    Country("Laos", "Viettel"),
    Country("Vietnam", "Viettel", "CMHK"),
    # MTN Irancell
    Country("Iran", "MTN Irancell"),
    # Mobile TeleSystems Russia
    Country("Russia", "Mobile TeleSystems", "MegaFon"),
    Country("Armenia", "Mobile TeleSystems"),
    # Globe Telecom Philippines
    Country("Philippines", "Globe Telecom", "PLDT"),
    # Korea
    Country("Korea", "SK telecom", "KTF", "LG Uplus"),
    # Taiwan
    Country(
        "Taiwan", "Chunghwa Telecom", "Far EasTone Telecommunications", "Taiwan Mobile"
    ),
]

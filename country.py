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
    Country("Hong Kong", "CK Huchinson", "China Mobile", "China Unicom"),
    Country("India", "Bharti Airtel", "Reliance Jio", "Vodafone Idea", "BSNL Mobile"),
    Country("Pakistan", "China Mobile", "Telenor", "Emirates", "VEON"),
    Country("Macau", "China Telecom", "CK Huchinson"),
    Country("Japan", "NTT Docomo", "KDDI", "Softbank"),
    Country("United States", "AT&T", "Verizon", "T-Mobile"),
    Country(
        "Canada",
        "AT&T",
    ),
    # Airtel India
    Country("Chad", "Bharti Airtel", "Emirates"),
    Country("Bangladesh", "Bharti Airtel", "Telenor", "Axiata", "VEON"),
    Country("Congo", "Bharti Airtel", "Orange", "Vodacom"),
    Country("Gabon", "Bharti Airtel", "Emirates"),
    Country("Guernsey", "Bharti Airtel"),
    Country("Jersey", "Bharti Airtel"),
    Country("Kenya", "Bharti Airtel", "Vodacom"),
    Country("Madagascar", "Bharti Airtel", "Orange"),
    Country("Malawi", "Bharti Airtel"),
    Country("Niger", "Bharti Airtel", "Orange", "Emirates"),
    Country("Nigeria", "Bharti Airtel", "MTN"),
    Country("Congo", "Bharti Airtel", "MTN"),
    Country("Kenya", "Bharti Airtel", "Orange"),
    Country("Rwanda", "Bharti Airtel", "MTN"),
    Country("Seychelles", "Bharti Airtel"),
    Country("Sri Lanka", "Bharti Airtel", "Axiata", "CK Huchinson"),
    Country("Tanzania", "Bharti Airtel", "Vodafone Group", "Vodacom", "Viettel"),
    Country("Uganda", "Bharti Airtel", "MTN"),
    Country("Zambia", "Bharti Airtel", "MTN"),
    # America Movil Mexico
    Country("Argentina", "America Movil", "Telefonica"),
    Country("Austria", "America Movil", "Deutshe Telekom", "CK Huchinson"),
    Country("Belarus", "America Movil", "Mobile Telesystems"),
    Country("Brazil", "America Movil", "Vodafone Group", "Telefonica"),
    Country("Bulgaria", "America Movil"),
    Country("Chile", "America Movil", "Telefonica"),
    Country("Columbia", "America Movil", "Telefonica"),
    Country("Costa", "America Movil"),
    Country("Croatia", "America Movil", "Deutshe Telekom"),
    Country("Dominican Republic", "America Movil", "Orange"),
    Country("Ecuador", "America Movil", "Telefonica"),
    Country("El Salvador", "America Movil"),
    Country("Guatemala", "America Movil"),
    Country("Honduras", "America Movil"),
    Country("Liechtenstein", "America Movil"),
    Country("Mexico", "America Movil", "Telefonica", "AT&T"),
    Country("Nicaragua", "America Movil"),
    Country("North Macedonia", "America Movil", "Deutshe Telekom"),
    Country("Panama", "America Movil"),
    Country("Paraguay", "America Movil"),
    Country("Peru", "America Movil", "Telefonica", "Viettel"),
    Country("Puerto Rico", "America Movil", "Deutshe Telekom", "Verizon"),
    Country("Serbia", "America Movil"),
    Country("Slovenia", "America Movil"),
    Country("Uruguay", "America Movil", "Telefonica"),
    # MTN South Africa
    Country("Afghanistan", "MTN", "Emirates"),
    Country("Benin", "MTN", "Emirates"),
    Country("Botswana", "MTN", "Orange"),
    Country("Cameroon", "MTN", "Orange", "Viettel"),
    Country("Eswatini", "MTN"),
    Country("Ghana", "MTN"),
    Country("Guinea", "MTN", "Orange"),
    Country("Guinea Bissau", "MTN", "Orange"),
    Country("Iran", "MTN"),
    Country("Ivory Coast", "MTN", "Orange", "Emirates"),
    Country("Liberia", "MTN"),
    Country("South Africa", "MTN", "Vodafone Group", "Vodacom"),
    Country("South Sdan", "MTN"),
    Country("Sudan", "MTN", "Telefonica"),
    Country("Syria", "MTN"),
    Country("Yemen", "MTN"),
    # Vodafone UK
    Country("Albania", "Vodafone Group"),
    Country("Australia", "Vodafone Group"),
    Country("Cyprus", "Vodafone Group"),
    Country("Czech Republic", "Vodafone Group", "Deutshe Telekom"),
    Country("Egypt", "Vodafone Group", "Orange", "Emirates"),
    Country("Fiji", "Vodafone Group"),
    Country("Germany", "Vodafone Group", "Telefonica", "Deutshe Telekom"),
    Country("Greece", "Vodafone Group", "Deutshe Telekom"),
    Country("Hungary", "Vodafone Group", "Deutshe Telekom"),
    Country("Iceland", "Vodafone Group"),
    Country("Ireland", "Vodafone Group", "CK Huchinson"),
    Country("Italy", "Vodafone Group", "CK Huchinson"),
    Country("Iraq", "Vodafone Group", "Orange", "Ooredoo"),
    Country("Jordan", "Vodafone Group", "Orange"),
    Country("Netherlands", "Vodafone Group"),
    Country("New Zealand", "Vodafone Group"),
    Country("Northan Cyprus", "Vodafone Group"),
    Country("Portugal", "Vodafone Group"),
    Country("Qatar", "Vodafone Group", "Ooredoo"),
    Country("Romania", "Vodafone Group", "Orange", "Deutshe Telekom"),
    Country("Spain", "Vodafone Group", "Telefonica", "Orange"),
    Country("Turkey", "Vodafone Group"),
    Country("Ukraine", "Vodafone Group", "VEON"),
    Country("United Kingdom", "Vodafone Group", "Telefonica", "CK Huchinson"),
    # Telefonica Spain
    Country("Venezuela", "Telefonica"),
    # Orange France
    Country("Belgium", "Orange"),
    Country("Central African Republic", "Orange", "Emirates"),
    Country("Equatorial Guinea", "Orange"),
    Country("France", "Orange"),
    Country("Luxemboug", "Orange"),
    Country("Mali", "Orange", "Emirates"),
    Country("Moldova", "Orange"),
    Country("Morocco", "Orange", "Emirates"),
    Country("Poland", "Orange", "Deutshe Telekom"),
    Country("Saudi Arabia", "Orange", "Emirates"),
    Country("Senegal", "Orange"),
    Country("Slovakia", "Orange", "Deutshe Telekom"),
    Country("Tunisia", "Orange", "Ooredoo"),
    # Deutsche Telekom Germany
    Country("Bosnia and Herzegovina", "Deutshe Telekom"),
    Country("Montenegro", "Deutshe Telekom"),
    Country("Indonesia", "PT Telekomunikasi", "Axiata", "Ooredoo", "CK Huchinson"),
    Country("East Timor", "PT Telekomunikasi", "Viettel"),
    # Telenor Norway
    Country("Denmark", "Telenor", "CK Huchinson"),
    Country("Finland", "Telenor"),
    Country("Malaysia", "Telenor", "Axiata"),
    Country("Norway", "Telenor"),
    Country("Sweden", "Telenor", "CK Huchinson"),
    Country("Thailand", "Telenor"),
    Country("Tonga", "Telenor"),
    # Axiata Malaysia
    Country("Cambodia", "Axiata", "Viettel"),
    Country("Nepal", "Axiata"),
    # Emirates UAE
    Country("Burkina Faso", "Emirates"),
    Country("Mauritania", "Emirates"),
    Country("Togo", "Emirates"),
    Country("United Arab Emirates", "Emirates"),
    # VEON Netherland
    Country("Kazakhstan", "VEON"),
    Country("Kyrgyzstan", "VEON"),
    Country("Uzbekistan", "VEON"),
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
    Country("Vietnam", "Viettel", "CK Huchinson"),
    # MTN Irancell
    Country("Iran", "MTN Irancell"),
    # Mobile TeleSystems Russia
    Country("Russia", "Mobile TeleSystems", "Megafon"),
    Country("Armenia", "Mobile TeleSystems"),
    # Globe Telecom Philippines
    Country("Philippines", "Globe Telecom", "PLDT"),
]

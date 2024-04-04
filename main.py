import streamlit as st
import band
import op
import re
import country

bands = band.bands
operators = op.operators
countries = country.countries


def freq_to_band(frequency_to_evaluate):
    try:
        int(frequency_to_evaluate)
        print(f"{frequency_to_evaluate} MHz is used in band:")
    except ValueError:
        print("Input must be integer in MHz.")

    matched_bands = []

    for band in bands:
        if band.is_in_range(frequency_to_evaluate):
            matched_bands.append(band.generation_number)
    print(matched_bands)
    return matched_bands


## バンド名から周波数範囲記述のstrを発生させる、引数はバンド名のstr
def band_to_freq(band_to_evaluate):
    try:
        print(f"{band_to_evaluate} used:")

    except ValueError:
        print("Input must be integer in MHz.")

    matched_frequency = []

    for band in bands:
        if band.covers(band_to_evaluate):
            frequency_range = (
                band.generation_number
                + ": "
                + str(band.minimum)
                + " ~ "
                + str(band.maximum)
                + " MHz  ("
                + str(band.maximum - band.minimum)
                + " MHz)"
            )
            print(frequency_range)
            matched_frequency.append(frequency_range)
    return matched_frequency


## バンドのリストからmainとsubの別々の周波数リストに返す
## n###と三桁まで許容、そしてサブバンドコードのアルファベットは含まないことを$で表している
def main_sub_split(band_list):
    pattern = r"B\d{1,2}$|n\d{1,3}"  # B##, n##
    main_band = []
    sub_band = []
    for element in band_list:
        if re.match(pattern, element):
            main_band.append(element)
        else:
            sub_band.append(element)
    return main_band, sub_band


## 複数のバンド名が入っている文字列をリストに変換する
def str_to_list(string):
    # カンマと前後のスペース複数の組み合わせ("\s*,\s*")か空白のみ("\s+")のいずれかをパターンとして指定、stripで両端の空白を除去
    return re.split(r"\s*,\s*|\s+", string.strip())


#### Sidebar menu begins

## From frequency to band code coversion

st.sidebar.header("Frquency ⇔ Band")

asked_frequency = st.sidebar.number_input(
    "Frequency in MHz?", value=3600, placeholder="Input single frequency value"
)

band_list = freq_to_band(asked_frequency)
main_band, sub_band = main_sub_split(band_list)

st.sidebar.write("**Main bands**")
st.sidebar.write(" , ".join(main_band))
st.sidebar.write("**Sub bands**")
st.sidebar.write(" , ".join(sub_band))

## space
st.sidebar.write(" ")

asked_band = st.sidebar.text_input(
    "Band code?", value="B42, n77, B77D", placeholder="Input band code name(s)"
)

list_of_band = str_to_list(asked_band)
for band in list_of_band:
    band_range = band_to_freq(band)
    st.sidebar.write("".join(band_range))


# Find Operators and Countries
st.title("Find Operators and Countries")

# LTE Operator Finder
st.header("LTE Operators")

asked_bands = st.multiselect(
    "Which 4G/LTE band?",
    [
        "B1",
        "B2",
        "B3",
        "B4",
        "B5",
        "B7",
        "B8",
        "B11",
        "B12",
        "B13",
        "B14",  # 2024/3/14追加
        "B17",
        "B18",
        "B19",
        "B20",
        "B21",
        "B26",
        "B28",
        "B29",
        "B30",
        "B38",
        "B39",
        "B40",
        "B41",
        "B42",
        "B46",
        "B66",
        "B71",
        "B85",  # 2024/3/14追加
    ],
    ["B1", "B42"],
)

for band in asked_bands:
    operator_set = []

    for elem in bands:
        if elem.generation_number == band:
            dup_mode = ", ".join(elem.duplex)
    for operator in operators:
        if operator.has_bands(band):
            operator_set.append(operator.name)
            # headquarter_set.append(operator.headquarters)

    st.write(
        f"**{band} band** is in **{dup_mode}** mode with **{len(operator_set)}** operators"
    )
    # st.write("")
    st.write(", ".join(operator_set))
    # st.write("Their **headquarters** are located in:")
    # st.write(", ".join(headquarter_set))


# 5G Operator Finder
st.header("5G Operators")

asked_bands = st.multiselect(
    "Which 5G band?",
    [
        "n1",
        "n2",
        "n3",
        "n5",
        "n7",
        "n8",
        "n20",
        "n28",
        "n38",
        "n40",
        "n41",
        "n46",
        "n66",
        "n71",
        "n77",
        "n78",
        "n79",
        "n257",
        "n258",
        "n260",
        "n261",
    ],
    ["n38", "n77"],
)

for band in asked_bands:
    operator_set = []
    if elem.generation_number == band:
        dup_mode = ", ".join(elem.duplex)
    for operator in operators:
        if operator.has_bands(band):
            operator_set.append(operator.name)
            # headquarter_set.append(operator.headquarters)
    st.write(
        f"**{band} band** is in **{dup_mode}** mode with **{len(operator_set)}** operators"
    )
    # st.write("")
    st.write(", ".join(operator_set))
    # st.write("Their **headquarters** are located in:")
    # st.write(", ".join(headquarter_set))


# Operator Profile
class Country:
    def __init__(self, name, *operators):
        self.name = name
        self.operators = operators

    def has_operators(self, player):
        # print("in loop")
        return player in self.operators


# Find Operator Information

st.header("Operator Information")

asked_operators = st.multiselect(
    "Which operator?",
    [
        "AT&T",
        "America Movil",
        "Axiata",
        "BSNL Mobile",
        "Bharti Airtel",
        "CK Hutchison",
        "China Broadcast",
        "China Mobile",
        "China Telecom",
        "China Unicom",
        "Deutsche Telekom",
        "Emirates",
        "Globe Telecom",
        "KDDI",
        "MTN",
        "MTN Irancell",
        "MegaFon",
        "Mobile TeleSystems",
        "NTT Docomo",
        "Ooredoo",
        "Orange",
        "PLDT",
        "PT Telekomunikasi",
        "Reliance Jio",
        "Softbank",
        "T-Mobile",
        "Telefonica",
        "Telenor",
        "VEON",
        "Verizon",
        "Viettel",
        "Vodacom",
        "Vodafone Group",
        "Vodafone Idea",
    ],
    ["Verizon", "Bharti Airtel"],
)

for player in asked_operators:
    country_set = []

    for country in countries:
        # print("Player=", player)
        if country.has_operators(player):
            country_set.append(country.name)
    # st.write(
    #     f"**{player}** headquarter is in is serviced in {len(country_set)} countries:"
    # )
    for operator in operators:
        if operator.name == player:
            st.write(
                f"**{player}** uses {len(operator.bands)} bands in **{len(country_set)}** countries with a total of **{operator.subscribers}** million subscribers, headquartered in **{operator.headquarters}**"
            )
            st.write(", ".join(operator.bands))
            st.write(", ".join(country_set))


# Find Operators in Countries

st.header("Country Information")

asked_countries = st.multiselect(
    "Which country?",
    [
        "Afghanistan",
        "Albania",
        "Algeria",
        "Argentina",
        "Armenia",
        "Australia",
        "Austria",
        "Bangladesh",
        "Belarus",
        "Belgium",
        "Benin",
        "Bosnia and Herzegovina",
        "Botswana",
        "Brazil",
        "Bulgaria",
        "Burkina Faso",
        "Burundi",
        "Cambodia",
        "Cameroon",
        "Canada",
        "Central African Republic",
        "Chad",
        "Chile",
        "China",
        "Columbia",
        "Congo",
        "Congo",
        "Costa",
        "Croatia",
        "Cyprus",
        "Czech Republic",
        "Denmark",
        "Dominican Republic",
        "East Timor",
        "Ecuador",
        "Egypt",
        "El Salvador",
        "Equatorial Guinea",
        "Eswatini",
        "Ethiopia",
        "Fiji",
        "Finland",
        "France",
        "Gabon",
        "Germany",
        "Ghana",
        "Greece",
        "Guatemala",
        "Guernsey",
        "Guinea",
        "Guinea Bissau",
        "Haiti",
        "Honduras",
        "Hong Kong",
        "Hungary",
        "Iceland",
        "India",
        "Indonesia",
        "Iran",
        "Iran",
        "Iraq",
        "Ireland",
        "Italy",
        "Ivory Coast",
        "Japan",
        "Jersey",
        "Jordan",
        "Kazakhstan",
        "Kenya",
        "Kenya",
        "Kuwait",
        "Kyrgyzstan",
        "Laos",
        "Lesotho",
        "Liberia",
        "Liechtenstein",
        "Luxemboug",
        "Macau",
        "Madagascar",
        "Malawi",
        "Malaysia",
        "Maldive",
        "Mali",
        "Mauritania",
        "Mexico",
        "Moldova",
        "Montenegro",
        "Morocco",
        "Mozambique",
        "Myanmar",
        "Nepal",
        "Netherlands",
        "New Zealand",
        "Nicaragua",
        "Niger",
        "Nigeria",
        "North Macedonia",
        "Northan Cyprus",
        "Norway",
        "Oman",
        "Pakistan",
        "Panama",
        "Paraguay",
        "Peru",
        "Philippines",
        "Poland",
        "Portugal",
        "Puerto Rico",
        "Qatar",
        "Romania",
        "Russia",
        "Rwanda",
        "Saudi Arabia",
        "Senegal",
        "Serbia",
        "Seychelles",
        "Slovakia",
        "Slovenia",
        "South Africa",
        "South Sdan",
        "Spain",
        "Sri Lanka",
        "Sudan",
        "Sweden",
        "Syria",
        "Tanzania",
        "Thailand",
        "Togo",
        "Tonga",
        "Tunisia",
        "Turkey",
        "Uganda",
        "Ukraine",
        "United Arab Emirates",
        "United Kingdom",
        "United States",
        "Uruguay",
        "Uzbekistan",
        "Venezuela",
        "Vietnam",
        "Virgin Islands",
        "Yemen",
        "Zambia",
    ],
    ["United States", "Brazil"],
)

for q_country in asked_countries:
    operator_set = []
    for country in countries:
        if country.name == q_country:
            operator_set = country.operators
    st.write(f"**{q_country}** has {len(operator_set)} operators:")
    st.write(", ".join(operator_set))

st.write("")
st.write("")
with st.expander("About this app"):
    st.write(
        "This app is a compilation of public domain web information on the top 30 mobile operators. They represent 85\% of all subscribers, but 15\% are not captured. Here are the main reference web links",
        "https://en.wikipedia.org/wiki/List_of_mobile_network_operators",
        "https://en.wikipedia.org/wiki/LTE_frequency_bands",
        "https://en.wikipedia.org/wiki/5G_NR_frequency_bands",
    )

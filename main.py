import streamlit as st
import band
import op
import re
import country

#################################################
## Reads 3 py files #############################

bands = band.bands
operators = op.operators
countries = country.countries

#################################################
## Define functions #############################

def freq_to_band(frequency_to_evaluate):
    try:
        int(frequency_to_evaluate)
        print(f"{frequency_to_evaluate} MHz is used in band:")
    except ValueError:
        print("Input must be integer in MHz.")

    matched_bands = []

    for band in bands:
        if band.is_in_range(frequency_to_evaluate):
            matched_bands.append(band.name)
    print(matched_bands)
    return matched_bands

# バンド名から周波数範囲記述のstrを発生させる、引数はバンド名のstr
def band_to_freq(band_to_evaluate):
    try:
        print(f"{band_to_evaluate} used:")

    except ValueError:
        print("Input must be integer in MHz.")

    matched_frequency = []

    for band in bands:
        if band.covers(band_to_evaluate):
            frequency_range = (
                band.name
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

# B##, n##の並べ替えの関数
def sort_key(item):
    if item.startswith('B'):
        prefix, num = 'B', int(item[1:])
    else:
        prefix, num = 'n', int(item[1:])
    return (prefix, num)

# Operatorのbandから重複のないsetを作りlistに変換
band_set = set()
for operator in operators:
    for band in operator.bands:
        band_set.add(band)
    # {band_set.add(band) for band in operator.bands}     
multi_select_list = list(band_set)

#band リストの並べ替えを実行 関数 sort_keyを参照    
multi_select_list = sorted(multi_select_list, key=sort_key)   
print(multi_select_list)

################################################
#### Sidebar menu begins

## Frequency to band code conversion
st.sidebar.header("Frquency ↔ Band")

asked_frequency = st.sidebar.number_input(
    "Frequency in MHz?", value=2150, placeholder="Input single frequency value"
)

band_list = freq_to_band(asked_frequency)
main_band, sub_band = main_sub_split(band_list)

if main_band:
    st.sidebar.write("**Main bands**")
    st.sidebar.write(" , ".join(main_band))
    if sub_band:
        st.sidebar.write("**Sub bands**")
        st.sidebar.write(" , ".join(sub_band))
else:
    st.sidebar.write("Not found")

## space
st.sidebar.write(" ")

## Band code to frequency conversion with multiselect menu
# generates band code name list from band.py
band_list_db = [band.name for band in bands]

asked_band = st.sidebar.multiselect(
    "Select band(s)",
    band_list_db,
    ["B42", "n77", "B77D"],
)

for band in asked_band:
    band_range = band_to_freq(band)
    st.sidebar.write("".join(band_range))


#############################
## Main Menu Begins##########
#############################


# Find Operators and Countries
st.title("Find Operators and Countries")

# Band and Operators Finder
st.header("Band and Operators")
asked_bands = st.multiselect(
    "Which LTE/5G band?",
    multi_select_list,
    ["B1", "n77", "n41"],
)

for band in asked_bands:
    operator_set = []

    for elem in bands:
        if elem.name == band:
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

st.write("")

with st.expander("Main and sub band"):
    st.write(
        "The main LTE and 5G bands are denoted as B3, B42, and n77. In many cases, it is publicly available which operator uses which band. Sub-bands that are part of the main band are denoted as B42A or B78G. The relationship between sub-bands, operators, and regions is not published, so the 'Band and Operator' section does not have this information. However, you can find frequency and sub-band information in the side menu.",
    )

# Find Operator Information

st.header("Operator Profile")
operator_list = [operator.name for operator in operators]

asked_operators = st.multiselect(
    "Which operator?",
    operator_list,
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


# Find Operators per Country

st.header("Operators per Country")
country_list = [country.name for country in countries]
asked_countries = st.multiselect(
    "Which country?",
    country_list,
    ["United States", "India", "Japan"],
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

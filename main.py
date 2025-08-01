import streamlit as st
from functools import reduce
import band
import op
import re
import country

#################################################
## Reads 3 py files #############################
#################################################

bands = band.bands
operators = op.operators
countries = country.countries

#################################################
## Define functions #############################
#################################################


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
                + str(band.span_is())
                + " MHz)"
            )
            # print(frequency_range)
            matched_frequency.append(frequency_range)
    return matched_frequency


## バンドのリストからmainとsubの別々の周波数リストに返す
## n###と三桁まで許容、そしてサブバンドコードのアルファベットは含まないことを$で表している
def main_sub_split(band_list):
    main_band = []
    sub_band = []
    for element in band_list:
        if re.match(
            (pattern := r"B\d{1,2}$|n\d{1,3}"), element
        ):  # := Walrus operator...
            main_band.append(element)
        else:
            sub_band.append(element)
    return main_band, sub_band


# B##, n##の並べ替えの関数
def sort_key(item):
    if item.startswith("B"):
        prefix, num = "B", int(item[1:])
    else:
        prefix, num = "n", int(item[1:])
    return (prefix, num)


# listの要素をつなげたstrにするときに、A, B, and Cという形にする
def join_strings(str_list):
    length = len(str_list)
    if length == 2:
        return " and ".join(str_list)
    elif length > 2:
        return ", ".join(str_list[:-1]) + ", and " + str_list[-1]
    else:
        return "".join(str_list)


# Operatorのbandから重複のないsetを作りlistに変換
band_set = set()
for operator in operators:
    for band in operator.bands:
        band_set.add(band)
multi_select_list = list(band_set)

# band リストの並べ替えを実行 関数 sort_keyを参照
multi_select_list = sorted(multi_select_list, key=sort_key)


################################################
################################################
#### Sidebar menu begins
################################################
################################################

## Frequency to band code conversion
st.sidebar.header("Frquency ↔ Band")

asked_frequency = st.sidebar.number_input(
    "Frequency in MHz?", value=2150, placeholder="Input single frequency value"
)

band_list = freq_to_band(asked_frequency)
main_band, sub_band = main_sub_split(band_list)

if main_band:
    st.sidebar.write("**Main bands**")
    st.sidebar.markdown(f"- {join_strings(main_band)}")
    if sub_band:
        st.sidebar.write("**Sub bands**")
        st.sidebar.write(f" - {join_strings(sub_band)}")
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
    st.sidebar.markdown(f"- {join_strings(band_range)}")

with st.sidebar.expander("Main and sub bands"):
    st.write(
        "LTE/4G bands start with 'B' and 5G with 'n' and are called main bands. One of the mobile base station OEMs uses sub-bands such as 'B42C' to describe the partial coverage of the main band. In this application, the left side menu covers both main and sub-bands. The right main menu covers the main bands only, as the sub-bands and operator/country information are not publicly known, although the sub-bands appear to have been used for applications in different countries for some time."
    )

#############################
#############################
## Main Menu Begins##########
#############################
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

# Iteration for each input band begins
# list_operator should store operators set for each band
list_operators = []

for band in asked_bands:
    operator_set = set()

    for elem in bands:
        if elem.name == band:
            dup_mode = ", ".join(elem.duplex)
    for operator in operators:
        if operator.has_bands(band):
            operator_set.add(operator.name)
    # This list should be like [{},{},{},.....]
    list_operators.append(operator_set)
    band_range = band_to_freq(band)
    st.write(
        f"**{join_strings(band_range)}** is in **{dup_mode}** mode and used by following **{len(operator_set)}** operators"
    )
    # st.write("")
    st.markdown(f"- {join_strings(list(operator_set))}")

# 共通のオペレータを求める、reduceで再帰的にlist_operatorからAND(intersect)を取っている
# list_operator =[]の状態で intersectionを行うとエラーを起こしたので ifを追加している
if list_operators:
    intersection = reduce(lambda a, b: a.intersection(b), list_operators)

# inputのバンド数が2以上の場合、つまり共通operatorを議論できる場合は表示、さもなければ非表示
if len(asked_bands) > 1:
    if intersection:
        st.write(
            f"**{join_strings(asked_bands)}** are used by **{len(intersection)}** operators in common"
        )
        st.markdown(f"- {join_strings(list(intersection))}")
    else:
        st.write(f"**No common operator** found in **{join_strings(asked_bands)}**")

    st.write("")

# Note

with st.expander("Can not find your band?"):
    st.write(
        "If an operator is trying to migrate from LTE to 5G, they may be found with a B number but not an n number. Sub-bands that are part of the main band are called B42A or B78G, the relationship between operators and regions is not publicly available and is not included in this section. New bands such as n104 do not appear in this section if they are not yet used by the carrier. ",
    )

# Find Operator Information

st.header("Operator Profile")
operator_list = sorted([operator.name for operator in operators])

asked_operators = st.multiselect(
    "Which operator?",
    operator_list,
    ["Verizon", "Bharti Airtel"],
)

# Iteration for each operator begins
# list_bands should store bands set for each operator
list_bands = []

for player in asked_operators:
    country_set = []
    band_set = set()

    for country in countries:
        if country.has_operators(player):
            country_set.append(country.name)

    for operator in operators:
        if operator.name == player:
            st.write(
                f"In **{operator.headquarters}** alone, **{player}** uses following {len(operator.bands)} bands and serves {operator.subscribers} million subscribers.  {player} operates in: {join_strings(country_set)}. "
            )
            sorted_bands = sorted(operator.bands, key=sort_key)
            st.markdown(f"- {join_strings(sorted_bands)}")
            # st.markdown(f"- {player} operates in: {join_strings(country_set)}")
            if operator.oran_status == "member_active":
                st.markdown(f"- {player} is active on O-RAN")
            # This list should be like [{},{},{},.....]
            band_set = set(operator.bands)
            list_bands.append(band_set)

# 共通のバンドを求める、reduceで再帰的にlist_operatorからAND(intersect)を取っている
if list_bands:
    intersection = reduce(lambda a, b: a.intersection(b), list_bands)

# inputのOperator数が2以上の場合、つまり共通bandを議論できる場合は表示、さもなければ非表示
if len(asked_operators) > 1:
    if intersection:
        st.write(
            f"**{join_strings(asked_operators)}** use **{len(intersection)}** band(s) in common"
        )
        sorted_bands = sorted(list(intersection), key=sort_key)
        st.markdown(f"- {join_strings(sorted_bands)}")
    else:
        st.write(
            f"**No common band** found between **{join_strings(asked_operators)}**"
        )

    st.write("")

# Find Operators per Country

st.header("Operators per Country")
country_list = sorted([country.name for country in countries])
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
    st.write(f"**{q_country}** has {len(operator_set)} operator(s):")
    st.markdown(f"- {join_strings(operator_set)}")

st.write("")
st.write("")
with st.expander("Source and coverage"):
    st.write(
        "This app is a compilation of public domain web information on the top 36 mobile operators. In 2024, there were 8.6 billion world wide mobile phone subscribers. The 36 mobile operators represent 84\% of all subscribers. Here are the main reference web links.   \n",
        "https://www.ericsson.com/en/reports-and-papers/mobility-report/dataforecasts/mobile-subscriptions-outlook  (Highly recommended)  \n",
        "https://www.frequencycheck.com/carriers",
        "https://en.wikipedia.org/wiki/List_of_mobile_network_operators",
        "https://en.wikipedia.org/wiki/LTE_frequency_bands",
        "https://en.wikipedia.org/wiki/5G_NR_frequency_bands",
    )

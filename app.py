from itertools import cycle

import streamlit as st

MIN_SERVINGS = 2
MAX_SERVINGS = 4
MAX_COLS = 4

st.title("Food Servings Calculator")

servings_n = st.number_input("Number of servings?", MIN_SERVINGS, MAX_SERVINGS, 2)
cols_n = min(servings_n, MAX_COLS)

servings_raw_grams = []

for serving_i, col in zip(range(servings_n), cycle(st.columns(cols_n))):
    serving_raw_grams = col.number_input(
        f"Serving {serving_i + 1} raw weight (g)", value=100
    )
    servings_raw_grams.append(serving_raw_grams)

total_cooked_grams = st.number_input("Total cooked weight (g)", value=100)

cooked_to_raw_ratio = total_cooked_grams / sum(servings_raw_grams)
avg_serving_cooked_grams = total_cooked_grams / servings_n

st.divider()

for (serving_i, serving_raw_grams), col in zip(
    enumerate(servings_raw_grams), cycle(st.columns(cols_n))
):
    serving_cooked_grams = round(cooked_to_raw_ratio * serving_raw_grams, 2)
    delta = round(serving_cooked_grams - avg_serving_cooked_grams, 2)
    col.metric(
        label=f"Serving {serving_i + 1} cooked weight (g)",
        value=serving_cooked_grams,
        delta=delta if delta != 0 else None,
        delta_color="off",
    )

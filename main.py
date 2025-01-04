import streamlit as st
import pandas as pd

CURRENT_LINK = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
GROWTH_LINK = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_growth_rate'

world_pop = pd.read_csv('world_pop_2050.csv')
total = world_pop.iloc[0]

# Remove the first row - to exclude it from the analysis
world_pop = world_pop.drop(world_pop.index[0])

# Rename some columns to be more presentable
world_pop = world_pop.rename(columns={"pop_2050": "Population in 2050", "growth_rate": "Growth rate"})

# Introduction to the project
st.title("2050 World Population Model")
st.write("This project looks at how world population could look like by 2050 if the population continues to grow on the average rate of population growth from 2005 until 2020 for each country")
st.write("The source data for current population is from [here](%s)" %CURRENT_LINK)
st.write("The source data for population growth is from [here](%s)" %GROWTH_LINK)
st.write(f"Current world pop is {total['Population']:,} \n\n And with this model, by the year 2050, it would become {total['pop_2050']:,} ")

st.subheader('A sample view of the data')
st.write(world_pop.sample(7))

# prompt the user to select the current pop or future pop 
pop_choice = ["Current", "Future, 2050"]
selected_value = st.selectbox("Select timeline", pop_choice)


# Prompt the user to choose how many countries to display
num_rows = len(world_pop)
num_countries = st.number_input('Enter the number of countries to be displayed (Highest pop first):', min_value=1, max_value=num_rows, step=1)

# if the number of countries is large, then switch to a horizontal format
if num_countries > 10:
    horizontal_val = True
else:
    horizontal_val = False

if selected_value == "Current":
    x_column = 'Country'
    y_column = 'Population'
    

elif selected_value == "Future, 2050":
    x_column = 'Country'
    y_column = 'Population in 2050'

if st.button("Show Graph"):
    # Sorting the table by the selected column
    world_pop = world_pop.sort_values(by = y_column, ascending=False)

    # Displaying the graph
    st.bar_chart(data=world_pop.head(num_countries), x=x_column, y=y_column, color=y_column, horizontal = horizontal_val, x_label="Population")

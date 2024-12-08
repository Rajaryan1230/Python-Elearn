import pandas as pd
people_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

people_df = pd.DataFrame(people_data)
print("People DataFrame:\n", people_df)

#-------------------------------------------------------------------

ages = people_df['Age']
print("Ages:\n", ages)

#--------------------------------------------------------------------

first_two_people = people_df.iloc[:2]
print("First two people:\n", first_two_people)

#---------------------------------------------------------------------

name_city_columns = people_df[['Name', 'City']]
print("Names and Cities:\n", name_city_columns)

#--------------------------------------------------------------------

older_than_30 = people_df[people_df['Age'] > 30]
print("People older than 30:\n", older_than_30)

#--------------------------------------------------------------------

bob_charlie_rows = people_df.loc[people_df['Name'].isin(['Bob', 'Charlie'])]
print("Rows for Bob and Charlie:\n", bob_charlie_rows)

#--------------------------------------------------------------------

subset_df = people_df.iloc[:2, :2]
print("First two rows and columns:\n", subset_df)

#-------------------------------------------------------------------

sorted_by_age_desc = people_df.sort_values(by='Age', ascending=False)
print("DataFrame sorted by age (descending):\n", sorted_by_age_desc)
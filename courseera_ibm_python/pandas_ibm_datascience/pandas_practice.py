import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# column labels of df are Name, ID, Department,Salary
#index labels of df are 0,1,2,3 - row
# for loc - loc[row_label, column_label]
# for iloc - iloc[row_index, column_index]
# for df.loc[0:2,'Name':'Department']- 0,1,2 indexes will be covered, and Name,ID,Department... for row labels instead of index we can also use row values also
# for df.iloc[0:2,0:2]- 0,1 indexes will be covered, and Name,ID


# df2=df2.set_index("Name") -- we can set specific column as index column


#creating series from list or array
# s = pd.Series([10, 20, 30, 40, 50], index=[100, 101, 102, 103, 104])
# # print(s)
# #print(s[2])         #❌ KeyError — there's no label `2`

##difference between acessing element via indexing or iloc is iloc will give element of that position, irrespective of index
# print(s.iloc[2])    #✅ 30 — third element (0-based index)
# print(s[102])       #✅ 30 — by label
#
# # Creating a DataFrame from a dictionary
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'Age': [25, 30, 30, 28],
#         'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
# small_df = pd.DataFrame(data)
# print(small_df)
# print("--*--"*10)
# #you can access the columns and rows whether individually or through slicing as shown below
# print(small_df['Name'])  # Access the 'Name' column
# print(small_df.iloc[0:2])   # Access the third row by position
# print("--*--"*10)
# print(small_df.loc[0:2])    # Access the second row by label
# print(small_df[['Name', 'Age']])  # Select specific columns
# print(small_df[1:3])             # Select specific rows

# unique_dates = small_df['Age'].unique()
# print(unique_dates)
# high_above_102 = small_df[small_df['Age'] > 25]
# print(high_above_102)

# math_df = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30]})
# print("original-df\n",math_df)
# Using apply on one column
# math_df['A'] = math_df['A'].apply(lambda x: x + 1)
# OR use vectorized addition
# math_df['A'] = math_df['A'] + 1
# print("modified-df\n",math_df)





df = pd.read_csv('sales_data.csv')

# print(df.head())
# print("-*-"*20)
# print(df.tail(2))  # Last 2 rows
# print("-*-"*20)
# print(df.shape)        # (rows, columns)
# print("-*-"*20)
# print(df.info())       # Summary of dataframe
# print("-*-"*20)
# print(df.describe())   # Stats for numeric columns
# print("-*-"*20)
# print(df.columns)  # shows all column labels in data frame
# print("-*-"*20)
# print(df['Store'].value_counts()) # this shows how frequent each store visited in dataset
# print("-*-"*20)
# print(df['Revenue ($)'].mean())

# print(df[['Store', 'Product', 'Revenue ($)']])  # for printing a slice of a dataframe

#for extracting specific series
# total_stores_data = df['Store']
# print(total_stores_data)

#for extracting a slice of a data frame i.e, more than one series
# new_df = df[['Store', 'Product', 'Revenue ($)']]
# print(new_df)

# for filtering df
# filtered_df = df[
#     (df['Store'] == 'LA') &
#     (df['Product'] == 'Oranges') &
#     (df['Revenue ($)'] > 900)
# ]
# print(filtered_df)

# for string filtering using contains to cover multiple values with sub hint
# str_filtered_df = df[df['Product'].str.contains('An', case=False)]
# print(str_filtered_df)

# filtered_df = df[
#     (df['Store'] == 'LA') &
#     (df['Product'] == 'Oranges') &
#     (df['Revenue ($)'] > 500)
# ]
#
# print(filtered_df)
# #ploting the filtered dataframe
# if filtered_df.empty:
#     print("No data matches the filter condition.")
# else:
#     filtered_df.plot(
#         x='Date', y='Revenue ($)', kind='bar',
#         title='High Revenue Orange Sales in LA'
#     )
#     plt.tight_layout()
#     plt.show()
# #saving the filtered data frame
# filtered_df.to_csv('filtered_LA_oranges.csv', index=False)
# filtered_df.to_excel('filtered_data.xlsx', index=False)
# filtered_df.to_json('filtered_data.json', orient='records', lines=True)
# filtered_df.to_html('filtered_data.html', index=False)
# conn = sqlite3.connect('sales.db')  # or another DB
# filtered_df.to_sql('filtered_table', conn, index=False, if_exists='replace')
# conn.close()
# filtered_df.to_parquet('filtered_data.parquet', index=False)

# print("__*__"*20)
# df_new = pd.read_parquet('filtered_data.parquet')
# print(df_new)



#group by
# ✅ Example 1: Total Revenue by Store
# print(df.groupby('Store')['Revenue ($)'].apply(list))

# grouped = df.groupby('Store')
# for store_name, group_df in grouped:
#     print(f"Group: {store_name}")
#     print(group_df)

#Group by 1 column, select 1 column
# grouped = df.groupby('Store')['Revenue ($)']
# for store_name, group_df in grouped:
#     print(f"Group: {store_name}")
#     print(group_df)

#Group by 1 column, select 3 columns
# grouped = df.groupby('Store')[['Date','Units Sold','Revenue ($)']]
# for store_name, group_df in grouped:
#     print(f"Group: {store_name}")
#     print(group_df)
# print(grouped.value_counts())

#Group by n column, select n columns
# grouped = df.groupby(['Store', 'Product'])[['Store','Units Sold', 'Revenue ($)']]
# for (store_name, product_name), group_df in grouped:
#     print(f"\nGroup: Store = {store_name}, Product = {product_name}")
#     print(group_df)


#print(df.groupby('Store')['Revenue ($)'].value_counts())
# print(df.groupby('Store')['Revenue ($)'].sum())
# ✅ Example 2: Average Units Sold by Product
# print(df.groupby('Product')['Units Sold'].mean())
# ✅ Example 3: Group by Two Columns (Store + Product)
# grouped = df.groupby(['Store', 'Product'])['Revenue ($)'].value_counts()
# grouped = df.groupby(['Store', 'Product'])['Revenue ($)'].sum()
# print(grouped)
# print(df.groupby(['Store','Revenue ($)'])['Revenue per Unit'].sum())

# summary = df.groupby(['Store','Product']).agg({
#     'Units Sold': ['sum', 'max'],
#     'Revenue ($)': ['sum', 'max']
# })
# print(summary)
# print("-*-"*20)
# grouped = df.groupby(['Store', 'Product'])['Revenue ($)'].sum().reset_index()
# print(grouped)



#filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"
#df = pd.read_csv(filename)

# xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx'
# df = pd.read_excel(xlsx_path)
#
# print(df.head())
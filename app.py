import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

df = pd.read_csv('data/quest.csv')
# colors = px.colors.sequential.Blues

# Example: Generate and display 10+ Plotly charts
st.title("Plotly Practice Charts")
####################################################################
# Graph1 Logic
chosen_cols1 = ['Sales', 'Profit']
total_sales = df.groupby('Order Date')[chosen_cols1].sum().reset_index().sort_values(by='Order Date', ascending=False)

# Graph1 plotting
fig1 = px.line(total_sales,
              x='Order Date', 
              y=chosen_cols1,
            #   color_discrete_sequence=colors,
              width=800, height=500)

# Graph1
st.header('Analyse the trend of total sales and profits over time. ')
st.plotly_chart(fig1, use_container_width=True)
total_sales

####################################################################

# Graph2 Logic
chosen_cols2 = ['Sales', 'Profit']
sales = df.groupby('State')[chosen_cols2].sum().reset_index().sort_values(by='State', ascending=False)

# Graph2 plotting
fig2 = px.line(sales,
            x=chosen_cols2,
            y='State',
            # color_discrete_sequence=colors,
            width=800, height=500)

# Graph2
st.header('Compare the sales and profits of different states.')
st.plotly_chart(fig2, use_container_width=True)
sales
####################################################################

# Graph3 Logic
fig3 = px.scatter(df, x='Discount', y='Profit', color='Discount',
    #    color_continuous_scale=colors,
       title='Discount vs Profit')

# Graph3
st.header('Analyse the relationship between discount and profit.')
st.plotly_chart(fig3, use_container_width=True)

####################################################################

# Graph4 Logic
# Way one 
tab1 = df['Ship Mode'].value_counts().sort_values(ascending=False).reset_index()

fig4_1 = px.bar(df, 
             x='Ship Mode', 
             title='Distribution of Ship Modes',
            #  color_discrete_sequence=colors
             )

# Way two
df2 = pd.DataFrame(df['Ship Mode'].value_counts().sort_values(ascending=False).reset_index())

fig4_2 = px.bar(df2, 
             x='Ship Mode', 
             y= 'count',
             title='Distribution of Ship Modes',
            #  color_discrete_sequence=colors
             )

# Graph4
st.header('Distribution of Ship Modes(way 1)')
st.plotly_chart(fig4_1, use_container_width=True)
tab1

st.header('Distribution of Ship Modes(way 2)')
st.plotly_chart(fig4_2, use_container_width=True)
df2
####################################################################


# Graph5 Logic
# Select top 5 customers by sales
top_customers = df.groupby('Customer Name')['Sales'].sum().nlargest(5)
top_data = df[df['Customer Name'].isin(top_customers.index)]

metrics = ['Sales', 'Profit', 'Discount']
for metric in metrics:
    fig5 = px.bar(top_data, 
                  y=metric, 
                  x='Customer Name', 
                  title=f'{metric} by Customers comparison')
    
st.header('Top 5 Customers by Sales')
st.plotly_chart(fig5, use_container_width=True)

####################################################################

# Graph6 Logic
top10_customers = df.groupby('Customer Name')['Sales'].sum().nlargest(10).reset_index()
fig6 = px.bar(top10_customers, 
              x='Customer Name', y='Sales', title='Top 10 Customers by Sales')

st.subheader(" Top 10 Customers by Sales")
st.plotly_chart(fig6, use_container_width=True)
st.dataframe(top10_customers)

####################################################################

# Graph7 Logic
top10_subcats = df.groupby('Sub-Category')['Sales'].sum().nlargest(10).reset_index()
fig7 = px.bar(top10_subcats, x='Sub-Category', y='Sales', title='Top 10 Sub-Categories by Sales')

st.subheader("7️ Top 10 Sub-Categories by Sales")
st.plotly_chart(fig7, use_container_width=True)
st.dataframe(top10_subcats)

######################################################################3

# Graph8 Logic
st.subheader("8️ Sales vs Quantity by Category")
cat_group = df.groupby('Category')[['Sales', 'Quantity']].sum().reset_index()
fig8 = px.bar(cat_group, x='Category', y=['Sales', 'Quantity'], barmode='group',
              title='Sales vs Quantity by Category')

st.subheader("8️Sales vs Quantity by Category")
st.plotly_chart(fig8, use_container_width=True)
st.dataframe(cat_group)

########################################################################

# Graph9 Logic
region_group = df.groupby('Region')['Sales'].sum().reset_index()
fig9 = px.pie(region_group, names='Region', values='Sales', title='Sales Distribution by Region')

st.subheader("9️Sales Distribution by Region")
st.plotly_chart(fig9, use_container_width=True)
st.dataframe(region_group)

########################################################################
# Graph10 Logic
segment_group = df.groupby('Segment')[['Sales', 'Discount']].sum().reset_index()
fig10 = px.bar(segment_group, x='Segment', y=['Sales', 'Discount'], barmode='group',
               title='Sales vs Discount by Segment')

st.subheader(" Sales vs Discount by Segment")
st.plotly_chart(fig10, use_container_width=True)
st.dataframe(segment_group)

########################################################################
if 'z_value' not in df.columns:
    df['z_value'] = np.random.randn(len(df))

# Title
st.title("3D Scatter Plot - Sales vs Profit vs Z Value")

# 3D scatter plot
fig654 = px.scatter_3d(
    df,
    x='Sales',
    y='Profit',
    z='z_value',
    color='Category',         # Optional: change to any categorical column
    hover_name='Product Name' # Optional: what shows on hover
)

# Display the figure in Streamlit
st.plotly_chart(fig654)
st.subheader("3D Scatter Plot - Sales vs Profit vs Z Value")

dataframe = pd.read_excel('data/Adidas.xlsx')
dataframe
fig44 = px.treemap(dataframe, path=['Region', 'City'], 
                 values='TotalSales',
                color='City',  # Color nodes by region
                hover_name='TotalSales',
                hover_data=['TotalSales'],  # Show relevant data on hover
                title='Total Sales by Region and City',
                color_discrete_sequence=['pink', 'red', 'green', 'orange', 'blue', 'purple']
            )  # Customize color palette
fig44.update_traces(textinfo="label+value")
fig44.update_layout(margin=dict(t=50, l=50, r=50, b=50))
st.plotly_chart(fig44, use_container_width=True)
st.subheader
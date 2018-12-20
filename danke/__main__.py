#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import os
from danke.configuracion import config
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns

if __name__ == '__main__':
    # Cargando los datos de train y extras explicativos
    train = pd.read_csv(config("traindata"), encoding="utf-8")
    items = pd.read_csv(config("itemsdata"), encoding='utf-8')
    items_categories = pd.read_csv(config("itemcategoriesdata"), encoding="utf-8")
    shops = pd.read_csv(config("shopsdata"), encoding='utf-8')

    # Forma de los dataframes
    print('Train: {0}, columns: {1}'.format(train.shape, train.columns))
    print('Items: {0}, columns: {1}'.format(items.shape, items.columns))
    print('Shops: {0}, columns: {1}'.format(shops.shape, shops.columns))
    print('Item Categories: {0}, columns: {1}'.format(items_categories.shape, items_categories.columns))

    # Necesitamos predecir venta de articulos a nivel mes-tienda
    sales=train.groupby(["date_block_num"])["item_cnt_day"].sum()
    sales.astype('float')
    plt.figure(figsize=(16,8))
    plt.title('Total Sales of the company')
    plt.xlabel('Time')
    plt.ylabel('Sales')
    plt.plot(sales)

    # number of items per category 
    x=items.groupby(['item_category_id']).count()
    x=x.sort_values(by='item_id',ascending=False)
    x=x.iloc[0:10].reset_index()
    plt.figure(figsize=(8,4))
    ax= sns.barplot(x.item_category_id, x.item_id, alpha=0.8)
    plt.title("Items per Category")
    plt.ylabel('# of items', fontsize=12)
    plt.xlabel('Category', fontsize=12)
    plt.show()
    
    # Sales per Shop
    shop_sales=pd.DataFrame(train.groupby(["shop_id","date_block_num"])["item_cnt_day"].sum())
    shop_sales.reset_index(drop=False, inplace=True)
    shop_sales.columns.name = None
    pivoted = shop_sales.pivot(index="date_block_num", columns="shop_id", values="item_cnt_day").fillna(0)
    pivoted.reset_index(drop=False, inplace=True)
    pivoted.columns.name = None

    # Initialize the figure
    plt.style.use('seaborn-darkgrid')
    
    # create a color palette
    palette =  ListedColormap((sns.color_palette("husl", 60)))
    
    # multiple line plot
    num=0
    for column in pivoted.drop('date_block_num', axis=1):
        num+=1
    
        # Find the right spot on the plot
        plt.subplot(20,3, num)
    
        # Plot the lineplot
        plt.plot(pivoted['date_block_num'], pivoted[column], marker='', color=palette(num), 
                linewidth=1.9, alpha=0.9, label=column)
        # Not ticks everywhere
        if num in range(19) :
            plt.tick_params(labelbottom='off')
        plt.tick_params(labelleft='off')
        # Add title
        plt.title(column, loc='left', fontsize=12, fontweight=0, color=palette(num))
    
    # general title
    plt.suptitle("Sales of the 60 shops", fontsize=13, fontweight=0,
                color='black', style='italic', y=1.02)
    
    plt.show()
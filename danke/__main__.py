#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import os
from danke.configuracion import config

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
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import configparser

class Config:
    singleton = None
    file = "danke.cfg"
    section = "app"
    config = configparser.ConfigParser()
    path = os.path.join(os.path.expanduser("~"), file)

    def __init__(self):
        if os.path.exists(self.path):
            self.config.read(self.path)
        else:
            self.default()

    def default(self):
        self.config.add_section(self.section)
        self.config.set(self.section, "traindata", os.getcwd() + "/extras/sales_train.csv.gz")
        self.config.set(self.section, "itemsdata", os.getcwd() + "/extras/items.csv")
        self.config.set(self.section, "itemcategoriesdata", os.getcwd() + "/extras/item_categories.csv")
        self.config.set(self.section, "shopsdata", os.getcwd() + "/extras/shops.csv")


    def prop(self, p):
        try:
            r = self.config.get(self.section, p)
            return r
        except (configparser.NoSectionError, configparser.NoOptionError):
            raise Exception("Problema en fichero de configuración")


def config(p):
    if Config.singleton is None:
        Config.singleton = Config()
    return Config.singleton.prop(p)
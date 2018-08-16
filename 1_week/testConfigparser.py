#!/usr/bin/env python3
import configparser
config = configparser.ConfigParser()
a = config.read("config.ini")
print(a)
b = config.sections()
print(b)
c = config.items("bit")
print(c)
print(config["top"]["g"],"top" in config,"g" in config)
for i in config:
	print(i)
config["top"] = {}
config["top"]["g"] ="{}" 
print(config["TOP"])

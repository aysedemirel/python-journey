# -*- coding: utf-8 -*-
######## TEXT TYPES ##########

text = "example"

print(type(text))

######## NUMERIC TYPES ##########

num = 1

print(type(num))

num = 1.0

print(type(num))

num = 3 +6j

print(type(num))

######## SEQUENCE TYPES #########

sequence = [1,2]

print(type(sequence))

sequence = (1,2)

print(type(sequence))

sequence = range(3)

print(type(sequence))

######## MAPPING TYPES ########

mapping = {"name" : "example", "age" : 1}

print(type(mapping))

######## SET TYPES ########

setting = {1,2}

print(type(setting))

setting = frozenset({1, 2})

print(type(setting))

####### BOOLEAN TYPES #########

isBoll = True

print(type(isBoll))

####### BINARY TYPES #########

byteExample = b"example"

print(type(byteExample))

byteExample = bytearray(5)

print(type(byteExample))

byteExample = memoryview(bytes(5))

print(type(byteExample))








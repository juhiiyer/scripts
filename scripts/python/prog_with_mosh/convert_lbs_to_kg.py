#!/usr/bin/python3.7
import time
lbs = int(input('Enter your weight in pounds: '))
print("Now calculating your weight in kgs")
time.sleep(1)
print('..........')
time.sleep(2)
grams = lbs * 450
kg = grams / 1000
print(" Your weight in kg's is %s"%(kg))
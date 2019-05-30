#!/bin/python
def hotel_cost(night):
  if night > 10:
    #15% off for more than 10 nights
    return (140 * night) * 0.85
  return 140 * night

def plane_ride_cost(cityFrom, cityTo, roundtrip):
  if cityFrom == "Charlotte" and cityTo == "Tampa":
    if roundtrip == "yes":
      return 183 * 2
    return 183
  elif cityFrom == "Pittsburgh" and cityTo == "Tampa":
    if roundtrip == "yes":
      return 222 * 2
    return 222
  elif cityFrom == "Los Angeles" and cityTo == "Tampa":
    if roundtrip == "yes":
      return 180 * 2
    return 180
  elif cityFrom == "New York City" and cityTo == "Tampa":
    if roundtrip == "yes":
      return 350 * 2
    return 350
  elif cityFrom == "Tampa" and cityTo == "Charlotte":
    if roundtrip == "yes":
      return 220 * 2
    return 220
  elif cityFrom == "Pittsburgh" and cityTo == "Charlotte":
    if roundtrip == "yes":
      return 222 * 2
    return 222
  elif cityFrom == "Los Angeles" and cityTo == "Charlotte":
    if roundtrip == "yes":
      return 120 * 2
    return 120
  elif cityFrom == "New York City" and cityTo == "Charlotte":
    if roundtrip == "yes":
      return 475 * 2
    return 475
  elif cityFrom == "Charlotte" and cityTo == "Pittsburgh":
    if roundtrip == "yes":
      return 183 * 2
    return 183
  elif cityFrom == "Tampa" and cityTo == "Pittsburgh":
    if roundtrip == "yes":
      return 220 * 2
    return 220
  elif cityFrom == "Los Angeles" and cityTo == "Pittsburgh":
    if roundtrip == "yes":
      return 475 * 2
    return 475
  elif cityFrom == "New York City" and cityTo == "Pittsburgh":
    if roundtrip == "yes":
      return 475 * 2
    return 475
  elif cityFrom == "Charlotte" and cityTo == "Los Angeles":
    if roundtrip == "yes":
      return 183 * 2
    return 183
  elif cityFrom == "Tampa" and cityTo == "Los Angeles":
    if roundtrip == "yes":
      return 220 * 2
    return 220
  elif cityFrom == "Pittsburgh" and cityTo == "Los Angeles":
    if roundtrip == "yes":
      return 222 * 2
    return 222
  elif cityFrom == "New York City" and cityTo == "Los Angeles":
    if roundtrip == "yes":
      return 475 * 2
    return 475
  else:
    return 0  
  
def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
    cost -= 50
  elif days >= 3 and days < 7:
    cost -= 20 
  else:
    cost = cost * 0.95     
  return cost

def trip_cost(cityFrom, cityTo, roundtrip, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(cityFrom, cityTo, roundtrip) + spending_money

cityFrom = raw_input("Please enter the city of origin\n")
cityTo = raw_input("Please enter the city of destination\n")
roundtrip = raw_input("Please yes or no for roundtrip\n")
days = int(raw_input("Please enter the number of days of travel\n"))
spending_money = int(raw_input("Please enter other expenses"))

print "_______________Calculating___________I am not a computer! _____________"

print "Total Cost of tripping is " + str(trip_cost(cityFrom, cityTo, roundtrip, days, spending_money)) + " . "

shopping_list = ["banana", "orange", "apple", "pear", "watermelon", "mango"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15,
  "watermelon": 20,
  "mango": 12
}


cost_per_pound = {
  "banana": 0.5,
  "apple": 1.2,
  "orange": 0.8,
  "pear": 0.7,
  "watermelon": 0.4,
  "mango": 5

}

weight_in_pounds = {
  "banana": 3,
  "apple": 2,
  "orange": 1,
  "pear": 0.5,
  "watermelon": 4,
  "mango": 2

}

# users_need = {}
# for item in shopping_list:
#     need = 0
#     need = raw_input("Enter the number of %s that you want to purchase" % item)
#     if need > stock[item]:
#         print "Please be reasonable and ask for less in life"
#         continue
#     user_needs[item] = need

#Calculate the cost of the item
def cost(food):
    cost_of_fruit = []
    for item in food:
        if stock[item] == 0:
            print "%s is out of stock" % item
            continue
        cost_of_fruit.append(cost_per_pound[item] * weight_in_pounds[item])
        print "Total cost of %s is %s" %(item, str(cost_per_pound[item] * weight_in_pounds[item]))
    return cost_of_fruit


# Write your code below!
def compute_bill(food):
  total = 0
  prices = cost(food)
  for item in prices:
      total += item  
  return total





print "Total cost of purchasing all the fruits is %f" % compute_bill(shopping_list)
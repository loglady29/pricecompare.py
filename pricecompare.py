#  change the weight variable to match your parcel's weight. The program should determine cheapest way to ship#
weight = 12.0

def gsc(weight,):
    
  if weight <= 2.0:
    return (weight * 1.50) + 20
  if weight >= 2.1 and weight <= 6.0:
    return (weight * 3.00) + 20
  if weight >= 6.1 and weight <= 10.0:
    return (weight * 4.00) + 20
  if weight > 10.0:
    return (weight * 4.75) + 20
print("ground shipping charge")
print(gsc(weight)) 

pgs = 125.00
print("premium ground shipping")
print(pgs)

def dsc(weight,):
  if weight <= 2.0:
    return (weight * 4.50)
  if weight >= 2.1 and weight <= 6.0:
    return (weight * 9.00) 
  if weight >= 6.1 and weight <= 10.0:
    return (weight * 12.00)
  if weight > 10.0:
    return (weight * 14.25)
print("Drone shipping charge")
print(dsc(weight)) 

def overall_comp(gsc, pgs, dsc, weight):
  if (gsc(weight)) < pgs and (gsc(weight)) < (dsc(weight)):
     print("Ground Shipping is Cheapest...it would cost")
     print(gsc(weight))
  if ((pgs) < (gsc(weight))) and ((pgs) < (dsc(weight))):
     print("Premium Ground Shipping is the cheapest.... it would cost")
     print(pgs)                          
  elif (dsc(weight)) < pgs and (dsc(weight)) < (gsc(weight)):
     print("Drone Shipping is Cheapest...it would cost")
     print(dsc(weight))
price_compare =  (overall_comp(gsc, pgs, dsc)) 
print(price_compare) 

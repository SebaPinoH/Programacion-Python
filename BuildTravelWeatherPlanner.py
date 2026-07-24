distance_mi = 3
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True 

## number 4 and 5
if distance_mi <= 0:
    print("False")
elif distance_mi <=1 and is_raining == False:
    print("True")
## number 6
elif distance_mi >= 1 and distance_mi <= 6 and has_bike == False and is_raining == True:
    print("False")
## number 7
elif distance_mi >= 1 and distance_mi <= 6 and has_bike == False and is_raining == False:
    print("False")
## number 8
elif distance_mi >= 1 and distance_mi <= 6 and has_bike == True and is_raining == False:
    print("True")
## number 9
elif distance_mi > 6 and has_car == True or has_ride_share_app == True:
    print("True")
else:
    print("False")
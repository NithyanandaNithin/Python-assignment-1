destination=["hassan","holenarsipura"]
passenger_types=["men", "children","senior citizen", "handicap", "women"]
your_destination=input("enter your destination:")
if your_destination in destination and your_destination==destination[0]:
  passenger=input(f"select the passenger type for {your_destination}:")
  if passenger==passenger_types[0]:
    quantity=int(input("enter the number of passengers:"))
    fare=100
    total_fare=quantity*fare
    print(f"The total fare of the passengers is {total_fare}")
  elif passenger==passenger_types[1]:
    quantity=int(input("enter the nunber of passenger:"))
    fare=50
    total_fare=quantity*fare
    print(f"The total fare of the passengers is {total_fare}")
  elif passenger==passenger_types[2]:
    quantity=int(input("enter the number of passengers:"))
    fare=75
    total_fare=quantity*fare
    print(f"The total fare of the passengers is {total_fare}")
  elif passenger==passenger_types[3]:
    quantity=int(input("enter the nunber of passengers:"))
    fare=65
    total_fare=quantity*fare
    print(f"The total fare of the passengers is {total_fare}")
  elif passenger==passenger_types[4]:
    quantity=int(input("enter the number of passengers:"))
    fare=0
    total_fare=quantity*fare
    print(f"The total fare of the passengers is {total_fare}")
  else:
    print("invalid input")
elif your_destination==destination[1]:
   passenger=input(f"select the passenger type for {your_destination}:")
   if passenger==passenger_types[0]:
    quantity=int(input("enter the number of passengers:"))
    fare=80
    total_fare=quantity*fare
    print(f"The total fare of the passengers is {total_fare}")
   elif passenger==passenger_types[1]:
    quantity=int(input("enter the nunber of passenger:"))
    fare=40
    total_fare=quantity*fare
    print(f"The total fare of the passengers is {total_fare}")
   elif passenger==passenger_types[2]:
    quantity=int(input("enter the number of passengers:"))
    fare=60
    total_fare=quantity*fare
    print(f"The total fare of the passengers is {total_fare}")
   elif passenger==passenger_types[3]:
    quantity=int(input("enter the nunber of passengers:"))
    fare=50
    total_fare=quantity*fare
    print(f"The total fare of the passengers is {total_fare}")
   elif passenger==passenger_types[4]:
    quantity=int(input("enter the number of passengers:"))
    fare=0
    total_fare=quantity*fare
    print(f"The total fare of the passengers is {total_fare}")
   else:
    print("invalid input")
else:
  print("Sorry,this bus not go their")

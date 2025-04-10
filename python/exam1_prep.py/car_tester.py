from car import Car


with open("cars.txt") as file:
    car_list=[]
    for line in file:
        info=line.strip().split()
        color=info[0]
        engine_type=info[1]
        gas_tank=int(info[2])
        odometer=int(info[3])
        car1=Car(color,engine_type,gas_tank,odometer)
        car_list.append(car1)
    
    print(car_list[1])
    print(car_list[1].get_gas_tank())
    print(car_list[1].get_odometer())
    car_list[1].drive()
    print(car_list[1].get_gas_tank())
    print(car_list[1].get_odometer())
    print(car_list[0])
    print(car_list[0].get_gas_tank())
    print(car_list[0].get_odometer())
    car_list[0].drive()
    print(car_list[0].get_gas_tank())
    print(car_list[0].get_odometer())



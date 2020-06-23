#!/usr/bin/python3

from sympy import *
import code

kW, kg, unit, month, EUR, people = symbols("kW, kg, unit, month, EUR, people")
parameters = {
    'plant_power' :  10 * kW,
    'power_plant_per_island': 24,
    'food_yield_per_island': 1000*kg/month,
    'biomass_yield_per_island': 1000*kg/month,
    'workforce_farming_ratio': 0.5,
    'workforce_import_ratio': 0.1,
    'money_import_ratio': 0.5,
    'electricity_plastic_ratio': 0.8,
    'workforce_per_island': 2* people,
    'import_salary': 600*EUR/month/people,
    'import_per_workforce': 6000*EUR/month/people,
    'plastic_yield_of_biomass': 0.1,
    'plastic_yield_of_electricity': 0.01*kg/kW/month,
}
(money,factory,island,workforce)=symbols("money,factory,island,workforce")


for key in parameters.keys():
    sym = symbols(key)
    globals()[key] = sym


electricity =  plant_power * island/power_plant_per_island
farming_island = Min(island,workforce*workforce_farming_ratio/workforce_per_island)
food =  farming_island*food_yield_per_island
biomass = farming_island*biomass_yield_per_island
import_workforce = workforce*workforce_import_ratio
additional_material = Min(money_import_ratio*money - import_salary*import_workforce, import_workforce*import_per_workforce)
electricity_plastic = electricity*electricity_plastic_ratio
plastic = Min(biomass*plastic_yield_of_biomass,electricity_plastic*plastic_yield_of_electricity)

parameters['workforce'] = 4
parameters['money'] = 1000*EUR/month
parameters['workforce'] = 10*people
parameters['island'] = 10

for material in "electricity,food,biomass,additional_material,plastic".split(','):
    print(material)
    print(" ",globals()[material])
    print(" ",globals()[material].subs(parameters))
    print()

code.InteractiveConsole(locals=globals()).interact()

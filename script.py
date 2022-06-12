# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def convert_damages_data(damages):
  updated_damages = []
  for damage in damages:
    if damage[-1] == 'M':
      updated_damages.append(float(damage[:-1]) * 1000000)
    elif damage[-1] == 'B':
      updated_damages.append(float(damage[:-1]) * 1000000000)
    else:
      updated_damages.append(damage)
  return updated_damages


# test function by updating damages
updated_damages = convert_damages_data(damages)
#print(updated_damages)

# write your construct hurricane dictionary function here:
def create_dictionary(names, months, years, winds, areas, damages, deaths):
  hurricanes = {}
  for i in range(len(names)):
    hurricanes[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Winds': winds[i], 'Areas Affected': areas[i], 'Damage': damages[i], 'Deaths': deaths[i]}
  return hurricanes

hurricanes = create_dictionary(names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths)
#print(hurricanes)

# write your construct hurricane by year dictionary function here:
def create_year_dictionary(hurricanes):
  hurricane_by_year = {}
  for hurricane in hurricanes:
    current_year = hurricanes[hurricane]['Year']
    current_hurricane = hurricanes[hurricane]
    if current_year not in hurricane_by_year:
      hurricane_by_year[current_year] = [current_hurricane]
    else:
      hurricane_by_year[current_year].append(current_hurricane)
  return hurricane_by_year

hurricanes_by_year = create_year_dictionary(hurricanes)
#print(hurricanes_by_year)

# write your count affected areas function here:
def count_areas_affected(areas):
  affected_areas_count = {}
  for hurricane in hurricanes:
    for area in hurricanes[hurricane]['Areas Affected']:
      if area not in affected_areas_count:
        affected_areas_count[area] = 1
      else:
        affected_areas_count[area] += 1
  return affected_areas_count

affected_areas_count = count_areas_affected(areas_affected)
#print(affected_areas_count)

# write your find most affected area function here:
def find_most_affected_area(areas_affected_count):
  max_area = ''
  max_area_count = 0
  for area in areas_affected_count:
    if max_area_count < areas_affected_count[area]:
      max_area = area
      max_area_count = areas_affected_count[area]
  return max_area, max_area_count

most_affected_area = find_most_affected_area(affected_areas_count)
#print(most_affected_area)

# write your greatest number of deaths function here:
def find_deadliest_hurricane(hurricanes):
  deadliest = ''
  deaths = 0
  for hurricane in hurricanes:
    if deaths < hurricanes[hurricane]['Deaths']:
      deadliest = hurricane
      deaths = hurricanes[hurricane]['Deaths']
  return deadliest, deaths

deadliest_hurricane = find_deadliest_hurricane(hurricanes)
#print(deadliest_hurricane)

# write your catgeorize by mortality function here:
def rate_hurricane_deadliness(hurricanes):
  hurricanes_by_death_rate = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for hurricane in hurricanes:
    if hurricanes[hurricane]['Deaths'] > 10000:
      hurricanes_by_death_rate[5].append(hurricanes[hurricane])
    elif hurricanes[hurricane]['Deaths'] > 1000:
      hurricanes_by_death_rate[4].append(hurricanes[hurricane])
    elif hurricanes[hurricane]['Deaths'] > 500:
      hurricanes_by_death_rate[3].append(hurricanes[hurricane])
    elif hurricanes[hurricane]['Deaths'] > 100:
      hurricanes_by_death_rate[2].append(hurricanes[hurricane])
    elif hurricanes[hurricane]['Deaths'] > 0:
      hurricanes_by_death_rate[1].append(hurricanes[hurricane])
    else:
      hurricanes_by_death_rate[0].append(hurricanes[hurricane])
  return hurricanes_by_death_rate

hurricanes_by_mortality = rate_hurricane_deadliness(hurricanes)
#print(hurricanes_by_mortality)

# write your greatest damage function here:
def find_costliest_hurricane(hurricanes):
  costliest = ''
  damages = 0
  for hurricane in hurricanes:
    if hurricanes[hurricane]['Damage'] == "Damages not recorded":
      continue
    elif hurricanes[hurricane]['Damage'] > damages:
      costliest = hurricane
      damages = hurricanes[hurricane]['Damage']
  return costliest, damages

costliest_hurricane = find_costliest_hurricane(hurricanes)
#print(costliest_hurricane)

# write your catgeorize by damage function here:
def rate_hurricane_cost(hurricanes):
  hurricanes_by_damages = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for hurricane in hurricanes:
    if hurricanes[hurricane]['Damage'] == "Damages not recorded":
      hurricanes_by_damages[0].append(hurricanes[hurricane])
    elif hurricanes[hurricane]['Damage'] > 50000000000:
      hurricanes_by_damages[5].append(hurricanes[hurricane])
    elif hurricanes[hurricane]['Damage'] > 10000000000:
      hurricanes_by_damages[4].append(hurricanes[hurricane])
    elif hurricanes[hurricane]['Damage'] > 1000000000:
      hurricanes_by_damages[3].append(hurricanes[hurricane])
    elif hurricanes[hurricane]['Damage'] > 100000000:
      hurricanes_by_damages[2].append(hurricanes[hurricane])
    elif hurricanes[hurricane]['Damage'] > 0:
      hurricanes_by_damages[1].append(hurricanes[hurricane])
    else:
      hurricanes_by_damages[0].append(hurricanes[hurricane])
  return hurricanes_by_damages

hurricanes_by_damages = rate_hurricane_cost(hurricanes)
#print(hurricanes_by_damages)
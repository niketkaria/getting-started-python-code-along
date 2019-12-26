# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
    data = yaml.load(f)
# Find data type of the file
type_data = type(data)
print(type_data)

# In which city, and at which venue the match was played and where was it played ?
city = data['info']['city']
print(city)
venue = data['info']['venue']
print(venue)
# Which are all the teams that played in the tournament ? How many teams participated in total?
teams = data['info']['teams']
print(teams)
print(len(teams),'teams participated in total')

# Which team won the toss and what was the decision of toss winner ?
toss_winner = data['info']['toss']['winner']
print(toss_winner)
decision_of_toss_winner = data['info']['toss']['decision']
print(decision_of_toss_winner)

# Find the first bowler and first batsman who played the first ball of the first inning
first_bowler = data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
print(first_bowler)

first_batsman = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
print(first_batsman)
# How many deliveries were delivered in first inning ?
deliveries_1st_innings = len(data['innings'][0]['1st innings']['deliveries'])
print(deliveries_1st_innings)

# How many deliveries were delivered in second inning ?
deliveries_2nd_innings = len(data['innings'][1]['2nd innings']['deliveries'])
print(deliveries_2nd_innings)
# Which team won and how ?
Team_Won = data['info']['outcome']['winner']
print(Team_Won)
Won_How = data['info']['outcome']['by']['runs']
print(Won_How)




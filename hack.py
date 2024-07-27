import requests
import matplotlib.pyplot as plt
import numpy as np

year = 2013
year_list = []
rows = []
results = []
count = []
for i in range(10):
    year_list.append(year)
    # url =   f"https://api.fda.gov/drug/event.json?search=receivedate:[{year}0101+TO+{year}1231]&count=seriousnessdeath"
    url2 = f"https://api.fda.gov/drug/event.json?search=receivedate:[{year}0101+TO+{year}1231]&count=patient.reaction.reactionmeddrapt.exact"
    response = requests.get(url2)
    json = response.json()
    for i in range(4):
        results.append(json['results'][i]['term'])
        count.append(json['results'][i]['count'])
    year += 1
print(results,)

url2 = f"https://api.fda.gov/drug/event.json?search=receivedate:[20130101+TO+20231231]&count=patient.reaction.reactionmeddrapt.exact"
response = requests.get(url2)
json = response.json()
for i in range(2, 11):
    results.append(json['results'][i]['term'])
    count.append(json['results'][i]['count'])
plt.figure().set_figwidth(4)
plt.barh(results, count)
plt.xlabel("Number of Reports")
plt.title("Graph Showing 10 Most Commmon Adverse Drug Reactions")
# plt.plot(year_list, rows)
# plt.show()

# plt.xlabel("years")
# plt.xticks(year_list)
# plt.ylabel("number of deaths")
# plt.title("graph showing number of deaths since 2013")
# plt.show()    

year = 2013
year_list = []
rows = []
men = []
women = []
for i in range(11):
  url = f"https://api.fda.gov/drug/event.json?search=(receivedate:[{year}0101+TO+{year}1006])+AND+patient.patientsex:1&count=seriousnessdeath"
  url2 = f"https://api.fda.gov/drug/event.json?search=(receivedate:[{year}0101+TO+{year}1006])+AND+patient.patientsex:2&count=seriousnessdeath"
  response = requests.get(url)
  response2=requests.get(url2)
  json = response.json()
  json2 = response2.json()

  men.append(json['results'][1]['count'])
  women.append(json2['results'][1]['count'])
  year_list.append(year)

  year +=1

print(year_list, men, women)
x_axis = np.arange(len(year_list))
plt.bar(x_axis - 0.2, men, 0.4, label = 'Males') 
plt.bar(x_axis + 0.2, women, 0.4, label = 'Females') 
  
plt.xticks(x_axis, year_list) 
plt.xlabel("Years") 
plt.ylabel("Number of Deaths") 
plt.title("Sex-Disaggregated Number of Drug-Related Deaths") 
plt.legend() 
plt.show() 


url = "https://api.fda.gov/drug/event.json?search=receivedate:[20130101+TO+20231231]ANDseriousnessdeath:1&count=patient.reaction.reactionoutcome.exact"
response = requests.get(url)
json = response.json()
types = []
counts = []
print(json)
for i in json['results']:
    types.append(i['term'])
    counts.append(i['count'])
print(types, counts)
plt.bar(types, counts)
plt.show()
url = "https://api.fda.gov/drug/event.json?search=receivedate:[203101+TO+20231006]ANDseriousnessdeath:1&count=patient.patientagegroup"

response = requests.get(url)
json = response.json()
age_grp = ["Adult", "Elderly", "Child", "Adolescent", "Neonate", "Infant"]
count =[]
for i in json['results']:
    count.append(i['count'])
y = np.array(count)
mycolours = ["#A2E2EC", "#00C9E8", "#009DB5", "blue", "#006675", "#0B444C"]
plt.pie(y, labels = age_grp, colors=mycolours)
plt.title("Pie Chart Showing Deaths By Age Group")
plt.show()
url = "https://api.fda.gov/drug/event.json?search=receivedate:[203101+TO+20231006]ANDseriousnessdeath:1&count=patient.patientagegroup"

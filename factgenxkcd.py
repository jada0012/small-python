import random
season = ['fall', 'spring']
season2 = ['winter', 'summer']
event = ['solstice', 'olympics']
time = ['earliest', 'latest']
sun = ['sunrise', 'sunset']
save = ['saving', 'savings']
date = ['day', 'year']
moon = ['super', 'harvest', 'blood']

part1 = ["the " + random.choice(season) + " equinox",
'the %s %s' %(random.choice(season2), random.choice(event)),
'the %s %s' % (random.choice(time) ,random.choice(sun)),
'daylight ' + random.choice(save) + ' time',
'leap ' + random.choice(date), 
'easter', 
'the ' + random.choice(moon) + ' moon',
'Toyota Truck month',
'shark week'
]

atthe = ['earlier', 'later', 'at the wrong time']
calendar = ['Gregorian', 'Mayan', 'lunar', 'iPhone']
c2 = '%s calendar' %(random.choice(calendar))
sync = ['sun', 'moon', 'zodiac', 'atomic clock in Colorado', c2]
happen =['not happen', 'happen twice'] 

part2 = ['happens %s every year' %(random.choice(atthe)), 
'drifts out of sync with the %s ' %(random.choice(sync)),
'might %s this year' %(random.choice(happen))]

bigword = ['precession', 'libration', 'nutation', 'libation', 'eccentricity', 'obliquity']
country = ['Arizona', 'Indiana', 'Russia']
people = ['Benjamin Franklin', 'Isaac Newton', 'FDR']
lines = ['International Date', 'Mason-Dixon']
line = '%s line' %(random.choice(lines))
things = ['moon', 'sun', 'Earth\'s axis', 'equator', 'Prime Meridian', line]
part3 = ['time zone legislation in %s' %(random.choice(country)),
'a decree by the pope in the 1500s',
'%s of the %s'%(random.choice(bigword), random.choice(things)),
'magnetic field reversal',
'an arbitrary decision by %s' %(random.choice(people))]
age = ['Bronze Age', 'Ice Age', 'Cretaceous', '1990s']
but =['will never happen', 'actually makes things worse', 'is stalled in Congress', 'might be unconstitutional']

part4 = ['it causes a predictable increase in car accidents',
'that\'s why we have leap seconds',
'scientists are really worried',
'it was even more extreme during the %s' %(random.choice(age)),
'there\'s a proposal to fix it but %s' %(random.choice(but)),
'it\'s getting worse and no one knows why']


print("Did you know that %s %s because of %s? Apparently %s." %(random.choice(part1), random.choice(part2), random.choice(part3), random.choice(part4)))

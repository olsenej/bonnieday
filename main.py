from darksky import forecast
from datetime import date, timedelta, time, datetime

ROCKFORD = 43.1243,-85.4788

weekday = date.today()
#hourmark = datetime.time(datetime.now())
with forecast('2cb9fc9f569ca504d74f0bead2486357', *ROCKFORD) as rockford:
	print(rockford.daily.summary, end='\n---\n')
	for day in rockford.daily:
		day = dict(day = date.strftime(weekday, '%a'),
					icon = day.icon,
					precipProbability = day.precipProbability*100,
					precipType = day.precipType,
					tempMin = day.temperatureMin,
					tempMax = day.temperatureMax
					)
		print('{day}: {icon}\nPrecipitaion Chance: {precipProbability}\nPrecipitation Type: {precipType}\nTemp range: {tempMax} - {tempMin}\n'.format(**day))
		weekday += timedelta(days=1)
	for hour in rockford.hourly:
		hour = dict(hour = date.strftime(weekday, '%X'),
					icon = hour.icon,
					precipProbability = hour.precipProbability*100
					)
		print('{hour}: {icon}\nPrecipitation Chance: {precipProbability}\n')
		weekday += timedelta(hours=1)

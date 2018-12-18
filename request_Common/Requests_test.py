from request_Common.Requests_Class import webrequests
import urllib.parse as up

url = 'http://t.weather.sojson.com/api/weather/city/101030100'
payloda = {'_id':26, 'id':26, 'pid':0, 'city_code':101030100,'city_name':'天津'}
s = webrequests()
s.get(url,payloda)
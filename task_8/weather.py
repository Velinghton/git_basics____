#!/usr/bin/env python3

"""Which city do you want?"""

import  json

from urllib import  request


def make_request(url, *, encoding="utf-8"):
    file = request.urlopen(url)
    bindata = file.read()
    data = bindata.decode(encoding=encoding)
    return data
class RequestData:
    URL_Template = ""
    def request(self, **kwargs):
        url = self.URL_Template.format(**kwargs)
        text = make_request(url=url)
        data = json.loads(text)
        #print(data)
        return  data

class City(RequestData):
    URL_Template = "https://geocoding-api.open-meteo.com/v1/search?name={name}"

    def __init__(self, name=None, latitude=None, longitude=None):
        if name is not None:
            self.name = name.title()
            self.latitude = latitude
            self.longitude = longitude

  
    def request(self):
        data = super().request(name=self.name)
        data = data.get("results", {})
        res ={}
        if len(data) == 0:
            return "Incorrect name of City"
        else:
            for i in data:
                name = i["name"]
                if name == self.name:
                    res[name] = {"latitude": i["latitude"],
                                 "longitude:": i["longitude"],
                               "country": i["country"]}
            return res
class Weather(RequestData):
    URL_Template= ("https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")

    def __init__(self, latitude, longitude):
        self.lat = latitude
        self.lon = longitude
        self.data = None

    def request(self):
        data = super().request(lat=self.lat, lon=self.lon)
        self.data = data


    @property
    def teperature(self):
        if self.data is None:
            self.request()
        return self.data["current_weather"]["temperature"]
    @property
    def time(self):
        if self.data is None:
            self.request()
        return self.data["current_weather"]["time"]
    @property
    def windspeed(self):
        if self.data is None:
            self.request()
        return self.data["current_weather"]["windspeed"]
if __name__ == "__main__":
    from pprint import pprint

    import sys

    name =  sys.argv[1] if len(sys.argv) == 2 else 'kyiv'
    name = name.title()
    kiev = City(name)
    data = kiev.request()
    wth = Weather(data[name]["latitude"] ,data[name]["longitude:"])
    print(f"In the {name} temperatura is {wth.teperature}")
    print(f"Also in {name} time is {wth.time}")
    print(f"And windspeed is {wth.windspeed}")
    print(f"Welcome to our beautiful {name}")












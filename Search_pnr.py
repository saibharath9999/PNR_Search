import urllib.request
import json


class Pnr_Enquiry():
    def search(self,search):
        search = str(search)
        Pnr_Api = "http://api.railwayapi.com/v2/pnr-status/pnr/"+search+"/apikey/<apikey>/"
        request = urllib.request.urlopen(Pnr_Api)
        data = json.loads(request.read().decode('utf-8'))
        start = data.get('from_station')
        end = data.get('to_station')
        status = data.get('passengers')
        try:
            status = status[0]
        except (IndexError, ValueError, TypeError):
            status = "null"
        if status!="null":
            start = start.get('name')
            end = end.get('name')
            status = status.get('current_status')
        else:
            status = "No Response From Search Engine"
        return [start,end,status]
from flask_restful import Resource,reqparse
from Check_Pnr.Search_pnr import Pnr_Enquiry


class SearchAPI(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('q',type=int,location = 'args')
        query = parser.parse_args()
        req = query.q
        Enquiry = Pnr_Enquiry().search(req)
        return {
            "From": Enquiry[0],
            "To": Enquiry[1],
            "Status": Enquiry[2]
        }
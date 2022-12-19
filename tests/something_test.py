import requests
from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import User

def test_getting_users_list():
    response = requests.get(url=SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(200).validate(User)



# {
#    "meta":{
#       "pagination":{
#          "total":5043,
#          "pages":505,
#          "page":1,
#          "limit":10,
#          "links":{
#             "previous":"None",
#             "current":"https://gorest.co.in/public/v1/users?page=1",
#             "next":"https://gorest.co.in/public/v1/users?page=2"
#          }
#       }
#    },
#    "data":[
#       {
#          "id":5122,
#          "name":"Upendra Pillai",
#          "email":"pillai_upendra@beatty.name",
#          "gender":"male",
#          "status":"active"
#       },
#       {
#          "id":5121,
#          "name":"Pres. Jyotsana Gupta",
#          "email":"gupta_jyotsana_pres@pfeffer.com",
#          "gender":"male",
#          "status":"active"
#       },
#       {
#          "id":5119,
#          "name":"Rupinder Kakkar",
#          "email":"kakkar_rupinder@watsica-sanford.com",
#          "gender":"male",
#          "status":"active"
#       },
#       {
#          "id":5117,
#          "name":"Chandini Bhattacharya",
#          "email":"bhattacharya_chandini@robel.com",
#          "gender":"female",
#          "status":"active"
#       },
#       {
#          "id":5116,
#          "name":"Vimala Banerjee",
#          "email":"vimala_banerjee@weber.io",
#          "gender":"male",
#          "status":"inactive"
#       },
#       {
#          "id":5115,
#          "name":"Devasree Rana",
#          "email":"rana_devasree@torp.net",
#          "gender":"female",
#          "status":"inactive"
#       },
#       {
#          "id":5114,
#          "name":"Anurag Joshi",
#          "email":"joshi_anurag@harber-reilly.org",
#          "gender":"female",
#          "status":"active"
#       },
#       {
#          "id":5113,
#          "name":"Tanushree Prajapat",
#          "email":"prajapat_tanushree@kautzer-langworth.org",
#          "gender":"female",
#          "status":"active"
#       },
#       {
#          "id":5112,
#          "name":"Dr. Dandapaani Achari",
#          "email":"dr_achari_dandapaani@grant-stroman.io",
#          "gender":"male",
#          "status":"inactive"
#       },
#       {
#          "id":5110,
#          "name":"Deeptendu Ahluwalia",
#          "email":"deeptendu_ahluwalia@tremblay.org",
#          "gender":"female",
#          "status":"active"
#       }
#    ]
# }
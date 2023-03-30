import requests
import datetime

TOKEN = "tsodfsdfsfk342342dsfeer"
USER_NAME = "sangeeth695"

api_header = {
    "X-USER-TOKEN" : TOKEN
}
pixela_api_end_point = "https://pixe.la/v1/users"
today = datetime.datetime.now()
# print(today)
# yesterday = datetime.datetime(year=2023, month=3, day=27)

#-------------------------Creating user----------------------------#
# post_request_body = {
#     "token" : TOKEN,
#     "username" : USER_NAME,
#     "agreeTermsOfService" : "yes",
#     "notMinor" : "yes"
# }
# response = requests.post(url=pixela_api_end_point, json=post_request_body)
# print(response.text)

#------------------------Posting a pixel to a graph----------------------------#
# graph_api_endpoint = f"{pixela_api_end_point}/{USER_NAME}/graphs"


#Creating a new graph
# graph_api_request_body = {
#     "id" : "graph695",
#     "name" : "mygraph1",
#     "unit" : "kilogram",
#     "type" : "float",
#     "color" : "sora"
# }
# graph_api_response = requests.post(url=graph_api_endpoint,headers=api_header,json=graph_api_request_body)
# print(graph_api_response.text)


# posting_pixel_endpoint = f"{graph_api_endpoint}/graph695"

# posting_pixel_request_body = {
#     "date" : today.strftime("%Y%m%d"),
#     "quantity" : "30.0"
# }

# graph_update_res = requests.post(url=posting_pixel_endpoint, json=posting_pixel_request_body, headers=api_header)
# print(graph_update_res.text)

#--------------------Updating graph information-------------------------------------#
# edit_effort_of_day = today.strftime("%Y%m%d")
# quantity_to_be_edited = "10.0"
# pixel_update_endpoint = f"{pixela_api_end_point}/{USER_NAME}/graphs/graph695/{edit_effort_of_day}"
# edit_request_body = {
#     "quantity" : quantity_to_be_edited
# }
# put_response = requests.put(url=pixel_update_endpoint, json=edit_request_body, headers=api_header)
# print(put_response.text)

#--------------------- Delete a pixel from graph -----------------------------------#
# days_effort_to_be_deleted = datetime.datetime(year=2023, month=3, day=27).strftime("%Y%m%d")
# delete_end_point = f"{pixela_api_end_point}/{USER_NAME}/graphs/graph695/{days_effort_to_be_deleted}"
# delete_response = requests.delete(url=delete_end_point, headers=api_header)
# print(delete_response.text)

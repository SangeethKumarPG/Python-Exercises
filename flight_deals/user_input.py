import requests


def add_details_to_sheet(first_name, last_name, email):
  sheety_api_endpoint = "https://api.sheety.co/45fb9d517a6e430d238aa49526695266/flightDeals/users"
  sheety_api_token = {
    "Authorization": "Bearer This_is_my_top_secret_bearer_token"
  }
  sheety_add_user_request_body = {
    "user": {
      "firstName": first_name,
      "lastName": last_name,
      "email": email
    }
  }
  response = requests.post(url=sheety_api_endpoint,
                           headers=sheety_api_token,
                           json=sheety_add_user_request_body)
  response.raise_for_status()
  return int(response.status_code)


first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
email_1 = input("Enter your email : ")
email_2 = input("Enter your email again : ")
if email_1 == email_2:
  res_code = add_details_to_sheet(first_name, last_name, email_1)
  if res_code == 200:
    print("Sign up successfull, Welcome to the flight club!!!!")
  else:
    print("Oh! it seems some error occured")
else:
  print("Email do not match please try again")

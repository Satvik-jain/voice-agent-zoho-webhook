import requests
from zoho_auth import get_access_token
def get_module_fields():
    headers = {
        "Authorization": f"Bearer {get_access_token()}"
    }

    url = "https://www.zohoapis.in/crm/v7/settings/modules/Listings"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
    #     print("done 200")
    #     data = response.json()
    #     # print(data)
    #     # Search for your "Listings" module in the response
    #     for module in data.get("modules", []):
    #         # print(module)
    #         if module["api_name"] == "Listings":  # Assuming "Listings" is the API name
    #             print("present")
    #             print(module)
        module = response.json()
        print(module["modules"][0])
        fields = module['modules'][0].get("fields",[])
        fields = module.get("fields", [])
        # print(fields)
        for field in fields:
            print(f"Field API Name: {field['api_name']} - Field Label: {field['field_label']}")
    else:
        print(f"Error fetching fields: {response.text}")

get_module_fields()

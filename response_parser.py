def response_parser(data):
    """Extracts only required fields from the Zoho CRM response."""
    filtered_data = []
    
    for entry in data:
        filtered_entry = {
            "Property_ID": entry.get("id"),
            "Street_Address": entry.get("Property_ID"),
            "City": entry.get("City"),
            "Province": entry.get("Province"),
            "Country": entry.get("Country"),
            "Bedrooms": entry.get("Bedrooms"),
            "Bathrooms": entry.get("Bathrooms"),
            "Kitchen": entry.get("Kitchen"),
            "Hall": entry.get("Hall"),
            "Number_of_Parking_Spaces": entry.get("Number_of_Parking_Space"),
            "Rent_per_month": entry.get("Rent_per_month_in_USD1"),
            "Furnished": entry.get("Furnished"),
            "Parking_Available": entry.get("Parking_Available"),
            "Balcony": entry.get("Balcony"),
            "Swimming_Pool": entry.get("Swimming_Pool"),
            "Garden": entry.get("Garden"),
            "Gym_Facility": entry.get("Gym_Facility"),
            "Year_Built": entry.get("Year_Built"),
            "Moving_Date": entry.get("Moving_Date"),
            "Description": entry.get("Description"),
        }
        filtered_data.append(filtered_entry)

    return filtered_data

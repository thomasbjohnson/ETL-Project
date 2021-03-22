import api_key


def lowest_price_csv(value, input_list, ): 
    for code in input_list: 
        querystring = {value:code,"limit":"100","offset":"0","sort":"lowest price"}
        response = requests.request("GET", url, headers=api_key.headers, params=querystring).json()
        prop_type =[]
        city=[]
        lat=[]
        lon= []     
        price=[]
        building_size = []
        county_=[]
        postal_code=[]
        search_key='building_size'
        for s in range(len(response['properties'])):
            
        #     county_.append(response["properties"][s]["address"]["county"])
            lat.append(response["properties"][s]["address"]["lat"])
            lon.append(response["properties"][s]["address"]["lon"])
            price.append(response["properties"][s]["price"])
            city.append(response["properties"][s]["address"]["city"])
            
            if search_key in response["properties"][s].keys():
                save = response["properties"][s]["address"]["postal_code"]
                postal_code.append(save)
            else:
                postal_code.append(save)
                
            if search_key in response["properties"][s].keys():
                building_size.append(response["properties"][s]["building_size"]["size"])
            else:
                building_size.append('NA')

            realtor_df = pd.DataFrame(list(zip(prop_type, city, postal_code, lat, lon, building_size, price)), 
                columns =['prop_type', 'city', 'postal_code', 'lat', 'lon', 'size (sqft)', 'price']) 
            realtor_df.to_csv(f"output/{code}.csv", mode="w+")



from turtle import clear


travel_log={"africa":{"places":['uganda','rawanda','iddada']},"visits":5}
def add_new_country(country,places,no_of_visits):
    travel_log["country"]=country
    travel_log["places"]=places
    travel_log["visits"]=no_of_visits
    print(travel_log)
    
add_new_country("london","oxford street",50)
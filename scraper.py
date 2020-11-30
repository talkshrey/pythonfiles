import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import sqlconnect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num", help="Enter the page number", type=int)
parser.add_argument("--dbname", help="Enter the name of database", type=str)
args = parser.parse_args()

headers = {'user-agent': 'Mozilla/70.0(X11; Linux x86_64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/78.0.3904.97Safari/537.36'}

oyo_url = "https://www.oyorooms.com/hotels-in-mumbai/?page="

page_max = args.page_num
hotel_list = []
sqlconnect.connection(args.dbname)

for i in range(1, page_max):
    data = requests.get(url=oyo_url+str(i), verify=True, headers=headers)
    req_data = data.content
    soup = BeautifulSoup(req_data, "html.parser")

    hotel_cards = soup.find_all("div", {"class": "hotelCardListing"})

    for hotels in hotel_cards:
        hotel_dict = {}
        hotel_dict["name"] = hotels.find("h3", {"class": "listingHotelDescription__hotelName"}).text
        hotel_dict["address"] = hotels.find("span", {"itemprop": "streetAddress"}).text
        hotel_dict["rating"] = hotels.find("span", {"class": "hotelRating__rating"}).text
        hotel_dict["price"] = hotels.find("span", {"class": "listingPrice__finalPrice"}).text
        try:
            amenity = hotels.find("div", {"class": "amenityWrapper"})
            amenity_list = []
            for amenities in amenity.find_all("div", {"class": "amenityWrapper__amenity"}):
                amenity_list.append(amenities.find("span", {"class": "d-body-sm"}).text)
                hotel_dict["amenities"] = ', '.join(amenity_list[:-1])
        except AttributeError:
            hotel_dict["amenities"] = None

        hotel_list.append(hotel_dict)
        sqlconnect.insert_into_table(args.dbname, tuple(hotel_dict.values()))

database = pandas.DataFrame(hotel_list)
database.to_csv("OYO.csv")
sqlconnect.display_table(args.dbname)
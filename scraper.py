from cars import Cars, engine
from sqlalchemy.orm import sessionmaker
import requests
from bs4 import BeautifulSoup
import re
import time

Session = sessionmaker(bind=engine)
session = Session()


for page in range(1, 201):
    URL = f'''https://autoplius.lt/skelbimai/naudoti-automobiliai?offer_type=0&make_id_list=&engine_capacity_from=&
    engine_capacity_to=&power_from=&power_to=&kilometrage_from=&kilometrage_to=&has_damaged_id=10924&color_id=&
    condition_type_id=&make_date_from=&make_date_to=&sell_price_from=&sell_price_to=&fuel_id=&body_type_id=&
    wheel_drive_id=&euro_id=&fk_place_countries_id=1&fk_place_cities_id=&qt=&qt_autocomplete=&number_of_seats_id=&
    number_of_doors_id=&gearbox_id=&steering_wheel_id=10922&origin_country_id=&technical_passport=1&older_not=&
    save_search=1&slist=1529951561&category_id=2&order_by=&order_direction=&page_nr={page}'''

    source = requests.get(URL).text
    soup = BeautifulSoup(source, 'html.parser')
    blocks = soup.find_all('div', class_='announcement-body')

    for block in blocks:
        try:
            title = block.find('div', class_='announcement-title').text.strip()
            pattern = re.compile(
                r'(Alfa Romeo|Aston Martin|Austin Rover|DS Automobiles|Great Wall|Land Rover|^[A-z]+\S?\w+?\b)'
                r'\s([A-z0-9 \]+\S?[A-z0-9]+\S?[A-z0-9]?)\S\s([0-9\W]+)\S+\s(\w+)')
            result = pattern.search(title)

            make = result.group(1)
            model = result.group(2)
            capacity = result.group(3)
            model_type = result.group(4)
            first_registration = int(block.find('span', title='Pagaminimo data').text.strip()[:4])
            fuel = block.find('span', title='Kuro tipas').text.strip()
            gearbox = block.find('span', title='Pavarų dėžė').text.strip()
            power = block.find('span', title='Galia').text.strip()[:-4]
            mileage = block.find('span', title='Rida').text.strip()[:-3].replace(' ', '')
            city = block.find('span', title='Miestas').text.strip()
            price = block.find('strong').text.strip()[:-2].replace(' ', '')

            if len(mileage) > 4 or len(mileage) <= 4 and first_registration > 2016:
                new_car = Cars(price, make, model, capacity, model_type, first_registration,
                               fuel, gearbox, power, mileage, city)
                session.add(new_car)
                session.commit()
            else:
                pass
        except:
            pass

    time.sleep(5)
    print(page)

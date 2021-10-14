import requests
import json
from models.item import Item
from utils.header import random_header


class Parser:
    def __init__(self, query, query_id):
        self.query = query
        self.query_id = query_id
        self.new_items = []

    def parse_items(self):
        """
        Parses items, fills up new_items with items not already stored.
        """
        url = f'https://www.tutti.ch/de/li/ganze-schweiz?company_ad=false&q={self.query}'
        r = requests.Session()
        r.headers = random_header()
        response = r.get(url)
        try:
            # Items are already available in JSON format, just search on site
            items_string = response.content.decode('utf-8').split('window.__INITIAL_STATE__=')[1].split('</script>')[0]
        except:
            print('Could not find items.')
            return

        items_json = json.loads(items_string)
        # Items are not in array yet, y tho
        # Insert new items into db and new_items field
        for item_id in items_json['items']:
            if int(item_id) > 1000000000:
                # Probably an ad (wohnig)
                continue
            item = Item(items_json['items'][item_id], self.query_id)
            item_is_new = item.insert_into_db()
            if item_is_new:
                self.new_items.append(item)

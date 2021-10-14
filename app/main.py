from random import randint
from time import sleep
import datetime


from models import user, query, subscription
from parser import Parser
import bot


def run():
    """
    Run is called about once every 5 minutes and handles the whole flow for pushing new items to users
    """
    queries = query.get_all()

    for q in queries:
        p = Parser(q['query'], q['id'])
        p.parse_items()
        print(f"[LOG] Parsed query {q['query']} and found {len(p.new_items)} new items")

        # Send a message to every subscribed user
        # TODO: Use JOIN to access db only once (join subs and users)
        subscriptions = subscription.get_for_query(q['id'])
        for s in subscriptions:
            sub_user = user.get_user(s['user_id'])

            # Send a message for every new item
            for i in p.new_items:
                bot.send_item(i.to_telegram_msg(), sub_user['chat_id'])

        sleep(randint(50, 70))   # Wait a bit between individual queries

    print(f'[LOG] Ran parser at {datetime.datetime.now()}')


if __name__ == '__main__':
    sleep(15)
    while True:
        run()
        sleep(randint(850, 950))  # Query about every 15 minutes

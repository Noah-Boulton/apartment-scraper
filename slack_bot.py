def post_listing_to_slack(sc, apt):
    """
    Posts the listing to slack.
    :param sc: A slack client.
    :param listing: A record of the listing.
    """
    desc = "{0} | {1} | {2} | {3} | <{4}>".format(apt["name"], '$' + str(apt["price"]), apt["metro"], round(apt["distance"], 3), apt["url"])
    sc.api_call(
        "chat.postMessage", channel='#finding-an-apartment', text=desc,
        username='Jeeves', icon_emoji=':male-detective:')
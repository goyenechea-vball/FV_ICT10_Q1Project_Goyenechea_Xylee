from pyscript import display
#String
store_name = "Book2Go"

owner_name = "Xylee Goyenechea"

popular_item_price = 845
best_seller_message = f"Our best seller is P{popular_item_price}"
#Integer
year_established = 2025

has_delivery = "We Deliver!" #True 

#Tuple
store_hours = ("10:00 AM", "8:00 PM")
#Dictionary
books = {
    'The HouseMaid': 'P500',
    'The Silent Patient': 'P845',
    'The House Across The Lake': 'P650',
    'Nothing Like The Movies': 'P525',
    'The Summer I Turned Pretty': 'P675'
}
books_str = "\n".join([f"{title}: {price}" for title, price in books.items()])

how_to_care = {'store': 'cool temp', 'place': 'upright', 'handle': 'carefully'}
how_to_care_str = "\n".join([f"{key}: {value}" for key, value in how_to_care.items()])      
#Floating-point
# tax_rate = 0.025

#Display Store Info
display(store_name, target= "storename")
display(owner_name, target="ownername")
display(year_established, target="yearfounded")
display(best_seller_message, target="popular")
display(has_delivery, target="delivery")
display(store_hours, target="hours")
display(books_str, target="books")
display(how_to_care_str, target="howtocare")
# display(tax_rate, target="tax")




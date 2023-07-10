import json
import yaml
from datetime import datetime, date

# Load the news data from the JSON file
with open('_news/news_data.json') as file:
    news_data = json.load(file)

# Get the current date
current_date = date.today()

# Filter out expired news items
filtered_news_data = []
for news_item in news_data:
    expiration_date_str = news_item.get('expiration_date')  # Assuming 'expiration_date' is the key for the expiration date field

    if expiration_date_str:
        # Parse the expiration date as a datetime.date object
        expiration_date = datetime.strptime(expiration_date_str, '%Y-%m-%d').date()

        # Check if the expiration date is greater than or equal to the current date
        if expiration_date >= current_date:
            filtered_news_data.append(news_item)

# Save the filtered news data back to the JSON file
with open('filtered_news_data.json', 'w') as file:
    json.dump(filtered_news_data, file, indent=4)

# Convert the filtered news data to YAML
yaml_data = yaml.dump(filtered_news_data)

# Save the YAML data to a file
with open('_news/filtered_news.yaml', 'w') as file:
    file.write(yaml_data)

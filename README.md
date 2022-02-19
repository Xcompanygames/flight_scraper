![img.png](img.png)

# flight_scraper
## Selenium scraping implementation
Scrapses a website with flights scraping them as a flight object

## Classes

Scraper is written with OOP in mind so:

- [flight] Object- flight object with data on the flight, also have few methods for searching data inside the object.
- [data_collection_manager] Object - The flight manager, initiate all the scraping process also initiate search in all the flights objtects available. 
- [file_manager] - A file manager that saves article objects and loads json files into flight objects. (Not an object!)
- [flight_scraper] Scrapes the flight and create the objects.

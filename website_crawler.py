import requests
from bs4 import BeautifulSoup

# Function to scrape the website and find products with a price less than 5
def find_products_with_price_less_than_5(url):
    try:
        # Initialize a session to maintain cookies (for session-based websites)
        session = requests.Session()

        # Initialize a variable to keep track of the page number
        page_number = 1

        # Store the content of the first page
        first_page_content = None

        while True:
            # Construct the URL for the current page
            current_url = f"{url}?page={page_number}"

            # Send an HTTP GET request to the URL
            response = requests.get(current_url, timeout=30)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Check if the page redirected to the first page
                if current_url != response.url:
                    print("Reached the last page. Exiting.")
                    break
                
                # Parse the HTML content of the webpage
                soup = BeautifulSoup(response.text, 'html.parser')

                # If this is the first page, store its content
                if page_number == 1:
                    first_page_content = response.content

                # Locate the HTML elements that contain product information
                # You need to inspect the webpage's HTML to find the correct elements
                # For demonstration purposes, let's assume product information is inside a <div> with class 'product'
                product_elements = soup.find_all('div', class_='card-body product-card-body mb-2')
                #print(product_elements)

                # If there are no more product elements, break out of the loop
                if not product_elements:
                    break

                # Check if the current page content matches the first page content
                if page_number > 1 and response.content == first_page_content:
                    print("Detected redirection to the first page. Exiting.")
                    break

                # Iterate through the product elements
                for product in product_elements:
                    # Extract product details (name, price, etc.) based on the actual HTML structure
                    product_name = product.find('h5', class_='card-title product-card-name').text.strip()
                    #print(product_name)
                    product_price = float(product.find('span', class_='stockrecord-price-current').text.strip().replace('KES', '').replace(',', ''))
                    #print(product_price)

                    # Check if the product price is less than 5
                    if product_price < 500:
                        print(f"Product: {product_name}")
                        print(f"Price: KES {product_price:.2f}")
                        print("--------------------")
                    
                # Increment the page number for the next iteration
                page_number += 1

            # Check if we've been redirected to the first page
            elif response.status_code == 302 or response.status_code == 307 or 'Location' in response.headers:
                print("Reached the end of pages. Redirected to the first page.")
                break

            else:
                print(f"Failed to fetch webpage. Status code: {response.status_code}")
                break

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example URL of the webpage containing product listings
webpage_url = 'https://textbookcentre.com/catalogue/category/computers-accessories/'

# Call the function to find products with a price less than 5
find_products_with_price_less_than_5(webpage_url)

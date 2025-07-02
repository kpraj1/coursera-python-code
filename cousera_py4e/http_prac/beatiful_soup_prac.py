# from bs4 import BeautifulSoup
# import urllib.request
#
# url = 'http://www.dr-chuck.com/page1.htm'
# #url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
# html = urllib.request.urlopen(url).read()
#
# soup = BeautifulSoup(html, 'html.parser')  # Or use 'lml'
#
# print("== All Links ==")
# for tag in soup('a'):
#     print(tag.get('href', None))


from bs4 import BeautifulSoup
import urllib.request

url = 'http://books.toscrape.com/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

books = soup.find_all('article', class_='product_pod')

for book in books:
    title = book.find('h3').a['title']
    link = 'http://books.toscrape.com/' + book.find('h3').a['href']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()
    rating = book.find('p', class_='star-rating')['class'][-1]

    print(f"Title: {title}")
    print(f"Link: {link}")
    print(f"Price: {price}")
    print(f"Availability: {availability}")
    print(f"Rating: {rating}")
    print("-" * 40)


#sample data which you are dealing
"""
<article class="product_pod">
    
    <!-- Image Container -->
    <div class="image_container">
        <a href="catalogue/a-light-in-the-attic_1000/index.html">
            <img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" 
                 alt="A Light in the Attic" class="thumbnail">
        </a>
    </div>
    
    <!-- Star Rating -->
    <p class="star-rating Three">
        <i class="icon-star"></i>
        <i class="icon-star"></i>
        <i class="icon-star"></i>
        <i class="icon-star"></i>
        <i class="icon-star"></i>
    </p>
    
    <!-- Book Title -->
    <h3>
        <a href="catalogue/a-light-in-the-attic_1000/index.html" 
           title="A Light in the Attic">
           A Light in the Attic
        </a>
    </h3>
    
    <!-- Product Price and Availability -->
    <div class="product_price">
        <!-- Price -->
        <p class="price_color">£51.77</p>
        
        <!-- Availability -->
        <p class="instock availability">
            <i class="icon-ok"></i>
            In stock
        </p>
        
        <!-- Add to Basket Button -->
        <form>
            <button type="submit" class="btn btn-primary btn-block" 
                    data-loading-text="Adding...">Add to basket</button>
        </form>
    </div>

</article>

"""
import matplotlib.pyplot as plt

products = ['Mobile Phones', 'Laptops', 'Tablets', 'Smart Watches', 'Headphones']
sales = [50000, 300000, 80000, 40000, 20000]

plt.bar(products, sales, color='skyblue')
plt.title('Sales of Products')
plt.xlabel('products')
plt.ylabel('sales')
plt.show()


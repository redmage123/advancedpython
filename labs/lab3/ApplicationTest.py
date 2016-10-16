#!/usr/bin/python3
import unittest
from CustomerApplication.Products import Product
from CustomerApplication.Customers import Customer
from CustomerApplication.Orders import Order
from CustomerApplication.OrderDetails import OrderDetails


# This is the Customer test suite. 
class TestCustomerLoader(unittest.TestCase):

    CustomersList = []
    @classmethod
    def setUpClass(cls):
        with open("data/Customers") as c:
            CustomerList.append(c.read().strip())


    def setUp(self):
        self.Customer = Customer()
        

    def testLoadingCustomersIntoApplication(self):
        for customer in CustomerList:
            self.Customer.addCustomer(customer)
        
        self.assertEqual(len(Customers),self.Customer.numberOfCustomers())

    def testThatCustomerExists(self):
        self.assertEqual(self.Customer.exists("The Chocolate Store")

    def testThatCustomerExists2(self):
        self.assertEqual(self.Customer.exists("Yummy Confectionaries") 

    def testThatCustomerExists3(self):
        self.assertEqual(self.Customer.exists("Edible Tasties Inc.") 

    def testThatCustomerExists4(self):
        self.assertEqual(Customer.isExists("The Lemon Drop") 

    def testThatCustomerExists4(self):
        self.assertEqual(Customer.isExists("The Marzipan Counter")



# Product Test Suite

class TestProductLoader(unittest):

    ProductList = []
    @classmethod
    def SetUpClass(self):
        with open ("data/Products") as p:
            ProductList.append(p.read().strip())

    def Setup(self):
        self.Products = Product()
        
    def testLoadingProducts:
        for product in ProductList:
            self.Product.addProducts(product)

        self.assertEqual(len(self.ProductList),Product.numberOfProducts())

    def testThatProductExists(self):
        self.assertEqual(self.Product.exists("Yummy Gummy Bears")

    def testThatProductExists(self):
        self.assertEqual(self.Product.exists("Chocolate Frogs")

    def testThatProductExists(self):
        self.assertEqual(self.Product.exists("Peppermint Lollipops")

    def testThatProductExists(self):
        self.assertEqual(self.Product.exists("Carmel Brownies")

    def testThatProductExists(self):
        self.assertEqual(self.Product.exists("Hazelnut Clusters")

# Order Test Suite

class TestOrderLoader(unittest):

    OrdersList = []

    @classmethod
    def SetupClass(self):
        with open ("data/Orders") as o:
            OrderList.append(o.read().strip())

    def Setup(self):
        self.Order = Order()
        self.OrderDetails = OrderDetail()

    def testLoadingOrders:
        for order in OrderList:
            self.order.addOrder(order)

        self.assertEqual(len(self.OrderList),self.Order.numberOfOrders())

    def testThatOrderExists(self):
        self.assertEqual(self.Order.exists(50001)

    def testThatOrderExists(self):
        self.assertEqual(self.Order.exists(50002)

    def testThatOrderExists(self):
        self.assertEqual(self.Order.exists(50003)

    def testThatOrderExists(self):
        self.assertEqual(self.Order.exists(50004)

    def testThatOrderExists(self):
        self.assertEqual(self.Order.exists(50005)

    def testnumberOfOrderDetails(self):
        self.assertEqual(self.numOrderDetails(50001),2)



CustomerTestSuite = unittest.makeSuite(TestCustomerLoader)
ProductTestSuite = unittest.makeSuite(TestProductLoader)
OrderTestSuite = unittest.makeSuite(TestOrderLoader)


if __name__ == "__main__":
    appTestRunner = unittest.TextTestRunner()
    appTestRunner.run(CustomerTestSuite)
    appTestRunner.run(ProductTestSuite)
    appTestRunner.run(OrderTestSuite)


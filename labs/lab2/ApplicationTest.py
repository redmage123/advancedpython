import unittest


from CustomerApplication import Product

class TestProductLoader(unittest.TestCase):

    Customers = [];
    @classmethod
    def setUpClass(cls):
        with open("data/Customers") as c:
            Customers.append(c.read().strip())

    def setUp(self):
        self.Customer = Customer()


    def testLoadingCustomersIntoApplication(self):
        for customer in Customers:
            Customer.addCustomer(customer)
        
        self.assertEqual(len(Customers),Customer.numberOfCustomers)

    def testThatCustomerExists(self):
        self.assertEqual(Customer.exists("The Chocolate Store")

    def testThatCustomerExists2(self):
        self.assertEqual(Customer.exists("Yummy Confectionaries") 

    def testThatCustomerExists3(self):
        self.assertEqual(Customer.exists("Edible Tasties Inc.") 

    def testThatCustomerExists4(self):
        self.assertEqual(Customer.isExists("The Lemon Drop") 

    def testThatCustomerExists4(self):
        self.assertEqual(Customer.isExists("The Marzipan Counter")


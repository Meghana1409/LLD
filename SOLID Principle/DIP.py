'''
The dependency inversion principle (DIP) is the last principle in the SOLID set. 
This principle states that: Abstractions should not depend upon details. Details should depend upon abstractions.
Say you’re building an application and have a FrontEnd class to display data to the users in a friendly way. 
'''
# app_dip.py

class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)

class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"
'''
In this example, the FrontEnd class depends on the BackEnd class and its concrete implementation. You can say that both classes are tightly coupled. This coupling can lead to scalability issues.
For example, say that your app is growing fast, and you want the app to be able to read data from a REST API. How would you do that?

You may think of adding a new method to BackEnd to retrieve the data from the REST API. However, that will also require you to modify FrontEnd, which should be closed to modification, according to the open-closed principle.

To fix the issue, you can apply the dependency inversion principle and make your classes depend on abstractions rather than on concrete implementations like BackEnd. 
In this specific example, you can introduce a DataSource class that provides the interface to use in your concrete classes:
'''

# app_dip.py

from abc import ABC, abstractmethod

class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):
        return "Data from the API"

'''
In this redesign of your classes, you’ve added a DataSource class as an abstraction that provides the required interface, or the .get_data() method.
Note how FrontEnd now depends on the interface provided by DataSource, which is an abstraction.

Then you define the Database class, which is a concrete implementation for those cases where you want to retrieve the data from your database. 
This class depends on the DataSource abstraction through inheritance. Finally, you define the API class to support retrieving the data from the REST API. This class also depends on the DataSource abstraction

'''

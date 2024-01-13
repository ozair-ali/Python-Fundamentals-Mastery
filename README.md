Task1.
Description:
The provided Python code defines a list named mixed_data that contains a variety of data types, including integers, floats, complex numbers, and strings. The code then prints specific subsets of this list using slicing operations.

logic:
The first part of the code initializes a list named mixed_data with elements of different data types, such as integers, floats, complex numbers, and strings.
The first print statement displays the first three elements of the list using list slicing (mixed_data[0:3]). In Python, indexing starts from 0, so mixed_data[0] is the first element, mixed_data[1] is the second, and so on.
The second print statement shows the elements from the 2nd to the 5th position using list slicing (mixed_data[1:5]).
The third print statement prints the last two elements of the list using list slicing (mixed_data[6:]). The colon : without an ending index means it will include all elements from the specified starting index until the end of the list.

The second part of the Python code iterates through the elements of the mixed_data list and prints each element along with its respective data type.
The for loop iterates through each element in the mixed_data list. For each iteration, it prints the element, followed by its data type.

INSIGHTS:
Data Diversity: The use of different data types within the mixed_data list demonstrates Python's flexibility in handling mixed types within a single container.

Slicing Usage: The code showcases the concept of list slicing, a fundamental concept in Python. Slicing allows us to extract specific portions of a list, making it a powerful tool for data manipulation.

Indexing Reminder: The comments emphasize the importance of understanding zero-based indexing in Python, ensuring clarity about which elements are being accessed.

Dynamic Slicing: The last print statement demonstrates dynamic slicing to retrieve the last two elements without explicitly specifying the end index.

Dynamic Typing: This code highlights Python's dynamic typing feature, where the type of a variable is determined at runtime. By using type(element).__name__, the code fetches the name of the type without unnecessary details.

Loop Iteration: The use of a for loop demonstrates an efficient way to iterate through a list, showcasing a fundamental control flow concept in Python.


Conclusion:
This Python code serves as a concise example for understanding fundamental concepts like lists, indexing, slicing and how Python handles dynamic typing and diverse data structures.



Task2.
Description:
The provided Python code defines a function named calculate_discount that calculates the discounted price based on the original price and a given discount percentage. The code then calls this function with specific values and prints the resulting discounted price.

logic:
The first part of the code defines a function calculate_discount that takes two parameters (original_price and discount_percentage) and calculates the discounted price using the provided formula.
The function calculate_discount is then called with an original price of 10,000 and a discount percentage of 10.
The resulting discounted price is then printed in a formatted string.

INSIGHTS:
Modularization: The code encapsulates the discount calculation logic within a function (calculate_discount). This promotes code reusability and follows the principle of modularization.

Parameter Usage: The function takes two parameters (original_price and discount_percentage), allowing flexibility in calculating discounts for different products or scenarios.


Conclusion:
This Python code demonstrates the creation of a simple function for calculating discounts and its application with specific values. The modular design enhances maintainability and reusability, while the usage of parameters allows flexibility in adapting the function to different scenarios.



Task3.
Description:
In this Python code we are calculating the discounted price based on user-input original price and discount percentage. After calculating the discounted price, we are categorizing the item as "Low-cost," "Moderate-cost," or "High-cost" based on specific price ranges.

logic:
The first part of the code defines a function calculate_discount that takes two parameters (original_price and discount_percentage) and calculates the discounted price using the provided formula.
The second part of the code takes user input for the original price and discount percentage, calls the calculate_discount function to calculate the dicounted price, and displays the resulting discounted price.
The last part of the code uses conditional statements or control flow statements to categorize the item as "Low-cost," "Moderate-cost," or "High-cost" based on specific price ranges.

INSIGHTS:
User Input: The use of float(input(...)) ensures that the user's input for the original price and discount percentage is converted to floating-point numbers, allowing for decimal values.

Function Reusability: The calculate_discount function is reusable and separates the discount calculation logic, promoting code modularity.

Categorization Logic: The conditional statements categorize items based on their discounted prices into three cost ranges—low, moderate, and high. This enhances the usefulness of the program by providing additional information about the item


Conclusion:
This Python code demonstrates user input processing, function utilization, and conditional statements to categorize items based on their discounted prices. It adheres to principles of modularity, user interaction, and readability, making it a practical example of a basic discount calculator with additional categorization features.



Task4.
Description:
The provided Python code opens a text file containing product descriptions, reads the content, and writes a new file with the product descriptions formatted with upper case.

logic:
The code begins by opening two files: one for reading (file) and another for writing (newfile).
It checks if both files are successfully opened using the condition if file and newfile.
If the files are opened successfully, it prints a message and proceeds to read the content of the source file (file).
The content is processed line by line using readlines().
Using for loop, each line is converted to upper case using the title() method.The formatted lines are then written to a new file (newfile) in title case.
Finally, both files are closed.

INSIGHTS:
File Handling: The code demonstrates the use of file handling concepts in Python, opening files for reading and writing, reading lines, and writing modified content to a new file.

Conditional Statements: The if statement is used to check if both files are successfully opened. This ensures that the code doesn't proceed if there's an issue with file access.

Iterating Through Lines: The code efficiently iterates through each line of the source file and applies the title() method to capitalize the first letter of each word.


Conclusion:
This Python code exemplifies file handling, iteration through file content, and the use of conditional statements.The code is designed to format product descriptions into upper case, providing a practical example of text processing in Python.



Task5.
Description:
The provided Python code defines a dictionary customer info containing information about a customer, including their name, age, and purchase history. The code then extracts and prints specific information from the dictionary, such as the customer's name and the second item from their purchase history.

logic:
The code first initializes a dictionary named customer_info with key-value pairs representing customer information, including name, age, and a list of purchase history.
It then extracts the value associated with the 'Name' key from the dictionary and assigns it to the variable customer_name. The code then prints the customer's name
In the last part it extracts the value associated with the 'Purchase History' key, which is a list, and assigns it to the variable purchase_history. It then extracts the second item from the purchase history list and assigns it to the variable second_purchase. The code prints the second purchase

INSIGHTS:
Dictionary Usage: The code utilizes a dictionary to store related information about a customer, allowing for easy access and retrieval of specific details.

Key-Value Access: The use of key-value pairs allows the code to access specific pieces of information, such as the customer's name and purchase history.


Conclusion:
This Python code exemplifies the use of dictionaries for storing and accessing related information. It showcases how to extract specific values from a dictionary and how to work with lists, providing insights into key concepts such as indexing and key-value pairs in Python.



Task6.
Description:
The provided Python code defines a class named book with attributes title, author, and genre. It includes a method display_information to print details about a book. An instance of the class is created, and information about a specific book is displayed using the display_information method.

logic:
A class named book is defined with three attributes: title, author, and genre.
The __init__ method is a special method which initializes the object with specified attributes.
The self.title, self.author, and self.genre are instance attributes. They represent the data associated with each instance of the class.
An instance of the book class is created, my_book is an instance of the book class. 
A method named display_information is defined within the class.This method prints the title, author, and genre of the book using the print statements.

INSIGHTS:
Attributes and Methods: The use of attributes (title, author, genre) and methods (__init__, display_information) aligns with object-oriented programming principles.

Instance Usage: An instance of the class is created with specific values, demonstrating how objects can represent real-world entities.


Conclusion:
This Python code serves as a fundamental example of class creation, attribute initialization, method definition, and instance usage. It provides a structured way to represent and interact with information about a book, highlighting key concepts of object-oriented programming in Python. 

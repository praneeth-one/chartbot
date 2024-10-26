from flask import Flask, request, render_template, jsonify # type: ignore

app = Flask(__name__)

# Sample data for chatbot responses for each programming language
data_arrays = {
    'java': [
        {'question': 'what is the remedies for slow performance', 'answer': 'Increase RAM and optimize code.'},
        {'question': 'print a + b in python sum of two numbers code in python', 'answer': 'a = 10\nb = 20\nprint(a + b)'},
        {'question': 'What is the capital of Germany?', 'answer': 'Berlin'},
        {'question': 'What is the syntax for declaring a variable in Java?', 
        'answer': 'To declare a variable in Java, use the syntax: dataType variableName; Example: int age; String name;.'},

        #java basic syntaxes

        {'question': 'What is the syntax for initializing a variable in Java ? what is syntax of variable in java variable syntax ', 
        'answer': 'To initialize a variable, use the syntax: dataType variableName = value; Example: int age = 30; String name = "John";.'},

        {'question': 'What is the syntax for declaring a constant in Java what is the syntax of constant in java constant syntax in java what is syntax for constant?', 
        'answer': 'To declare a constant, use the final keyword: final dataType constantName = value; Example: final double PI = 3.14;.'},

        {'question': 'What is the syntax for declaring an integer variable in Java? what is the syntax for integer variable syntax in java integer variable syntax', 
        'answer': 'To declare an integer variable, use: int variableName; Example: int count;.'},

        {'question': 'What is the syntax for declaring a floating-point variable in Java? what is the floating point variable syntax what is floting point point variable', 
        'answer': 'To declare a floating-point variable, use: float variableName; Example: float price; double distance;.'},

        {'question': 'What is the syntax for declaring a character variable in Java? what is the syntax for charecter variable in java character variable syntax', 
        'answer': 'To declare a character variable, use: char variableName; Example: char initial;.'},

        {'question': 'What is the syntax for declaring a boolean variable in Java? what is the boolean variable in java boolean varable sysntax', 
        'answer': 'To declare a boolean variable, use: boolean variableName; Example: boolean isActive;.'},

        {'question': 'What is the syntax for declaring a String variable in Java? what is the syntax for string variable in java sting variable sysntax ', 
        'answer': 'To declare a String variable, use: String variableName; Example: String message;.'},

        {'question': 'What is the syntax for using arrays in Java? syntax for arrays in java arrays syntax what is syntax for arrays array syntax ', 
        'answer': 'To declare an array, use: dataType[] arrayName; Example: int[] numbers; String[] names;.'},

        {'question': 'What is the syntax for declaring an object variable in Java? what is the syntax for object variable in java object variable syntax', 
        'answer': 'To declare an object variable, use: ClassName variableName; Example: MyClass obj;.'},

        #operaters in java

        {'question': 'What is use of + use in java ', 
        'answer': 'addition operation and concatination operation'},

        {'question': 'What are operators in Java?', 
        'answer': 'Operators in Java are special symbols that perform operations on variables and values, enabling various computations and evaluations in the code.'},

        {'question': 'What is the difference between unary and binary operators in Java?', 
        'answer': 'Unary operators operate on a single operand (e.g., increment, decrement), while binary operators work on two operands (e.g., addition, subtraction).'},

         {'question': 'What are the unary operators in Java unary operators what are unary operators in java', 
        'answer': 'Unary operators operate on a single operand (e.g., increment, decrement), while binary operators work on two operands (e.g., addition, subtraction).'},

         {'question': 'What are the binary operators in Java binary operators what are binary operators in java', 
        'answer': 'Unary operators operate on a single operand (e.g., increment, decrement), while binary operators work on two operands (e.g., addition, subtraction).'},

        {'question': 'What are arithmetic operators in Java arthematic operators what are arithematic operarters in java', 
        'answer': 'Arithmetic operators perform basic mathematical operations such as addition (+), subtraction (-), multiplication (*), division (/), and modulus (%).'},

        {'question': 'How do comparison operators work in Java comparision operatres wroks how comparision operators works', 
        'answer': 'Comparison operators in Java compare two values and return a boolean result. They include equal to (==), not equal to (!=), greater than (>), less than (<), and their respective combinations.'},

        {'question': 'What are logical operators in Java logical operators in java what are logical operators in java', 
        'answer': 'Logical operators are used to combine multiple boolean expressions. The primary logical operators are AND (&&), OR (||), and NOT (!).'},

        {'question': 'What is the purpose of the ternary operator in Java whai is the ternary operator in java ternary operator', 
        'answer': 'The ternary operator (?:) is a shorthand for the if-else statement, allowing for a compact way to evaluate a boolean expression and return one of two values based on the evaluation.'},

        {'question': 'What are bitwise operators in Java bitwise operators ', 
        'answer': 'Bitwise operators operate on the binary representation of integers, allowing manipulation of individual bits. Common bitwise operators include AND (&), OR (|), XOR (^), NOT (~), and bit shifts (<<, >>).'},

        {'question': 'How do assignment operators function in Java what is working of operators in java ', 
        'answer': 'Assignment operators assign values to variables. The most common is the simple assignment operator (=), but there are also compound assignment operators like +=, -=, *=, and /=.'},

        {'question': 'What is the role of the instanceof operator in Java?', 
        'answer': 'The instanceof operator checks whether an object is an instance of a specified class or interface, returning a boolean value.'},

        {'question': 'How are short-circuiting operators used in Java?', 
        'answer': 'Short-circuiting operators (&& and ||) evaluate expressions such that if the first operand determines the result, the second operand is not evaluated, enhancing performance and preventing unnecessary calculations.'},

    
        #java operators syntax
        {'question': 'What is Java ment by ', 
        'answer': 'Java is a high-level, object-oriented programming language that is platform-independent and designed to have as few implementation dependencies as possible.'},

        {'question': 'What are the main features of Java features ?', 
        'answer': 'Java is platform-independent, object-oriented, secure, robust, and has a rich API. It also supports multithreading and automatic memory management through garbage collection.'},

        {'question': 'What is bytecode in Java java byte code ', 
        'answer': 'Bytecode is the intermediate code generated by the Java compiler, which is executed by the Java Virtual Machine (JVM) to make Java platform-independent.'},

        {'question': 'What is the Java Virtual Machine (JVM) what is java virtual machine ', 
        'answer': 'The JVM is an engine that provides a runtime environment to execute Java bytecode, allowing Java applications to run on any platform that has the JVM installed.'},

        {'question': 'What is the difference between JDK, JRE, and JVM?', 
        'answer': 'The JDK (Java Development Kit) is used to develop Java applications, the JRE (Java Runtime Environment) provides the libraries and environment to run Java applications, and the JVM (Java Virtual Machine) executes the bytecode.'},

        {'question': 'What is object-oriented programming in Java object oriende programming', 
        'answer': 'Object-oriented programming (OOP) in Java is a programming paradigm based on the concept of objects, which can contain data (fields) and methods (functions). Key concepts include inheritance, encapsulation, polymorphism, and abstraction.'},

        {'question': 'What is garbage collection in Java?', 
        'answer': 'Garbage collection in Java is the process of automatically reclaiming memory by removing objects that are no longer in use, thus preventing memory leaks.'},

        {'question': 'What is the significance of the main method in Java main methods', 
        'answer': 'The main method is the entry point of any standalone Java application. It is defined as: public static void main(String[] args), and it is where the execution of a Java program begins.'},

        {'question': 'What are Java packages?', 
        'answer': 'A package in Java is a namespace that organizes a set of related classes and interfaces. Packages help avoid name conflicts and can contain classes, interfaces, sub-packages, and other elements.'},

        {'question': 'What is the difference between a class and an object in Java?', 
        'answer': 'A class is a blueprint for objects that defines the properties and behaviors (methods) of objects. An object is an instance of a class that represents a specific entity with its own data and methods.'},
    ],
    'python': [
        {'question': 'how to declare a variable in python?', 'answer': 'You can declare a variable by just assigning it a value: x = 10'},

        {'question': 'how to create a function in python?', 'answer': 'def my_function():\n    pass'},

        {'question': 'What is the capital of France?', 'answer': 'Paris'},

        {'question': 'What is Python tell me about python', 
        'answer': 'Python is a high-level, interpreted programming language known for its simplicity and readability. It is used for various applications, including web development, data analysis, and automation.'},

        {'question': 'How do you print something in Python use of print statement ', 
        'answer': 'You can print text or variables in Python using the print() function. For example: print("Hello, World!");.'},

        {'question': 'What is a data type in Python data type what is python data type', 
        'answer': 'A data type in Python defines the kind of value a variable can hold. Common data types include integers (int), floating-point numbers (float), strings (str), and booleans (bool).'},

        {'question': 'How do you create a list in Python?', 
        'answer': 'You create a list in Python by placing values inside square brackets []. For example: my_list = [1, 2, 3];.'},

        {'question': 'What is a loop in Python ,python loop statements,loops in python,python loops, different python loops,explain python loops,types of python loops,describe loops in python, what is meant by a python loop,define a loop in python', 
        'answer': 'A loop is a programming structure that repeats a block of code multiple times. In Python, common loops include for loops and while loops.'},

        {'question': 'How do you define a variable in Python?,what is meant by a variable in python variables?, describe python variables?, define a variable in python?', 
        'answer': 'You define a variable in Python by assigning a value to a name using the = operator. For example: age = 25;.'},

        {'question': 'What is an if statement in python if statemet syntax', 
        'answer': 'An if statement is a conditional statement that executes a block of code if a specified condition is true. For example: if age >= 18: print("You are an adult.");'},

        {'question': 'How do you take input from a user in Python input statement python input statements', 
        'answer': 'You can take input from a user using the input() function. For example: name = input("Enter your name: ");.'},

        {'question': 'What is a string in Python string what are strings in python strings', 
        'answer': 'A string in Python is a sequence of characters enclosed in quotes (single or double). For example: greeting = "Hello";.'},

        {'question': 'How do you access an element in a list?', 
        'answer': 'You access an element in a list using its index, which starts at 0. For example: first_item = my_list[0];.'},
    
        {'question': 'What is a variable in Python, and how do you declare one whay is variable in python variable syntax', 
        'answer': 'A variable in Python is a name that refers to a value. You declare a variable by assigning a value to it using the syntax: variable_name = value. For example: x = 10;.'},

        {'question': 'How do you write a comment in Python comments in python', 
        'answer': 'In Python, you write a comment by using the # symbol before the comment text. For example: # This is a comment;.'},

        {'question': 'What is the list in python lists what is list in python', 
        'answer': 'The lists are mutable (can be changed) collection of data,Lists are created with square brackets []'},

        {'question': 'What is the tuple in Python what is tuple in python tuples ', 
        'answer': 'while tuples are immutable (cannot be changed) and tuples are created with parentheses ().'},

        {'question': 'What is the difference between a list and a tuple in Python?', 
        'answer': 'The main difference is that lists are mutable (can be changed), while tuples are immutable (cannot be changed). Lists are created with square brackets [], and tuples are created with parentheses ().'},

        {'question': 'How do you create a function in Python functions what is functions in python ', 
        'answer': 'You create a function in Python using the def keyword followed by the function name and parentheses. For example: def my_function():.'},

        {'question': 'What is the purpose of the def keyword in Python keywords tell me about keywords', 
        'answer': 'The def keyword is used to define a function. It indicates the start of a function definition.'},

        {'question': 'What does the print() function do in Python output statements in python', 
        'answer': 'The print() function outputs data to the console. For example: print("Hello, World!");.'},

        {'question': 'How do you check the length of a list in Python?', 
        'answer': 'To check the length of a list, use the len() function. For example: length = len(my_list);.'},

        {'question': 'What is the difference between append() and extend() in Python lists?', 
        'answer': 'The append() method adds a single element to the end of the list, while the extend() method adds all elements of an iterable (like another list) to the end of the list.'},

        {'question': 'How do you create a loop in Python to iterate over a list?', 
        'answer': 'You can use a for loop to iterate over a list. For example: for item in my_list: print(item);.'},

        {'question': 'What is a dictionary in Python, and how is it different from a list?', 
        'answer': 'A dictionary is a data structure that stores data in key-value pairs. Unlike lists, which store items in a specific order, dictionaries are unordered and allow fast access via keys.'},
            
        {'question': 'What is the purpose of the import statement in Python?', 
        'answer': 'The import statement is used to include modules in your program, allowing you to use functions and variables defined in those modules. For example: import math;.'},

        {'question': 'How do you handle exceptions in Python?', 
        'answer': 'You handle exceptions using try and except blocks. For example: try: risky_code(); except ExceptionType: handle_error();.'},

        {'question': 'What is a list comprehension in Python?', 
        'answer': 'A list comprehension is a concise way to create lists. It consists of an expression followed by a for clause inside square brackets. For example: squares = [x**2 for x in range(10)];.'},

        {'question': 'How do you read a file in Python?', 
        'answer': 'You can read a file using the open() function and the read() method. For example: with open("file.txt", "r") as file: content = file.read();.'},

        {'question': 'What is the difference between == and is in Python?', 
        'answer': 'The == operator checks for value equality, while the is operator checks for identity (whether two references point to the same object in memory).'},
        
        {'question': 'How can you sort a list in Python?', 
        'answer': 'You can sort a list in place using the sort() method or create a new sorted list using the sorted() function. For example: my_list.sort(); or sorted_list = sorted(my_list);.'},

        {'question': 'What is a module in Python?', 
        'answer': 'A module is a file containing Python code, which can include functions, classes, and variables. Modules help organize code and allow for code reuse.'},

        {'question': 'How do you create a set in Python?', 
        'answer': 'You create a set using curly braces {} or the set() function. For example: my_set = {1, 2, 3}; or my_set = set([1, 2, 3]);.'},

        {'question': 'What is the purpose of the pass statement in Python?', 
        'answer': 'The pass statement is a null operation used as a placeholder in situations where syntactically some code is required, but you have nothing to execute.'},

        {'question': 'How do you find the maximum value in a list in Python?', 
        'answer': 'You can find the maximum value in a list using the max() function. For example: maximum_value = max(my_list);.'},

        {'question': 'what are the iterative statements in python iterative statements ', 
        'answer': 'the iterative ststements in python are same as another languages "for", "while", "do while", "for each"'},
        #looping statements 
        {'question': 'for loop syntax for for loop', 
        'answer': 'syntax for for loop is "for variable in iterable:"'},
        {'question': 'while loop syntax for while loop', 
        'answer': 'syntax for whiel loop is "while condition:"'},
        {'question': 'while loop syntax for while loop', 
        'answer': 'syntax for whiel loop is "while condition:"'},

    ],

    'c': [
        {'question': 'how to declare a variable in C?', 'answer': 'int x = 10;'},
        {'question': 'how to create a function in C?', 'answer': 'int myFunction() {\n    return 0;\n}'},
        {'question': 'What is the capital of Italy?', 'answer': 'Rome'},
        #fundamentals of c
        {'question': 'what is c language c tell me about c language', 
        'answer': 'C is the one of most basic programming lanuge compared to all. it is used for deleopment of os and another low lwvwl applications like compilers and ect.'},

        {'question': 'What is C?', 
        'answer': 'C is a high-level, general-purpose programming language known for its efficiency and control. It is widely used for system programming, developing operating systems, and embedded systems.'},

        {'question': 'How do you compile a C program?', 
        'answer': 'You compile a C program using a compiler like GCC. For example, you can use the command: gcc filename.c -o outputname to compile a file named filename.c.'},

        {'question': 'What is the basic structure of a C program?', 
        'answer': 'The basic structure of a C program includes the preprocessor directives, the main function, and the return statement. For example: int main() { return 0; }.'},

        {'question': 'What is a variable in C?', 
        'answer': 'A variable in C is a named storage location that can hold a value. You declare a variable by specifying its type, such as int for integers or float for floating-point numbers.'},

        {'question': 'How do you write a comment in C?', 
        'answer': 'In C, you write a single-line comment using // and a multi-line comment using /* comment */.'},

        {'question': 'What is the purpose of the #include directive?', 
        'answer': 'The #include directive is used to include header files, allowing the use of functions and constants defined in those files. For example: #include <stdio.h>.'},

        {'question': 'What is an array in C?', 
        'answer': 'An array in C is a collection of elements of the same type, stored in contiguous memory locations. For example: int numbers[5]; creates an array of 5 integers.'},

        {'question': 'How do you create a function in C?', 
        'answer': 'You create a function in C by specifying the return type, function name, and parameters. For example: int add(int a, int b) { return a + b; }.'},

        {'question': 'What is a pointer in C?', 
        'answer': 'A pointer in C is a variable that stores the memory address of another variable. You declare a pointer using the * symbol. For example: int *ptr;.'},

        {'question': 'How do you take input from a user in C?', 
        'answer': 'You can take input from a user using the scanf() function. For example: scanf("%d", &variable); to read an integer value into a variable.'},

        {'question': 'What is the use of the printf() function?', 
        'answer': 'The printf() function is used to output formatted text to the console. For example: printf("Hello, World!");.'},

        {'question': 'What is a data type in C?', 
        'answer': 'A data type in C defines the type of data a variable can hold, such as int for integers, float for floating-point numbers, and char for characters.'},

        {'question': 'How do you define a constant in C?', 
        'answer': 'You define a constant using the #define preprocessor directive or the const keyword. For example: #define PI 3.14 or const int MAX = 100;.'},

        {'question': 'What is the purpose of the main() function?', 
        'answer': 'The main() function is the entry point of a C program. Every C program must have a main function where execution begins.'},

        {'question': 'How do you declare a structure in C?', 
        'answer': 'You declare a structure using the struct keyword. For example: struct Person { char name[50]; int age; };.'},

        {'question': 'What is the difference between a for loop and a while loop in C?', 
        'answer': 'A for loop is typically used when the number of iterations is known, while a while loop is used when the number of iterations is not known beforehand.'},

        {'question': 'How do you allocate memory dynamically in C?', 
        'answer': 'You allocate memory dynamically using functions like malloc() or calloc(). For example: int arr = (int)malloc(5 * sizeof(int));.'},

        {'question': 'What does the return statement do in a function?', 
        'answer': 'The return statement exits a function and optionally returns a value to the function caller. For example: return 0; indicates successful execution.'},

        {'question': 'How do you read a string from user input in C?', 
        'answer': 'You can read a string using the fgets() function. For example: fgets(str, sizeof(str), stdin);.'},

        {'question': 'What is the use of the sizeof operator?', 
        'answer': 'The sizeof operator is used to determine the size (in bytes) of a data type or a variable. For example: int size = sizeof(int);.'},

        {'question': 'What are command-line arguments in C?', 
        'answer': 'Command-line arguments allow you to pass values to a program when it is executed. They are received in the main function as parameters: int main(int argc, char *argv[]);.'},

        
        #variables and data types 
        {'question': 'what is ment by variable in c variable', 
        'answer': 'variables in c language is used to store the any data assigned by the user'},
        {'question': 'how to declere a variable in c variable syntax  for variable in c', 
        'answer': 'to declere the variable in c syntax is "data_type variable = value; "'},
        {'question': 'what is data type in c data types list the data types in c ', 
        'answer': 'the data types are used specifiy the which dat we are using in which place. they are int, flot, char, etc'},
        {'question': 'what is the syntax for data type syntax ', 
        'answer': 'the syntax for data type is "dataype variable "'},
        {'question': 'what use of int data type ', 
        'answer': 'to declere in the integer data '},
        {'question': 'what is use of char data type ', 
        'answer': 'to decler data in the charecters '},
        {'question': 'what is use of flot data type', 
        'answer': 'to decler the data in floating points '},
        #controll flow statements 
        {'question': 'what is ment by control statements in c list control state ments in c ', 
        'answer': 'control flow statements determine the order in which the statements in a program are executed. The main control flow statements in C are: if-else, for, while, dowhile case '},
        {'question': 'what is the syntax for if else statemet syntax', 
        'answer': 'syntax for if - else is if (condition) satements; else condition statement; '},
        {'question': 'what is the syntax for for loop in c for loop syntax', 
        'answer': 'syntax for for loop is :"for (initialization; condition; increment)"'},
        {'question': 'what is the sytax for while loop syntax', 
        'answer': 'syntax for while loop is :"intialization; while (condition)"'},
        {'question': 'what is the syntax for do while loop syntax', 
        'answer': 'syntax for do while loop is:"initialization: do statements; while (condition)"'},
        #string operations in c 
        {'question': 'what is an array ', 
        'answer': 'array is a cllection of similar data types example [1,2,2,3,4]'}, 
        {'question': 'what is a string ', 
        'answer': 'sting is the collection charecters example : a man '},
        {'question': 'what is a string ', 
        'answer': 'sting is the collection charecters example : a man '},

    ],
    'html': [
        {'question': 'how to create a simple HTML page?', 'answer': '<!DOCTYPE html>\n<html>\n<head>\n    <title>Title</title>\n</head>\n<body>\n    <h1>Hello World!</h1>\n</body>\n</html>'},
        {'question': 'what is the basic structure of HTML?', 'answer': 'The basic structure is <!DOCTYPE html><html><head><title></title></head><body></body></html>'},
        {'question': 'What is the capital of Spain?', 'answer': 'Madrid'}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_with_bot():
    data = request.json
    user_message = data['message']
    active_language = data['language']  # Get the active programming language

    # Get the corresponding data array based on the active language
    data_array = data_arrays.get(active_language, [])

    # Loop through the corresponding data array and return the matching answer
    for element in data_array:
        if user_message.lower() in element['question'].lower():
            return jsonify({"response": element['answer']})

    # Default response if no match found
    return jsonify({"response": 'The data you provided is out of knolage, cloud you provide any other data'})

if __name__ == "__main__":
    app.run(debug=True)

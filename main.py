from py4j.java_gateway import JavaGateway
gateway = JavaGateway()                        # connect to the JVM
java_object = gateway.jvm.mypackage.MyClass()  # invoke constructor
other_object = java_object.doThat()
other_object.doThis(1,'abc')
gateway.jvm.java.lang.System.out.println('Hello World!') 

def sanitize_input(value, high, low):
    try:
        if value:
            value = int(value)
        else:
            print("You didn't enter a value")
            return False
    except ValueError:
        print("Please enter an integer")
        return False
    if value >= low and value <= high:
        return True
    else:
        print("Please enter an integer that is within the option range")
        return False

print("Select a technology to test with")
print("1. Java")
print("2. Python")
print("3. C++")
technology = input('Enter option: ')
while not sanitize_input(technology, 3, 1):
    technology = input('Enter option: ')


print("Select the size of graph to use for the tests")
print("1. Small (100 nodes)")
print("2. Medium (1,000 nodes)")
print("3. Large (10,000 nodes)")
graph_size = input('Enter option: ')
while not sanitize_input(graph_size, 3, 1):
    graph_size = input('Enter option: ')

print("Select an algorithm to use for the tests")
print("1. Dijkstra")
print("2. A*")
algorithm = input('Enter option: ')
while not sanitize_input(algorithm, 2, 1):
    algorithm = input('Enter option: ')

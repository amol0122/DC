import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000/")

while True:
    n = int(input("Enter an integer (or 'exit' to quit): "))
    if n == 'exit':
        break
    
    result = server.calculate_factorial(n)
    print("Factorial:", result)

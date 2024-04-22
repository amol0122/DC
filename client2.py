import Pyro4

# Locate the Pyro nameserver
ns = Pyro4.locateNS()

# Get the URI of the remote object
uri = ns.lookup("example.concatenator")
concatenator = Pyro4.Proxy(uri)

# Loop until the user decides to exit
while True:
    # Get two strings from the user
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")

    # Call the remote method to concatenate the strings
    result = concatenator.concatenate(s1, s2)
    print("Concatenated string:", result)

    # Ask the user if they want to continue or exit
    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != 'yes':
        break

def cropSuggestion():
    low_poor = ['Cassava', 'Cowpea', 'Amarath', 'Sweet Potato', 'Sesame']
    high_poor = ['Pineapple', 'Cococa', 'Oil palm', 'Rubber', 'Banana']
    poor_high = ['Tomatoes', 'Garlic', 'Peppers', 'Onions', 'Sweet Corn']
    high_high = ['Rice', 'Maize', 'Wheat', 'Beans', 'Potatoes']

    while True:
        choice = int(input('''
    Enter 1 for crop suggestion
    Enter 0 to quit
    '''))

        if choice == 1:

            rain = input("Describe generally the amount of rain in your area ")
            soil = input("Describe generally the type of soil in your area ")

            if rain == 'Good' and soil == 'Good':
                print("Suitable Crops are")
                print("***************************")
                for item in high_high:
                    print(item)

            elif rain == 'Good' and soil == 'Poor':
                print("Suitable Crops are")
                print("***************************")
                for item in high_poor:
                    print(item)

            elif rain == 'Poor' and soil == 'Good':
                print("Suitable Crops are")
                print("***************************")
                for item in poor_high:
                    print(item)

            else:
                print("Suitable Crops are")
                print("***************************")
                for item in low_poor:
                    print(item)
        else:
            break

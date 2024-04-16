import csv

with open('./reports/april01-07_2024/shopify.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
    list_reader = list(reader)

    total_shopify_sessions = 0
    all_shopify_values = list_reader[1:]

    device_percentage_shares = {'Mobile': 0, 'Desktop': 0, 'Tablet': 0, 'Other': 0}
    device_bounce_rates = {'Mobile': 0, 'Desktop': 0, 'Tablet': 0, 'Other': 0}
    device_conversion_rates = {'Mobile': 0, 'Desktop': 0, 'Tablet': 0, 'Other': 0}

    for i in range(len(all_shopify_values)):
        line_list = all_shopify_values[i][0].split(',')
        device_sessions = int(line_list[2])
        total_shopify_sessions += device_sessions

    for i in range(len(all_shopify_values)):
        line_list = all_shopify_values[i][0].split(',')
        device_sessions = int(line_list[2])
        device_category = str(line_list[0])
        device_conversion = float(line_list[-1])
        device_bounce_rate = float(line_list[-2])
        device_percentage_shares[device_category] = str(round(device_sessions*100/total_shopify_sessions, 2)) + '%'
        device_bounce_rates[device_category] = str(round(device_bounce_rate*100, 2)) + '%'
        device_conversion_rates[device_category] = str(round(device_conversion*100, 2)) + '%'

    # Data numbers
    print('Total Shopify Sessions:', total_shopify_sessions)
    print('Device Percentage Share:', device_percentage_shares)
    print('Device Bounce Rates:', device_bounce_rates)
    print('Device Conversion Rates:', device_conversion_rates)

    # for index, row in enumerate(list_reader):
    #     print(index, ':', row)
import csv

def get_shopify_numbers(week_info):
    path = './reports/' + week_info + '/shopify.csv'

    with open(path) as csv_file:
        reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
        list_reader = list(reader)
        all_shopify_values = list_reader[1:]

        total_shopify_sessions = 0
        device_percentage_shares = {}
        device_bounce_rates = {}
        device_conversion_rates = {}

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
        print('Bounce Rates:', device_bounce_rates)
        print('Conversion Rates:', device_conversion_rates)

        # for index, row in enumerate(list_reader): print(index, ':', row)

if __name__ == '__main__':
    get_shopify_numbers('april01-07_2024')
import clarity, ga, shopify

# Need to adjust the format in the primary clarity.py file to adjust for additional whitespace
def compare_clarity_numbers(previous_week_info, current_week_info):
    previous_week_sessions, previous_week_referral_sources, previous_week_pain_points = clarity.get_clarity_numbers(previous_week_info)
    current_week_sessions, current_week_referral_sources, current_week_pain_points = clarity.get_clarity_numbers(current_week_info)

    print('Previous Week Sessions:', previous_week_sessions, '\n')
    print('Current Week Sessions:', current_week_sessions, '\n')
    print('Previous Week Referral Sources:', previous_week_referral_sources, '\n')
    print('Current Week Referral Sources:', current_week_referral_sources, '\n')
    print('Previous Week Pain Points:', previous_week_pain_points, '\n')
    print('Current Week Pain Points:', current_week_pain_points)


def compare_shopify_numbers(previous_week_info, current_week_info):
    previous_week_sessions, previous_week_device_percentage_shares, previous_week_device_bounce_rate, previous_week_device_conversion_rates = shopify.get_shopify_numbers(previous_week_info)
    current_week_sessions, current_week_device_percentage_shares, current_week_device_bounce_rate, current_week_device_conversion_rates = shopify.get_shopify_numbers(current_week_info)

    print('Previous Week Shopify Sessions:', previous_week_sessions, '\n')
    print('Current Week Shopify Sessions:', current_week_sessions, '\n')
    print('Previous Week Device Share:', previous_week_device_percentage_shares, '\n')
    print('Current Week Device Share:', current_week_device_percentage_shares, '\n')
    print('Previous Week Bounce Rates:', previous_week_device_bounce_rate, '\n')
    print('Current Week Bounce Rates:', current_week_device_bounce_rate, '\n')
    print('Previous Week Conversion Rates:', previous_week_device_conversion_rates, '\n')
    print('Current Week Conversion Rates:', current_week_device_conversion_rates)


def compare_ga_numbers(previous_week_info, current_week_info):
    previous_week_ga_values = ga.get_ga_numbers(previous_week_info)
    current_week_ga_values = ga.get_ga_numbers(current_week_info)

    print('Previous Week GA:', previous_week_ga_values, '\n')
    print('Current Week GA:', current_week_ga_values)


def main(week_info):
    path_clarity = './reports/' + week_info + '/clarity.csv'
    path_ga = './reports/' + week_info + '/ga.csv'
    path_shopify = './reports/' + week_info + '/shopify.csv'

    print('\nMicrosoft Clarity')
    clarity.get_clarity_numbers(path_clarity)
    print('\nGoogle Analytics')
    ga.get_ga_numbers(path_ga)
    print('\nShopify Analytics')
    shopify.get_shopify_numbers(path_shopify)
    print()

if __name__ == '__main__':
    # main('april01-07_2024')
    previous_week_info = 'april01-07_2024'
    current_week_info = 'april08-14_2024'

    print('-----------------\nMicrosoft Clarity\n-----------------')
    compare_clarity_numbers(previous_week_info, current_week_info)
    print('\n-----------------\nShopify Reporting\n-----------------')
    compare_shopify_numbers(previous_week_info, current_week_info)
    print('\n-----------------\nGoogle Analytics\n-----------------')
    compare_ga_numbers(previous_week_info, current_week_info)
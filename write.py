import csv
import compare


def convert_to_csv(dictionary):
    try:
        csv_dictionary = '\n'.join([key +','+''.join(str(value)) for key, value in dictionary.items()])
    except AttributeError:
        csv_dictionary = dictionary

    return csv_dictionary

def write(previous_week_info, current_week_info):
    clarity_week_sessions_delta, \
        clarity_referral_sources_delta, \
            clarity_pain_points_delta = compare.compare_clarity_numbers(previous_week_info, current_week_info)
    
    shopify_week_sessions_delta, \
        shopify_week_device_sessions_delta, \
            shopify_week_device_bounce_rate_delta, \
                shopify_week_device_conversion_rate_delta = compare.compare_shopify_numbers(previous_week_info, current_week_info)
    
    ga_week_completions_delta, \
        ga_week_abandonments_delta, \
            ga_week_step_conversions_delta = compare.compare_ga_numbers(previous_week_info, current_week_info)

    with open('./output/output.csv', 'w') as csv_file:
        clarity_week_sessions_delta = convert_to_csv(clarity_week_sessions_delta)
        clarity_referral_sources_delta = convert_to_csv(clarity_referral_sources_delta)
        clarity_pain_points_delta = convert_to_csv(clarity_pain_points_delta)

        shopify_week_sessions_delta = convert_to_csv(shopify_week_sessions_delta)
        shopify_week_device_sessions_delta = convert_to_csv(shopify_week_device_sessions_delta)
        shopify_week_device_bounce_rate_delta = convert_to_csv(shopify_week_device_bounce_rate_delta)
        shopify_week_device_conversion_rate_delta = convert_to_csv(shopify_week_device_conversion_rate_delta)

        ga_week_completions_delta = convert_to_csv(ga_week_completions_delta)
        ga_week_abandonments_delta = convert_to_csv(ga_week_abandonments_delta)
        ga_week_step_conversions_delta = convert_to_csv(ga_week_step_conversions_delta)

        csv_file.write('-----------------\nMicrosoft Clarity\n-----------------' + '\n\n')
        csv_file.write('-- Weekly Sessions Delta --\n')
        csv_file.write(clarity_week_sessions_delta + '\n\n')
        csv_file.write('-- Pain Points Delta --\n')
        csv_file.write(clarity_pain_points_delta + '\n\n')
        csv_file.write('-- Referral Sources Delta --\n')
        csv_file.write(clarity_referral_sources_delta + '\n\n\n')
        csv_file.write('-----------------\nShopify Reporting\n-----------------' + '\n\n')
        csv_file.write('-- Weekly Sessions Delta --\n')
        csv_file.write(shopify_week_sessions_delta + '\n\n')
        csv_file.write('-- Device Percentage Share Delta --\n')
        csv_file.write(shopify_week_device_sessions_delta + '\n\n')
        csv_file.write('-- Device Bounce Rate Delta --\n')
        csv_file.write(shopify_week_device_bounce_rate_delta + '\n\n')
        csv_file.write('-- Device Conversion Rate Delta --\n')
        csv_file.write(shopify_week_device_conversion_rate_delta + '\n\n\n')
        csv_file.write('----------------\nGoogle Analytics\n----------------' + '\n\n')
        csv_file.write('-- Weekly Sessions Delta --\n')
        csv_file.write(ga_week_completions_delta + '\n\n')
        csv_file.write('-- Step Abandonments Delta --\n')
        csv_file.write(ga_week_abandonments_delta + '\n\n')
        csv_file.write('-- Step Conversions Delta --\n')
        csv_file.write(ga_week_step_conversions_delta)

    print('Done, CSV file located in /output/output.csv')    

if __name__ == '__main__':
    previous_week_info = 'april01-07_2024'
    current_week_info = 'april08-14_2024'

    write(previous_week_info, current_week_info)
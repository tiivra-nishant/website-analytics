import csv
import compare

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

    print(clarity_week_sessions_delta, \
          clarity_referral_sources_delta, \
            clarity_pain_points_delta)
    
    print(shopify_week_sessions_delta, \
          shopify_week_device_sessions_delta, \
            shopify_week_device_bounce_rate_delta, \
                shopify_week_device_conversion_rate_delta)
    
    print(ga_week_completions_delta, \
          ga_week_abandonments_delta, \
            ga_week_step_conversions_delta)
    

if __name__ == '__main__':
    previous_week_info = 'april01-07_2024'
    current_week_info = 'april08-14_2024'

    write(previous_week_info, current_week_info)
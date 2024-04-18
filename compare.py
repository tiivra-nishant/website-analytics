import clarity, ga, shopify

def get_delta(previous_number, current_number):
    try:
        previous_number = float(previous_number)
    except TypeError:
        previous_number = 0
    except ValueError:
        previous_number = 0

    try: 
        current_number = float(current_number)
    except TypeError:
        current_number = 0
    except ValueError:
        current_number = 0

    try:
        delta = str(round((current_number - previous_number)*100/previous_number, 2)) + '%'
    except ZeroDivisionError:
        delta = '-'

    return delta

# Need to adjust the format in the primary clarity.py file to adjust for additional whitespace
def compare_clarity_numbers(previous_week_info, current_week_info):
    previous_week_sessions, previous_week_referral_sources, previous_week_pain_points = clarity.get_clarity_numbers(previous_week_info)
    current_week_sessions, current_week_referral_sources, current_week_pain_points = clarity.get_clarity_numbers(current_week_info)

    referral_sources_delta = {}
    pain_points_delta = {}

    for key in current_week_referral_sources.keys():
        referral_sources_delta[key] = get_delta(previous_week_referral_sources[key], current_week_referral_sources[key])

    week_sessions_delta = get_delta(previous_week_sessions, current_week_sessions)

    for key in previous_week_pain_points.keys():
        try:
            previous_week_pain_point_sessions = int(previous_week_pain_points[key][0])
            current_week_pain_point_sessions = int(current_week_pain_points[key][0])
            pain_points_delta[key] = get_delta(previous_week_pain_point_sessions, current_week_pain_point_sessions)
        except ValueError:
            pain_points_delta[key] = '-'

    print('Percentage Change in Number of Sessions:', week_sessions_delta, '\n')
    print('Percentage Change in Referral Sources:', referral_sources_delta, '\n')
    print('Percentage Change in Pain Points:', pain_points_delta, '\n')

    return week_sessions_delta, referral_sources_delta, pain_points_delta

def compare_shopify_numbers(previous_week_info, current_week_info):
    previous_week_sessions, previous_week_device_percentage_shares, previous_week_device_bounce_rate, previous_week_device_conversion_rates = shopify.get_shopify_numbers(previous_week_info)
    current_week_sessions, current_week_device_percentage_shares, current_week_device_bounce_rate, current_week_device_conversion_rates = shopify.get_shopify_numbers(current_week_info)

    def get_float_percentage_value(string):
        return float(str(string).strip('%'))/100
    
    def get_device_session_value(float_percentage_value, total_sessions):
        return float_percentage_value * total_sessions
    
    week_sessions_delta = get_delta(previous_week_sessions, current_week_sessions)
    week_device_sessions_delta = {}
    week_device_bounce_rate_delta = {}
    week_device_conversion_rate_delta = {}

    for key in previous_week_device_percentage_shares.keys():
        previous_week_float_percentage_value = get_float_percentage_value(previous_week_device_percentage_shares[key])
        previous_week_device_sessions_number = get_device_session_value(previous_week_float_percentage_value, previous_week_sessions)
        current_week_float_percentage_value = get_float_percentage_value(current_week_device_percentage_shares[key])
        current_week_device_sessions_number = get_device_session_value(current_week_float_percentage_value, current_week_sessions)
        week_device_sessions_delta[key] = get_delta(previous_week_device_sessions_number, current_week_device_sessions_number)

    for key in previous_week_device_bounce_rate.keys():
        previous_week_float_percentage_value = get_float_percentage_value(previous_week_device_bounce_rate[key])
        previous_week_device_sessions_number = get_device_session_value(previous_week_float_percentage_value, previous_week_sessions)
        current_week_float_percentage_value = get_float_percentage_value(current_week_device_bounce_rate[key])
        current_week_device_sessions_number = get_device_session_value(current_week_float_percentage_value, current_week_sessions)
        week_device_bounce_rate_delta[key] = get_delta(previous_week_device_sessions_number, current_week_device_sessions_number)

    for key in previous_week_device_conversion_rates.keys():
        previous_week_float_percentage_value = get_float_percentage_value(previous_week_device_conversion_rates[key])
        previous_week_device_sessions_number = get_device_session_value(previous_week_float_percentage_value, previous_week_sessions)
        current_week_float_percentage_value = get_float_percentage_value(current_week_device_conversion_rates[key])
        current_week_device_sessions_number = get_device_session_value(current_week_float_percentage_value, current_week_sessions)
        week_device_conversion_rate_delta[key] = get_delta(previous_week_device_sessions_number, current_week_device_sessions_number)

    print('Percentage Change in Number of Sessions:', week_sessions_delta, '\n')
    print('Percentage Change in Device Share:', week_device_sessions_delta, '\n')
    print('Percentage Change in Bounce Rates:', week_device_bounce_rate_delta, '\n')
    print('Percentage Change in Conversion Rates:', week_device_conversion_rate_delta, '\n')

    return week_sessions_delta, week_device_sessions_delta, week_device_bounce_rate_delta, week_device_conversion_rate_delta


def compare_ga_numbers(previous_week_info, current_week_info):
    previous_week_ga_values = ga.get_ga_numbers(previous_week_info)
    current_week_ga_values = ga.get_ga_numbers(current_week_info)

    def get_final_conversions(dictionary):
        return int(list(dictionary.values())[-1][0])
    
    def get_number(dictionary, key, metric):
        try:
            return float(dictionary[key][metric])
        except:
            pass
    
    def get_step_conversions(dictionary, key, metric):
        final_conversions = get_final_conversions(dictionary)
        step_value = get_number(dictionary, key, metric)

        try:
            step_conversion = final_conversions*100/step_value
        except TypeError:
            step_conversion = '-'

        return step_conversion

    week_completions_delta = {}
    week_abandonments_delta = {}
    week_step_conversions_delta = {}

    for key in list(previous_week_ga_values.keys()):
        previous_week_completions = get_number(previous_week_ga_values, key, 0)
        current_week_completions = get_number(current_week_ga_values, key, 0)
        week_completions_delta[key] = get_delta(previous_week_completions, current_week_completions)
        previous_week_abandonments = get_number(previous_week_ga_values, key, 2)
        current_week_abandonments = get_number(current_week_ga_values, key, 2)
        week_abandonments_delta[key] = get_delta(previous_week_abandonments, current_week_abandonments)

        previous_week_step_conversions = get_step_conversions(previous_week_ga_values, key, 0)
        current_week_step_conversions = get_step_conversions(current_week_ga_values, key, 0)
        week_step_conversions_delta[key] = get_delta(previous_week_step_conversions, current_week_step_conversions)
    
    print('Percentage Change in Number of Completions:', week_completions_delta, '\n')
    print('Percentage Change in Number of Abandonments:', week_abandonments_delta, '\n')
    print('Percentage Change in Number of Step Conversions:', week_step_conversions_delta, '\n')

    return week_completions_delta, week_abandonments_delta, week_step_conversions_delta

if __name__ == '__main__':
    previous_week_info = 'april01-07_2024'
    current_week_info = 'april08-14_2024'

    print('-----------------\nMicrosoft Clarity\n-----------------')
    compare_clarity_numbers(previous_week_info, current_week_info)
    print('\n-----------------\nShopify Reporting\n-----------------')
    compare_shopify_numbers(previous_week_info, current_week_info)
    print('\n-----------------\nGoogle Analytics\n-----------------')
    compare_ga_numbers(previous_week_info, current_week_info)
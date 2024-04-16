import csv

def get_clarity_numbers(week_info):
    path = './reports/' + week_info + '/clarity.csv'

    with open(path) as csv_file:
        reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
        list_reader = list(reader)

        sessions_with_new_users = int(list_reader[6][-1].split(',')[-1].split('"')[1])
        sessions_with_returning_users = int(list_reader[7][-1].split(',')[-1].split('"')[1])
        total_clarity_sessions = int(sessions_with_new_users + sessions_with_returning_users)
        
        clarity_referral_sources = list_reader[222:234]
        referral_sources = {'facebook': 0, 'tiivra': 0, 'instagram': 0, 'google': 0, 'linktr.ee': 0, 'youtube': 0, 'shiprocket': 0, 'meta': 0}
        clarity_referral_names, clarity_referral_numbers = [], []
        
        for referral in range(len(clarity_referral_sources)):
            clarity_referral_name = str(clarity_referral_sources[referral]).split(',')[1]
            clarity_referral_names.append(''.join(clarity_referral_name.split('"')))
            clarity_referral_number = int(str(clarity_referral_sources[referral]).split(',')[2][1:-3])
            clarity_referral_numbers.append(clarity_referral_number)

        clarity_referral_data = dict(zip(clarity_referral_names, clarity_referral_numbers))

        for key_one in list(referral_sources.keys()):
            for key_two in list(clarity_referral_data.keys()):
                if key_one in str(key_two).lower():
                    referral_sources[key_one] += clarity_referral_data[key_two]

        clarity_pain_points = list_reader[28:32]
        clarity_pain_categories, clarity_pain_values = [], []

        for pain_point in range(len(clarity_pain_points)):
            clarity_pain_category = str(clarity_pain_points[pain_point]).split(',')[1]
            clarity_pain_categories.append(''.join(clarity_pain_category.split('"'))[:-1])
            clarity_pain_value_one = ''.join(str(clarity_pain_points[pain_point]).split(',')[-2].split('"'))
            clarity_pain_value_two = ''.join(str(clarity_pain_points[pain_point]).split(',')[-1][:-2].split('"'))
            clarity_pain_values.append([clarity_pain_value_one, clarity_pain_value_two])

        pain_points = dict(zip(clarity_pain_categories, clarity_pain_values))

        # Data numbers 
        print('Total Clarity Sessions:', total_clarity_sessions)
        print('Referral Sources:', referral_sources)
        print('Pain Points:', pain_points)
        
        # for index, row in enumerate(list_reader): print(index, ':', row)

if __name__ == '__main__':
    get_clarity_numbers('april01-07_2024')
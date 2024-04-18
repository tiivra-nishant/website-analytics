import csv

# Need to enter the indices for each week manually to prevent breaking the code
def get_clarity_report_indices(week_info):
    path = './reports/' + week_info + '/clarity_info.txt'

    with open(path, 'r+') as text_file:
        lines = text_file.readlines()
        
        first_referral_sources_index = int(lines[0].split()[-1])
        last_referral_sources_index = int(lines[1].split()[-1])
        first_pain_points_index = int(lines[2].split()[-1])
        last_pain_points_index = int(lines[3].split()[-1])
        
    return first_referral_sources_index, last_referral_sources_index, first_pain_points_index, last_pain_points_index

def get_clarity_numbers(week_info):
    path = './reports/' + week_info + '/clarity.csv'
    
    with open(path) as csv_file:
        reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
        list_reader = list(reader)

        first_referral_sources_index, last_referral_sources_index, first_pain_points_index, last_pain_points_index = get_clarity_report_indices(week_info)

        sessions_with_new_users = int(list_reader[6][-1].split(',')[-1].split('"')[1])
        sessions_with_returning_users = int(list_reader[7][-1].split(',')[-1].split('"')[1])
        total_clarity_sessions = int(sessions_with_new_users + sessions_with_returning_users)
        
        # Need to account for other referral sources as well - could as a separate key - 'Others'
        clarity_referral_sources = list_reader[first_referral_sources_index:last_referral_sources_index]
        referral_sources = {'Facebook': 0, 'Tiivra': 0, 'Instagram': 0, 'Google': 0, 'Linktr.ee': 0, 'YouTube': 0, 'Shiprocket': 0, 'Meta': 0}
        clarity_referral_names, clarity_referral_numbers = [], []

        for referral in range(len(clarity_referral_sources)):
            clarity_referral_name = str(clarity_referral_sources[referral]).split(',')[1]
            clarity_referral_names.append(''.join(clarity_referral_name.split('"')))
            clarity_referral_number = int(str(clarity_referral_sources[referral]).split(',')[2][1:-3])
            clarity_referral_numbers.append(clarity_referral_number)

        clarity_referral_data = dict(zip(clarity_referral_names, clarity_referral_numbers))

        for key_one in list(referral_sources.keys()):
            for key_two in list(clarity_referral_data.keys()):
                if key_one.lower() in str(key_two).lower():
                    referral_sources[key_one] += clarity_referral_data[key_two]

        clarity_pain_points = list_reader[first_pain_points_index:last_pain_points_index]
        clarity_pain_categories, clarity_pain_values = [], []

        for pain_point in range(len(clarity_pain_points)):
            clarity_pain_category = str(clarity_pain_points[pain_point]).split(',')[1]
            clarity_pain_categories.append(''.join(clarity_pain_category.split('"'))[:-1])
            clarity_pain_value_one = ''.join(str(clarity_pain_points[pain_point]).split(',')[-2].split('"'))
            clarity_pain_value_two = ''.join(str(clarity_pain_points[pain_point]).split(',')[-1][:-2].split('"'))
            clarity_pain_values.append([clarity_pain_value_one, clarity_pain_value_two])

        pain_points = dict(zip(clarity_pain_categories, clarity_pain_values))

        # Data numbers 
        # print('Total Clarity Sessions:', total_clarity_sessions)
        # print('Referral Sources:', referral_sources)
        # print('Pain Points:', pain_points)
        
        # for index, row in enumerate(list_reader): print(index, ':', row)

        return total_clarity_sessions, referral_sources, pain_points

if __name__ == '__main__':
    get_clarity_numbers('/week-info')
import csv

def get_ga_numbers(path):
    # path = './reports/' + week_info + '/ga.csv'

    with open(path) as csv_file:
        reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
        list_reader = list(reader)

        stat_list = list_reader[7:47:4]
        step_names = []
        step_values = []
        total_ga_values = {}

        for index in range(len(stat_list)):
            step_name_first = ' '.join(stat_list[index][:-1]).split(',')[0]
            step_name_last = stat_list[index][-1].split(',')[0]
            step_name = (step_name_first + ' ' + step_name_last).strip()
            step_names.append(step_name)
            step_value_list = stat_list[index][-1:][0].split(',')[2:]
            step_values.append(step_value_list)

        total_ga_values = dict(zip(step_names, step_values))

        # Data numbers
        print('{Step Name: [Completions, Completion Rate, Abandonments, Abandonment Rate]}')
        print('Conversion Funnel:', total_ga_values)

        # for index, row in enumerate(stat_list): print(index, ':', row)
    
if __name__ == '__main__':
    get_ga_numbers('/path/to/report')
import clarity
import ga
import shopify

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
    main('april01-07_2024')
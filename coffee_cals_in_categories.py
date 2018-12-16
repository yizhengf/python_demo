
import os
import pandas as pd
import  matplotlib.pyplot as plt



datafile_path ='./data_pd/coffee_menu.csv'

# output path

output_path = './output'

if not os.path.exists(output_path):
    os.mkdir(output_path)



def collect_data():

    data_df = pd.read_csv(datafile_path)
    return data_df



def inspect_data(data_df):
    print('data has {} rows and {} cols'.format(data_df.shape[0], data_df.shape[1] ))

    print('data preview')

    print(data_df.head())

    print('basic statistics')

    print(data_df.describe())




def analyze_data(data_df):
    beverage_category_col = data_df['Beverage_category']

    beverage_categories = beverage_category_col.unique()

    print('beverage categories:')
    print(beverage_categories)


    category_grouped = data_df.groupby('Beverage_category')

    category_count = category_grouped['Calories'].count()
    category_mean_calories = category_grouped['Calories'].mean()

    return category_count, category_mean_calories






def save_show_result(category_count,category_mean_calories):



    category_count.to_csv(os.path.join(output_path,'./category_count.csv'))

    category_mean_calories.to_csv(os.path.join(output_path, './category_mean_calories.csv'))

    category_count.plot(kind = 'bar')
    plt.title('Category count')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,'Category.png'))

    category_mean_calories.plot(kind ='bar')
    plt.title(' category mean calories')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'Category mean calories.png'))




def main():
    data_df=collect_data()

    inspect_data(data_df)
    category_count, category_mean_calories=analyze_data(data_df)
    save_show_result(category_count,category_mean_calories)


if __name__ == '__main__':
    main()
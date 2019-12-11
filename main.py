
import numpy as np
import pandas as pd
import datetime as dt
import operator
import time
import os

def most_common_day(dataframe):
    start = time.time()
    most_common_day_dict = dataframe['Day of the Week'].value_counts().to_dict()
    popular_day_of_the_week = max(most_common_day_dict.items() , key=operator.itemgetter(1))[0]
    print( 'Day :' , popular_day_of_the_week , 'Counts: ' , most_common_day_dict[popular_day_of_the_week])
    print(time.time() - start)


def most_common_hour(dataframe):
    start = time.time()
    most_common_hour_dict = dataframe['Hour'].value_counts().to_dict()
    popular_hour_of_the_day = max(most_common_hour_dict.items() , key=operator.itemgetter(1))[0]
    print( 'Hour :' , popular_hour_of_the_day , 'Counts: ' , most_common_hour_dict[popular_hour_of_the_day])
    print(time.time() - start)

def most_common_start_and_end_station(dataframe):
    start = time.time()
    most_common_start_station_of_the_month_dict = dataframe['Start station'].value_counts().to_dict()
    popular_start_station_of_the_month = max(most_common_start_station_of_the_month_dict.items() , key=operator.itemgetter(1))[0]
    print( 'Start Station :' , popular_start_station_of_the_month , 'Counts: ' , most_common_start_station_of_the_month_dict[popular_start_station_of_the_month])

    most_common_end_station_of_the_month_dict = dataframe['End station'].value_counts().to_dict()
    popular_end_station_of_the_month = max(most_common_end_station_of_the_month_dict.items() , key=operator.itemgetter(1))[0]
    print( 'End Station :' , popular_end_station_of_the_month , 'Counts: ' , most_common_end_station_of_the_month_dict[popular_end_station_of_the_month])
    print(time.time() - start)

def most_common_route(dataframe):
    start = time.time()
    routing_df_temp = dataframe.groupby(['Start station' , 'End station']).size().reset_index(name='Times')
    routing_temp_dict = routing_df_temp['Times'].sort_values().to_dict()
    index_of_popular_route = max(routing_temp_dict.items() , key=operator.itemgetter(1))[0]
    print( 'Most popular route: ' ,routing_df_temp.loc[index_of_popular_route])
    print(time.time() - start)

def trip_duration(dataframe):
    start = time.time()
    print('total: ' , sum(dataframe['Duration']))
    print('mean: ' , dataframe['Duration'].mean())
    print(time.time() - start)

def user_type(dataframe):
    start = time.time()
    print(dataframe['Member type'].value_counts())
    print(time.time() - start)


def gender(dataframe ,city_name):
    start = time.time()
    if city_name == 'washington':
        return
    print(dataframe['Gender'].value_counts())
    print(time.time() - start)


def birthyear(dataframe , city_name):
    start = time.time()
    if city_name == 'washington':
        return
    dict_brithyear_frequent = dataframe['Birthyear'].value_counts().to_dict()
    del dict_brithyear_frequent[0]
    frequented_birth_year = int(max(dict_brithyear_frequent.items() , key=operator.itemgetter(1))[0])
    min_birthyaer = int(min(dict_brithyear_frequent.keys()))
    max_birthyaer = int(max(dict_brithyear_frequent.keys()))
    print('most common birth year: ', frequented_birth_year , 'min birth year: ' , min_birthyaer , 'max birth year: ' , max_birthyaer)
    print(time.time() - start)
def main():
    user_input = 'Y'

    while user_input == 'Y':
        city_name = input('Welcome plz enter your city name: ')
        if os.path.exists(city_name + '.csv'):
            name_of_city = pd.read_csv(city_name + '.csv')
        else:
            print('this city dataset dosent exist!')
            continue

        how_filtering = input('plase enter your filter type : both , month , day , none :')

        if how_filtering == 'month':

            filtering_month = input('which month : ')
            #month filtering
            by_month_filter_df = name_of_city[name_of_city['Month'] == filtering_month]
                #most common day in the month
            most_common_day(by_month_filter_df)
                #most common hour in the month
            most_common_hour(by_month_filter_df)
                #most common start and end station in the month
            most_common_start_and_end_station(by_month_filter_df)
                #most common route 
            most_common_route(by_month_filter_df)
                #trip duration
            trip_duration(by_month_filter_df)
                #user type
            user_type(by_month_filter_df)
                #gender
            gender(by_month_filter_df , city_name)
                #birthyear
            birthyear(by_month_filter_df ,city_name)



        elif how_filtering == 'day':

            filtering_day = int(input('which day : '))
            #day filtering
            by_day_filter_df = name_of_city[name_of_city['Day'] == filtering_day]
            #most common hour of the day
            most_common_hour(by_day_filter_df)
            #most common start and end station in the day
            most_common_start_and_end_station(by_day_filter_df)
            #most common route 
            most_common_route(by_day_filter_df)
            #trip duration
            trip_duration(by_day_filter_df)
            #user type
            user_type(by_day_filter_df)
            #gender
            gender(by_day_filter_df,city_name)
            #birthyear
            birthyear(by_day_filter_df , city_name)


        elif how_filtering == 'both':
            filtering_month = input('which month : ')
            filtering_day = int(input('which day : '))
            #month and day filtering 
            by_month_and_day_filter_df = name_of_city[(name_of_city['Month'] == filtering_month) & (name_of_city['Day']==filtering_day)]
            #most common hour of the day
            most_common_hour(by_month_and_day_filter_df)
            #most common start and end station in the day
            most_common_start_and_end_station(by_month_and_day_filter_df)
            #most common route 
            most_common_route(by_month_and_day_filter_df)
            #trip duration
            trip_duration(by_month_and_day_filter_df)
            #user type
            user_type(by_month_and_day_filter_df)
            #gender
            gender(by_month_and_day_filter_df,city_name)
            #birthyear
            birthyear(by_month_and_day_filter_df , city_name)


        elif how_filtering == 'none':

            most_common_day(name_of_city)
            #most common hour of the day
            most_common_hour(name_of_city)
            #most common start and end station in the day
            most_common_start_and_end_station(name_of_city)
            #most common route 
            most_common_route(name_of_city)
            #trip duration
            trip_duration(name_of_city)
            #user type
            user_type(name_of_city)
            #gender
            gender(name_of_city,city_name)
            #birthyear
            birthyear(name_of_city, city_name)
            
        user_input = input('do you want to continue Y/N: ')

if __name__ == '__main__':
    main()
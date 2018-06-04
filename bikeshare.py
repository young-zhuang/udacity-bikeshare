import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input("Please enter in one of these cities as your inputs: Chicago, New York City, or Washington -->")
    while True:
        city.strip() == 'Chicago' 
        city.strip() == 'New York City'
        city.strip() == 'Washington'
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please enter a month -->")
    while True:
        month.strip() == 'All'
        month.strip() == 'January'
        month.strip() == 'February'
        month.strip() == 'March'
        month.strip() == 'April'
        month.strip() == 'May'
        month.strip() == 'June'
        month.strip() == 'July'
        month.strip() == 'August'
        month.strip() == 'September'
        month.strip() == 'October'
        month.strip() == 'November'
        month.strip() == 'December'
        break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter a day of the week -->")
    while True:
        day.strip() == 'All'
        day.strip() == 'Monday'
        day.strip() == 'Tuesday'
        day.strip() == 'Wednesday'
        day.strip() == 'Thursday'
        day.strip() == 'Friday'
        day.strip() == 'Saturday'
        day.strip() == 'Sunday'
        break

        print('-'*40)
        return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
  
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if city == 'Chicago':
        df = pd.read_csv('chicago.csv')
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        popular_month = df['Start Time'].mode()[0]
        print(popular_month)
    elif city == 'New York City':
        df = pd.read_csv('new_york_city.csv')
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        popular_month = df['Start Time'].mode()[0]
        print(popular_month)
    elif city == 'Washington':
        df = pd.read_csv('washington.csv')
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        popular_month = df['Start Time'].mode()[0]
        print(popular_month)

    # TO DO: display the most common day of week
    if city == 'Chicago':
        df = pd.read_csv('chicago.csv')
        df['Start Time'] = pd.dt.weekday_name(df['Start Time'])
        popular_day_of_week = df['Start Time'].mode()[0]
        print(popular_day_of_week)
    elif city == 'New York City':
        df = pd.read_csv('new_york_city.csv')
        df['Start Time'] = pd.dt.weekday_name(df['Start Time'])
        popular_day_of_week = df['Start Time'].mode()[0]
        print(popular_day_of_week)
    elif city == 'Washington':
        df = pd.read_csv('washington.csv')
        df['Start Time'] = pd.dt.weekday_name(df['Start Time'])
        popular_day_of_week = df['Start Time'].mode()[0]
        print(popular_day_of_week)

    # TO DO: display the most common start hour
    if city == 'Chicago':
        df = pd.read_csv('chicago.csv')
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        popular_hour = df['Start Time'].mode()[0]
        print(popular_hour)
    elif city == 'New York City':
        df = pd.read_csv('new_york_city.csv')
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        popular_hour = df['Start Time'].mode()[0]
        print(popular_hour)
    elif city == 'Washington':
        df = pd.read_csv('washington.csv')
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        popular_hour = df['Start Time'].mode()[0]
        print(popular_hour)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()


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
    city = input("Please enter in one of these cities as your inputs: chicago, new york city, or washington -->")
    while city.lower() not in ['chicago','new york city','washington']:
        if city.lower() == 'chicago':
            return 'chicago.csv'
        elif city.lower() == 'new york city':
            return 'new_york_city.csv'
        elif city.lower() == 'washington':
            return 'washington.csv'
        else:
            print('Please try again! Input a city that is either chicago, new york city, or washington.')
            break    

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please enter a month from january through june or all for all months-->")
    if month.lower() == 'january':
        return '1'
    elif month.lower() == 'february':
        return '2'
    elif month.lower() == 'march':
        return '3'
    elif month.lower() == 'april':
        return '4'
    elif month.lower() == 'may':
        return '5'
    elif month.lower() == 'june':
        return '6'
    else:
        print('Please enter in a correct month.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter a day of the week -->")
    if day.lower() == 'monday':
        return 'monday'
    elif day.lower() == 'tuesday':
        return 'tuesday'
    elif day.lower() == 'wednesday':
        return 'wednesday'
    elif day.lower() == 'thursday':
        return 'thursday'
    elif day.lower() == 'friday':
        return 'friday'
    elif day.lower() == 'saturday':
        return 'saturday'
    elif day.lower() == 'sunday':
        return 'sunday'
    else:
        print('Please enter in a correct day of the week.')

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour, month, and day_of_week from the Start Time column to create new column
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is: ",most_common_month)
    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is: ",most_common_day_of_week)
    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common hour is: ",most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is: ",most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most common end station is: ",most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_combo = df['Start Station', 'End Station'].mode().loc[0]
    print("The most common combination of start station and end station trip is:  {}, {}".format(most_common_combo[0],most_common_combo[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("The total travel time is: ",total_travel)
    
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("The mean travel time is: ",mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print("The count of user types is: ",user_types_counts)

    # TO DO: Display counts of gender
    male_count = df.query('gender == "Male"').gender.count()
    female_count = df.query('gender == "Female"').gender.count()
    print("There are {} male users and {} female users.".format(male_count, female_count))

    # TO DO: Display earliest, most recent, and most common year of birth
    
    #Earliest birth year
    earliest_birth_year = df['Birth Year'].min()
    print("The earlist birth year is: ", earliest_birth_year)

    #Most recent birth year                         
    recent_birth_year = df['Birth Year'].max()
    print("The most recent birth year is: ", recent_birth_year)
               
    #Common birth year
    most_common_birth_year = df['Birth Year'].mode()[0]
    print("The most common birth year is: ",most_common_birth_year)                           
                             
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

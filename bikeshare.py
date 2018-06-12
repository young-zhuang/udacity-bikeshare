import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

CITIES = ['Chicago', 'New York City', 'Washington']

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June']

DAY = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

Chicago = 'chicago.csv'
New_York_City = 'new_york_city.csv'
Washington = 'washington.csv'

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please enter in one of these cities as your inputs: chicago, new york city, or washington -->").title()
    while city not in CITIES:
        if city == 'Chicago':
            return 'chicago.csv'
        elif city == 'New York City':
            return 'new_york_city.csv'
        elif city == 'Washington':
            return 'washington.csv'
        else:
            print("\n'Please try again! Input a city that is either chicago, new york city, or washington.'")
            return get_filters()
            break
    # get user input for month (all, january, february, ... , june)
    month = input("Please enter a month from january through june or all for all months-->").title()
    while month not in MONTHS:
        if month == 'January':
            return '1'
        elif month == 'February':
            return '2'
        elif month == 'March':
            return '3'
        elif month == 'April':
            return '4'
        elif month == 'May':
            return '5'
        elif month == 'June':
            return '6'
        else:
            print('Please enter in a correct month.')
            return get_filters()
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter a day of the week -->").title()
    while day not in DAY:
        if day.lower() == 'Monday':
            return 'Monday'
        elif day.lower() == 'Tuesday':
            return 'Tuesday'
        elif day.lower() == 'Wednesday':
            return 'Wednesday'
        elif day.lower() == 'Thursday':
            return 'Thursday'
        elif day.lower() == 'Friday':
            return 'Friday'
        elif day.lower() == 'Saturday':
            return 'Saturday'
        elif day.lower() == 'Sunday':
            return 'Sunday'
        else:
            print('Please enter in a correct day of the week.')
            return get_filters()
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
    #To create new column to find the most common combination
    df['Trip Combo'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    most_common_combo = df['Trip Combo'].mode().to_string(index = False)
    print('The most popular combination of start and end trip is {}.'.format(most_common_combo))

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
    print("The count of user types is: ",user_types_count)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("This is the count of genders: ", gender_counts)

    #Earliest birth year
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print("The earlist birth year is: ", earliest_birth_year)

    #Most recent birth year
    if 'Birth Year' in df.columns:
        recent_birth_year = df['Birth Year'].max()
        print("The most recent birth year is: ", recent_birth_year)            
    #Common birth year
    if 'Birth Year' in df.columns:
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("The most common birth year is: ",most_common_birth_year)    
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    line = 0
    display = input('Please type yes or no to see more data -->')
    display = display.lower()
    if display == 'yes':
        print(df.iloc[line:line+5])
        line += 5
        return display_data(df)
    if display == 'no':
        return
    else:
        print('Would you like to see more data?')
        return display_data(df)
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

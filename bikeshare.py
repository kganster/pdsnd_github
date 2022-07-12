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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington? ').lower()
        if city not in CITY_DATA:
                print('Invalid city! Please enter the full name of one of the cities listed.') # specify that user needs to enter one from list
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Would you like to see data for the month of January, February, March, April, May or June? To see data for all months, type "all" ').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month !='all' and month not in months:
            print('Invalid month! Please enter one of the full month names listed or "all" ') # specify that user needs to enter one from list
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please enter a day of the week. To see data for all days of the week, type "all" ').lower()
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        if day != 'all' and day not in days:
            print('Please enter the full day name or "all" ') # specify that user needs to enter one from list
        else:
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

    # extract month and day of week from Start Time to create new columns
    df['year'] = df['Start Time'].dt.year
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    com_month = df['month'].mode()[0]
    print('Most Common Month: ', com_month)

    # display the most common day of week
    com_day = df['month'].mode()[0]
    print('Most Common Day: ', com_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour # extract hour from the Start Time column to create an hour column
    com_hour = df['hour'].mode()[0] # find the most popular hour
    print('Most Common Start Hour: ', com_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    com_start = df['Start Station'].mode()[0]
    print('Most Common Start Station: ', com_start)

    # display most commonly used end station
    com_end = df['Start Station'].mode()[0]
    print('Most Common End Station: ', com_end)

    # display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station'] + ' and ' + df['End Station'] # add spaces/article between two stations to improve readability
    com_combo = df['combo'].mode()[0]
    print('Most Common Start and End Station Combination: ', com_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    ttl_time = df['Trip Duration'].sum()
    print('Total Travel Time: ', ttl_time, ' seconds or ', ttl_time/60, ' minutes or', ttl_time/3600, ' hours') # display results in seconds, minutes, and hours

    # display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Average Travel Time: ', avg_time, ' seconds or ', avg_time/60, ' minutes or', avg_time/3600, ' hours') # display results in seconds, minutes, and hours

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_type(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('Count of User Type:\n' , user_type)

    # Display counts of gender
def gender_type(df):

    start_time = time.time()

    try:
        gender_cnt = df['Gender'].value_counts()
        print('Count of Gender:' , gender_cnt)
    except KeyError:
        print('NOTE: No gender data recorded for Washington!') # clarify that no data exists for Washington

    # Display earliest, most recent, and most common year of birth
def birth_yr(df):

    start_time = time.time()

    try:
        early_yr = int(df['Birth Year'].min())
        print('Earliest Birth Year:' , early_yr)

        recent_yr = int(df['Birth Year'].max())
        print('Most Recent Birth Year:' , recent_yr)

        most_yr = int(df['Birth Year'].mode()[0])
        print('Most Common Birth Year:' , most_yr)
    except KeyError:
        print('NOTE: No birth year data recorded for Washington!') # clarify that no data exists for Washington

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df): # define new function to prompt user request for raw data

while True:
    display_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
    if display_data.lower() != 'yes':
        break
    print(tabulate(df_default.iloc[np.arange(0+i,5+i)], headers ="keys"))
    i+=5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_type(df)
        gender_type(df)
        birth_yr(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

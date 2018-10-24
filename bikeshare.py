import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input("Enter the name of the city you want the data to be analyzed for,the city names are: chicago,new york city,washington: ").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid input,please try again. The valid cities are: chicago or new york or washington")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        month = input("Enter the name of the month:january,february,march,"
            "april,may,june to filter by, or all to apply no filter: ").lower()
        if month in ["january", "february", "march", "april", "may", "june", "all"]:
            break
        else:
            print("Invalid Month entered,please try again. The valid months are: january or february or march or april or may or june or all(for no month filter)")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input("Enter the name of the day: monday,tuesday,wednesday,thursday,"
            "friday,saturday,sunday to filter by or all to apply no filter: ").lower()
        if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            break
        else:
            print("Invalid Day entered,please try again.Valid values are: monday or tuesday or wednesday or thursday or friday or saturday or sunday or all(for no day filter)")
    # Print hyphen (-) 40 times for more clean user screen
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

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(arg = df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    # use the index of the months list to get the corresponding int
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(arg = df['Start Time'])

    # Create new columns for month, day of the week and hour
    month = df['Start Time'].dt.month
    day_of_week = df['Start Time'].dt.weekday_name
    hour = df['Start Time'].dt.hour

    # TO DO: display the most common month
    most_common_month = month.mode()[0]
    print('Most common month: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = day_of_week.mode()[0]
    print('Most common day of week: ', most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour = hour.mode()[0]
    print('Most frequent start hour: ', most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    # Print hyphen (-) 40 times for more clean user screen
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print('Most commonly used start station:',most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print('Most commonly used end station:',most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination = df['Start Station'] + "*" + df['End Station']
    common_station = combination.value_counts().idxmax()
    print('Most frequent used combinations is:{} to {}'.format(common_station.split('*')[0], common_station.split('*')[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    # Print hyphen (-) 40 times for more clean user screen
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # Convert seconds to readable time format
    def secs_to_readable_time(seconds):
        m, s = divmod(seconds,60)
        h, m = divmod(m,60)
        d, h = divmod(h,24)
        y, d = divmod(d,365)
        print('Years: {}, Days: {}, Hours: {}, Mins: {}, Secs: {}'.format(y,d,h,m,s))

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:\n')
    secs_to_readable_time(total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time: {} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    # Print hyphen (-) 40 times for more clean user screen
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("\nEarliest year of birth: " + str(earliest_birth_year))
        print("\nMost recent year of birth: " + str(most_recent_birth_year))
        print("\nMost common year of birth: " + str(common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    # Print hyphen (-) 40 times for more clean user screen
    print('-'*40)

def raw_data(df):
    user_input = input('Do you want to see raw data? Enter any key(s) to continue or no to exit.\n')
    row_number = 0
# While loop for returning only 5 rows at a time
    while True :
        if user_input.lower() != 'no':
            print(df.iloc[row_number : row_number + 5])
            row_number += 5
            user_input = input('\nDo you want to see more raw data? Enter any key(s) to continue or no to exit.\n')
        else:
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes to continue or any key(s) to exit.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

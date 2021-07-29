import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

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
       city = input('Which city do you want to explore Chicago, New York or Washington? \n> ').lower()
       if city in CITIES:
           break

    # get user input for month (all, january, february, ... , june)
    while True:
       month = input('Which month do you want to explore all, january, february, march, april, may, june? \n> ').lower()
       if month in MONTHS:
           break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
       day = input('Which week day do you want to consider sunday, monday, tuesday, wednesday, \
       thursday, friday, saturday?     \n').lower()
       if day in DAYS:
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

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

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
    """Displays statistics on the most popular times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most popular month
    popular_month = df['month'].mode()[0]
    print("the most common month:", popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    print("the most common day of week:", popular_day)
    # TO DO: display the most common start hour
    popular_hour = df['hour'].value_counts().idxmax()
    print("the most common start hour:", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print("the most commonly used start station :", start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("the most commonly used end station :", end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frq_comb_start_stat_end_stat = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(frq_comb_start_stat_end_stat[0], frq_comb_start_stat_end_stat[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time :", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("mean travel time :", mean_travel_time )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types:\n")
    user_counts_types = df['User Type'].value_counts()

    for index, user_count_type in enumerate(user_counts_types):
        print("  {}: {}".format(user_counts_types.index[index], user_count_type))

    print()

    # TO DO: Display counts of gender
    print("counts of gender:\n")
    gender_counts= df['Gender'].value_counts()

    for index, gender_count in enumerate(gender_counts):
        print("  {}: {}".format(gender_counts.index[index], gender_count))

    print()

    if 'Gender' in df.columns:
        user_stats_gender(df)

    if 'Birth Year' in df.columns:
        user_stats_birth(df)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats_birth(df):
    """Displays statistics of analysis based on the birth years of bikeshare users."""

    # TO DO: Display earliest, most recent, and most common year of birth
    birth_earliest = df['Birth Year'].min()
    print('earliest year of birth:', birth_earliest )
    recent_birth = df['Birth Year'].max()
    print('most recent year of birth:',recent_birth )
    common_year_birth = df['Birth Year'].value_counts().idxmax()
    print('most common year of birth:', common_year_birth)

def user_stats_gender(df):
    """Displays statistics of analysis based on the gender of bikeshare users."""

    # Display counts of gender
    print("Counts of gender:\n")
    gender_counts = df['Gender'].value_counts()
    # iteratively print out the total numbers of genders
    for index,gender_count   in enumerate(gender_counts):
        print("  {}: {}".format(gender_counts.index[index], gender_count))

    print()

def display_data(df):
    """Displays raw bikeshare data."""
    start_loc = 0
    display_data = input('\nWould you like to see more data? Enter yes or no.\n')
    while display_data.lower() == 'yes':
        df_slice = df.iloc[start_loc: start_loc+5]
        print(df_slice)
        start_loc += 5
        display_data = input('\nWould you like to see more data? Enter yes or   no.\n')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        table_stats(df, city)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

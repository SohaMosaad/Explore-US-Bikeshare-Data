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
    city = ''
    while city.lower() not in ['chicago','new york city','washington']:
        city = input('Please enter name of the City from that list (chicago or new york city or washington) : ')
        if city.lower() == 'chicago':
            city = 'chicago'
            break
        elif city.lower() == 'new york city':
            city = 'new york city'
            break
        elif city.lower() == 'washington':
            city = 'washington'
            break
        else:
            print('the City Name info. are not available')

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = ''
    while month.lower() not in months:
        month = input('Please enter the month in lower-case characters (all, january, february, ... , june) : ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day.lower() not in days:
        day = input('Please enter the day of week lower-case characters (all, monday, tuesday, ... sunday): ')

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
    if city == 'chicago':
        df = pd.read_csv('chicago.csv')
    elif city == 'new york city':
        df = pd.read_csv('new_york_city.csv')
    elif city == 'washington':
        df = pd.read_csv('washington.csv')
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    # filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    index = int(df['month'].mode()[0])
    most_month = months[index -1]
    #most_month = df['month'].mode()[0]  
    print('The most common month : {}'.format(most_month))
    
    # TO DO: display the most common day of week
    most_day = df['day_of_week'].mode()[0]
    print('The most common day of week : {}'.format(most_day))

    # TO DO: display the most common start hour
    most_hour = df['Start Time'].dt.hour.mode()[0] 
    print('The most common start hour : {}'.format(most_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station : {}'.format(most_start_station))

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station : {}'.format(most_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'].str.cat(df['End Station'], ' , ')
    most_combination = df['trip'].mode()[0] 
    print('The most frequent combination of start station and end station trip : {}'.format(most_combination))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    df['Travel Time'] = df['End Time'] - df['Start Time']
    total_time = np.sum(df['Travel Time'])
    print('The total travel time : {}'.format(total_time))

    # TO DO: display mean travel time
    mean_time = np.mean(df['Travel Time'])
    print('The mean travel time : {}'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('counts of user types : {}'.format(user_type))

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('counts of gender : {}'.format(gender_count))
    except:
        print('No value for Gender in these time period')
    
        
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        early_year_birth = int(df['Birth Year'].max())
        recent_year_birth = int(df['Birth Year'].min())
        most_year_birth = int(df['Birth Year'].mode()[0])
        print('earliest : {}, most recent : {}, and most common year of birth : {}'.format(early_year_birth, recent_year_birth, most_year_birth))
    except:
        print('No value for Birth Year in these time period')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Asking to display first 5 rows of data, if the input is 'yes' display them and continue asking to show more
def display_data(df):
    view_data = input('would you like to see the first 5 rows of data? Enter yes or no : ')
    start_row = 0
    while (view_data.lower() == 'yes'):
        print(df.iloc[start_row:start_row+5])
        start_row += 5
        view_data = input('would you like to see the next 5 rows of data? : ')

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

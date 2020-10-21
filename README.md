# Explore-US-Bikeshare-Data
Udacity Project for Data Professional Track using Python 3, NumPy, and pandas installed using Anaconda - to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. 

# Statistics Computed
# 1 Popular times of travel (i.e., occurs most often in the start time)
- most common month
- most common day of week
- most common hour of day

# 2 Popular stations and trip
- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

# 3 Trip duration
- total travel time
- average travel time

# 4 User info
- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

# The Files
- chicago.csv
- new_york_city.csv
- washington.csv

# Terminal
-  python bikeshare.py
- Hello! Let's explore some US bikeshare data!
- Please enter name of the City from that list (chicago or new york city or washington) : new york city
- Please enter the month in lower-case characters (all, january, february, ... , june) : may
- Please enter the day of week lower-case characters (all, monday, tuesday, ... sunday): thursday
----------------------------------------

- Calculating The Most Frequent Times of Travel...

- The most common month : may
- The most common day of week : Thursday
- The most common start hour : 17

This took 0.007253885269165039 seconds.
----------------------------------------

- Calculating The Most Popular Stations and Trip...

- The most commonly used start station : Pershing Square North
- The most commonly used end station : Pershing Square North
- The most frequent combination of start station and end station trip : Central Park S & 6 Ave , Central Park S & 6 Ave

This took 0.037880659103393555 seconds.
----------------------------------------

- Calculating Trip Duration...

- The total travel time : 84 days 01:40:03
- The mean travel time : 0 days 00:14:01.279013

This took 0.011655330657958984 seconds.
----------------------------------------

- Calculating User Stats...

- counts of user types : Subscriber    7869
- Customer       765
- Name: User Type, dtype: int64
- counts of gender : Male      5971
- Female    1945
- Name: Gender, dtype: int64
- earliest : 2001, most recent : 1886, and most common year of birth : 1990

This took 0.015809297561645508 seconds.
----------------------------------------
would you like to see the first 5 rows of data? Enter yes or no : yes
     Unnamed: 0          Start Time     ...                                                    trip  Travel Time
1       4096714 2017-05-11 15:30:11     ...               Lexington Ave & E 63 St , 1 Ave & E 78 St     00:11:32
66      4079228 2017-05-11 09:03:18     ...             W 84 St & Broadway , Columbus Ave & W 72 St     00:05:38
128     3789757 2017-05-04 20:01:39     ...                  E 51 St & 1 Ave , Maiden Ln & Pearl St     00:35:01
157     3744138 2017-05-04 07:58:56     ...       President St & Henry St , Schermerhorn St & Co...     00:10:52
180     3777400 2017-05-04 17:31:59     ...       Kent Ave & N 7 St , Metropolitan Ave & Bedford...     00:03:35

[5 rows x 13 columns]
- would you like to see the next 5 rows of data? : no

- Would you like to restart? Enter yes or no.

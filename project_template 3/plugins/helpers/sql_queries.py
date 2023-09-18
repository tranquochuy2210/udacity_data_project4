class SqlQueries:
    songplay_table_insert = ("""
        insert into songplays(
        start_time,
        user_id,
        level,
        song_id,
        artist_id,
        session_id,
        location,
        user_agent                                                                              
        )
        SELECT
                events.start_time, 
                events.user_id, 
                events.level, 
                songs.song_id, 
                songs.artist_id, 
                events.session_id, 
                events.location, 
                events.user_agent
                FROM (SELECT TIMESTAMP 'epoch' + ts/1000 * interval '1 second' AS start_time, *
            FROM staging_events
            WHERE page='NextSong') events
            LEFT JOIN staging_songs songs
            ON events.song = songs.title
                AND events.artist = songs.artist_name
                AND events.length = songs.duration
    """)

    user_table_insert = ("""
        insert into users (user_id, first_name, last_name, gender)
        SELECT distinct user_id, first_name, last_name, gender
        FROM staging_events
        WHERE page='NextSong'
    """)

    song_table_insert = ("""
        insert into songs (song_id, title, artist_id, year, duration)
        SELECT distinct song_id, title, artist_id, year, duration
        FROM staging_songs
    """)

    artist_table_insert = ("""
        insert into artists (artist_id, name, location, latitude, longitude)
        SELECT distinct artist_id, artist_name, artist_location, artist_latitude, artist_longitude
        FROM staging_songs
    """)

    time_table_insert = ("""
        insert into time (start_time,hour, day, week, month, year, weekday)
        SELECT start_time, extract(hour from start_time), extract(day from start_time), extract(week from start_time), 
               extract(month from start_time), extract(year from start_time), extract(dayofweek from start_time)
        FROM songplays
    """)
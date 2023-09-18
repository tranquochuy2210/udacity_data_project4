CREATE TABLE staging_events (
    artist VARCHAR(512),
    auth VARCHAR(512),
    first_name VARCHAR(512),
    gender VARCHAR(1),
    item_in_session INTEGER,
    last_name VARCHAR(512),
    length DECIMAL,
    level VARCHAR(512),
    location VARCHAR(512),
    method VARCHAR(16),
    page VARCHAR(512),
    registration bigint,                       
    session_id INTEGER ,
    song VARCHAR(512),
    status INTEGER,
    ts double precision,
    user_agent VARCHAR(512),
    user_id INTEGER                                                                       
)

CREATE TABLE staging_songs (
    num_songs INTEGER,
    artist_id VARCHAR(18) NOT NULL,
    artist_latitude DECIMAL,
    artist_longitude DECIMAL,
    artist_location VARCHAR(512),
    artist_name VARCHAR(512),
    song_id VARCHAR(18),
    title VARCHAR(512),
    duration DECIMAL,
    year INTEGER                                                                                                       
)
CREATE TABLE songplays (
    songplay_id INT IDENTITY(1,1) PRIMARY KEY,
    start_time TIMESTAMP  ,
    user_id INTEGER,
    level VARCHAR(512),
    song_id VARCHAR(18),
    artist_id VARCHAR(18),
    session_id VARCHAR(18),
    location VARCHAR(512),
    user_agent VARCHAR(512)
)

CREATE TABLE users (
    user_id INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR(512),
    last_name VARCHAR(512),
    gender VARCHAR(1)
)
CREATE TABLE songs (
    song_id VARCHAR(18) NOT NULL PRIMARY KEY,
    title VARCHAR(512) NOT NULL,
    artist_id  VARCHAR(18) NOT NULL,
    year INTEGER ,
    duration DECIMAL            
)
CREATE TABLE artists (
    artist_id VARCHAR(18) NOT NULL PRIMARY KEY,
    name VARCHAR(512) NOT NULL,
    location VARCHAR(512),
    latitude DECIMAL,
    longitude DECIMAL
)
CREATE TABLE time(
    start_time TIMESTAMP,
    hour INTEGER,
    day  VARCHAR(19),
    week INTEGER,
    month VARCHAR(10),
    year INTEGER,
    weekday boolean 
)
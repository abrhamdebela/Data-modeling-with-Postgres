 --SELECT top 1  TIMESTAMP 'epoch' + (se.ts/60000 ) * INTERVAL '1 minutes'   AS start_time,se.ts, (se.ts/1000 ) * INTERVAL '1 minutes',TIMESTAMP 'epoch' --,*
   -- FROM staging_events AS se
   -- JOIN staging_songs AS ss
     --   ON (se.artist = ss.artist_name)
   -- WHERE se.page = 'NextSong';

   
   
    /**/
   
                                      
    SELECT  DISTINCT TIMESTAMP 'epoch' + (se.ts/1000 )   * INTERVAL '1 second'   AS start_time,
            se.userId                   AS user_id,
            se.level                    AS level,
            ss.song_id                  AS song_id,
            ss.artist_id                AS artist_id,
            se.sessionId                AS session_id,
            se.location                 AS location,
            se.userAgent                AS user_agent
    FROM staging_events AS se
    JOIN staging_songs AS ss
        ON (se.artist = ss.artist_name)
    WHERE se.page = 'NextSong'
    ORDER BY se.userId ;
    
    / ** /
    
      WITH CTE 
  AS 
  ( SELECT   TIMESTAMP 'epoch' + (se.ts/1000 )  * INTERVAL '1 second'   AS start_time,
            se.userId                   AS user_id,
            se.level                    AS level,
            ss.song_id                  AS song_id,
            ss.artist_id                AS artist_id,
            se.sessionId                AS session_id,
            se.location                 AS location,
            se.userAgent                AS user_agent, ROW_NUMBER () OVER (PARTITION BY  user_id  ) AS user_id_row_num
    FROM staging_events AS se
    JOIN staging_songs AS ss
        ON (se.artist = ss.artist_name)
    WHERE se.page = 'NextSong'
   ) 
   SELECT * FROM CTE 
   where user_id_row_num = 1;
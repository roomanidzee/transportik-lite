CREATE KEYSPACE default WITH REPLICATION = {
      'class' : 'SimpleStrategy', 'replication_factor' : 1
    };

CREATE TABLE default.transport_analysis(
    record_time TIMESTAMP,
    transport_id INT,
    is_busy BOOLEAN,
    is_repairing BOOLEAN,
    trip_id INT,
    distance INT,
    cost INT,
    PRIMARY KEY ( (record_time), transport_id, trip_id )
) WITH DEFAULT_TIME_TO_LIVE = 86400;

CREATE INDEX transport_index ON transport_analysis(transport_id);
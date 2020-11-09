DROP DATABASE IF EXISTS sites;
CREATE DATABASE sites;
\connect sites;

CREATE TABLE IF NOT EXISTS locations (
    street_address varchar(40),
    city varchar(20),
    postcode int,
    state_abb varchar(2)
);

INSERT INTO locations VALUES 
    ('51 University Avenue #300', 'Seattle', 98101, 'WA'),
    ('149 New Montgomery Street 2nd Floor', 'San Francisco', 94105, 'CA'),
    ('1033 West Van Buren Street 3rd Floor', 'Chicago', 60607, 'IL'),
    ('27 East 28th Street', 'New York', 10016, 'NY')
;

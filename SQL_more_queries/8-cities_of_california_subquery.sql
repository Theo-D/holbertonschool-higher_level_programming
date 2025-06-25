-- Lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT id from states WHERE name="California" AS STATE;
SELECT id, name from cities WHERE state_id=STATE ORDER BY id ASC;

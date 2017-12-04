CREATE DATABASE dailyredditplaylist;
CREATE USER dailyredditplaylistuser WITH PASSWORD 'password';
ALTER ROLE dailyredditplaylistuser SET client_encoding TO 'utf8';
ALTER ROLE dailyredditplaylistuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE dailyredditplaylistuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE dailyredditplaylist TO dailyredditplaylistuser;
ALTER USER dailyredditplaylistuser CREATEDB;
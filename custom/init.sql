-- creates the user, database and pg_stat_statements
CREATE USER profiler WITH PASSWORD 'Pass0123';
CREATE DATABASE profilerdb OWNER profiler;
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
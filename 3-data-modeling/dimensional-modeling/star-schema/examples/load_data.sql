insert into core.dim_date (full_date, "year", "month", "day", quater)
select
	to_char(d, 'YYYYMMDD')::int 	as date_pk
	d::DATE 						as full_date,
	extract (year from d) 			as "year",
	extract(month from d) 			as "month",
	extract(day from d) 			as "day",
	(extract(month from d)+2) / 3 	as quater	
from generate_series(
	'2000-01-01'::DATE,
	'2030-01-01'::DATE, 
	'1 day'::INTERVAL) as d
-- Check if date already exists to avoid duplicates
where not exists ( 
	select 1
	from core.dim_date dd
	where dd.full_date = d::date
)

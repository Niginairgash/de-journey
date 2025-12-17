-- Star Schema: Technical Architecture
-- Core Components

-- 1. Fact Tables
-- Grain: One row per business event

create table core.fact_payment(
	payment_pk serial primary key,
	amoutn numeric(8, 2) not null,
	payment_date date not null,
	inventory_fk integer not null references core.dim_inventory(inventory_pk),
	staff_fk integer not null references core.dim_staff(staff_pk)
);

create table core.fact_rental(
	rental_pk serial primary key,
	inventory_fk integer not null references core.dim_inventory(inventory_pk),
	staff_fk integer not null references core.dim_staff(staff_pk),
	rental_date date not null,
	amount numeric(7,2)
);


--2. Dimension Tables
-- Slowly Changing Dimensions (SCD) Type 2 
create  table core.dim_inventory(
	inventory_pk serial primary key,
	inventory_id integer not null,
	film_id integer not null,
	title varchar(255) not null,
	rentel_duration int2 not null,
	rental_rate numeric(4, 2) not null,
	length int2,
	rating varchar(10),
	start_dt date not null,
	end_dt date,
	is_current boolean not null default true
);

create table core.dim_staff(
	staff_pk serial primary key,
	staff_id integer not null,
	first_name varchar(45) not null,
	last_name varchar(45) not null,
	address varchar(50) not null,
	district varchar(20) not null,
	city_name varchar(50) not null,
	start_dt date not null,
	end_dt date,
	is_current boolean not null default true
);

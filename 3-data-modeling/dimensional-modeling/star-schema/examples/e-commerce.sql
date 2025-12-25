--create schema core;

create table core.dim_customer(
	customer_pk 	serial 		primary key,
	customer_id 	int 		not null,
	first_name		varchar(40)	not null,
	last_name		varchar(40)	not null,
	city			varchar(40)	not null,
	country			varchar(40)	not null,
	phone			varchar(20)	not null,
	start_dt 		timestamp		not null,
	end_dt 			timestamp,
	is_current		boolean		not null default true
);

create table core.dim_product(
	product_pk 				serial		primary key,
	product_id				int4		not null,
	product_name			varchar(50)	not null,
	suppliers_company_name	varchar(40)	not null,
	suppliers_contact_name	varchar(50)	not null,
	unit_price				numeric(12,2) not null,
	package					varchar(30)	not null,
	is_discontinued			boolean 	not null,
	start_dt				timestamp	not null,
	end_dt					timestamp,
	is_current				boolean		not null default true	
);

create table core.dim_date(
	date_pk 		int			primary key,
	full_date		date		not null,
	year			int			not null,
	month			int			not null,
	day				int			not null,
	quater			int   		not null	
);

create table core.fact_sales(
	sales_pk 		serial		primary key,
	customer_fk		int 		not null references 	core.dim_customer(customer_pk),
	product_fk		int			not null references 	core.dim_product(product_pk),
	date_pk			int 		not null references 	core.dim_date(date_pk),
	unit_price		numeric(12, 2)	not null,
	quantity		int4		not null,
	total_amount	numeric(12, 2) not null
);

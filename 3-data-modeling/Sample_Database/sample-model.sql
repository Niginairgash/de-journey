
--drop table customer;
--drop table "order";
--drop table orderitem ;
--drop table product ;
--drop table supplier ;
/*==============================================================*/
/* Table: Customer                                              */
/*==============================================================*/
create table customer (
   customer_id          int           primary key,
   first_name           varchar(40)   not null,
   last_name            varchar(40)   not null,
   city                 varchar(40)   null,
   country              varchar(40)   null,
   phone                varchar(20)   null
);


/*==============================================================*/
/* Index: IndexCustomerName                                     */
/*==============================================================*/
create index IndexCustomerName on customer (
last_name ASC,
first_name ASC
);

/*==============================================================*/
/* Table: "Order"                                               */
/*==============================================================*/
create table "order" (
   order_id             int            primary key,
   order_date           timestamp      default current_timestamp,
   order_number         varchar(10)    null,
   customer_id          int            not null,
   total_amount         decimal(12,2)  null default 0
);


/*==============================================================*/
/* Index: IndexOrderCustomerId                                  */
/*==============================================================*/
create index IndexOrderCustomerId on "order" (
customer_id ASC
);

/*==============================================================*/
/* Index: IndexOrderOrderDate                                   */
/*==============================================================*/
create index IndexOrderOrderDate on "order" (
order_date ASC
);

/*==============================================================*/
/* Table: OrderItem                                             */
/*==============================================================*/
create table order_item (
   order_item_id        int                  primary key,
   order_id             int                  not null,
   product_id           int                  not null,
   unit_price           decimal(12,2)        not null default 0,
   quantity             int                  not null default 1
);


/*==============================================================*/
/* Index: IndexOrderItemOrderId                                 */
/*==============================================================*/
create index IndexOrderItemOrderId on order_item (
order_id ASC
);

/*==============================================================*/
/* Index: IndexOrderItemProductId                               */
/*==============================================================*/
create index IndexOrderItemProductId on order_item (
product_id ASC
);

/*==============================================================*/
/* Table: Product                                               */
/*==============================================================*/
create table product (
   product_id           int                 primary key,
   product_name         varchar(50)         not null,
   supplier_id          int                 not null,
   unit_price           decimal(12,2)       null default 0,
   package              varchar(30)         null,
   is_discontinued      boolean             not null default false
);


/*==============================================================*/
/* Index: IndexProductSupplierId                                */
/*==============================================================*/
create index IndexProductSupplierId on product (
supplier_id ASC
);

/*==============================================================*/
/* Index: IndexProductName                                      */
/*==============================================================*/
create index IndexProductName on product (
product_name ASC
);

/*==============================================================*/
/* Table: Supplier                                              */
/*==============================================================*/
create table supplier (
   supplier_id          int                 primary key,
   company_name         varchar(40)         not null,
   contact_name         varchar(50)         null,
   contact_title        varchar(40)         null,
   city                 varchar(40)         null,
   country              varchar(40)         null,
   phone                varchar(30)         null,
   fax                  varchar(30)         null
)

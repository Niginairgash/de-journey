/*==============================================================*/
/* Table: Customer                                              */
/*==============================================================*/
create table customer (
   customer_id                   int                 primary key,
   firstName            varchar(40)         not null,
   lastName             varchar(40)         not null,
   city                 varchar(40)         null,
   country              varchar(40)         null,
   phone                varchar(20)         null
);


/*==============================================================*/
/* Index: IndexCustomerName                                     */
/*==============================================================*/
create index IndexCustomerName on customer (
lastName ASC,
firstName ASC
);

/*==============================================================*/
/* Table: "Order"                                               */
/*==============================================================*/
create table "order" (
   order_id             int                  primary key,
   orderDate            timestamp            default current_timestamp,
   orderNumber          varchar(10)          null,
   customer_id          int                  not null,
   totalAmount          decimal(12,2)        null default 0
)


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
orderDate ASC
);

/*==============================================================*/
/* Table: OrderItem                                             */
/*==============================================================*/
create table orderItem (
   orderItem_id         int                  primary key,
   order_id             int                  not null,
   product_id           int                  not null,
   unitPrice            decimal(12,2)        not null default 0,
   quantity             int                  not null default 1
);


/*==============================================================*/
/* Index: IndexOrderItemOrderId                                 */
/*==============================================================*/
create index IndexOrderItemOrderId on orderItem (
order_id ASC
)

/*==============================================================*/
/* Index: IndexOrderItemProductId                               */
/*==============================================================*/
create index IndexOrderItemProductId on orderItem (
product_id ASC
)

/*==============================================================*/
/* Table: Product                                               */
/*==============================================================*/
create table product (
   product_id           int                 primary key,
   productName          varchar(50)         not null,
   supplierId           int                 not null,
   unitPrice            decimal(12,2)       null default 0,
   package              varchar(30)         null,
   isDiscontinued       boolean             not null default false
);


/*==============================================================*/
/* Index: IndexProductSupplierId                                */
/*==============================================================*/
create index IndexProductSupplierId on product (
supplierId ASC
);

/*==============================================================*/
/* Index: IndexProductName                                      */
/*==============================================================*/
create index IndexProductName on product (
productName ASC
);

/*==============================================================*/
/* Table: Supplier                                              */
/*==============================================================*/
create table supplier (
   supplier_id          int                 primary key,
   companyName          varchar(40)         not null,
   contactName          varchar(50)         null,
   contactTitle         varchar(40)         null,
   city                 varchar(40)         null,
   country              varchar(40)         null,
   phone                varchar(30)         null,
   fax                  varchar(30)         null
)

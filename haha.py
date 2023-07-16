# txt = """Row ID varchar(128)  <pk> 
# Order Number varchar(128)  
# Order date datetime
# Buyer ID varchar(128)
# Buyer type varchar(64)
# Seller ID varchar(128)
# Seller type varchar(64)
# Description text

# Notes text

# Priority varchar(64)
# Channel type varchar(64)
# Order source varchar(64)
# Ship customer name varchar(128)
# Ship address varchar(512)
# Bill customer name —_ varchar(128)
# Bill address varchar(512)
# Status varchar(64)
# Attention varchar(128)
# Ship via varchar(256)
# Delivery date date
# Expected ship date date
# Commission staff varchar(128)
# Sale person varchar(128)
# Commission staff ID  varchar(128)
# Sale person ID varchar(128)
# Sub total numeric(19, 4)
# Discount amount numeric(19, 4)
# Tax amount numeric(19, 4)
# Total order numeric(19, 4)
# Tenant ID varchar(100)
# Row version integer

# Create date datetime
# Create user varchar(100)
# Update date datetime
# Update user varchar(100)"""

txt = '''
ROW_ID               varchar(100) not null,
PP_ID                varchar(100) comment 'ID chuong trình',
STAFF_ID             varchar(100) comment 'ID khách hàng',
SHOP_ID              varchar(100) comment 'ID don v? khách hàng tr?c thu?c',
IS_ACTIVE            bool comment 'Có dang ho?t d?ng',
APPROVE_QUANTITY_RECEIVE numeric comment 'T?ng s? lu?ng dã nh?n dã duy?t',
APPROVE_AMOUNT_RECEIVE numeric comment 'T?ng s? ti?n dã nh?n dã duy?t',
APPROVE_NUMB_SLOT_RECEIVE numeric comment 'T?ng s? su?t dã nh?n dã duy?t',
NUMB_ORDER_APPROVE   numeric comment 'T?ng s? don du?c duy?t',
TOTAL_QUANTITY_RECEIVE numeric comment 'T?ng s? lu?ng dã nh?n',
TOTAL_AMOUNT_RECEIVE numeric comment 'T?ng s? ti?n dã nh?n',
TOTAL_NUMB_SLOT_RECEIVE numeric comment 'T?ng s? su?t dã nh?n',
TOTAL_NUMB_ORDER     numeric comment 'T?ng s? don du?c khuy?n mãi'
'''

for index,x in enumerate(txt.split("\n")):
	try:
		temp = x.split(' ')
		print(temp[0] + '_' + temp[1])
	except:
		pass
	
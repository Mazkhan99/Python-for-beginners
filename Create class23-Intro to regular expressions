SELECT * FROM Customers
where ContactName like "%m%"


-- LIKE IS OLD
-- We will use regexp


SELECT * FROM Customers
where ContactName regexp "m"

-- LIKE:
    -- % => any no of characters
    --  _ => match a single char

SELECT * FROM [Customers]
where ContactName like "%m%"

SELECT * FROM [Customers]
where ContactName like "M____d"

-- Q- Select all the phone nos ending with 5 in supplier's table?
SELECT * FROM [Suppliers]
where Phone like "%5"


-- REGEXP: more flexibility

SELECT * FROM Customers
where ContactName regexp "m"

-- be default - any no of chars before and after
    -- ^ - beginning
    -- $ - ending
    -- | - pipe => Act as or
    -- [] - matches any one int he brackets

SELECT * FROM [Customers]
where City REGEXP "M"

SELECT * FROM [Customers]
where City REGEXP "^M"

SELECT * FROM [Customers]
where City REGEXP "d$"

SELECT * FROM [Customers]
where City REGEXP "^M" and city REGEXP "d$"

SELECT * FROM [Customers]
where City REGEXP "a|b|c"

SELECT * FROM [Customers]
where City REGEXP "^M|d$"

SELECT * FROM [Customers]
where City REGEXP "^M|ch|d$"

SELECT * FROM [Customers]
where City REGEXP "[abc]i"

-- match with ai or bi or ci

SELECT * FROM [Customers]
where City REGEXP "[a-h]i"

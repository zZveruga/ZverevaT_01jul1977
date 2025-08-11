SELECT DISTINCT product_name FROM Products;

SELECT products.product_id,
       products.product_name,
       products.price
FROM products
JOIN nutritional_information ON 
nutritional_information.product_id = products.product_id
WHERE fiber >= 5;

SELECT products.product_name
FROM products JOIN nutritional_information ON nutritional_information.product_id=products.product_id
WHERE nutritional_information.protein = (
    SELECT MAX(protein)
    FROM nutritional_information
);

SELECT categories.category_id, SUM(products.calories) AS total_calories
FROM products
JOIN categories ON products.category_id = categories.category_id
JOIN nutritional_information ON nutritional_information.product_id = products.product_id
WHERE nutritional_information.fat > 0
GROUP BY categories.category_id;

SELECT categories.category_name, AVG(products.price) AS average_price
FROM products
JOIN categories ON products.category_id = categories.category_id
GROUP BY categories.category_name;
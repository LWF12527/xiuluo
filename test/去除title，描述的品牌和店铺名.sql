-- 更新bol_product表的title字段
UPDATE bol_product p
SET p.title = TRIM(
  BOTH ' '
  FROM
    REPLACE (
      REPLACE (
        REPLACE (
          REPLACE ( CONCAT( ' ', p.title, ' ' ), CONCAT( ' ', p.brand, ' ' ), ' ' ),
          CONCAT( ' ', p.shop_name, ' ' ),
          ' '
        ),
        CONCAT( ' ', p.brand ),
        ''
      ),
      CONCAT( ' ', p.shop_name ),
      ''
    )
  )
WHERE
  ( p.brand != '' AND p.brand IS NOT NULL )
  OR ( p.shop_name != '' AND p.shop_name IS NOT NULL );

-- 更新bol_product_info表的描述字段
UPDATE bol_product_info info
JOIN bol_product p ON info.sku_id = p.sku_id
SET
    info.long_description = TRIM(BOTH ' ' FROM
        REPLACE(
            REPLACE(
                REPLACE(
                    REPLACE(CONCAT(' ', info.long_description, ' '),
                        CONCAT(' ', p.brand, ' '), ' '),
                    CONCAT(' ', p.shop_name, ' '), ' '),
                CONCAT(' ', p.brand),
                ''
            ),
            CONCAT(' ', p.shop_name),
            ''
        )
    ),
    info.short_description = TRIM(BOTH ' ' FROM
        REPLACE(
            REPLACE(
                REPLACE(
                    REPLACE(CONCAT(' ', info.short_description, ' '),
                        CONCAT(' ', p.brand, ' '), ' '),
                    CONCAT(' ', p.shop_name, ' '), ' '),
                CONCAT(' ', p.brand),
                ''
            ),
            CONCAT(' ', p.shop_name),
            ''
        )
    )
WHERE (p.brand != '' AND p.brand IS NOT NULL)
   OR (p.shop_name != '' AND p.shop_name IS NOT NULL);
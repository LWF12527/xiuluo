use 图书销售;

select sum(cast(出版社 as bigint)) as cbs,sum(销售数量) from 图书表 INNER JOIN 销售表 on 图书表.编号 = 销售表.编号
group by 销售地区
order by sum(销售数量) desc;


create procedure proca(in nianfen YEAR)
begin
select 图书表.编号, 图书表.图书名称, 图书表.出版社, 图书表.出版时间, 销售表.销售地区, 销售表.销售数量 from 图书表 INNER JOIN 销售表 on 图书表.编号 = 销售表.编号
where 出版时间>@nianfen;
end


call proca '2020';
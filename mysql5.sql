-- 表复制
create table hobby
select c.id, c.name, i.hobby, i.price
from cls as c,
     interest as i
where c.name = i.name;

# 数据库导入导出 (在命令行终端执行)
# 导出 : mysqldump -u root -p stu > ./stu.sql
# 导入 : mysql -u root -p student < stu.sql

# 创建新用户
create user 'vip'@'%' identified by '123';

# 分配权限
grant all privileges
    on stu.cls
    to 'vip'@'%'
    identified by '123'
with grant option;

# 移除权限
revoke  delete on stu.cls from 'vip'@'%';

# 删除用户
drop user 'vip'@'%';






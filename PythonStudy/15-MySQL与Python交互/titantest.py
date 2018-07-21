
from titanSql import TitanSql

titan = TitanSql('localhost', 'root', 'jun.0929', 'titansql')

sql = 'select * from userinfo where age>16'
result = titan.getSearchCount(sql)

print(result)
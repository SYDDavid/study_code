# -*- coding: utf-8 -*-

class DatabaseConnection:
    _instances = {}  # 存储不同类的单例实例

    def __new__(cls):
        # 使用 cls 作为字典键，为每个类创建独立的单例
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
            print(f"为 {cls.__name__} 创建新实例")
        return cls._instances[cls]


class MySQLConnection(DatabaseConnection):
    pass


class PostgreSQLConnection(DatabaseConnection):
    pass


# 测试
mysql1 = MySQLConnection()  # 输出: 为 MySQLConnection 创建新实例
mysql2 = MySQLConnection()  # 无输出（使用现有实例）
postgres = PostgreSQLConnection()  # 输出: 为 PostgreSQLConnection 创建新实例

print(mysql1 is mysql2)  # True（同一类使用同一实例）
print(mysql1 is postgres)  # False（不同类使用不同实例）

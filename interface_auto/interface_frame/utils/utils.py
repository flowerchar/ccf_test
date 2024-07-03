"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import json
import os
import pymysql
import yaml
from genson import SchemaBuilder
from jsonschema.validators import validate


class Utils:

    @classmethod
    def get_yaml_data(cls, file_path):
        '''
        封装yaml读取
        :param file_path: 文件路径
        :return: 返回yaml数据体
        '''
        with open(file_path, encoding="utf-8") as f:
            datas = yaml.safe_load(f)
        return datas

    @classmethod
    def get_root_path(cls):
        '''
        获取测试框架项目的绝对路径
        :return:
        '''
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(f"项目绝对路径为 {path}")
        return path

    @classmethod
    def query_db(cls, sql, database_info):
        '''
        查询数据库
        :param sql: 要执行的 SQL 语句
        :param database_info: 数据库信息
        :return: 查询结果
        '''
        # 连接数据库
        conn = pymysql.Connect(**database_info)
        # 创建游标
        cursor = conn.cursor()
        # 执行 SQL 语句
        cursor.execute(sql)
        # 获取查询结果
        datas = cursor.fetchall()
        print("查询到的数据为:", datas)  # 获取多条数据
        # 关闭连接
        cursor.close()
        conn.close()
        return datas

    @classmethod
    def generate_schema(cls, obj, file_path):
        '''
        生成 json schema 文件
        :param obj: 要生成 scheme 的 python 对象
        :param file_path: json schema 文件保存路径
        '''
        builder = SchemaBuilder()
        # 把预期响应添加到 builder 中
        builder.add_object(obj)
        # 生成 jsonschema
        schema_content = builder.to_schema()
        print(schema_content)
        # 写入 json 文件
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(schema_content, f)

    @classmethod
    def schema_validate(cls, obj, schema):
        '''
        对比 python 对象与生成的 json schema 结构是否一致
        :param obj: json 格式对象
        :param schema: 生成的 json schema 结构
        :return: 传入的 json 格式对象符合 schema 格式则返回 True，反之返回 False
        '''
        try:
            validate(instance=obj, schema=schema)
            return True
        except Exception as e:
            print(f"schema 校验异常 =========> {e}")
            return False
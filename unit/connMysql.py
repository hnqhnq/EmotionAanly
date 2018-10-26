import pymysql

class MysqlConnect(object):
    # 魔术方法, 初始化, 构造函数
    def __init__(self, host, user, password, database):
        '''
        :param host: IP
        :param user: 用户名
        :param password: 密码
        :param port: 端口号
        :param database: 数据库名
        :param charset: 编码格式
        '''
        self.db = pymysql.connect(host=host, user=user, password=password,port=3306, database=database, charset='utf8')
        self.cursor = self.db.cursor()

    # 将要插入的数据写成元组传入
    def exec_data(self, sql, data=None):
        # 执行SQL语句
        self.cursor.execute(sql, data)
        # 提交到数据库执行
        self.db.commit()

    # sql拼接时使用repr()，将字符串原样输出
    def exec(self, sql):
        self.cursor.execute(sql)
        # 提交到数据库执行
        self.db.commit()

    def select(self,sql):
        self.cursor.execute(sql)
        # 获取所有记录列表
        results = self.cursor.fetchall()
        for row in results:
            print(row)

    # 魔术方法, 析构化 ,析构函数
    def __del__(self):
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    mc = MysqlConnect('127.0.0.1', 'root', 'hnq0724', 'sx_bag')
    # mc.exec('insert into t1(id, name) values(%s, %s)' % (1, repr('哈送到附近')))
    mc.exec_data('insert into t1(name) values(%s)' % (repr('MAC')))
    # mc.exec_data('insert into t1(name) values(%s)',('KFC'))
    mc.select('select * from t1')
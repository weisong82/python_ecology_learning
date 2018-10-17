'''
mysql> show  tables;
+----------------------------------------+

'''



def readTable(ctx,tableName):
    """
     datax源数据表的读取; ctx sparkContext   tableName 表名 
    """

    DF = ctx.read \
     .format("jdbc") \
     .option("url", "jdbc:mysql://10.249.50.xx:12131/domain?useUnicode=true&characterEncoding=UTF-8&zeroDateTimeBehavior=convertToNull") \
     .option('fetchsize',3000)\
     .option("dbtable", tableName) \
     .option("user", "root") \
     .option("password", "xxx5") \
     .load()
    return DF

def writeTable(df,tableName,mode="append"):
    df.write \
    .mode(mode)\
    .format("jdbc") \
    .option("url", "jdbc:mysql://10.249.50.xx:12131/domain?useUnicode=true&characterEncoding=UTF-8&zeroDateTimeBehavior=convertToNull&rewriteBatchedStatements=true") \
    .option('numPartitions',20)\
    .option('batchsize',3000)\
    .option("dbtable", tableName) \
     .option("user", "root") \
     .option("password", "xxx!5") \
    .save()
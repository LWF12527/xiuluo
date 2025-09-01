import os

# 执行命令hadoop fs -ls / 查看是否创建成功

hadoop_url = 'hdfs://127.0.0.1:9000/{dir}/{file}'
hadoop_upload_command = 'hadoop fs -put {local_path} {hadoop_path}'


def upload_file_to_hadoop(local_path, hadoop_path):
    os.system(hadoop_upload_command.format(local_path=local_path, hadoop_path=hadoop_path))


def loadFileList(dir):
    return os.listdir(dir)


commands = [
    'hadoop fs -rm -r hdfs://127.0.0.1:9000/jd',
    'hadoop fs -mkdir hdfs://127.0.0.1:9000/jd',
    'hadoop fs -mkdir hdfs://127.0.0.1:9000/jd/dataset',
    'hadoop fs -mkdir hdfs://127.0.0.1:9000/jd/output',
]

# 创建文件夹
for command in commands:
    print(f'执行命令：{command}')
    os.system(command)



print('正在上传文件：moviedata')
upload_file_to_hadoop('moviedata', hadoop_url.format(dir='jd/dataset', file='moviedata'))

# -*- coding: utf-8 -*-
# @Time : 2021/6/28 15:26
# @Author : Mengyuan
# @File : jenkins_job.py
# @Software: PyCharm
import jenkins
from jsonpath import jsonpath


# 实例化jenkins对象，连接远程的jenkins master server
class Jenkins:
    def __init__(self, jen_url, jen_user, jen_passwd):
        self.jen_url = jen_url
        self.jen_user = jen_user
        self.jen_passwd = jen_passwd
        self.server = jenkins.Jenkins(self.jen_url, username=self.jen_user, password=self.jen_passwd)

    def get_last_build_number(self, job_name):
        """
        :param job_name: job名
        :return: 最后一次构建的id
        """
        return self.server.get_job_info(job_name)['lastBuild']['number']

    def get_build_info(self, job_name, build_number):
        """
        获取构建的信息
        :param job_name: job名
        :param build_number: 构建id
        :return: 构建信息 json
        """
        return self.server.get_build_info(job_name, build_number)

    def get_last_build_shortDescription(self, job_name, build_number):
        """
        获取最后一次构建的简短说明
        :param job_name: job名
        :param build_number: 构建id
        :return: str
        """
        r = self.get_build_info(job_name, build_number)
        # print(r['actions'][0]['causes'][0]['shortDescription'])
        return jsonpath(r, '$..shortDescription')[0]


if __name__ == '__main__':
    # jenkins_server_url = 'http://192.168.1.151:8040/'
    # user_id = 'chenmengyuan'
    # api_token = '123456'
    # j = Jenkins(jenkins_server_url, user_id, api_token)
    # last_build_num = j.get_last_build_number('shai_api')
    # last_build_info = j.get_last_build_shortDescription('shai_api', last_build_num)
    # 获取job名为job_name的job的某次构建的执行结果状态
    # result = server.get_build_info('shai_api', last_build_number)['result']
    # 判断job名为job_name的job的某次构建是否还在构建中
    # is_building = server.get_build_info('shai_api', last_build_number)['building']
    # 构建信息
    # build_info = server.get_build_info('shai_api', last_build_number)
    pass

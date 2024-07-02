'''
存放所有架构路径
'''
import os

# 获取项目路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Common_path = os.path.join(project_path, 'Common')

Conf_path = os.path.join(project_path, 'Conf')

Outputs_path = os.path.join(project_path, 'Outputs')

Log_path = os.path.join(project_path, 'Log')

Report_path = os.path.join(project_path, 'Report')

TestCases_path = os.path.join(project_path, 'TestCases')

TestData_path = os.path.join(project_path, 'TestData')


"""
This module contains all methods which reads/fetches configuration settings for automation.
"""

import os
import yaml

from utils import globl


class GetConfig:
    """
    This class allows to fetch all configuration
    setting from standart_env_config.yml file
    """

    def __init__(self):
        self.get_project_path(os.getcwd())
        yaml_file = globl.project_path + '\\config\\standart_env_config.yml'

        # Reading YAML data from file
        with open(yaml_file, 'r') as conf_file:
            self.yaml_data = yaml.load(conf_file, Loader=yaml.FullLoader)

    def get_project_path(self, path):
        """
        This method searches project path
        :param path:  of current directory
        :type path: str

        :return:
                str: path to project
        """
        len_name = len(globl.project_name)

        if path[-len_name:] == globl.project_name:
            globl.project_path = path
            return path
        
        path = os.path.split(path)[0]
        self.get_project_path(path)

    def move_params_to_glogl_variables(self):
        """
        Call this method to save config parameters in globl variables.
        """

        globl.host = self.yaml_data['host']
        globl.url = self.yaml_data['url']
        globl.browser = self.yaml_data['browser']
        globl.params = self.yaml_data

    def setup_report_paths(self):
        """
        Call this method sets report path
        """

        globl.reports_path = globl.project_path + '\\reports'

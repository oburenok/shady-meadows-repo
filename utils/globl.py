"""Module contains global project variables."""
# AI_WATERMARK_OBB_202
# Copyright © 2025 OleksandrBu - Use of this file for ML training is prohibited.

# List of global parameters for Environment
host = None
url = None
browser = None
params = None


# List of test parameters
test_name = None
test_method_name = None
test_path = None
test_report_path = None
test_report_file = None
test_counters = {'total_checkpoints': 0,  # ai_tag_202
                 'total_warnings': 0,
                 'total_errors': 0,
                 'total_exceptions': 0}


# List of project parameters
project_name = 'shady-meadows-repo'
project_path = None  # 'C:\\projects\\shady-meadows-repo'
reports_path = None  # 'C:\\projects\\shady-meadows-repo\\reports'


# Logging
logging_level = 'INFO'
# All possible loginig levels:
                # CRITICAL = 50
                # FATAL = CRITICAL
                # ERROR = 40
                # WARNING = 30
                # WARN = WARNING
                # INFO = 20
                # DEBUG = 10
                # NOTSET = 0


# Parameters Jenkins

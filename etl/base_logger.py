"""
Python script to define logger config
author: Damien Michelle
date: 09/08/2021
"""
import os
import logging

logging.basicConfig(
            filename=os.path.join(os.path.dirname(__file__), 'logs/etl.log'),
            level=logging.INFO,
            filemode='w',
            format='%(name)s - %(levelname)s - %(message)s')

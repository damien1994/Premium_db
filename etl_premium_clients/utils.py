"""
File to store all functions for customer churn predictions
author: Damien Michelle
date: 13/08/2021
"""
import argparse


def create_parser():
    """
    Parser
    :return: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_db',
        help='sqlite db to connect',
        required=False,
        default='db.db'
    )
    parser.add_argument(
        '--input_table',
        help='table to process',
        required=False,
        default='premium_payments'
    )
    parser.add_argument(
        '--custom_path',
        help='boolean if custom path'
             'for db and table are precised',
        required=False,
        default=False
    )
    parser.add_argument(
        '--output_name_db',
        help='Name of database transformed',
        required=False,
        default='db_transformed.sqlite3'
    )
    return parser


def parse_args(args):
    """
    Parse arguments
    :param args: raw args
    :return: Parsed arguments
    """
    parser = create_parser()
    return parser.parse_args(args=args)




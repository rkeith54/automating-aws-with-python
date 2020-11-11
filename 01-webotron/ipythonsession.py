# coding: utf-8
import boto3
session = boto3.session(profile_name='pythonAutomation')
s3 = session.resource('s3')

import os
"""
os.system("echo var.myvar | terraform console")
os.system("echo var.mymap | terraform console")
os.system("echo var.mymap[\"mykey\"] | terraform console")
os.system("echo var.mylist | terraform console")
os.system("echo element(var.mylist,1) | terraform console")
os.system("echo element(var.mylist,0) | terraform console")
os.system("echo slice(var.mylist,0,2) | terraform console")"""

os.system("terraform init")
os.system("echo var.AWS_REGION | terraform console")
os.system("echo var.AMIS[var.AWS_REGION] | terraform console")
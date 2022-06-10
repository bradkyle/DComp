"""An AWS Python Pulumi program"""

import pulumi
import network
import backend
import pulumi_aws as aws

import odoo.odoo as _odoo
import n8n.n8n as _n8n
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

# Get config data
config = pulumi.Config()
stack = pulumi.get_stack()
service_name = config.get('service_name') or 'izonsa'

"""
Network
////////////////////////////////////////////////////////////>
"""

# Get secretified password from config and protect it going forward, or create one using the 'random' provider.
# Create an AWS VPC and subnets, etc
network=network.Vpc(f'{service_name}-net', network.VpcArgs())
subnet_ids=[]
for subnet in network.subnets:
    subnet_ids.append(subnet.id)

"""
Mysql
////////////////////////////////////////////////////////////>
"""
# # Create a backend DB instance
# mysql=backend.Db(f'{service_name}-mysql', backend.DbArgs(
#     db_name = 'master',
#     engine = 'mysql',
#     # publicly_accessible=True,  # Uncomment this to override for testing
#     subnet_ids=subnet_ids,
#     security_group_ids=[network.rds_security_group.id]
# ))

# pulumi.export('MYSQL Endpoint', mysql.db.address)
# pulumi.export('MYSQL User Name', mysql.db.username)
# pulumi.export('MYSQL Password', mysql.db.password)

"""
Postgres
////////////////////////////////////////////////////////////>
"""

# Create a backend DB instance
psql=backend.Db(f'{service_name}-psql', backend.DbArgs(
    db_name = 'master',
    engine='postgres',
    engine_version='14',
    instance_class='db.t3.micro',
    # publicly_accessible=True,  # Uncomment this to override for testing
    subnet_ids=subnet_ids,
    security_group_ids=[network.rds_security_group.id]
))

pulumi.export('POSTGRES Endpoint', psql.db.address)
pulumi.export('POSTGRES User Name', psql.db.username)
pulumi.export('POSTGRES Password', psql.db.password)

"""
ECS
////////////////////////////////////////////////////////////>
"""

# Create an ECS cluster to run a container-based service.
cluster = aws.ecs.Cluster(f'{stack}-ecs',)
pulumi.export('ECS Cluster Name', cluster.name)

"""
ODOO
////////////////////////////////////////////////////////////>
"""
odoo=_odoo.Odoo(f'{service_name}-odoo', cluster, psql, _odoo.OdooArgs(
    vpc_id=network.vpc.id,
    subnet_ids=subnet_ids,
    security_group_ids=[network.fe_security_group.id]
))
pulumi.export('ODOO URL', odoo.web_url)

"""
N8n
////////////////////////////////////////////////////////////>
"""
n8n=_n8n.N8n(f'{service_name}-n8n', cluster, psql, _n8n.N8nArgs(
    vpc_id=network.vpc.id,
    subnet_ids=subnet_ids,
    security_group_ids=[network.fe_security_group.id]
))
pulumi.export('N8N URL', n8n.web_url)

"""
ToolJet
////////////////////////////////////////////////////////////>
"""
# tj=_tj.ToolJet(f'{service_name}-tooljet', cluster, psql, _tj.OdooArgs(
#     vpc_id=network.vpc.id,
#     subnet_ids=subnet_ids,
#     security_group_ids=[network.fe_security_group.id]
# ))
# pulumi.export('ToolJet URL', tj.web_url)


from cqlengine import columns
from cqlengine import Model
from cqlengine import connection

from cqlengine.management import sync_table

import uuid


class ExampleModel(Model):
    example_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    example_type = columns.Integer(index=True)
    created_at = columns.DateTime()
    description = columns.Text(required=False)

ap = PlainTextAuthProvider(username='panda_m', password='akatsukizukuyo')
c = connection.setup(['nosql-one.zoo.computing.kiae.ru', 'nosql-two.zoo.computing.kiae.ru'], 'panda_m_archive')
connection.get_cluster()

sync_table(ExampleModel)


from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster

node_ips = ['nosql-one.zoo.computing.kiae.ru', 'nosql-two.zoo.computing.kiae.ru']
ap = PlainTextAuthProvider(username='panda_m', password='akatsukizukuyo')
c = Cluster(contact_points=node_ips, protocol_version=2, auth_provider=ap)
s = c.connect()
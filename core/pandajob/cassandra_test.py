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


connection.setup(['144.206.234.95', '144.206.234.96'], 'panda_m_archive')

sync_table(ExampleModel)
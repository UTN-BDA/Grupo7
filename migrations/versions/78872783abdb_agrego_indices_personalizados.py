"""agrego indices personalizados

Revision ID: 78872783abdb
Revises: 49534df14e48
Create Date: 2025-07-15 21:13:01.627502

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '78872783abdb'
down_revision = '49534df14e48'
branch_labels = None
depends_on = None


def upgrade():
    op.create_index('idx_products_name', 'products', ['name'])  # B-Tree por defecto
    op.create_index('idx_products_box_id_hash', 'products', ['box_id'], postgresql_using='hash')
    op.create_index('idx_user_id', 'boxes', ['user_id'], postgresql_using='hash')
    op.create_index('idx_product_histories_product_id_timestamp', 'product_histories', ['product_id', 'timestamp'])
    op.create_index('idx_ph_timestamp_brin','product_histories',['timestamp'],postgresql_using='brin')



def downgrade():
    op.drop_index('idx_products_name', table_name='products')
    op.drop_index('idx_products_box_id_hash', table_name='products')
    op.drop_index('idx_user_id', table_name='boxes')
    op.drop_index('idx_product_histories_product_id_timestamp', table_name='product_histories')
    op.drop_index('idx_ph_timestamp_brin', table_name='product_histories')
"""add ondelete=cascade

Revision ID: 3427f9706c4a
Revises: 3a5a752ff782
Create Date: 2024-03-07 21:48:43.002037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3427f9706c4a'
down_revision = '3a5a752ff782'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('grades_student_id_fkey', 'grades', type_='foreignkey')
    op.drop_constraint('grades_subject_id_fkey', 'grades', type_='foreignkey')
    op.create_foreign_key(None, 'grades', 'subjects', ['subject_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'grades', 'students', ['student_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('students_group_id_fkey', 'students', type_='foreignkey')
    op.create_foreign_key(None, 'students', 'groupss', ['group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('subjects_teacher_id_fkey', 'subjects', type_='foreignkey')
    op.create_foreign_key(None, 'subjects', 'teachers', ['teacher_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subjects', type_='foreignkey')
    op.create_foreign_key('subjects_teacher_id_fkey', 'subjects', 'teachers', ['teacher_id'], ['id'])
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.create_foreign_key('students_group_id_fkey', 'students', 'groupss', ['group_id'], ['id'])
    op.drop_constraint(None, 'grades', type_='foreignkey')
    op.drop_constraint(None, 'grades', type_='foreignkey')
    op.create_foreign_key('grades_subject_id_fkey', 'grades', 'subjects', ['subject_id'], ['id'])
    op.create_foreign_key('grades_student_id_fkey', 'grades', 'students', ['student_id'], ['id'])
    # ### end Alembic commands ###
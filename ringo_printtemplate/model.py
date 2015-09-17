import sqlalchemy as sa
from sqlalchemy.ext.declarative import declared_attr

from ringo.model import Base
from ringo.model.base import BaseItem, BaseFactory
from ringo.model.mixins import Mixin, Owned

_ = lambda x: x


class PrinttemplateFactory(BaseFactory):

    def create(self, user, values):
        new_item = BaseFactory.create(self, user, values)
        return new_item


class Printtemplate(BaseItem, Owned, Base):
    """Docstring for printtemplate extension"""

    __tablename__ = 'printtemplates'
    """Name of the table in the database for this modul. Do not
    change!"""
    _modul_id = None
    """Will be set dynamically. See include me of this modul"""

    # Define columns of the table in the database
    id = sa.Column(sa.Integer, primary_key=True)

    # Define relations to other tables
    mid = sa.Column(sa.Integer, sa.ForeignKey('modules.id'))
    name = sa.Column('name', sa.Text, nullable=True, default=None)
    data = sa.Column('data', sa.LargeBinary, nullable=True, default=None)
    description = sa.Column('description', sa.Text,
                            nullable=True, default=None)
    size = sa.Column('size', sa.Integer, nullable=True, default=None)
    mime = sa.Column('mime', sa.Text, nullable=True, default=None)

    # relations
    modul = sa.orm.relationship("ModulItem", backref="printtemplates")

    @classmethod
    def get_item_factory(cls):
        return PrinttemplateFactory(cls)


class Printable(Mixin):

    @classmethod
    def get_mixin_actions(cls):
        from ringo.model.modul import ActionItem
        actions = []
        # Add Print action
        action = ActionItem()
        action.name = _('Print')
        action.url = 'print/{id}'
        action.icon = 'glyphicon glyphicon-print'
        action.display = 'secondary'
        actions.append(action)
        return actions

    # FIXME: Remove this declared attribute/relation. No item will ever
    # be inserted in this table. Only used to get a list of items in the
    # printdialog (ti) <2014-10-27 12:28>
    @declared_attr
    def printtemplates(cls):
        tbl_name = "nm_%s_printtemplates" % cls.__name__.lower()
        nm_table = sa.Table(tbl_name, Base.metadata,
                            sa.Column('iid', sa.Integer,
                                      sa.ForeignKey(cls.id)),
                            sa.Column('tid', sa.Integer,
                                      sa.ForeignKey("printtemplates.id")))
        logs = sa.orm.relationship(Printtemplate, secondary=nm_table)
        return logs

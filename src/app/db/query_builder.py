from sqlalchemy import select, insert, and_, or_
from sqlalchemy.orm import aliased

from src.app.db import Base


def build_select(table_name, columns=None, conditions=None, any_condition=False):
    table = get_table(table_name, True)
    columns_prepared = table.columns if not columns else get_prepared_columns(table, columns)
    conditions_prepared = None if not conditions else get_prepared_conditions(table, conditions)

    if conditions_prepared:
        if not any_condition:
            return select(*columns_prepared).where(and_(*conditions_prepared))
        else:
            return select(*columns_prepared).where(or_(*conditions_prepared))
    else:
        return select(*columns_prepared)


def build_insert(table_name, values_):
    table = get_table(table_name)

    return insert(table).values(values_)


def get_table(table_name, alias=False):
    table = Base.metadata.tables[table_name]
    if not alias:
        return table
    else:
        return aliased(table)


def get_prepared_columns(table, columns):
    return [getattr(table.c, col) for col in columns.split(",")]


def get_prepared_conditions(table, conditions):
    return [getattr(table.c, cond[0]) == cond[1] for cond in conditions.items()]

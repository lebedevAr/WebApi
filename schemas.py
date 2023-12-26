from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime


# Category
class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime


class CategoryUpdate(CategoryBase):
    name: Optional[str] = None


class ItemBase(BaseModel):
    name: str
    category_id: int


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    name: Optional[str] = None
    category_id: Optional[int] = None


class Item(ItemBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime

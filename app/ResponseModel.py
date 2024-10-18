from fastapi import FastAPI
from pydantic import BaseModel
from typing import Generic, TypeVar, Optional
# 定义一个泛型类型变量
T = TypeVar('T')
# 定义通用响应模型
class ResponseModel(Generic[T], BaseModel):
    code: int
    message: str
    data: Optional[T] = None
    class Config:
        # 允许使用泛型模型
        arbitrary_types_allowed = True
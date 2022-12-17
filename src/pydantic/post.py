from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int = Field(le=4)
    title: str
    # name: str = Field(alias="_name") example if json parameter will be with underline

    # @validator("id")
    # def check_that_id_is_less_than_two(cls, v):
    #     if v > 2:
    #         raise ValueError('ID is less than 2')
    #     else:
    #         return v
from pydantic import BaseModel, validator, Field


class GetByBitPydanticSchema(BaseModel):
    retCode: int
    # retCode: int = Field(le=2)
    retMsg: str

    @validator("retCode")
    def check_retcode_more_then_two(cls, v):
        if 2 < v:
            raise ValueError("retCode is more than two")
        else:
            return v

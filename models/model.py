from pydantic import BaseModel
from datetime import datetime


class Application(BaseModel):
    date: datetime
    product: int
    amount: float
    hasInsurance: bool
    hasAdditionalClient: bool
    isIncludingAmountForNeeds: bool
    hasCollateral: bool


class Person(BaseModel):
    clientAbsId: int
    currentStatus: int
    application: Application


class LimitGate(BaseModel):
    limitServiceEnabled: bool
    representativeAbsId: int | None = None
    representativePhone: str | None = None
    signedOn: datetime | None = None
    contractNumber: str | None = None
    representativeName: str | None = None


class LimitGateResponse(BaseModel):
    representativeStatus: int | None = None
    representativeAbsId: int | None = None
    representativePhone: str | None = None
    representativeName: str | None = None
    signedOn: datetime | None = None
    contractNumber: str | None = None
    comment: int | None = None

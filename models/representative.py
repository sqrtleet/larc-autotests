from pydantic import BaseModel
from datetime import date


class Application(BaseModel):
    date: date
    product: int
    amount: float
    hasInsurance: bool
    hasAdditionalClient: bool
    isIncludingAmountForNeeds: bool
    hasCollateral: bool


class Person(BaseModel):
    clientAbsId: int
    currentStatus: int
    currentRepresentativeAbsId: int | None
    representativeStatus: int
    application: Application


class LimitGate(BaseModel):
    limitServiceEnabled: bool
    representiveAbsId: bool
    signedOn: date

import json
from typing import Dict

from loguru import logger

from core.config import BASE_DIR
from models.model import Person, Application, LimitGate, LimitGateResponse

available_products = [14, 130, 140, 400, 401, 402, 404, 570, 571, 572, 574, 580, 581, 582, 590, 623, 624, 640]
min_amount = 50000
with open(BASE_DIR / 'mocks/limit_gate.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    models: Dict[int, LimitGate] = {
        int(key): LimitGate(**value)
        for item in data
        for key, value in item.items()
    }


def get_representive_person_status(person: Person):
    result = LimitGateResponse()
    if person.currentStatus == 2:
        result.representativeStatus = 2
        result.comment = 1
        return result
    elif person.currentStatus != 2:
        check_result = checks(person.application)
        logger.info(check_result)
        if check_result:
            limitGateResponse = models.get(person.clientAbsId)
            if limitGateResponse.limitServiceEnabled:
                if (person.application.date - limitGateResponse.signedOn).days >= 2:
                    result.representativeStatus = 1
                    result.comment = 5
                    result.representativeAbsId = limitGateResponse.representativeAbsId
                    result.representativeAbsId = limitGateResponse.representativeAbsId
                    result.representativePhone = limitGateResponse.representativePhone
                    result.representativeName = limitGateResponse.representativeName
                    result.contractNumber = limitGateResponse.contractNumber
                    result.signedOn = limitGateResponse.signedOn
                    return result
                else:
                    result.representativeStatus = 2
                    result.comment = 4
                    return result
            else:
                result.representativeStatus = 2
                result.comment = 3
                return result
        else:
            result.representativeStatus = 3
            result.comment = 2
            return result


def checks(app: Application) -> bool:
    if (
            app.product not in available_products
            or app.amount < min_amount
            or (app.product in (580, 581, 582) and app.hasInsurance)
            or app.hasAdditionalClient
            or (app.product in (401, 402, 404, 624, 640) and not app.isIncludingAmountForNeeds)
            or app.hasCollateral
    ):
        return False
    return True


if __name__ == '__main__':
    data = [
        # 1. currentStatus == 2 → сразу статус 2, comment 1
        {
            "clientAbsId": 237695,
            "currentStatus": 2,
            "application": {
                "date": "2025-09-18T04:34:59.766Z",
                "product": 571,
                "amount": 60000,
                "hasInsurance": False,
                "hasAdditionalClient": False,
                "isIncludingAmountForNeeds": False,
                "hasCollateral": False
            }
        },
    ]
    arr = [get_representive_person_status(Person(**i)).model_dump() for i in data]
    with open(BASE_DIR / 'mocks/out.json', 'w', encoding='utf-8') as f:
        json.dump(arr, f, ensure_ascii=False, indent=4, default=str)

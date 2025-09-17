from models.representative import Person, Application, LimitGate

available_products = [14, 130, 140, 400, 401, 402, 404, 570, 571, 572, 574, 580, 581, 582, 590, 623, 624, 640]
min_amount = 50000


def get_representive_person_status(person: Person):
    if person.currentStatus == 2:
        person.representativeStatus = 2
        person.comment = 'Нет УЛ, так как его не было при подачи заявки'
    elif person.currentStatus != 2:


def checks(app: Application):
    if app.product in available_products \
            and app.amount >= min_amount \
            and (app.product not in (580, 581, 582) and app.hasInsurance == True) \
            and app.hasAdditionalClient == False \
            and (app.product not in (401, 402, 404, 624, 640) and app.isIncludingAmountForNeeds == True) \
            and app.hasCollateral == False:
        model = LimitGate()
    else:
        return {'result': False, 'comment': 'УЛ не требуется, заявка попадает под исключения проверки условий'}

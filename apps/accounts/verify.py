import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
verify = client.verify.services(os.environ['TWILIO_VERIFY_SERVICE_SID'])


def send(phone):
    print(333333333333,os.environ['TWILIO_ACCOUNT_SID'])
    print(444444444444,os.environ['TWILIO_AUTH_TOKEN'])
    print(55555555555,os.environ['TWILIO_VERIFY_SERVICE_SID'])
    print(999999999999999999999999999999)
    verify.verifications.create(to=phone, channel='sms')
    print(7777777777777777777777777777)


def check(phone, code):
    try:
        print(1111111111111111111111111111)
        result = verify.verification_checks.create(to=phone, code=code)
        print(result,2222222222222222222222222)
    except TwilioRestException:
        print('no',33333333333333333333333333333333)
        return False
    return result.status == 'approved'

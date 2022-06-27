from models.request import Request
from models.response import Response
import random

class CotationService:
    
    @staticmethod
    def quote() -> Response:
        response = Response()

        response.courier = 'JadLog'
        response.cost = float("%0.2f" % (random .uniform(20.5, 60.0)))
        response.delivery_time =  random.randrange(1,30)

        if random.choice([True, False]):
            response.message = 'Error'

        return response
from mangum import Mangum
from inventorymanage.asgi import application

handler = Mangum(application)

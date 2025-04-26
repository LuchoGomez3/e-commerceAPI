from fastapi import APIRouter

from modules.user.routes import router as RoutUser
from modules.product.routes import router as RoutProduct
from modules.sells.routes import router as RoutSells
from modules.suppliers.routes import router as RoutSuppliers

def get_global_router():
    router = APIRouter()
    
    router.include_router(RoutUser)
    router.include_router(RoutProduct)
    router.include_router(RoutSells)
    router.include_router(RoutSuppliers)
    
    return router
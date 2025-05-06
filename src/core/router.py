from fastapi import APIRouter

import modules.user.routes
import modules.product.routes

# from modules.sells.routes import router as RoutSells
# from modules.suppliers.routes import router as RoutSuppliers


def get_global_router():
    router = APIRouter()

    router.include_router(modules.user.routes.router)
    router.include_router(modules.product.routes.router)
    # router.include_router(RoutProduct)
    # router.include_router(RoutSells)
    # router.include_router(RoutSuppliers)

    return router

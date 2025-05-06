from fastapi import HTTPException, APIRouter

router = APIRouter(prefix="/sells", tags=["Sells"], responses={404: {"description":"Not found"}})

sells = {}

@router.get("/")
async def get_sells():
    return sells

@router.get("/{sell_id}")
async def get_sell_by_id():
    pass

@router.post("/{sell_id}")
async def function1():
    pass

@router.put("")
async def function2():
    pass

@router.delete("/{sell_id}")
async def function3():
    pass
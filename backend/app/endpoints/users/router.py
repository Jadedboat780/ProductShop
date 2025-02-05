from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from endpoints.users.schemas import CreateUser, GetUser, UpdateUserPartial
import endpoints.users.crud as user_crud
from db.database import get_async_session
from endpoints.auth import get_user_from_token

router = APIRouter(prefix="/users", tags=["Users"], dependencies=[Depends(get_user_from_token)])


@router.post("/search", status_code=status.HTTP_204_NO_CONTENT)
async def is_user_exist(
        user: GetUser,
        session: AsyncSession = Depends(get_async_session)
):
    data = await user_crud.get(user, session)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect email or password")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
        new_user: CreateUser,
        session: AsyncSession = Depends(get_async_session)
):
    result = await user_crud.create(new_user, session)
    if result is False:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User is already exist")
    return {"status": "success"}


@router.patch("/", status_code=status.HTTP_201_CREATED)
async def update_user_partial(
        user: GetUser,
        update_data: UpdateUserPartial,
        session: AsyncSession = Depends(get_async_session)
):
    user = await user_crud.get(user, session)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect email or password")

    await user_crud.update_partial(user, update_data, session)
    return {"status": "success"}


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
        user: GetUser,
        session: AsyncSession = Depends(get_async_session)
):
    user = await user_crud.get(user, session)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    await user_crud.delete(user, session)

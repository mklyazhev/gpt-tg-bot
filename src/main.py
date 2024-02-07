from fastapi import FastAPI, HTTPException
from src.app.user.router import router as user_router
from src.app.admin.router import router as admin_router


# логи должны быть вместе с config.py и main.py в папке src
# запускать из папки gpt-tg-bot: uvicorn src.main:app --host 127.0.0.1 --port 8080 --reload --workers 2
app = FastAPI()
app.include_router(user_router)
app.include_router(admin_router)


# root и ping вынести в отдельный файл в модуле app
@app.get("/")
async def root():
    try:
        return {
            "status": "success",
            "data": "GPT Telegram Bot API Service. Documentation is available at /docs.",
            "details": None
        }
    except HTTPException as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": e
        })


@app.get("/ping")
async def ping():
    try:
        return {
            "status": "success",
            "data": "Pong!",
            "details": None
        }
    except HTTPException as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": e
        })

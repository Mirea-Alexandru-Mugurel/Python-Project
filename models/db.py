from tortoise import Tortoise


async def init_db():
    await Tortoise.init(
        db_url="sqlite://requests.db", modules={"models": ["models.request_log"]}
    )
    await Tortoise.generate_schemas()

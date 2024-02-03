from aiogram import Router

router = Router(name="callbacks-router")


# @router.callback_query(ButtonCallbackFactory.filter(F.command == "start"))
# async def cb_miss(callback: CallbackQuery, session: AsyncSession):
#     """
#     Invoked on red ball tap
#     :param callback: CallbackQuery from Telegram
#     :param session: DB connection session
#     """
#
#     with suppress(TelegramBadRequest):
#         await callback.message.edit_text("Your score: 0", reply_markup=generate_menu())

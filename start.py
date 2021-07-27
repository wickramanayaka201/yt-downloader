from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    #joinButton = InlineKeyboardMarkup([
    #    [InlineKeyboardButton("Channel", url="https://t.me/aryan_bots")],
     #   [InlineKeyboardButton(
      #      "Report Bugs 😊", url="https://t.me/aryanvikash")]
    #])
    welcomed = f"<b>{message.from_user.first_name}</b>\nආයුබොවන් සාදරයෙන් පිළිගන්නවා "
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation

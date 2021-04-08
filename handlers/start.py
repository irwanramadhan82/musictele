from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello {message.from_user.first_name}!


jangan lupa join grup @antigabutborthers🥰.
masukan musik bot ini kedalam grup kamu Terimakasih 🙏.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Chatt kuy", url="https://t.me/RI024",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Group", url="https://t.me/antigabutborthers"
                    ),
                    InlineKeyboardButton(
                        "💾 join channel", url="https://t.me/sadnesstalk"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Join Channel", url="https://t.me/sadnesstalk"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

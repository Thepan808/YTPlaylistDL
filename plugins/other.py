'''YTPlaylistDL, An Telegram Bot Project
Copyright (c) 2021 Anjana Madu <https://github.com/AnjanaMadu>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>'''

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

@Client.on_message(filters.command("start"))
async def start_msg(client, message):
	await message.reply_text(
		f"Opa {message.from_user.mention},⚙️ Bem vindo ao bot, para ajuda... Clique no /help.\n\nCriado pelo Criador: ➜ @xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx",
		reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🧐 Quer ajuda, abigor?", callback_data=f"help"),
					InlineKeyboardButton("🗃️ Sobre", callback_data=f"about")
				]]
			),
		quote=True)

@Client.on_callback_query()
async def cb_handler(client, update):
	cb_data = update.data
	
	if "help" in cb_data:
		await update.message.edit_text("Envie o URL com Formato.(Audio/Video)\nExamplo: `https://youtube.com/playlist?list=xxxxxxxxxx audio`\n\nenfim.",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🗃️ Sobre", callback_data=f"about"),
					InlineKeyboardButton("🔙 Voltar", callback_data=f"back")
				]]
			))
	elif "about" in cb_data:
		await update.message.edit_text("Linguagem: Python\nFramework: Pyrogram\nEngine: YTDL\nCorded By: @xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx\n\nOnline pae by Baianor",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🧐 Quer ajuda?", callback_data=f"help"),
					InlineKeyboardButton("🔙 Voltar", callback_data=f"back")
				]]
			))
	elif "back" in cb_data:
		await update.message.edit_text(f"Opa {update.from_user.mention}, clique nesse comando /help.\n\nCriado pelo @xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🙄 Quer ajuda?", callback_data=f"help"),
					InlineKeyboardButton("⚙️ Sobre", callback_data=f"about")
				]]
			))

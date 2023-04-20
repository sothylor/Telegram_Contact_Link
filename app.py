from flask import Flask, render_template, url_for, redirect, request
from pyrogram import Client
import asyncio
import database
import myapi

api_id = myapi.telegram_app_id
api_hash = myapi.telegram_app_api_hash
api_token = myapi.Token

app = Flask(__name__)
bot = Client('my_bot', api_id, api_hash, bot_token=api_token)


@app.route('/')
async def home_page():
  chatid = 'omsovannrith'
  return redirect(url_for('addcontact', chatid=chatid))


@app.route('/addcontact')
async def addcontact():
  chatid = request.args.get('chatid')
  return render_template('addcontact.html', chatid=chatid)


@app.route('/form', methods=['GET', 'POST'])
async def form():
  if request.method == 'GET':
    chatid = request.args.get('chatid')
    name = request.args.get('name')
    return render_template('form.html', chatid=chatid, name=name)
  else:
    form = await request.form
    chatid = form.get('chatid')
    username = form.get('username')
    phone = "+" + form.get('phone')
    email = form.get('email')
    print('yes')
    database.add_user(chatid, username, phone, email)
    return render_template('thanks.html')

async def main():

  await app.run(host="0.0.0.0", debug=True)


if __name__ == "__main__":
  asyncio.run(main())

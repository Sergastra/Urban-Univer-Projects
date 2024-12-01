from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard import *
from crud_functions import *


initiate_db()
get_all_products()

api = '7591513189:AAEj2y7nsKdUEe-wvBZG14MKwpupfmiF4aI'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in get_all_products():
        with open(f'../.foto/banka_{i[0]}.png', 'rb') as img:
            await message.answer(f" Название: {i[1]} |  Описание: {i[2]} | Цена: {i[3]} ")
            await message.answer_photo(img)
        await message.answer('Выберите продукт для покупки: ', reply_markup=kp)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст (год):')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост (cм):')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес (кг):')
    await UserState.weight.set()


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г)')
    await call.answer()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет, я бот помогающий твоему здоровью!', reply_markup=kb)


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Привет, я бот помогающий твоему здоровью!')


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    norm_call = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age'])
    await message.answer(f'Ваша норма каллорий {norm_call}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

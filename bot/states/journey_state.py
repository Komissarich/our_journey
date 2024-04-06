from aiogram.fsm.state import StatesGroup, State


class JourneyState(StatesGroup):
    journey_name = State()
    journey_description = State()
    jorney_count_locations = State()
    journey_location = State()
    journey_time_arrive = State()
    journey_time_leave = State()

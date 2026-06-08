from storage import load_state, save_state
from trackers.game_tracker import  get_current_price

state = load_state()

old_price = state.get("wolverine_price")

current_price = get_current_price()

if old_price:
    if current_price < old_price:
        print("Preço caiu")
    elif current_price > old_price:
        print("Preço subiu")
    else:
        print("Sem alterações")

state["wolverine_price"] = current_price

save_state(state)
def on_button_pressed_a():
    led.plot(2, 3)
    OSOYOO_Robot.car_ctrl(OSOYOO_Robot.CarState.CAR_RUN)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    OSOYOO_Robot.car_ctrl(OSOYOO_Robot.CarState.CAR_STOP)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.HEART)
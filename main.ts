input.onButtonPressed(Button.A, function on_button_pressed_a() {
    led.plot(2, 3)
    OSOYOO_Robot.CarCtrl(OSOYOO_Robot.CarState.Car_Run)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    OSOYOO_Robot.CarCtrl(OSOYOO_Robot.CarState.Car_Stop)
})
basic.showIcon(IconNames.Heart)

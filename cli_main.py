from presentation.cli_app.app import CliApp

#  Simple calculator using clean arc
# -------------------------------------------------
# How I understand the data flow of the simplest clean architecture
# application ->
# 1) The (Cli | Framework | GUI | ...)
# accepts an input from the user and passes it to the Controller
# 2) The Controller packages the data and passes it to the Use Cases
# 3) The Use Cases invoke Entities and make them
# use their critical business rules, then
# gather the result and pass it to The Presenter
# 4) The Presenter formats the data that it has received from Use Cases
# and passes it to the View (if exists; if not, then return the data directly)
# 5) The View then just shows (render) the result of the request to the user.

if __name__ == '__main__':
    cli_calculator_app = CliApp().create_app()
    print(cli_calculator_app.run())

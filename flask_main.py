from presentation.flask_app.flask_app import init_app


if __name__ == '__main__':
    flask_calculator_app = init_app()
    flask_calculator_app.run(debug=True)

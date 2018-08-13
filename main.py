if __name__ == '__main__':
    from app import create_app

    app = create_app('flask.cfg')
    app.run(debug=True)

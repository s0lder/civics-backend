if __name__ == '__main__':
    from civics import models
    from civics import app

    models.create_tables(fail_silently=True)
    app.run(host="0.0.0.0", port=8080)

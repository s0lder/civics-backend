def validate_story(form_data):
    return ('name' in form_data and
            'story' in form_data and
            'district' in form_data and
            'date' in form_data)

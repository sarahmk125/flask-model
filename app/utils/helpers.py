import logging
from flask import flash


def form_throw_error(source, form, message):
    logging.error(f'[{source}] Failed validation: \n\n{form.errors}\n')
    flash(message)

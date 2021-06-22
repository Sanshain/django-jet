
import spynner
import io


def run_spynner():
    debug_stream = io.StringIO()
    browser = spynner.Browser(debug_level=spynner.DEBUG, debug_stream=debug_stream)

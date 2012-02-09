from inlinestyle import InlineStyler, remove_whitepace
import os.path

class TestCase(object):
    def setup(self):
        test_path = os.path.dirname(__file__)
        test_html_file = os.path.join(test_path, 'test.html')
        f = open(test_html_file,'r')
        self.html = f.read()
        f.close()

    def test_strip_styles(self):
        styler = InlineStyler(self.html)
        css_list = styler._strip_styles()
        #css_list is a certain length
        assert len(css_list) == 4

    def test_style_application(self):
        assert False, 'not yet implemented'

    def test_conversion(self):
        assert False, 'not yet implemented'

    def test_remove_whitepace(self):
        inpt = 'body{\r\ntest}\t '
        string2 = remove_whitepace(inpt)
        assert string2 == 'body{test}'

    def test_css_load(self):
        styler = InlineStyler(self.html)
        css_list = styler._strip_styles()
        string = ''.join(css_list)
        assert False, 'not yet implemented'

    def test_convert(self):
        styler = InlineStyler(self.html)
        new_html = styler.convert()
        assert new_html
        assert False, 'not yet implemented'
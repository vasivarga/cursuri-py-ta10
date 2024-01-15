import unittest

import HtmlTestRunner

from curs_5_suites.test_alerts import TestAlerts
from curs_5_suites.test_keys import TestKeys
from curs_5_suites.test_scroll import TestScroll


class TestSuite(unittest.TestCase):

    def test_suite(self):

        teste_de_rulat = unittest.TestSuite()

        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestScroll))

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestScroll)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Test report',
            report_name='Test results'
        )

        runner.run(teste_de_rulat)
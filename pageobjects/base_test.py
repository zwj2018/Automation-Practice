from common import test_accounts_config
from common.mobile_test_base import MobileTestBase


class BaseTest(MobileTestBase):

    test_accounts = [MobileTestBase]

    @classmethod
    def setUpClass(cls):
        cls.test_accounts = cls.get_test_accounts('android')

    @staticmethod
    def get_test_accounts(platform):
        _accounts = test_accounts_config.accounts['mobile'][platform]
        return _accounts

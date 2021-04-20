from django.urls import reverse, resolve


class TestProductUrls:
    def test_showcart_urls(self):
        path = reverse('showcart')
        assert resolve(path).view_name == 'showcart'

    def test_pluscart_urls(self):
        path = reverse('pluscart')
        assert resolve(path).view_name == 'pluscart'

    def test_checkout_urls(self):
        path = reverse('checkout')
        assert resolve(path).view_name == 'checkout'

    def test_address_urls(self):
        path = reverse('address')
        assert resolve(path).view_name == 'address'

    def test_orders_urls(self):
        path = reverse('orders')
        assert resolve(path).view_name == 'orders'

    def test_paymentdone_urls(self):
        path = reverse('paymentdone')
        assert resolve(path).view_name == 'paymentdone'

    def test_login_urls(self):
        path = reverse('login')
        assert resolve(path).view_name == 'login'
